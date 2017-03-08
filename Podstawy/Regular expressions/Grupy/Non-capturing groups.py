#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

#named groups have the format(?P<name>...)
#where name is the name of the group, and ...
#is the content

match = re.match(pattern,"abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

