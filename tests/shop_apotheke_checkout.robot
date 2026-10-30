*** Settings ***
Documentation     Search for two products, add their requested quantities, compare the Panthenol price,
...               then open checkout only when the price is unchanged. No login or order submission.
Resource          ../resources/common.resource
Library           components.header.Header
Library           pages.product_page.ProductPage
Library           pages.cart_page.CartPage
Test Setup        Open Shop Apotheke
Test Teardown     Close Shop Apotheke

*** Variables ***
${IBUPROFEN_PZN}    18300010
${IBUPROFEN_NAME}    Redcare Ibuprofen 400 mg
${IBUPROFEN_QUANTITY}    2
${PANTHENOL_PZN}    20175954
${PANTHENOL_NAME}    Redcare Derma Panthenol Salbe
${PANTHENOL_QUANTITY}    1

*** Test Cases ***
Add Requested Products And Verify Price Before Checkout
    [Documentation]    Search by PZN, add 2 Ibuprofen and 1 Panthenol, compare price,
    ...                then navigate to checkout only if the price is unchanged.

    Search For Pzn    ${IBUPROFEN_PZN}
    Product Page Should Match Pzn And Name    ${IBUPROFEN_PZN}    ${IBUPROFEN_NAME}
    Add Current Product To Cart    ${IBUPROFEN_QUANTITY}

    Search For Pzn    ${PANTHENOL_PZN}
    Product Page Should Match Pzn And Name    ${PANTHENOL_PZN}    ${PANTHENOL_NAME}
    ${product_price}=    Get Displayed Product Price
    Log    Panthenol price on product page: EUR ${product_price}
    Add Current Product To Cart    ${PANTHENOL_QUANTITY}

    Open Cart
    Cart Should Contain Product    ${IBUPROFEN_NAME}
    Cart Should Contain Product    ${PANTHENOL_NAME}
    ${basket_price}=    Get Cart Item Price    ${PANTHENOL_NAME}
    Log    Panthenol price in basket: EUR ${basket_price}

    Should Be Equal As Strings
    ...    ${basket_price}
    ...    ${product_price}
    ...    msg=Panthenol price changed: product page EUR ${product_price}, cart EUR ${basket_price}. Checkout was not opened.

    Proceed To Checkout
