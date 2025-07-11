from pages.base_page import Page


class TermsCondPage(Page):

    def verify_tc_opened(self):
        self.wait_for_url_contains('terms-conditions')

