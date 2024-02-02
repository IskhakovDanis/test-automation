import os



class ConfigPath:
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))



class ConfigURL:
    BASE_URL = "https://toghrulmirzayev.github.io/ui-simulator"
    HOVER_AND_SELECT_URL = f"{BASE_URL}/hover_and_select.html"
    INPUT_AND_CLICK = f"{BASE_URL}/input-and-click.html"
    DRAG_AND_DROP = f"{BASE_URL}/drag-and-drop.html"