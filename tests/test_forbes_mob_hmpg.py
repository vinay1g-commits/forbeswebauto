import pytest

#from conftest import wait_random_time
from pages.forbes_desk_homepg import DeskPg

@pytest.mark.parametrize("browser",["mobile"],indirect=True)
def test_desktop_search_for_news(browser):
    ref = DeskPg(browser)
    browser.get("https://www.forbes.com/")
    #wait_random_time()
    ref.search_for_news()

