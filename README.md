This repository contains a sample Python app demonstrating some of the
Sandstorm platform features.  It was built as a testcase for
[vagrant-spk](https://github.com/zarvox/vagrant-spk)'s support for a Python stack.

To build this Sandstorm package:

    git clone git://github.com/zarvox/vagrant-spk
    git clone git://github.com/zarvox/python-app-to-package-for-sandstorm
    export PATH=$(pwd)/vagrant-spk:$PATH
    cd python-app-to-package-for-sandstorm
    vagrant-spk setupvm uwsgi
    vagrant-spk up
    vagrant-spk init
    # edit .sandstorm/sandstorm-pkgdef.capnp in your editor of choice
    vagrant-spk dev
    # visit http://local.sandstorm.io:6080 in a web browser
    # log in as Alice, the admin account
    # launch an instance of the example app, play around with it
    # then, press Ctrl-C to stop the tracing vagrant-spk dev
    vagrant-spk pack example.spk
    # You now have an .spk file.  Yay!
