# -*- coding: utf-8 -*-
"""
@author: prasaanth s
"""

for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):
            if a*a + b*b == c*c:
                print(a,b,c)
            else:
                continue