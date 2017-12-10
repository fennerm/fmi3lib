"""Personal library code for i3 scripting"""
import i3

def empty_workspace():
    """Return the index of the first empty workspace"""
    workspaces = i3.get_workspaces()
    for i in range(1, len(workspaces)):
        if i != workspaces[i]['num'] - 1:
            return i + 1
    return i + 2



def focused_workspace():
    """Return the number of the workspace that is currently in focus"""
    for workspace in i3.get_workspaces():
        if workspace['focused']:
            return workspace['num']
    raise OSError("Can't find a focused workspace")
