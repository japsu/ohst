#!/usr/bin/env python
#
# ohst.py - A wrapper around `host` that turns URLs into hostnames
# Licensed under the MIT License
#
# Copyright (c) 2017 Santtu Pajukanta
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


HOST_BINARY = '/usr/bin/host'


def mangle_arg(arg):
    try:
        url = urlparse(arg)
        return url.netloc if url.netloc else arg
    except RuntimeError:
        return arg


def main(args):
    os.execv(HOST_BINARY, [HOST_BINARY] + [mangle_arg(arg) for arg in args])


if __name__ == '__main__':
    from sys import argv
    main(argv[1:])
