import os
import click
import DRSpy

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    print(f"DRSpy v{DRSpy.__version__}")
    ctx.exit()
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.option('-d','--db', 'fdb', help='Database location', type=str, default="data.csv", show_default=True)
#@click.option('-t','--type', 'ftype', help='Choose input file formatting', type=click.Choice(['txt', 'xml']), default=None)
#@click.option('-e','--plot-ext', 'ext', help='Plot output extension', default='png', type=click.Choice(['png', 'pdf']), show_default=True)
#@click.option('-a', '--auto-decode', 'fadecode', help='Load additional information from filename. Supported name: <+-pos>_<C|U|D>_(opt.t)', is_flag=True, default=False)
@click.option('-v', '--verbose', 'fverbose', help='Enable verbosity mode', is_flag=True, default=False)
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.pass_context
def main(ctx, fdb, fverbose):
    """
        Data analysis tool for DRS4(PSI) board.
        
        Examples:

            - a

            - b

            - c
        
    """
    if fadecode:
        instance = DataStruct(fadecode=True, fverbosity=fverbose)
    print(f"\n{ctx.get_help()}\n")
    ctx.info_name = "run"
    print(main.get_command(ctx, "run").get_help(ctx))
    ctx.info_name = "gencfg"
    print(main.get_command(ctx, "gencfg").get_help(ctx))

@main.command(short_help="Update database")
@click.option('-f','--format', 'fformat', help='Input file format', default=click.Choice(["xml","PtP", "delay"]), default="PtP", show_default=True)
@click.option('-a','--auto', 'fauto', help='Recognize file automatically', is_flag=True, default=False)
@click.argument("files", nargs=-1, metavar="<files or dir>")
@click.pass_context
def update(ctx, files, fformat, fauto):
    if fauto:
        ctx.obj.auto_recognize(files[0])
    else:
        for file in files:
            ctx.obj.load_file(file, fformat)

@main.command(short_help="Data description")
@click.pass_context
def describe(ctx):
    log("->DEsc", "red")

@main.command(short_help="Generate graphs")
@click.option("-e", "--ext", "fext", help="Picture extension", default="pdf", type=click.Choice(["pdf", "png"]), show_default=True)
@click.argument("expression", nargs=-1, metavar="<expression>")
@click.pass_context
def plot(ctx, expression, fext):
    ctx.obj


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

def log(msg, color="white", wait=False):
    if wait:    print(click.style(msg, fg=color), end="")
    else:       print(click.style(msg, fg=color))
    return None

if __name__ == '__main__':
    print(f"Started: DRSpy v{DRSpy.__version__}")

