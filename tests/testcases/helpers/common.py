from selenium.common.exceptions import NoSuchElementException

HOME_USERNAME_XPATH = r"/html/body/div[1]/section/main/div/header/section/div[1]/h2"  # NOQA
OPEN_PHOTO_XPATH = '/html/body/div[4]/div[2]/div/article/div[2]'


def element_exists_by_xpath(bot, xpath):
    try:
        bot.driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def get_element_text_by_xpath(bot, xpath):
    try:
        element = bot.driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return None

    return element.text if hasattr(element, 'text') else None

def get_home_owner_username(bot) -> str:
    return get_element_text_by_xpath(bot, HOME_USERNAME_XPATH)

def a_photo_is_open(bot):
    from time import sleep; sleep(10)
    return element_exists_by_xpath(
        bot, OPEN_PHOTO_XPATH
    )
