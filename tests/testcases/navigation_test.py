from decouple import config
from instabot.tests.testcases.helpers.common import (
    get_element_text_by_xpath, get_home_owner_username, a_photo_is_open
)

ANOTHER_USER = 'duartepaula23'


def test_redirect_to_another_user_page_and_check_username(bot):
    """Verifica redirecionamento de bot para a página de um usuário."""
    bot.login(config('INSTA_USERNAME'), config('INSTA_PASSWORD'))
    bot.go_to_home_of(ANOTHER_USER)
    assert get_home_owner_username(bot) == ANOTHER_USER, \
        f"O redirecionamento para página do usuário '{ANOTHER_USER}' falhou."

def test_open_user_photo(authenticated_bot):
    bot = authenticated_bot
    bot.go_to_home_of(ANOTHER_USER)
    bot.open_user_photo(1, 1)
    assert a_photo_is_open(bot)
