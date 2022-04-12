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

import subprocess

import os_release


class PackageManagerNotFoundError(Exception):
    """
    Exception raised when a supported package manager is not found.
    
    :meta private:
    """

    def __init__(self):
        Exception.__init__(
            self,
            "No dependency-resolving package manager was found. Please install one from the list on the official documentation.",
        )


class OSNotSupportedError(Exception):
    """
    Exception raised when a OS is not supported.
    
    :meta private:
    """

    def __init__(self):
        Exception.__init__(
            self,
            "The OS you are using is not supported or the os-release file is incorrect.",
        )


def install_packages(pkgs: list):

    release = os_release.current_release()

    if release.is_like("debian"):
        if os.path.exists("usr/bin/apt"):
            subprocess.call(["/usr/bin/apt", "install", "-y"] + pkgs)
        elif os.path.exists("/usr/bin/aptitude"):
            subprocess.call(["/usr/bin/aptitude", "install", "-y"] + pkgs)
        else:
            raise PackageManagerNotFoundError
    elif release.is_like("rhel"):
        if os.path.exists("/usr/bin/dnf"):
            subprocess.call(["/usr/bin/dnf", "install"] + pkgs)
        elif os.path.exists("/usr/bin/yum"):
            subprocess.call(["/usr/bin/yum", "install"] + pkgs)
        else:
            raise PackageManagerNotFoundError
    elif release.is_like("arch"):
        if os.path.exists("/usr/bin/pacman"):
            subprocess.call(["/usr/bin/pacman", "-S"] + pkgs)
        else:
            raise PackageManagerNotFoundError

    else:
        raise OSNotSupportedError
