docs.scipy.org front page
=========================

This repository contains the Sphinx source for the front page of
https://docs.scipy.org/

The documentation itself comes from the Numpy and Scipy main repositories.

After cloning this repository, run::

    $ git submodule init
    $ git submodule update

To get the Sphinx theme used.

To make a local build of the website::

    $ make dist

To build and upload the site (requires ssh access to www.scipy.org)::

    $ make upload USER=myusername

