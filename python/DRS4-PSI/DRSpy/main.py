import os
import click
import DRSpy
from DRSpy.data_struct import *

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
@click.option('--live', 'flive', help='Enable live preview', is_flag=True, default=False)
@click.argument("expression", nargs=2, metavar="<expression>")
@click.pass_context
def plot(ctx, expression, fext, flive):
    ctx.obj.plot(*expression, flive=flive)


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


if __name__ == '__main__':
    print(f"Started: DRSpy v{DRSpy.__version__}")

