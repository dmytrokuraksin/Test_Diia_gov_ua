from .base_page import BasePage


class SearchResultPage(BasePage):
    def search_result_is_correct(self, request_data):
        assert request_data in self.browser.current_url, "Request result is not correct"
