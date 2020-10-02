#!/usr/bin/env python3
# The script will work on Linux only.

import os
import sys

def check_reboot():
    """ Returns True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot")
        sys.exit(1)
    print("Everyhting ok")
    sys.exit(0)

main()