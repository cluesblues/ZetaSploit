#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os
import sys
import re

from core.badges import badges
from core.execute import execute
from core.exceptions import exceptions
from core.modules import modules
from core.io import io

class menu:
    def __init__(self):
        self.badges = badges()
        self.execute = execute()
        self.exceptions = exceptions()
        self.modules = modules()
        self.io = io()
        
    def launch(self):
        while True:
            try:
                if not self.modules.check_current_module():
                    prompt = '(zsf)> '
                else:
                    module = self.modules.get_current_module_name()
                    name = self.modules.get_platform(module) + '/' + self.modules.get_name(module)
                    prompt = '(zsf: ' + self.modules.get_category(module) + ': ' + self.badges.RED + self.badges.BOLD + name + self.badges.END + ')> '
                commands, arguments = self.io.input(prompt)
                
                if not commands:
                    continue
                else:
                    self.execute.execute_command(commands, arguments)

            except (KeyboardInterrupt, EOFError):
                self.io.output("")
            except self.exceptions.GlobalException:
                pass
            except Exception as e:
                self.badges.output_error("An error occurred: " + str(e) + "!")
