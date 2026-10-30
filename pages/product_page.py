from Browser import Browser

from utils.browser import get_browser
from utils.price import parse_price


class ProductPage:
    QUANTITY_BUTTON = 'css=[data-qa-id="product-quantity-select"]'
    ADD_TO_CART_BUTTON = 'role=button[name=/In den Warenkorb/i]'
    CLOSE_POPUP_BUTTON = 'css=[data-qa-id="cartIntermediateDrawer"] button[aria-label="Schließen"]'
    PRODUCT_PRICE = 'css=[data-qa-id="displayAmountField"]'

    @property
    def browser(self) -> Browser:
        return get_browser()

    def quantity_select_option(self, quantity: int) -> str:
        return (
            'css=li[data-qa-id="product-quantity-select-option"]'
            f'[data-value="{quantity}"]'
        )

    def product_page_should_match_pzn_and_name(self, pzn: str, expected_name: str) -> None:
        self.browser.get_url("contains", pzn)
        self.browser.get_text(
            "h1",
            "contains",
            expected_name,
            "Product heading mismatch"
        )
        self.browser.get_text(
            'css=[data-qa-id="product-attribute-pzn"]',
            "contains",
            pzn,
            "PZN not shown on the product page"
        )

    def get_displayed_product_price(self) -> str:
        price = self.browser.get_text(self.PRODUCT_PRICE)
        return parse_price(price)

    def add_current_product_to_cart(self, quantity: int) -> None:
        quantity = int(quantity)
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.browser.click(self.QUANTITY_BUTTON)
        self.browser.click(self.quantity_select_option(quantity))
        self.browser.click(self.ADD_TO_CART_BUTTON)
        self.browser.click(self.CLOSE_POPUP_BUTTON)
