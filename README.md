# A wrapper around `host` that turns URLs into hostnames

Have you ever pasted something from eg. the browser address bar to `host` just to get this?

    $ host https://google.com
    Host https://google.com not found: 3(NXDOMAIN)

Enter `ohst`, a thin wrapper around `host` that turns URLs into hostnames!

    $ ohst https://google.com
    google.com has address 172.217.22.174

All parameters that are not understood by `urllib.parse` are passed verbatim:

    $ ohst -t TXT https://google.com
    google.com descriptive text "v=spf1 include:_spf.google.com ~all"

## Installation

    # symlink
    ln -sf $PWD/ohst.py /usr/local/bin

    # or copy
    install -m 755 ohst.py /usr/local/bin

## License

    The MIT License (MIT)

    Copyright © 2017 Santtu Pajukanta

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
