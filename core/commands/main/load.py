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

from core.io import io
from core.badges import badges
from core.storage import storage
from core.importer import importer

class ZetaSploitCommand:
    def __init__(self):
        self.io = io()
        self.badges = badges()
        self.storage = storage()
        self.importer = importer()

        self.details = {
            'Name': "load",
            'Description': "Load specified plugin.",
            'Usage': "load <plugin>",
            'ArgsCount': 1,
            'NeedsArgs': True,
            'Args': list()
        }

    def add_plugin(self, plugin):
        plugins = self.storage.get("plugins")
        loaded_plugins = dict()
        not_installed = list()
        for dependence in plugins[plugin]['Dependencies']:
            if not self.importer.import_check(dependence):
                not_installed.append(dependence)
        if not not_installed:
            try:
                plugins[plugin] = self.importer.import_plugin(plugins[plugin]['Path'])
            except:
                return
            if self.storage.get("loaded_plugins"):
                self.storage.update("loaded_plugins", plugins)
            else:
                self.storage.set("loaded_plugins", plugins)
                self.storage.get("loaded_plugins")[plugin].run()
                self.badges.output_success("Successfully loaded " + plugin + " plugin!")
        else:
            self.badges.output_error("Plugin depends this dependencies which is not installed:")
            for dependence in not_installed:
                self.io.output("    " + dependence)
        
    def run(self):
        plugin = self.details['Args'][0]
        plugins = self.storage.get("plugins")
        self.badges.output_process("Loading " + plugin + " plugin...")
        if plugins:
            if self.storage.get("loaded_plugins"):
                if plugin in self.storage.get("loaded_plugins").keys():
                    self.badges.output_error("Already loaded!")
                else:
                    if plugin in plugins.keys():
                        self.add_plugin(plugin)
                    else:
                        self.badges.output_error("Failed to load " + plugin + " plugin!")
            else:
                if plugin in plugins.keys():
                    self.add_plugin(plugin)
                else:
                    self.badges.output_error("Failed to load " + plugin + " plugin!")
        else:
            self.badges.output_error("Failed to load " + plugin + " plugin!")
