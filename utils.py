#!/usr/bin/env python

import hashlib
import os

def generateToken():
    """
    生成一个可用的Token
    """
    return hashlib.sha1(os.urandom(128)).hexdigest()
