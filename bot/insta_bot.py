from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException


class InstaBot:
    WAIT_TIME = 20
    INSTAGRAM_URL = 'https://www.instagram.com/'
    GECKODRIVER_PATH = r'./webdrivers/geckodriver'
    LOGIN = r"//input[@name='username']"
    PASSWORD = r"//input[@name='password']"
    LOGIN_SUBMIT = r"//button[@type='submit']"
    NOT_SAVE_LOGIN_DATA = r"//button[text()='Agora não']"
    SEARCH_FIELD = r"//input[@placeholder='Pesquisar']"
    USER_PHOTO = r"/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[{line}]/div[{column}]"  # NOQA
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

    def login(self, username, password):
        self.driver.get(self.INSTAGRAM_URL)
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

    def is_logged_in(self):
        element_proves_login = self.SEARCH_FIELD
        return self._have_element_by_xpath(element_proves_login)

    def _have_element_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def go_to_home_of(self, target_username):
        self.driver.get(self.INSTAGRAM_URL+target_username)

    def open_user_photo(self, line, column):
        photo = self.driver.find_element_by_xpath(
            self.USER_PHOTO.format(line=line, column=column)
        )
        photo.click()
