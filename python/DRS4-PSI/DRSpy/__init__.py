__version__ = "0.9"
import os
import click

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    print(f"DRSpy v{__version__}")
    ctx.exit()

@click.group(invoke_without_command=True)
@click.option('-t','--type', 'ftype', help='Choose input file formatting', required=True, type=click.Choice(['txt', 'xml']))
@click.option('-e','--plot-ext', 'ext', help='Plot output extension', default='png', type=click.Choice(['png', 'pdf']), show_default=True)
@click.option('-a', '--auto-decode', 'fadecode', help='Load additional information from filename. Supported name: <+-pos>_<C|U|D>_(opt.t)', is_flag=True, default=False)
@click.option('-v', '--verbose', 'fverbose', help='Enable verbosity mode', is_flag=True, default=False)
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def main(ftype, ext, fadecode, fverbose):
    if ftype == 'txt':
        raise Exception("Function temporary unavailable")
    elif ftype == 'xml':
        raise Exception("Function temporary unavailable")

@main.command()
@click.argument("files", nargs=-1)
@click.option('-q', '--verboseq', 'q', help='Enable verbosity mode', is_flag=True, default=False)
def genCfg(files, q):
    print("gencfg")
    pass

def log(msg, color="white", wait=False):
    if wait:
        print(click.style(msg, fg=color), end="")
    else:
        print(click.style(msg, fg=color))
    return None
        

if __name__ == '__main__':
    print(f"Started: DRSpy v{__version__}")

