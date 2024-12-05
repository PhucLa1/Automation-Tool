import os
import eel
import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import read_json_file
from post_api import add_position, login_admin, add_contract, approve_decline
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Lấy đường dẫn tới file hiện tại
admin_path = os.path.join(parent_dir, "auth", "admin")


eel.init('../web')
@eel.expose
def login_admin_main():
    result = login_admin(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def add_position_main():
    result = add_position(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def add_contract_main():
    result = add_contract(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def approve_decline_main():
    result = approve_decline(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def get_tool_data():
    data = read_json_file()
    return data

#Init html
width = pyautogui.size().width
height = pyautogui.size().height
eel.start('index.html',size=(width,height))

