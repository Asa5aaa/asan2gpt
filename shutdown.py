state = {"shutdown": False}

def turn_off():
    state["shutdown"] = True

def turn_on():
    state["shutdown"] = False

def check_shutdown():
    return state["shutdown"]
