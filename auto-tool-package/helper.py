import eel
import json

# Đọc dữ liệu từ file JSON
def read_json_file():
    with open('data_save.json', 'r') as f:
        data = json.load(f)
    return data