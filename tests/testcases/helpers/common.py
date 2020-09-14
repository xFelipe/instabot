from selenium.common.exceptions import NoSuchElementException

def element_exists_by_xpath(bot, xpath):
    try:
        bot.driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
