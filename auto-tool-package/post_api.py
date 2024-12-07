from selenium import webdriver
from selenium.webdriver.support.select import Select

def login_admin(WebDriverWait, EC, time, By, path):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/login-admin')
        wait = WebDriverWait(driver, 10)
        txt_email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r0:-form-item"]')))
        txt_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r1:-form-item"]')))
        txt_email.send_keys("phucminhbeos@gmail.com")
        txt_password.send_keys("Phucdeptrai")
        time.sleep(2)
        btn_login = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/form/div/button')))
        btn_login.click()
        time.sleep(1000)
        return "Test auth admin successfully"
    except Exception as e:
        print(f"An error occurred: {e}")  # In ra thông báo lỗi
        return "An error occurred during login."
    finally:
        driver.quit()

def add_position(WebDriverWait, EC, time, By, path):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/company/position')
        wait = WebDriverWait(driver, 10)
        btn_add = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')))
        btn_add.click()
        txt_position_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]')))
        txt_position_name.send_keys("Vij tri a")
        txt_amount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="totalPositionsNeeded"]')))
        txt_amount.send_keys("4")
        drop_department = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rd:"]/form/div[1]/div[3]/select')))
        select = Select(drop_department)
        select.select_by_index(1)
        btn_save = wait.until(
            EC.presence_of_element_located((By.XPATH, '// *[ @ id = "radix-:rd:"] / form / div[2] / button[2]')))
        btn_save.click()
        time.sleep(10)
        driver.quit()
        return "Success"
    except:
        return "Error"


def add_contract(WebDriverWait, EC, time, By, path):
    try:
        # edge_options = webdriver.EdgeOptions()
        # edge_options.add_argument("--start-maximized")  # Mở trình duyệt ở chế độ toàn màn hình
        # edge_options.add_argument("user-data-dir="+path)
        # driver = webdriver.Edge(options=edge_options)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=" + path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/contract/contract-list')
        wait = WebDriverWait(driver, 10)
        btn_add = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')))
        btn_add.click()
        # Fill
        txt_employee_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="name"]')))
        txt_employee_name.send_keys("Nguyễn Văn Tự Động")
        txt_address = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="address"]')))
        txt_address.send_keys("Số 420 đường Test, Thread City")
        txt_countrySide = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="countrySide"]')))
        txt_countrySide.send_keys("Bắc Ninh")
        txt_nationalid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="nationalID"]')))
        txt_nationalid.send_keys("008206000042")
        txt_nationaladdress = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="nationalAddress"]')))
        txt_nationaladdress.send_keys("Bắc Ninh")
        txt_level = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="level"]')))
        txt_level.send_keys("008206000042")
        txt_major = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="major"]')))
        txt_major.send_keys("008206000042")
        # Select
        # drop_contracttype = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rn:"]/form/div[1]/div[11]/select')))
        # selectcontracttype = Select(drop_contracttype)
        # selectcontracttype.select_by_index(1)
        # drop_department = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rn:"]/form/div[1]/div[15]/select')))
        # driver.execute_script("""
        #     arguments[0].value = arguments[1];
        #     arguments[0].dispatchEvent(new Event('input'));
        #     arguments[0].dispatchEvent(new Event('change'));
        # """, drop_department, "1")
        # selectdepartment = Select(drop_department)
        # selectdepartment.select_by_index(1)
        # drop_position = wait.until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rn:"]/form/div[1]/div[16]/select')))
        # selectposition = Select(drop_position)
        # selectposition.select_by_index(1)
        # drop_salary = wait.until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rn:"]/form/div[1]/div[17]/select')))
        # selectsalary = Select(drop_salary)
        # selectsalary.select_by_index(1)
        # drop_allowance = wait.until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rn:"]/form/div[1]/div[18]/div/div/div[1]/div[2]')))
        # selectallowance = Select(drop_allowance)
        # selectallowance.select_by_index(1)
        # selectallowance.select_by_index(2)
        # selectallowance.select_by_index(3)
        # drop_insurance = wait.until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rn:"]/form/div[1]/div[19]/div/div/div[1]/div[2]')))
        # selectinsurance = Select(drop_insurance)
        # selectinsurance.select_by_index(1)
        # selectinsurance.select_by_index(2)
        # selectinsurance.select_by_index(3)
        # DateTime
        txt_date_of_birth = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="date"]')))[0]
        txt_date_of_birth.send_keys("01-01-2000")
        txt_date_of_making_id = \
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="date"]')))[1]
        txt_date_of_making_id.send_keys("01-01-2022")
        txt_date_of_start = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="date"]')))[2]
        txt_date_of_start.send_keys("11-24-2024")
        txt_date_of_end = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="date"]')))[3]
        txt_date_of_end.send_keys("11-24-2026")
        btn_save = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rn4:"]/form/div[2]/div[2]/button[2]')))
        btn_save.click()
        driver.quit()
        return "Success"
    except:
        return "Error"

def approve_decline(WebDriverWait, EC, time, By, path):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/contract/contract-approval')
        wait = WebDriverWait(driver, 10)
        time.sleep(4)
        btn_approve = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="radix-:r9:-content-pending"]/div/div[2]/table/tbody/tr[1]/td[13]/div/button[1]')))
        btn_approve.click()
        time.sleep(3)
        btn_switch_approve = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="radix-:r9:-trigger-approved"]')))
        btn_switch_approve.click()
        time.sleep(5)
        btn_cancel = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="radix-:r9:-content-approved"]/div/div[2]/table/tbody/tr[1]/td[13]/div/button[2]')))
        btn_cancel.click()
        time.sleep(3)
        btn_switch_pending = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="radix-:r9:-trigger-pending"]')))
        btn_switch_pending.click()
        time.sleep(4)
        btn_decline = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="radix-:r9:-content-pending"]/div/div[2]/table/tbody/tr[1]/td[13]/div/button[2]')))
        btn_decline.click()
        time.sleep(3)
        btn_switch_denied = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="radix-:r9:-trigger-refused"]')))
        btn_switch_denied.click()
        time.sleep(20)
        driver.quit()
        return "Success"
    except:
        return "Error"