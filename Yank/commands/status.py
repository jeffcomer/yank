#!/usr/local/bin/env python

#=============================================================================================
# MODULE DOCSTRING
#=============================================================================================

"""
Query output files for quick status.

"""

#=============================================================================================
# MODULE IMPORTS
#=============================================================================================

from yank import utils

#=============================================================================================
# COMMAND DISPATCH
#=============================================================================================

def dispatch(args):
    from yank import analyze
    utils.config_root_logger(args['--verbose'])
    success = analyze.print_status(args['--store'])
    return success
