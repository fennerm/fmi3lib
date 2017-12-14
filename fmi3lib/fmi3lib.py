"""Personal library code for i3 scripting"""
import i3
from plumbum import local
from plumbum.cmd import bash


def empty_workspace():
    """Return the index of the first empty workspace"""
    workspaces = i3.get_workspaces()
    nworkspaces = len(workspaces)
    for i in range(1, nworkspaces):
        if i != workspaces[i]['num'] - 1:
            return i + 1
    return nworkspaces + 1


def focused_workspace():
    """Return the number of the workspace that is currently in focus"""
    for workspace in i3.get_workspaces():
        if workspace['focused']:
            return workspace['num']
    raise OSError("Can't find a focused workspace")

def termite(instance, command):
    """Start termite in a new i3 window"""
    bash['-c', 'termite', "--hold", "--name", instance, "-e", command] & FG
