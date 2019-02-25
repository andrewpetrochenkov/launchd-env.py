#!/usr/bin/env python
import plistlib
import public


@public.add
def read(path):
    """return a dictionary with plist file environment variables"""
    if hasattr(plistlib, "load"):
        data = plistlib.load(open(path, 'rb'))
    data = plistlib.readPlist(path)
    return data.get("EnvironmentVariables", {})


@public.add
def write(path, **vars):
    """write environment variables to a plist file"""
    data = read(path)
    data["EnvironmentVariables"] = vars
    if data != read(path):
        if hasattr(plistlib, "dump"):
            plistlib.dump(data, open(path, 'wb'))
        else:
            plistlib.writePlist(data, path)
