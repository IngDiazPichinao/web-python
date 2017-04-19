from pkg_resources import get_distribution

__version__ = get_distribution('cns-web-sav').version
__all__     = ['__version__']
