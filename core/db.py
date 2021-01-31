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

import json

from core.badges import badges
from core.storage import storage

class db:
    def __init__(self):
        self.badges = badges()
        self.storage = storage()
        
    def disconnect_modules_database(self, name):
        self.storage.delete_element("connected_databases", name)
        self.storage.delete_element("modules", name)
        
    def disconnect_plugins_database(self, name):
        self.storage.delete_element("connected_databases", name)
        self.storage.delete_element("plugins", name)
        
    def connect_modules_database(self, name, path):
        modules = {
            name: json.load(open(path))
        }
        
        data = {
            name: {
                'type': 'modules',
                'path': path
            }
        }
        if not self.storage.get("connected_databases"):
            self.storage.set("connected_databases", dict())
        self.storage.update("connected_databases", data)
        
        if self.storage.get("modules"):
            self.storage.update("modules", modules)
        else:
            self.storage.set("modules", modules)
      
    def connect_plugins_database(self, name, path):
        plugins = {
            name: json.load(open(path))
        }
        
        data = {
            name: {
                'type': 'plugins',
                'path': path
            }
        }
        if not self.storage.get("connected_databases"):
            self.storage.set("connected_databases", dict())
        self.storage.update("connected_databases", data)
        
        if self.storage.get("plugins"):
            self.storage.update("plugins", plugins)
        else:
            self.storage.set("plugins", plugins)
