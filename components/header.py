from typing import cast

from Browser import Browser
from robot.libraries.BuiltIn import BuiltIn


class Header:
    SEARCH_INPUT = 'css=input[data-qa-id="search-box-query"]'

    @property
    def browser(self) -> Browser:
        return cast(
            Browser,
            BuiltIn().get_library_instance("Browser"),
        )

    def search_for_pzn(self, pzn: str) -> None:
        self.browser.fill_text(self.SEARCH_INPUT, str(pzn))
        self.browser.click(f'css=li[data-product-id="{pzn}"]')
