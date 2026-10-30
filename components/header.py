from Browser import Browser

from utils.browser import get_browser


class Header:
    SEARCH_INPUT = 'css=input[data-qa-id="search-box-query"]'

    @property
    def browser(self) -> Browser:
        return get_browser()

    def search_for_pzn(self, pzn: str) -> None:
        self.browser.fill_text(self.SEARCH_INPUT, str(pzn))
        self.browser.click(f'css=li[data-product-id="{pzn}"]')
