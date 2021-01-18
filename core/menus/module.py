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
import readline

from core.badges import badges
from core.execute import execute
from core.exceptions import exceptions
from core.storage import storage
from core.io import io
from core.modules import modules

class module:
    def __init__(self):
        self.badges = badges()
        self.execute = execute()
        self.exceptions = exceptions()
        self.storage = storage()
        self.io = io()
        self.modules = modules()

    def module_menu(self):
        while True:
            try:
                current_module = self.storage.get_array("current_module", self.storage.get("pwd"))
                prompt = '(zsf: ' + self.modules.get_category(current_module.details['Name']) + ': \033[1;31m' + self.modules.get_name(current_module.details['Name']) + '\033[0m)> '
                commands, arguments = self.io.input(prompt)
                if commands == list():
                    continue
                else:
                    if not self.execute.execute_core_command(commands, arguments, "module"):
                        if not self.execute.execute_module_command(commands, arguments):
                            if not self.execute_plugin_command(commands, arguments):
                                self.badges.output_error("Unrecognized command!")

            except (KeyboardInterrupt, EOFError):
                self.io.output("")
            except self.exceptions.ExitMenuException:
                break
            except self.exceptions.GlobalException:
                pass
            except Exception as e:
                self.badges.output_error("An error occurred: " + str(e) + "!")
