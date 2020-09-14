from selenium.common.exceptions import NoSuchElementException

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
    else:
        return element.text if hasattr(element, 'text') else None
