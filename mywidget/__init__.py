from libqtile.utils import lazify_imports
from libqtile.widget.import_error import make_error

mywidgets = {
    "PowerOff": "poweroff",
    "Net": "net",
    "myTheme": "theme"
    # "fcthemeColor": "theme"
}

__all__, __dir__, __getattr__ = lazify_imports(mywidgets, __package__, fallback=make_error)