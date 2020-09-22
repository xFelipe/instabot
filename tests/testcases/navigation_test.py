from decouple import config
from instabot.tests.testcases.helpers.common import (
    get_element_text_by_xpath, get_home_owner_username
)

ANOTHER_USER = 'duartepaula23'


def test_redirect_to_another_user_page(bot):
    bot.login(config('INSTA_USERNAME'), config('INSTA_PASSWORD'))
    bot.go_to_home_of(ANOTHER_USER)
    assert get_home_owner_username(bot) == ANOTHER_USER, \
        f"O redirecionamento para página do usuário '{ANOTHER_USER}' falhou."

def test_open_user_photo(authenticated_bot):
    bot = authenticated_bot
    bot.go_to_home_of(ANOTHER_USER)
    bot.open_user_photo(1, 1)
    assert bot.a_photo_is_open()

def test_open_users_who_liked_photo(authenticated_bot):
    bot = authenticated_bot
    bot.go_to_home_of(ANOTHER_USER)
    bot.open_user_photo(1, 1)
    bot.open_who_liked_photo()
    assert bot.likes_list_is_open(),\
        "A tela de listas de pessoas que curtiram não abriu."

def test_follow_first_user_who_liked_photo(authenticated_bot):
    first_user = 1
    bot = authenticated_bot
    bot.go_to_home_of(ANOTHER_USER)
    bot.open_user_photo(1, 1)
    bot.open_who_liked_photo()
    bot.follow_user(first_user)
    is_following_user = bot.is_following_user(first_user)
    bot.unfollow_user(first_user)
    from time import sleep; sleep(10)  # Em teste
    assert is_following_user,\
        "Erro ao seguir usuário que curtiu a foto selecionada."
