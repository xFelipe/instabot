from decouple import config
from instabot.tests.testcases.helpers.common import get_element_text_by_xpath

def test_insta_bot_have_webdriver(bot):
    """Verifica se o bot possui um webdriver após ser iniciado."""
    assert hasattr(bot, 'driver'), 'Bot não possui um webdriver.'

def test_redirect_to_another_user_page_and_check_username(bot):
    """Verifica redirecionamento de bot para a página de um usuário."""
    instagram_url = r'https://www.instagram.com/'
    username = r'duartepaula23'
    username_xpath = r"/html/body/div[1]/section/main/div/header/section/div[1]/h2"  # noqa

    bot.login(config('INSTA_USERNAME'), config('INSTA_PASSWORD'))
    bot.driver.get(instagram_url+username)
    assert get_element_text_by_xpath(bot, username_xpath) == username, \
        'Redirecionamento para página de usuário falhou.'
