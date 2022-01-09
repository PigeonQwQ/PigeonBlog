
debug = print

# load devtools if installed
try:
    from devtools import debug as dbg
except ImportError:
    debug = print
else:
    debug = debug
