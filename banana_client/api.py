#
# Copyright (C) 2022  Alexey Pavlov <pezleha@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Please don't make this message a docstring. It breaks sphinx autodoc.


# Imports
from urllib.request import urlopen
import json
from difflib import get_close_matches

# ----------Errors----------
class InvalidChannelError(Exception):
    """
    Exception raised when a passed channel is incorrect.
    
    :meta private:
    """

    def __init__(self):
        Exception.__init__(
            self, "Invalid channel name selected. Please use available channel names."
        )


# ----------Methods----------


def _get_index() -> dict:
    """
    Returns JSON loaded into a dict from the mirror
    """
    return json.loads(urlopen("http://mirror.thebananastore.cf" + "index.json").read())


def get_appindex(channel: str = "stable") -> dict:
    """
    Get the Banana Store's App Index as a Python Dict.
    Behind the scenes, it calls an internal function, ``_get_index()`` and extracts the channel dictionary from it.

    Parameters:
    
    * channel
        A string indicating the channel to check. Can be ``stable``, ``unstable``, or ``testing``.
    """

    if channel not in ["stable", "testing", "unstable"]:
        raise InvalidChannelError

    return _get_index()[channel.lower()]


def get_app_name_list(channel: str = "stable") -> list:
    """
    Get the names of apps available in a channel as a list.
    Behind the scenes, it actually calls ``get_appindex`` and parses it.

    Parameters:
    
    * channel
        A string indicating the channel to check. Can be ``stable``, ``unstable``, or ``testing``.
    """

    applist = list()
    index = get_appindex(channel)

    for app in index:
        applist.append(index[app]["name"])

    return applist


def search_applist(query: str) -> list:
    """
    Get the closest matches for the apps.
    Currently it re-downloads the index again. 

    Parameters:
    
    * query
        A string for the query.
    """
    
    # TODO: collect everything from a local file

    return get_close_matches(query, get_app_name_list())
