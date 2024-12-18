import os

import eel
import pyautogui
from auth_admin import login_admin
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import read_json_file
from post_api import add_position, add_bonus, add_deduction, add_tax_rate, add_bonus_error

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Lấy đường dẫn tới file hiện tại
admin_path = os.path.join(parent_dir, "auth", "admin")


eel.init('../web')
@eel.expose
def login():
    result = login_admin(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def add_position_main():
    result = add_position(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def add_bonus_main():
    result = add_bonus(WebDriverWait, EC, time, By, admin_path)
    return result
@eel.expose
def add_bonus_error_main():
    result = add_bonus_error(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def add_deduction_main():
    result = add_deduction(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def add_tax_rate_main():
    result = add_tax_rate(WebDriverWait, EC, time, By, admin_path)
    return result

@eel.expose
def get_tool_data():
    data = read_json_file()
    return data

#Init html
width = pyautogui.size().width
height = pyautogui.size().height
eel.start('index.html',size=(width,height))

