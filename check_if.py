#!/usr/bin/env python
# -*- coding: utf-8 -*-
import netifaces

# For netifaces
# On debian/raspbian/kali:
# apt-get install python3-dev
# On every distro:
# pip-3.2 install netifaces

def is_interface_up(interface):
    try:
        addr = netifaces.ifaddresses(interface)
        return netifaces.AF_INET in addr
    except ValueError:
        return False

print (is_interface_up("tun0"))


