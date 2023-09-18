from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class LinkedInBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get('https://www.linkedin.com/home')
        email_field = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="session_key"]')))
        email_field.send_keys(self.username + Keys.TAB)
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="session_password"]')))
        password_field.send_keys(self.password + Keys.ENTER)
        self.wait.until(EC.title_contains("LinkedIn"))
        sleep(20)

    def search(self, keyword):
        search_field = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input')))
        search_field.send_keys(keyword + Keys.ENTER)
        people_filter = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')))
        people_filter.click()

    def connect(self):
        while True:
            try:
                connect_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'artdeco-button__text')))
                for button in connect_buttons:
                    if button.text == 'Connect':
                        button.click()
                        try:
                            classmates_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Classmates']")))
                            classmates_button.click()
                            final_connect = self.driver.find_element(By.XPATH,"//span[text()='Connect']")
                            final_connect.click()
                            final_send = self.driver.find_element(By.XPATH, "//span[text()='Send']")
                            final_send.click()
                        except:
                            final_send = self.driver.find_element(By.XPATH, "//span[text()='Send']")
                            final_send.click()
                        self.driver.execute_script("arguments[0].scrollIntoView();", button)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                next_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Next']")))
                next_button.click()
            except (StaleElementReferenceException, TimeoutException):
                continue

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")
    keyword = input("Enter whatever u wanted to search:")
    bot = LinkedInBot(username, password)
    bot.login()
    bot.search(keyword)
    bot.connect()
    bot.quit()
