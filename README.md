[![Build Status](https://travis-ci.org/ccnmtl/ctlmezzanine.svg?branch=master)](https://travis-ci.org/ccnmtl/ctlmezzanine)

ctlmezzanine is a custom Mezzanine template similar to
[ccnmtldjango](https://github.com/ccnmtl/ccnmtldjango).
It's meant to be used with the `mezzanine-project` command provided
by Mezzanine.

# Installation

    $ virtualenv ~/ve
    $ source ~/ve/bin/activate
    $ pip install https://github.com/stephenmcd/mezzanine/archive/master.tar.gz
    $ mezzanine-project \
      --template=https://github.com/ccnmtl/ctlmezzanine/archive/master.tar.gz \
      --name=Makefile \
      myproject
    $ cd myproject
    $ make
