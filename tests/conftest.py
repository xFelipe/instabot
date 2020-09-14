import pytest
from ..bot.insta_bot import InstaBot


@pytest.fixture(scope="function")
def bot():
    """Retorna um InstaBot com o mínimo de configurações"""
    yield InstaBot(silent=False)
