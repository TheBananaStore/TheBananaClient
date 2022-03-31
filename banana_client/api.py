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
import re

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
        
class FilenameNotSpecifiedError(Exception):
    """
    Exception raised when a filename is not specified.
    
    :meta private:
    """

    def __init__(self):
        Exception.__init__(
            self, "Filename is not specified, or the default one is used."
        )


# ----------Private Methods----------


def _get_index() -> dict:
    """
    Returns JSON loaded into a dict from the mirror
    """
    return json.loads(urlopen("http://mirror.thebananastore.cf/" + "index.json").read())

# ----------Public Methods----------

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
        applist.append(app["name"])

    return applist


def search_appindex(query: str,  download: bool = False,  filename: str = "/fake",  channel: str = "stable") -> list:
    """
    Get the closest matches for the apps. Searches the names, description, and the website.

    Parameters:
    
    * query
        A string for the query.
    * download
        A boolean, if ``True``, it re-downloads the index. Elseway, it takes a path from ``filename``.
    * filename
        Only needed if ``download`` parameter is set to ``False``. Path to the already-downloaded index.
    * channel
        Only needed if ``download`` is set to ``True``. Channel for downloading the index from. Default is ``"stable"``
    """
    
    if download == False and filename in ["",  "/fake"]:
        raise FilenameNotSpecifiedError
    
    if download:
        namelist = get_appindex(channel)
    else:
        with open(filename) as file:
            namelist = list()
            namelist = json.loads(file.read())
    
    results = list()
    for appname in namelist:
        for field in ["name", "description",  "website"]:
            result = re.search(query, appname[field],  flags=re.IGNORECASE)
            if result != None and appname not in results:
                results.append(appname["name"])

    return results
    
