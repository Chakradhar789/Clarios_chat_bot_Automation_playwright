from playwright.sync_api import Page, expect

from config.bot_data import (
    WELCOME_MESSAGE,
    HELLO_RADER_MESSAGE,
    CLOSING_MESSAGE,
    LANGUAGES,
    TASK_OPTIONS,
    SCROLL_RIGHT,
    MESSAGE_PLACEHOLDER,
    SEND_BUTTON
)


class BotPage:

    def __init__(self, page: Page):

        self.page = page

        # -------------------------------
        # Welcome
        # -------------------------------

        self.welcome_message = page.get_by_text(
            WELCOME_MESSAGE,
            exact=True
        )

        # -------------------------------
        # Languages
        # -------------------------------

        self.scroll_right = page.get_by_role(
            "button",
            name=SCROLL_RIGHT
        )

        self.language_buttons = {
            language: page.get_by_role(
                "button",
                name=language
            )
            for language in LANGUAGES
        }

        # -------------------------------
        # Chat
        # -------------------------------

        self.message_box = page.get_by_role(
            "textbox",
            name=MESSAGE_PLACEHOLDER
        )

        self.send_button = page.get_by_role(
            "button",
            name=SEND_BUTTON
        )

        # -------------------------------
        # Bot response
        # -------------------------------

        self.hello_rader = page.get_by_text(
            HELLO_RADER_MESSAGE,
            exact=False
        )

        # -------------------------------
        # Task buttons
        # -------------------------------

        self.task_buttons = {
            task: page.get_by_role(
                "button",
                name=task
            )
            for task in TASK_OPTIONS
        }

        # -------------------------------
        # Closing message
        # -------------------------------

        self.closing_message = page.get_by_text(
            CLOSING_MESSAGE,
            exact=True
        )

    # ==================================================
    # ACTIONS
    # ==================================================

    def click_scroll_right(self):

        self.scroll_right.click()

    def select_language(self, language):

        self.language_buttons[language].click()

    def type_message(self, message):

        self.message_box.fill(message)

    def click_send(self):

        self.send_button.click()

    def click_task(self, task):

        self.task_buttons[task].click()

    # ==================================================
    # ASSERTIONS
    # ==================================================

    def verify_welcome_message(self):

        expect(
            self.welcome_message
        ).to_be_visible(timeout=15000)

    def verify_languages(self):

        for language in LANGUAGES:

            expect(
                self.language_buttons[language]
            ).to_be_visible(timeout=10000)

    def verify_hello_rader(self):

        expect(
            self.hello_rader
        ).to_be_visible(timeout=15000)

    def verify_task_options(self):

        for task in TASK_OPTIONS:

            expect(
                self.task_buttons[task]
            ).to_be_visible(timeout=10000)

    def verify_closing_message(self):

        expect(
            self.closing_message
        ).to_be_visible(timeout=15000)