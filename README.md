# Shop Apotheke UI test - Robot Framework + Browser Library

This example automates the requested flow in `tests/shop_apotheke_checkout.robot`.
The end-to-end scenario is written in Robot Framework; UI interactions live in
Python Page Objects and a small component object. The test stops at the checkout
entry point: it does not log in and does not place an order.

## Setup (Windows PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
rfbrowser install chromium
```

## Run

From the project root:

```powershell
robot --pythonpath . --outputdir results tests
```

To run with a visible browser in PowerShell:

```powershell
$env:HEADLESS = "false"
robot --pythonpath . --outputdir results tests
```

Useful artifacts are `results/report.html`, `results/log.html` and `results/output.xml`.
Unset `HEADLESS` or set it to `true` to return to headless mode. `BASE_URL`, `BROWSER`,
`ASSERTION_TIMEOUT` and `BROWSER_TIMEOUT` can also be set as environment
variables.