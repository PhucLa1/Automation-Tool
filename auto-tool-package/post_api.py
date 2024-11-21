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