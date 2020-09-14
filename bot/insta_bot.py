from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException


class InstaBot:
    WAIT_TIME = 20
    GECKODRIVER_PATH = r'./webdrivers/geckodriver'
    LOGIN = r"//input[@name='username']"
    PASSWORD = r"//input[@name='password']"
    LOGIN_SUBMIT = r"//button[@type='submit']"
    NOT_SAVE_LOGIN_DATA = r"//button[text()='Agora não']"
    SEARCH_FIELD = r"//input[@placeholder='Pesquisar']"
    # r"/html/body/div[4]/div/div/div/div[3]/button[2]" | type="text"

    def __init__(self, silent: bool = False):
        options = Options()
        if silent:
            options.add_argument('--headless')

        self.driver = webdriver.Firefox(
            executable_path=self.GECKODRIVER_PATH, options=options
        )
        self.driver.implicitly_wait(self.WAIT_TIME)

    def __del__(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

    def is_logged_in(self):
        try:
            self.driver.find_element_by_xpath(self.SEARCH_FIELD)
        except NoSuchElementException:
            return False
        return True

    def login(self, username, password):
        self.driver.get('https://www.instagram.com/')
        find_element_by_xpath = self.driver.find_element_by_xpath

        find_element_by_xpath(self.LOGIN).send_keys(username)
        find_element_by_xpath(self.PASSWORD).send_keys(password)
        find_element_by_xpath(self.LOGIN_SUBMIT).click()
        try:
            find_element_by_xpath(self.NOT_SAVE_LOGIN_DATA).click()
            sleep(1)
            find_element_by_xpath(self.NOT_SAVE_LOGIN_DATA).click()
            sleep(1)
        except NoSuchElementException:
            pass
        sleep(2)
