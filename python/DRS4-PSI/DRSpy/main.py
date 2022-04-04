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
@click.option('-t','--type', 'ftype', help='Choose input file formatting', type=click.Choice(['txt', 'xml']), default=None)
@click.option('-e','--plot-ext', 'ext', help='Plot output extension', default='png', type=click.Choice(['png', 'pdf']), show_default=True)
@click.option('-a', '--auto-decode', 'fadecode', help='Load additional information from filename. Supported name: <+-pos>_<C|U|D>_(opt.t)', is_flag=True, default=False)
@click.option('-v', '--verbose', 'fverbose', help='Enable verbosity mode', is_flag=True, default=False)
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.pass_context
def main(ctx, ftype, ext, fadecode, fverbose):
    """
        Data analysis tool for DRS4(PSI) board.
        
        Examples:

            - a

            - b

            - c
        
    """
    print(f"\n{ctx.get_help()}\n")
    ctx.info_name = "run"
    print(main.get_command(ctx, "run").get_help(ctx))
    ctx.info_name = "gencfg"
    print(main.get_command(ctx, "gencfg").get_help(ctx))
    if ftype == 'txt':
        log("->TXT")
    elif ftype == 'xml':
        log("->XML")

@main.command(short_help="Generate configuration file")
@click.argument("files", nargs=-1, metavar="<files>")
@click.pass_context
def genCfg(ctx, files):
    print("gencfg")

@main.command(short_help="Generate output files")
@click.option('-x','--xxx', 'x', help='Cho', default=None, required=True)
@click.argument("config", nargs=1, metavar="<config_file>")
@click.pass_context
def run(ctx, config, x):
    log("->RUN", "red")

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

