#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)
print(type(s))
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
