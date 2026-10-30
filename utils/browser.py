from typing import cast

from Browser import Browser
from robot.libraries.BuiltIn import BuiltIn


def get_browser() -> Browser:
    return cast(
        Browser,
        BuiltIn().get_library_instance("Browser"),
    )
