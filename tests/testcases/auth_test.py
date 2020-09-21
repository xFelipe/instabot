from decouple import config
from instabot.tests.testcases.helpers.common import element_exists_by_xpath

ARTICLE_XPATH = r"//article[@role='presentation']"

def test_login(bot):
    """Verifica se o bot consta como logado após processo de login"""
    bot.login(config('INSTA_USERNAME'), config('INSTA_PASSWORD'))
    assert bot.is_logged_in(), 'Bot não se reconhece como logado após login.'

def test_not_login_takes_the_user_not_logged(bot):
    """Verifica se o bot consta como logado após processo de login"""
    assert not bot.is_logged_in(), \
        'Bot se reconhece como logado sem fazer o processo de login.'

def test_login_move_user_to_home_page_with_a_article(bot):
    """Verifica se algum post é exibido após processo de login."""
    bot.login(config('INSTA_USERNAME'), config('INSTA_PASSWORD'))
    assert element_exists_by_xpath(bot, ARTICLE_XPATH),\
        'Após login, não foi possível ver um post em home.'
