#!/usr/bin/python3
""" a function that returns a list of available attritubes """

def lookup(obj):
    """Return a list of an object's available attributes"""
    return (dir(obj))
