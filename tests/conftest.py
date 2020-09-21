import pytest
from ..bot.insta_bot import InstaBot
from decouple import config


@pytest.fixture(scope="function")
def bot():
    """Retorna um InstaBot com o mínimo de configurações"""
    yield InstaBot(silent=config('SILENT', False, cast=bool))

@pytest.fixture(scope="function")
def authenticated_bot(bot):
    """Retorna um InstaBot após realizar o login com conta de testes"""
    bot.login(config('INSTA_USERNAME'), config('INSTA_PASSWORD'))
    yield bot
