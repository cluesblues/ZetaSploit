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

from core.formatter import formatter
from core.storage import storage
from core.io import io

class ZetaSploitCommand:
    def __init__(self):
        self.formatter = formatter()
        self.storage = storage()
        self.io = io()

        self.details = {
            'Category': "core",
            'Name': "help",
            'Description': "Show available commands.",
            'Usage': "help",
            'ArgsCount': 0,
            'NeedsArgs': False,
            'Args': list()
        }

    def run(self):
        commands_data = list()
        headers = ("Command", "Description")
        commands = self.storage.get("commands")['module']
        for command in sorted(commands.keys()):
            commands_data.append((command, commands[command].details['Description']))
        self.io.output("")
        self.formatter.format_table("Core Commands", headers, *commands_data)
        self.io.output("")
        current_module = self.storage.get_array("current_module", self.storage.get("pwd"))
        if hasattr(current_module, "commands"):
            commands_data = list()
            commands = current_module.commands
            for command in sorted(commands.keys()):
                commands_data.append((command, commands[command]['Description']))
            self.formatter.format_table("Custom Commands", headers, *commands_data)
            self.io.output("")
        if self.storage.get("loaded_plugins"):
            for plugin in self.storage.get("loaded_plugins").keys():
                if hasattr(self.storage.get("loaded_plugins")[plugin], "commands"):
                    commands_data = list()
                    commands = self.storage.get("loaded_plugins")[plugin].commands
                    for command in sorted(commands.keys()):
                        commands_data.append((command, commands[command]['Description']))
                    self.formatter.format_table(plugin.title() + " Commands", headers, *commands_data)
                    self.io.output("")
