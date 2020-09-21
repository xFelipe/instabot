from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException


class InstaBot:
    WAIT_TIME = 20
    # XPATHS
    INSTAGRAM_URL = 'https://www.instagram.com/'
    GECKODRIVER_PATH = r'./webdrivers/geckodriver'
    LOGIN = r"//input[@name='username']"
    PASSWORD = r"//input[@name='password']"
    LOGIN_SUBMIT = r"//button[@type='submit']"
    NOT_SAVE_LOGIN_DATA = r"//button[text()='Agora não']"
    SEARCH_FIELD = r"//input[@placeholder='Pesquisar']"
    USER_PHOTO = r"/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[{line}]/div[{column}]"  # NOQA
    OPEN_PHOTO_XPATH = r"/html/body/div[4]/div[2]/div/article/div[2]"
    WHO_LIKES_PHOTO = r"/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div[2]/button"  # NOQA
    WHO_LIKES_DIV = "/html/body/div[5]/div[@role='dialog']"

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

    def _have_element_by_xpath(self, xpath):
        """Checa existência de elemento na tela através de seu xpath."""
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def login(self, username, password):
        """Faz login no no instagram e tira mensagens iniciais"""
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
        """Verifica se o login está realizado através da presença da busca."""
        element_proves_login = self.SEARCH_FIELD
        return self._have_element_by_xpath(element_proves_login)

    def go_to_home_of(self, target_username):
        """Abre o instagram de determinado usuário."""
        self.driver.get(self.INSTAGRAM_URL+target_username)

    def open_user_photo(self, line, column):
        """Abre a foto de determinada linha e coluna de uma home."""
        photo = self.driver.find_element_by_xpath(
            self.USER_PHOTO.format(line=line, column=column)
        )
        photo.click()

    def a_photo_is_open(self):
        return self._have_element_by_xpath(self.OPEN_PHOTO_XPATH)

    def open_who_liked_photo(self):
        who_likes = self.driver.find_element_by_xpath(self.WHO_LIKES_PHOTO)
        who_likes.click()

    def likes_list_is_open(self):
        return self._have_element_by_xpath(self.WHO_LIKES_DIV)
