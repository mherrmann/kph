# kph
Python 2/3 ready implementation of the [Kölner Phonetik](http://de.wikipedia.org/wiki/K%C3%B6lner_Phonetik) phonetic algorithm. Based on the original work of Robert Schindler.

# Usage
    >>> import kph
    >>> kph.encode("Horst Meier")
    '078267'
    >>> kph.encode("Horst Mayer")
    '078267'
    >>> kph.encode("Horst Meier") == kph.encode("Horst Mayer")
    True
    >>> kph.encode("Detlef Krumm") == kph.encode("Detlef Krum") == \
    ... kph.encode("Detlef Krunn") == kph.encode("Detlef Krun")
    True

# Copyright
Original copyright (C) 2011 by Robert Schindler <robert-sch@gmx.net>. Python 3 port copyright 2015 Michael Herrmann ([first name] at [last name].io).