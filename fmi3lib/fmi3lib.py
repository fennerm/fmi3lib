"""Personal library code for i3 scripting"""
import i3

def focused_workspace():
    """Return the number of the workspace that is currently in focus"""
    for workspace in i3.get_workspaces():
        if workspace['focused']:
            return workspace['num']
    raise OSError("Can't find a focused workspace")
