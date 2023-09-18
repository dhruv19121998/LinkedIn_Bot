from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
# rest of the code


# Input Email id/ Username & password
Username = input("Enter the Username: ")
Passcode = input("Enter the Password: ")
Look = input("Enter whatever u wanted to search:")

# Set browser Properties and webdriver-wait 
driver = webdriver.Chrome()
driver2 = webdriver.Safari()
wait = WebDriverWait(driver, 10)

# Visit LinkedIn
driver.get('https://www.linkedin.com/home')

# Click on Username/Email_Id field and type
Email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="session_key"]')))
Email.send_keys(Username + Keys.TAB)

# Click on Password field and type
Password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="session_password"]')))
Password.send_keys(Passcode + Keys.ENTER)

wait.until(EC.title_contains("LinkedIn"))

sleep(20)  # Wait for 10 seconds


# Search
Search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input')))
Search.send_keys(Look + Keys.ENTER)

# People
People = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')))
People.click()

# Scroll down and press the Connect butto

while True:
    try:
        connect_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'artdeco-button__text')))
        for button in connect_buttons:
            if button.text == 'Connect':
                button.click()
                try:
                    # Wait for the "Classmates" button to become clickable
                    classmates_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Classmates']")))
                    classmates_button.click()
                    final_connect = driver.find_element(By.XPATH,"//span[text()='Connect']")
                    final_connect.click()
                    final_send = driver.find_element(By.XPATH, "//span[text()='Send']")
                    final_send.click()
                except:
                    final_send = driver.find_element(By.XPATH, "//span[text()='Send']")
                    final_send.click()
                    # If the "Classmates" button is not clickable, just continue to the next button
                driver.execute_script("arguments[0].scrollIntoView();", button)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Next']")))
        next_button.click()
    except StaleElementReferenceException:
        continue
    except TimeoutException:
        continue

