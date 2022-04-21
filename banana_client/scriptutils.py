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

import os
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

def get_package_manager() -> str:
    """
    Get the preferred OS package manager as a string.
    """
    
    release = os_release.current_release()

    if release.is_like("debian"):
        if os.path.exists("usr/bin/apt"):
            return "apt"
        elif os.path.exists("/usr/bin/aptitude"):
           return "aptitude"
        else:
            raise PackageManagerNotFoundError
    elif release.is_like("rhel"):
        if os.path.exists("/usr/bin/dnf"):
            return "dnf"
        elif os.path.exists("/usr/bin/yum"):
            return "yum"
        else:
            raise PackageManagerNotFoundError
    elif release.is_like("arch"):
        if os.path.exists("/usr/bin/pacman"):
            return "pacman"
        else:
            raise PackageManagerNotFoundError
    elif release.is_like("gentoo"):
        if os.path.exists("/usr/bin/emerge"):
            return "emerge"
        else:
            raise PackageManagerNotFoundError

    else:
        raise OSNotSupportedError
        
def get_package_manager_install_arguments(manager: str) -> list:
    
    if manager in ["apt",  "aptitude",  "dnf",  "yum"]:
        return ["install",  "-y"]
        
    elif manager == "pacman":
        return ["noconfirm","-S"]
    elif manager == "emerge":
        return ["-uD"]
    else:
        raise OSNotSupportedError
def install_packages(pkgs: list):
    """
    Install the packages via the system's package manager. 
    If no compaptible package manager is found, ``OSNotSupportedError`` is raised.
    If the OS release is detected and is supported but a package manager is not found, ``PackageManagerNotFoundError`` is raised.
    
    Parameters:
    
    * pkgs
        A list with package strings.
    """
    
    manager = get_package_manager()
    args = get_package_manager_install_arguments(manager)
    
    subprocess.call([manager,  args] + pkgs)
        
