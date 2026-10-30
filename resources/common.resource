*** Settings ***
Variables        ../config/test_config.py
Library          Browser    timeout=${BROWSER_TIMEOUT}    retry_assertions_for=${ASSERTION_TIMEOUT}    run_on_failure=Take Screenshot

*** Variables ***
${COOKIE_BUTTON}    role=button[name="Nur technisch Notwendige"]

*** Keywords ***
Open Shop Apotheke
    New Browser    ${BROWSER}    headless=${HEADLESS}    args=["--start-maximized"]
    New Context    viewport=${None}    locale="de-DE"
    New Page    ${BASE_URL}
    Handle Cookie Consent If Present

Close Shop Apotheke
    Run Keyword And Ignore Error    Close Browser

Handle Cookie Consent If Present
    [Documentation]    Choose necessary-only cookies if the matching option is present.
    ${consent_visible}=    Run Keyword And Return Status
    ...    Wait For Elements State    ${COOKIE_BUTTON}    visible    10 seconds
    IF    ${consent_visible}
        Click    ${COOKIE_BUTTON}
    END
