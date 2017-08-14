kph
===

Python 2/3 ready implementation of the Kölner Phonetik
(http://de.wikipedia.org/wiki/K%C3%B6lner\_Phonetik) algorithm.

Usage
-----

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

License
-------

    kph - Python module implementing the 'Koelner Phonetik' algorithm.
    Copyright (C) 2011  Robert Schindler

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Copyright
---------

Copyright 2011 by Robert Schindler <robert-sch@gmx.net>. Python 3
compatibility added by Michael Herrmann &lt;\[first name\] at \[last
name\].io&gt;.
