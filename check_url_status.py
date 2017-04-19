#!/usr/bin/env python
# -*- coding: utf-8 -*-
import http.client

def testurl(site, path):
    try:
        conn = http.client.HTTPSConnection(site)
        conn.request("GET", path)
        r1 = conn.getresponse()
        #return (r1.status, r1.reason)
        return r1.status == 200
    except:
        return r1.status == 404

print (testurl("www.adamantio.net", "/index.htm"))

