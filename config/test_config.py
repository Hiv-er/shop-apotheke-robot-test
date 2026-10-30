import os

BASE_URL = os.getenv("BASE_URL", "https://www.shop-apotheke.com/")
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "true")
BROWSER_TIMEOUT = os.getenv("BROWSER_TIMEOUT", "25 seconds")
ASSERTION_TIMEOUT = os.getenv("ASSERTION_TIMEOUT", "25 seconds")
LOCALE = os.getenv("LOCALE", "de-DE")
