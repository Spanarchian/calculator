#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example Google style docstrings."""


def helloworld():
    """Return the pathname of the KOS root directory."""
    print("Hello World ! this is my first pip package")


def plus(ref):
    """Return the pathname of the KOS root directory."""
    res = ref+ref
    return res


def sqr(ref):
    """Return the pathname of the KOS root directory."""
    return ref * ref


def cube(ref):
    """Return the pathname of the KOS root directory."""
    return ref * ref * ref


def name(ref):
    """Return the pathname of the KOS root directory."""
    numnames = ["Zero", "One", "Two", "Three", "Four", "To be added"]
    if ref < 5:
        spelling = numnames[ref]
    else:
        spelling = numnames[5]
    return spelling
