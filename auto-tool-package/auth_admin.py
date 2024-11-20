from selenium import webdriver
admin = "C:\\Users\\Hong Phuc\\Desktop\\Study\\Ki1-Nam4\\Project1\\AutomationTest\\auth\\admin"

def login_admin(WebDriverWait, EC, time, By):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+admin)
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
        time.sleep(2)
        driver.refresh()
        time.sleep(10)
        return "Test auth admin successfully"
    except Exception as e:
        print(f"An error occurred: {e}")  # In ra thông báo lỗi
        return "An error occurred during login."
    finally:
        driver.quit()