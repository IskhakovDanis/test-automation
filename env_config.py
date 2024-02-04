import os
from support.json_handler import JSONHandler


class ConfigPath:
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    SECRETS = os.path.join(ROOT_PATH, "files", "secrets.json")


class ConfigURL:
    BASE_URL = "https://toghrulmirzayev.github.io/ui-simulator"
    HOVER_AND_SELECT_URL = f"{BASE_URL}/hover_and_select.html"
    INPUT_AND_CLICK = f"{BASE_URL}/input-and-click.html"
    DRAG_AND_DROP = f"{BASE_URL}/drag-and-drop.html"

class Secrets:

    USERNAME = JSONHandler.load_json('username', ConfigPath.SECRETS)
    PASSWORD = JSONHandler.load_json('password', ConfigPath.SECRETS)

print(f"secret username is {Secrets.USERNAME}")
print(f"secret username is {Secrets.PASSWORD}")