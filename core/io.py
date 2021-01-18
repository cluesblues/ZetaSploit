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
import readline

from core.storage import storage

class io:
    def __init__(self):
        self.storage = storage()

    def output(self, message, end=os.linesep):
        sys.stdout.write('\033[1K\r' + message + end)
        sys.stdout.flush()
        if self.storage.get("current_prompt") and self.storage.get("active_input"):
            sys.stdout.write('\033[1K\r' + self.storage.get("current_prompt") + readline.get_line_buffer())
            sys.stdout.flush()

    def input(self, prompt_message):
        self.storage.set("current_prompt", prompt_message)
        self.storage.set("active_input", True)
        command = input('\033[1K\r' + prompt_message)
        commands = command.split()
        arguments = ""
        if commands:
            arguments = command.replace(commands[0], "", 1).strip()
        self.storage.set("active_input", False)
        return (commands, arguments)
