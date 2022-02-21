# -*- coding: utf-8

# kph - Python module implementing the 'Koelner Phonetik' algorithm.
# Copyright (C) 2008-2017 Robert Schindler
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
This module implements the 'Koelner Phonetik'.

Examples of usage:
>>> encode("Moritz Müller")
'678657'
>>> encode("Moriz Müler")
'678657'
>>> encode("Laura Mayer")
'5767'
>>> encode("Laura Meier")
'5767'
"""


__version__ = "0.4.1"
__all__     = ["encode"]


try:
    # for static type checking
    import typing
except ImportError:
    pass


import collections
import re


RULES = collections.OrderedDict() \
        # type: typing.collections.OrderedDict[typing.Pattern[str], str]
RULES[re.compile(r".[AEIJOUYÄÖÜ].", re.I)]    = "0"
RULES[re.compile(r".[B].", re.I)]             = "1"
RULES[re.compile(r".[P][^H]", re.I)]          = "1"
RULES[re.compile(r".[DT][^CSZ]", re.I)]       = "2"
RULES[re.compile(r".[FVW].", re.I)]           = "3"
RULES[re.compile(r".[P][H]", re.I)]           = "3"
RULES[re.compile(r".[GKQ].", re.I)]           = "4"
RULES[re.compile(r"\s[C][AHKLOQRUX]", re.I)]  = "4"
RULES[re.compile(r"[^SZ][C][AHKOQUX]", re.I)] = "4"
RULES[re.compile(r"[^CKQ][X].", re.I)]        = "48"
RULES[re.compile(r".[L].", re.I)]             = "5"
RULES[re.compile(r".[MN].", re.I)]            = "6"
RULES[re.compile(r".[R].", re.I)]             = "7"
RULES[re.compile(r".[SZß].", re.I)]           = "8"
RULES[re.compile(r"[SZ][C].", re.I)]          = "8"
RULES[re.compile(r"\s[C][^AHKLOQRUX]", re.I)] = "8"
RULES[re.compile(r".[C][^AHKOQUX]", re.I)]    = "8"
RULES[re.compile(r".[DT][CSZ]", re.I)]        = "8"
RULES[re.compile(r"[CKQ][X].", re.I)]         = "8"

INVALID_CHAR_PATTERN = re.compile(r"[^a-zäöüß\s]", re.I)


def encode(inputstring):  # type: (str) -> str
    """
    encode(string inputstring) -> string
      Returns the phonetic code of given inputstring.
    """

    # remove anything except characters and whitespace
    inputstring = INVALID_CHAR_PATTERN.sub("", inputstring)

    encoded = ""
    for i in range(len(inputstring)):
        part = inputstring[i-1 : i+2]
        if len(inputstring) == 1:
            part = " %s " % inputstring[0]
        elif i == 0:
            part = " %s" % inputstring[:2]
        elif i == len(inputstring) - 1:
            part = "%s " % inputstring[i - 1:]

        for rule, code in RULES.items():
            if rule.match(part):
                encoded += code
                break

    # remove immediately repeated occurrences of phonetic codes
    while [v for v in RULES.values() if encoded.find(v*2) != -1]:
        for v in RULES.values():
            encoded = encoded.replace(v*2, v)

    if encoded:
        encoded = encoded[0] + encoded[1:].replace("0", "")

    return encoded
