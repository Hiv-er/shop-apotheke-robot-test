from Browser import Browser

from utils.browser import get_browser
from utils.price import parse_price


class CartPage:
    CART_LINK = 'role=link[name=/Warenkorb/i]'
    CHECKOUT_BUTTON = 'role=button[name=/Zur Kasse/i]'

    def cart_product(self, product_name: str) -> str:
        return f'css=li[data-qa-id="cart-entry-product"]:has-text("{product_name}")'

    def product_price(self, product_name: str) -> str:
        return (
            f'{self.cart_product(product_name)} '
            '[data-qa-id="cart-entry-totalSumTerm"] span'
        )

    @property
    def browser(self) -> Browser:
        return get_browser()

    def open_cart(self) -> None:
        self.browser.click(self.CART_LINK)
        self.browser.get_url("contains", "cart")

    def cart_should_contain_product(self, product_name: str) -> None:
        self.browser.get_element_states(
            self.cart_product(product_name),
            "contains",
            "visible"
        )

    def get_cart_item_price(self, product_name: str) -> str:
        price = self.browser.get_text(self.product_price(product_name))
        return parse_price(price)

    def proceed_to_checkout(self) -> None:
        self.browser.click(self.CHECKOUT_BUTTON)
