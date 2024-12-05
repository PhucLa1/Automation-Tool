from selenium import webdriver
from selenium.webdriver.support.select import Select


def add_position(WebDriverWait, EC, time, By, path):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/company/position')
        wait = WebDriverWait(driver, 10)
        btn_add = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')))
        btn_add.click()
        txt_position_name =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]')))
        txt_position_name.send_keys("Vij tri a")
        txt_amount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="totalPositionsNeeded"]')))
        txt_amount.send_keys("4")
        drop_department = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rd:"]/form/div[1]/div[3]/select')))
        select = Select(drop_department)
        select.select_by_index(1)
        btn_save = wait.until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "radix-:rd:"] / form / div[2] / button[2]')))
        btn_save.click()
        time.sleep(10)
        driver.quit()
        return "Success"
    except:
        return "Error";

def add_bonus(WebDriverWait, EC, time, By, path):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/salary-components/bonus')
        wait = WebDriverWait(driver, 10)
        btn_add = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')))
        btn_add.click()
        txt_bonus_name =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]')))
        txt_bonus_name.send_keys("Thưởng thêm Đóng góp cá nhân")
        txt_bonus_amount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="amount"]')))
        txt_bonus_amount.send_keys("2500000")
        btn_save = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rv:"]/form/div[2]/button[2]')))
        btn_save.click()
        time.sleep(10)
        driver.quit()
        return "Success"
    except:
        return "Error";

def add_bonus_error(WebDriverWait, EC, time, By, path):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/salary-components/bonus')
        wait = WebDriverWait(driver, 10)
        btn_add = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')))
        btn_add.click()
        txt_bonus_name =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]')))
        txt_bonus_name.send_keys("Thưởng thêm tiết kiệm")
        txt_bonus_amount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="amount"]')))
        txt_bonus_amount.send_keys("-10000")
        btn_save = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rv:"]/form/div[2]/button[2]')))
        btn_save.click()
        time.sleep(10)
        driver.quit()
        return "Success"
    except:
        return "Error";
def add_deduction(WebDriverWait, EC, time, By, path):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/salary-components/deduction')
        wait = WebDriverWait(driver, 10)
        btn_add = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')))
        btn_add.click()
        txt_deducion_name =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]')))
        txt_deducion_name.send_keys("Khấu trừ Vi phạm luật Giao Thông")
        txt_deducion_amount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="amount"]')))
        txt_deducion_amount.send_keys("500000")
        btn_save = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rv:"]/form/div[2]/button[2]')))
        btn_save.click()
        time.sleep(10)
        driver.quit()
        return "Success"
    except:
        return "Error";

def add_tax_rate(WebDriverWait, EC, time, By, path):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://localhost:3000/salary-components/tax-rate')
        wait = WebDriverWait(driver, 10)
        btn_add = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')))
        btn_add.click()
        txt_tax_rate_name =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]')))
        txt_tax_rate_name.send_keys("Trên 10 trđ đến 25 trđ")
        wait = WebDriverWait(driver, 10)
        txt_tax_rate_percent = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="percent"]')))
        txt_tax_rate_percent.send_keys("0.04")
        txt_tax_rate_min_tax_income = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="minTaxIncome"]')))
        txt_tax_rate_min_tax_income.send_keys("10000000")
        txt_tax_rate_max_tax_income = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="maxTaxIncome"]')))
        txt_tax_rate_max_tax_income.send_keys("25000000")
        wait = WebDriverWait(driver, 10)
        txt_tax_rate_condition = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="condition"]')))
        txt_tax_rate_condition.send_keys("Thu nhập tính thuế /tháng > 10 triệu đồng (trđ) và <= 25 triệu đồng (trđ)")
        btn_save = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="radix-:rv:"]/form/div[2]/button[2]')))
        btn_save.click()
        time.sleep(10)
        driver.quit()
        return "Success"
    except:
        return "Error";