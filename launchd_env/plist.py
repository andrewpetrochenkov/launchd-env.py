#!/usr/bin/env python
import plistlib


def read(path):
    if hasattr(plistlib, "load"):
        return plistlib.load(open(path, 'rb'))
    return plistlib.readPlist(path)


def write(path, data):
    if data != read(path):
        if hasattr(plistlib, "dump"):
            plistlib.dump(data, open(path, 'wb'))
        else:
            plistlib.writePlist(data, path)
