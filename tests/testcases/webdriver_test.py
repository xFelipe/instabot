
def test_insta_bot_have_webdriver(bot):
    """Verifica se o bot possui um webdriver após ser iniciado."""
    assert hasattr(bot, 'driver'), 'Bot não possui um webdriver.'
