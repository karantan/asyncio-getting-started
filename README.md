Asyncio Getting Started
======================

The purpose of this project is to demonstrate how asyncio
(ref: [link](https://docs.python.org/3/library/asyncio.html)) works.

The project contains several simple examples which should help you understand
when and how to use `asyncio` module. It also contains a few advanced examples
for deeper understanding of the `asyncio`.

This project does NOT provide documentation about `asyncio` or any other
library that we use here. 


Installation
------------

Install Asyncio Getting Started by running:

```bash
git clone https://github.com/karantan/asyncio-getting-started
make
```

Read `Makefile` for additional commands.


Run
---

To see how non-blocking asyncio works type:

```bash
make run-non-blocking
```


Blocking asyncio code can be tested with the following command.

```bash
make run-blocking
```

The source code for blocking code is in `src/blocking_asyncio.py` and for
non-blocking it is in `src/nonblocking_asyncio.py`.



Contribute
----------

- Issue Tracker: github.com/karantan/asyncio-getting-started/issues
- Source Code: github.com/karantan/asyncio-getting-started

Support
-------

If you are having issues, please let us know.

License
-------

MIT License

Copyright (c) 2017 Gasper Vozel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
