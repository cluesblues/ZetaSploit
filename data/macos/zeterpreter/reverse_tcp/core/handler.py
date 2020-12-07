#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020 EntySec
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

from core.helper import helper

class handler:
    def __init__(self, client):
        self.client = client
        self.helper = helper()
        
    def sendterm(self):
        terminator = self.helper.generate_terminator()
        self.client.send((terminator + '\x04').encode())
        return terminator
        
    def send(self, buffer):
        if not isinstance(buffer, bytes):
            buffer = buffer.encode()
        self.client.send(buffer + '\x04'.encode())
        
    def sendall(self, buffer):
        terminator = self.sendterm()
        if not isinstance(buffer, bytes):
            buffer = buffer.encode()
        self.client.send(buffer + '\x04'.encode())
        return terminator
    
    def recvstr(self, char='\n'):
        result = self.recvall(char)
        return result
    
    def recvall(self, terminator):
        result = b''
        while 1:
            data = self.client.recv(1024)
            if terminator.encode() in data:
                data = data.replace(terminator.encode(), b'')
                result += data
                break
            else:
                result += data
        return result

    def recvfile(self, terminator, input_file):
        output_file = open(input_file, "wb")
        while 1:
            data = self.client.recv(1024)
            if terminator.encode() in data:
                data = data.replace(terminator.encode(), b'')
                output_file.write(data)
                break
            else:
                output_file.write(data)
        output_file.close()
