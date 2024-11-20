import eel
import pyautogui
from auth_admin import login_admin
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import read_json_file
eel.init('../web')
@eel.expose
def login():
    result = login_admin(WebDriverWait, EC, time, By)
    return result

@eel.expose
def get_tool_data():
    data = read_json_file()
    return data

#Init html
width = pyautogui.size().width
height = pyautogui.size().height
eel.start('index.html',size=(width,height))

