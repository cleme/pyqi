#!/usr/bin/env python

#-----------------------------------------------------------------------------
# Copyright (c) 2013, The BiPy Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2013, The QCLI Project"
__credits__ = ["Daniel McDonald", "Greg Caporaso", "Doug Wendel",
               "Jai Ram Rideout"]
__license__ = "BSD"
__version__ = "0.1.0-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "mcdonadt@colorado.edu"

from pyqi.core.interfaces.optparse import (CLOption,
                                           UsageExample,
                                           ParameterConversion,
                                           OutputHandler)
from pyqi.core.interfaces.optparse.output_handler import write_string
from pyqi.commands.make_cli import CommandConstructor
from pyqi.core.interfaces.optparse.input_handler import command_handler

usage_examples = [UsageExample(ShortDesc='Stub out a CLI configuration',
                               LongDesc="""Consume an existing Command object and produce the base CLI configuration""",
                               Ex="%prog -c pyqi.commands.make_cli.MakeCLI -m pyqi.commands -o make_cli.py")
    ]

param_conversions = {
            'command':ParameterConversion(ShortName='c',
                    LongName='command',
                    CLType=str,
                    InHandler=command_handler),
            'mod':ParameterConversion(ShortName='m',
                    LongName='mod',
                    CLType=str),
    }

additional_options = [
        CLOption(Type='output_file',
                 Help='the resulting configuration file',
                 Name='output_fp',
                 Required=True,
                 LongName='output-fp',
                 CLType='new_filepath',
                 ShortName='o')
    ]

output_map = {'result':OutputHandler(OptionName='output_fp',
                                     Function=write_string)}
