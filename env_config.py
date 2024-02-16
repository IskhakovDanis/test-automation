from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_1 = os.getenv("TOKEN_1")
TOKEN_2 = os.getenv("TOKEN_2")


def test_encryption(): # try printing your secrets while running the code in CI to check if they are really encrypted
    print(TOKEN_1)
    print(TOKEN_2)





class ConfigURL:
    BASE_URL = "https://toghrulmirzayev.github.io/ui-simulator"
    HOVER_AND_SELECT_URL = f"{BASE_URL}/hover_and_select.html"
    INPUT_AND_CLICK = f"{BASE_URL}/input-and-click.html"
    DRAG_AND_DROP = f"{BASE_URL}/drag-and-drop.html"

