'''
Copyright (C) 2022  Alexey Pavlov <pezleha@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

'''

# Imports
from urllib.request import urlopen
import json

# ----------Errors----------
class InvalidChannelError(Exception):
    def __init__(self):
        Exception.__init__(self, 'Invalid channel name selected. Please use available channel names.')

# ----------Methods----------

def _get_index() -> dict:
    return json.loads(urlopen("http://thebananastore.github.io/TheBananaStore/" + "index.json").read())

def get_applist(channel = "stable") -> dict:
    """
    Get the Banana Store's App List.
    Parameters
    ----------
    channel
        A string indicating the channel to check. Can be "stable", "unstable", or "testing".
    """
    
    if channel not in ["stable",  "testing",  "unstable"]:
        raise InvalidChannelError
    
    return _get_index()[channel.lower()]
