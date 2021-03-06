# Stubs for matplotlib (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

__version__numpy__ = ...  # type: Any

def compare_versions(a, b): ...

f = ...  # type: Any
bad_pyparsing = ...  # type: Any
major = ...  # type: Any
minor1 = ...  # type: Any
minor2 = ...  # type: Any
s = ...  # type: Any
tmp = ...  # type: Any

class Verbose:
    levels = ...  # type: Any
    vald = ...  # type: Any
    level_str = ...  # type: Any
    fileo = ...  # type: Any
    def __init__(self) -> None: ...
    level = ...  # type: Any
    def set_level(self, level): ...
    def set_fileo(self, fname): ...
    def report(self, s, level: str = ...): ...
    def wrap(self, fmt, func, level: str = ..., always: bool = ...): ...
    def ge(self, level): ...

verbose = ...  # type: Any

def checkdep_dvipng(): ...
def checkdep_ghostscript(): ...
def checkdep_tex(): ...
def checkdep_pdftops(): ...
def checkdep_inkscape(): ...
def checkdep_xmllint(): ...
def checkdep_ps_distiller(s): ...
def checkdep_usetex(s): ...

get_home = ...  # type: Any
get_configdir = ...  # type: Any
get_cachedir = ...  # type: Any
get_data_path = ...  # type: Any

def get_example_data(fname): ...
def get_py2exe_datafiles(): ...
def matplotlib_fname(): ...

class RcParams(dict):
    validate = ...  # type: Any
    msg_depr = ...  # type: str
    msg_depr_ignore = ...  # type: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __setitem__(self, key, val): ...
    def __getitem__(self, key): ...
    def update(self, *args, **kwargs): ...
    def keys(self): ...
    def values(self): ...
    def find_all(self, pattern): ...

def rc_params(fail_on_error: bool = ...): ...

URL_REGEX = ...  # type: Any

def is_url(filename): ...
def rc_params_from_file(fname, fail_on_error: bool = ..., use_default_template: bool = ...): ...

rcParams = ...  # type: Any
rcParamsOrig = ...  # type: Any
rcParamsDefault = ...  # type: Any

def rc(group, **kwargs): ...
def rcdefaults(): ...
def rc_file(fname): ...

class rc_context:
    rcdict = ...  # type: Any
    fname = ...  # type: Any
    def __init__(self, rc: Optional[Any] = ..., fname: Optional[Any] = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type, value, tb): ...

def rc_file_defaults(): ...
def use(arg, warn: bool = ..., force: bool = ...): ...
def get_backend(): ...
def interactive(b): ...
def is_interactive(): ...
def tk_window_focus(): ...

default_test_modules = ...  # type: Any

def verify_test_dependencies(): ...
def test(verbosity: int = ...): ...
def unpack_labeled_data(replace_names: Optional[Any] = ..., replace_all_args: bool = ..., label_namer: Optional[Any] = ..., positional_parameter_names: Optional[Any] = ...): ...
