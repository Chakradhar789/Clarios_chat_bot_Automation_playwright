from pages.bot_page import BotPage


def test_clarios_complete_conversation(page):

    # Launch CLARIOS POC UAT
    page.goto(
        "https://platform.kore.ai/xo-webclient/"
        "7ad43b7f51544ec8864a434dbaefd84cd7901045c6594000"
        "bf957bab9c33cdadst9e?lang=en"
    )

    page.wait_for_load_state("domcontentloaded")

    bot = BotPage(page)

    # Verify welcome message
    bot.verify_welcome_message()

    # Scroll language options
    bot.click_scroll_right()

    # Verify all 9 languages
    bot.verify_languages()

    # Select English
    bot.select_language("English")

    # Verify bot response
    bot.verify_hello_rader()

    # Verify task options
    bot.verify_task_options()

    # End session
    bot.click_task("End the session")

    # Verify closing message
    bot.verify_closing_message()