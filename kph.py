# -*- coding: iso-8859-15 -*-


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


__version__ = "0.2"
__all__     = ["encode"]


import re


RULETABLE = {re.compile(r".[A|E|I|J|O|U|Y|Ä|Ö|Ü].", re.I):     "0",
             re.compile(r".[B].", re.I):                       "1",
             re.compile(r".[P][^H]", re.I):                    "1",
             re.compile(r".[D|T][^C|S|Z]", re.I):              "2",
             re.compile(r".[F|V|W].", re.I):                   "3",
             re.compile(r"[P][H].", re.I):                     "3",
             re.compile(r".[G|K|Q].", re.I):                   "4",
             re.compile(r"[\b][C][A|H|K|L|O|Q]", re.I):        "4",
             re.compile(r"[^S|Z][C][A|H|K|O|Q|U|X]", re.I):    "4",
             re.compile(r"[^C|K|Q][X].", re.I):                "48",
             re.compile(r".[L].", re.I):                       "5",
             re.compile(r".[M|N].", re.I):                     "6",
             re.compile(r".[R].", re.I):                       "7",
             re.compile(r".[S|Z|ß].", re.I):                   "8",
             re.compile(r"[S|Z][C].", re.I):                   "8",
             re.compile(r"\b[C][^A|H|K|L|O|Q|R|U|X]", re.I):   "8",
             re.compile(r".[C][^A|H|K|O|Q|U|X]", re.I):        "8",
             re.compile(r".[D|T][C|S|Z]", re.I):               "8",
             re.compile(r"[C|K|Q][X].", re.I):                 "8",
            }


def encode(inputstring):
  """
  encode(string inputstring) -> string
    Returns the phonetic code of inputstring
  """

  encoded = ""
  for i in range(len(inputstring)):
    part = inputstring[i - 1:i + 2]
    if len(inputstring) == 1:
      part = " %s " % inputstring[0]
    elif i == 0:
      part = " %s" % inputstring[:2]
    elif i == len(inputstring) - 1:
      part = "%s " % inputstring[i - 1:]
    for rule, code in RULETABLE.items():
      if rule.match(part):
        encoded += code
        break

  while [v for v in RULETABLE.values() if encoded.find(v * 2) != -1]:
    for v in RULETABLE.values():
      encoded = encoded.replace(v * 2, v)

  if encoded:
    encoded = encoded[0] + encoded[1:].replace("0", "")

  return encoded