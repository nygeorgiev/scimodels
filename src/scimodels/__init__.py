from .abstract import Model
from .response import Response
from .loaders import load_model as load
from .loaders import get_providers
from .temp import get_temp_dir, set_temp_dir

__version__ = "0.0.1"

providers = get_providers()

__all__ = [
    "Model",
    "Response",
    "load",
    "get_temp_dir",
    "set_temp_dir",
    "providers",
]

__license__ = "MIT"

__author__ = "Nikolay Georgiev"