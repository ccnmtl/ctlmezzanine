ctlmezzanine is a custom Mezzanine template similar to
[ccnmtldjango](https://github.com/ccnmtl/ccnmtldjango).
It's meant to be used with the `mezzanine-project` command provided
by Mezzanine.

# Installation

    $ virtualenv ~/ve
    $ source ~/ve/bin/activate
    $ pip install Mezzanine
    $ mezzanine-project \
      --template=https://github.com/nikolas/ctlmezzanine/archive/master.tar.gz \
      --name=Makefile \
      myproject
