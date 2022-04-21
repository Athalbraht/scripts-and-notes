import os
import click
import DRSpy
from DRSpy.data_struct import *

from scipy.optimize import curve_fit
import numpy as np

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    print(f"DRSpy v{DRSpy.__version__}")
    ctx.exit()
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.option('-d','--db', 'fdb', help='Database location', type=str, default="data.csv", show_default=True)
@click.option('-c','--config', 'fconfig', help='Configuration file', type=str, default="drspy.config", show_default=True)
@click.option('-v', '--verbose', 'fverbose', help='Enable verbosity mode', is_flag=True, default=False)
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.pass_context
def main(ctx, fdb, fverbose, fconfig):
    """
        Data analysis tool for DRS4(PSI) board.
        
    """
    ctx.obj = DataStruct(fverbose=fverbose, config_file=fconfig, drsframe=fdb)
    """
    print(f"\n{ctx.get_help()}\n")
    ctx.info_name = "run"
    print(main.get_command(ctx, "run").get_help(ctx))
    ctx.info_name = "gencfg"
    print(main.get_command(ctx, "gencfg").get_help(ctx))
    """
@main.command(short_help="Update database")
@click.option('-f','--format', 'fformat', help='Input file format', type=click.Choice(["xml","PtP", "delay"]), default="PtP", show_default=True)
@click.option('-a','--auto', 'fauto', help='Recognize file automatically', is_flag=True, default=False)
@click.option('-t','--tag', 'ftag', help='Add <tag> to data headers', default="", type=str)
@click.argument("files", nargs=-1, metavar="<files or dir>")
@click.pass_context
def update(ctx, files, fformat, fauto, ftag):
    if fauto:
        ctx.obj.auto_recognize(files[0], ftag)
    else:
        for file in files:
            ctx.obj.load_file(file, fformat, ftag)

@main.command(short_help="Data description")
@click.pass_context
def desc(ctx):
    log(ctx.obj.data.describe(), "green")

@main.command(short_help="Command line")
@click.option('--exec', 'fexec', help='Execute without print()', is_flag=True, default=False)
@click.argument("command", nargs=1, default="""print("DRSpy CLI")""")
@click.pass_context
def cli(ctx, command, fexec):
    if fexec: eval(command)
    else: print(eval(command))
    while True:
        log("> ", wait=True)
        command = input()
        try: print(eval(command))
        except Exception as e: log(e, "red")

@main.command(short_help="Generate graphs")
@click.option("-e", "--ext", "fext", help="Picture extension", default="pdf", type=click.Choice(["pdf", "png"]), show_default=True)
@click.option("-k", "--kind", "fkind", help="Plot type", default="line", type=str, show_default=True)
@click.option('--live', 'flive', help='Enable live preview', is_flag=True, default=False)
@click.argument("expression", nargs=2, metavar="<expression>")
@click.pass_context
def plot(ctx, expression, fext, flive, fkind):
    ctx.obj.plot(*expression, flive=flive, ext=fext, fkind=fkind)

@main.command(short_help="Load macro")
@click.argument("macro", metavar="<macro>")
@click.pass_context
def macro(ctx, macro):
    db = ctx.obj
    dataset = ctx.obj.data
    with open(macro, "r") as file:
        code = file.read()
        exec(code)

@main.command()
@click.argument('subcommand')
@click.pass_context
def help(ctx, subcommand):
    ctx.info_name = subcommand
    subcommand_obj = main.get_command(ctx, subcommand)
    if subcommand_obj is None:
        click.echo("I don't know that command.")
    else:
        click.echo(subcommand_obj.get_help(ctx))

@main.command(short_help="run")
@click.pass_context
def run(ctx):
    dataset = ctx.obj.data
    def nconv(n, spl="_"):
        return float(n.split(spl)[0])

    def t_sum(df, v, w):
        ww = df[w]
        vv = df[v]
        return (ww*vv).sum()/ww.sum()

    def asym(df, c1, c2):
        return  (df[c1] - df[c2])/(df[c1] + df[c2])

    def rr(dxr, dyr):
        return ctx.obj.plot(dxr,dyr, regx=True)   

    def f_l(X,a,b):
        return a*X+b

    dl = ".*Delay.*"
    chn = ".*Channel"

    dall = ".*_t"
    ccent = ".*C_t"
    ucent = ".*U_t"
    dcent = ".*D_t"


    dall_w = rr(dcent, dcent)
    uall_w = rr(ucent, dcent)
    call_w = rr(ccent, dcent)
    dall_w_l = []
    uall_w_l = []
    call_w_l = []
    
    dw_C = [[],[],[]]
    dw_U = [[],[],[]]
    dw_D = [[],[],[]]
    for dw in rr(ccent, ccent)[0]:
        dw_C[0].append(nconv(dw))
        dw_C[1].append(t_sum(ctx.obj.data, dw, "Delay [ns]"))
        dw_C[2].append(ctx.obj.data[["Delay [ns]", dw]].to_numpy())
        print(dw_C)
    for dw in rr(dcent, dcent)[0]:
        dw_D[0].append(nconv(dw))
        dw_D[1].append(t_sum(ctx.obj.data, dw, "Delay [ns]"))
        dw_D[2].append(ctx.obj.data[["Delay [ns]", dw]].to_numpy())
        print(dw_D)
    for dw in rr(ucent, dcent)[0]:
        dw_U[0].append(nconv(dw))
        dw_U[1].append(t_sum(ctx.obj.data, dw, "Delay [ns]"))
        dw_U[2].append(ctx.obj.data[["Delay [ns]", dw]].to_numpy())
        print(dw_U)
    dw_X =  np.linspace(-40,40,100)
    dw_ppc, _ = curve_fit(f_l, dw_C[0], dw_C[1])
    dw_ppu, _ = curve_fit(f_l, dw_U[0], dw_U[1])
    dw_ppd, _ = curve_fit(f_l, dw_D[0], dw_D[1])
    plt.plot(dw_C[0], dw_C[1],"go", label="Center")
    plt.plot(dw_X, f_l(dw_X,*dw_ppc),"g--", alpha=0.5)
    plt.plot(dw_D[0], dw_D[1], "ro", label="Edge D")
    plt.plot(dw_X, f_l(dw_X,*dw_ppd),"r--", alpha=0.5)
    plt.plot(dw_U[0], dw_U[1], "bo", label="Edge U")
    plt.plot(dw_X, f_l(dw_X,*dw_ppu),"b--", alpha=0.5)
    plt.legend()
    plt.grid(True)
    plt.xlabel("Distance [cm]")
    plt.ylabel("Delay [ns] ")
    plt.show()
    plt.clf()

    plt.plot(dw_C[1])


    time_C = ".*\-[1-4][0-9]_C.*_t"
    time_D = ".*\-[1-4][0-9]_D.*_t"
    time_U = ".*\-[1-4][0-9]_U.*_t"
    t_C = [[],[]]
    t_U = [[],[]]
    t_D = [[],[]]

    fig, (ax1,ax2,ax3) = plt.subplots(3)
    for i in  rr(time_C,time_C):
        ctx.obj.data.plot.line("Delay [ns]", i, ax=ax1, c="blue", label=False, alpha=0.4)
    ax1.get_legend().remove()
    ax1.set_xlim(-8,2)
    ax1.set_xlabel("")
    ax1.set_title("Center")
    for i in  rr(time_U,time_C):
        ctx.obj.data.plot.line("Delay [ns]", i, ax=ax2, c="red", label=False, alpha=0.4)
    ax2.get_legend().remove()
    ax2.set_xlim(-8,2)
    ax2.set_title("Edge U")
    ax2.set_xlabel("")
    for i in  rr(time_D,time_C):
        ctx.obj.data.plot.line("Delay [ns]", i, ax=ax3, c="green", label=False, alpha=0.4)
    ax3.get_legend().remove()
    ax3.set_xlim(-8,2)
    ax3.set_title("Edge D")
    ax3.set_xlabel("Delay [ns]")
    
    plt.show()
    plt.clf()

    c_call = ".*-CH[0-1]"
    c0_call = ".*C-CH0"
    c1_call = ".*C-CH1"
    c0_uall = ".*U-CH0"
    c1_uall = ".*U-CH1"
    c0_dall = ".*D-CH0"
    c1_dall = ".*D-CH1"
    
    cx0 = rr(".*C.*CH0", c_call)[0]
    cx1 = rr(".*C.*CH1", c_call)[0]
    plt.clf()

    def landau(X,E,S, N):
        return 1/np.sqrt(2*np.pi) * np.exp(-((((X-E)/S)+np.exp(-((X-E)/S)))/2)) *N
    cD = []
    uD = []
    dD = []
    cH0e = []
    cH0 = []
    cH1e = []
    cH1 = []

    uH0 = []
    uH1 = []
    uH0e =[]
    uH1e = []

    dH0 = []
    dH1 = []
    dH0e =[]
    dH1e = []

    for i,j  in enumerate(cx0): 
        fig, ax = plt.subplots(1)
        cx_max = np.linspace(10, 160,300)
        cx_x = ctx.obj.data[["Channel", cx0[i], cx1[i]]].dropna().to_numpy().T
        tm = [[],[],[]]
        print(cx_x.shape)
        for e in range(cx_x.shape[1]):
            if cx_x[1][e] > 40 or cx_x[2][e] >40:
                tm[0].append(cx_x[0][e])
                tm[1].append(cx_x[1][e])
                tm[2].append(cx_x[2][e])
        cx_x = np.array(tm)

        try: 
            ux_x = ctx.obj.data[["Channel", cx0[i].replace("_C","_U"), cx1[i].replace("_C","_U")]].dropna().to_numpy().T
            um = [[],[],[]]
            print(cx_x.shape)
            for e in range(cx_x.shape[1]):
                if ux_x[1][e] > 40 or ux_x[2][e] >40:
                    um[0].append(ux_x[0][e])
                    um[1].append(ux_x[1][e])
                    um[2].append(ux_x[2][e])
        except: 
            print("u")
        else:
            ux_x = np.array(ux_x)
            ux_pp0, _ = curve_fit(landau, ux_x[0],ux_x[1])
            ux_pp1, _ = curve_fit(landau, ux_x[0],ux_x[2])
            uD.append(nconv(j))
            uH0.append(ux_pp0[0])
            uH1.append(ux_pp1[0])
            uH0e.append(ux_pp0[1])
            uH1e.append(ux_pp1[1])

        try:
            dx_x = ctx.obj.data[["Channel", cx0[i].replace("_C", "_D"), cx1[i].replace("_C", "_D")]].dropna().to_numpy().T
            dm = [[],[],[]]
            print(cx_x.shape)
            for e in range(cx_x.shape[1]):
                print(e)
                if dx_x[1][e] > 40 or dx_x[2][e] >40:
                    dm[0].append(dx_x[0][e])
                    dm[1].append(dx_x[1][e])
                    dm[2].append(dx_x[2][e])
            dx_x = np.array(dx_x)
            dx_pp0, _ = curve_fit(landau, dx_x[0],dx_x[1])
            dx_pp1, _ = curve_fit(landau, dx_x[0],dx_x[2])
            ctx.obj.data.plot.line("Channel", cx0[i].replace("_C", "_D"), ax=ax,alpha=0.7, c="red", markersize=1)
            ctx.obj.data.plot.line("Channel", cx1[i].replace("_C", "_D"), ax=ax,alpha=0.7,c="green", markersize=1)
            ax.plot(cx_max, landau(cx_max, *dx_pp0), "r--",alpha=0.9, markersize=1)
            ax.plot(cx_max, landau(cx_max, *dx_pp1), "g--",alpha=0.9, markersize=1)
        except:
            print("d")
        else:
            dD.append(nconv(j))
            dH0.append(dx_pp0[0])
            dH1.append(dx_pp1[0])
            dH0e.append(dx_pp0[1])
            dH1e.append(dx_pp1[1])

        cx_pp0, _ = curve_fit(landau, cx_x[0],cx_x[1])
        cx_pp1, _ = curve_fit(landau, cx_x[0],cx_x[2])
        cD.append(nconv(j))
        cH0.append(cx_pp0[0])
        cH1.append(cx_pp1[0])
        cH0e.append(cx_pp0[1])
        cH1e.append(cx_pp1[1])
        ctx.obj.data.plot.line("Channel", cx0[i], ax=ax,alpha=0.7, c="red", markersize=1)
        ctx.obj.data.plot.line("Channel", cx1[i], ax=ax,alpha=0.7,c="green", markersize=1)
        ax.plot(cx_max, landau(cx_max, *cx_pp0), "r--",alpha=0.9, markersize=1)
        ax.plot(cx_max, landau(cx_max, *cx_pp1), "g--",alpha=0.9, markersize=1)
        ax.set_xlim(-10,160)
        
        ax.set_title(f"")
        plt.grid(True)
        plt.ylabel("Counts")
        
        plt.show()
        ax.cla()
    
    
    def fxx(X,A, B,C):
        return A + B*X + C*X**2
    cD = np.array(cD,dtype=float)
    cH0 = np.array(cH0,dtype=float)
    cH1 = np.array(cH1,dtype=float)
    print(cD)
    print(cH0)
    print(cH1)
    wx = np.linspace(np.array(cD).min(), np.array(cD).max(),300)
    pp0, _ = curve_fit(fxx, cD, cH0)
    pp1, _ = curve_fit(fxx, cD, cH1)
    #plt.plot(wx, fxx(wx, *pp0), "r--", alpha=0.5)
    #plt.plot(wx, fxx(wx, *pp1), "g--", alpha=0.5)
    plt.errorbar(cD, cH0,cH0e, 0.001, "ro",label="CH0", elinewidth=1, capsize=1, markersize=2)
    plt.errorbar(cD, cH1,cH1e,0.001, "go", label="CH1", elinewidth=1, capsize=1,markersize=2)
    plt.grid(True)
    plt.legend()
    plt.xlabel("Distance [cm]")
    plt.ylabel("Channel [mV]")
    plt.title("Landau Peaks")
    plt.show()

    def moyal(X, E, S, N):
        #xx = (X-E)/S
        #mm = -0.5 * (xx + np.exp(-xx))
        #return 1/np.sqrt(2)/S * np.exp(mm)
        #xx = (X - P)/S
        #fm = xx/S
        #threexp = np.exp(-0.5*(fm+np.exp(-fm)))
        #return threexp/np.sqrt(2*np.pi)
        return 1/np.sqrt(2*np.pi) * np.exp(-0.5*(((X-E)/S)+np.exp(-((X-E)/S)))) / S * N
        

    xc0, xc00 = rr(c0_call, c0_call)
    xc0x = ctx.obj.data[["Channel", xc0[0]]].dropna().to_numpy().T
    xc0t = np.linspace(xc0x[0].min(), xc0x[0].max(), 300)
    xc0pp, xc0pc = curve_fit(landau, xc0x[0], xc0x[1] )
    f, ax = plt.subplots()
    ctx.obj.data.plot("Channel", xc0[0],ax=ax,xerr=1)
    plt.plot(xc0t, landau(xc0t, *xc0pp))
    plt.autoscale()
    plt.show()
    print(xc0pc)
    print(xc0pp)
        
    

if __name__ == '__main__':
    print(f"Started: DRSpy v{DRSpy.__version__}")

