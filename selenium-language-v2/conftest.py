
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Select language: de, en, es, ru, uk or other")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")  # Get language from CLI
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

# # На всякий случай - простая фикстура, которая возвращает браузер
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     # этот код выполнится после завершения теста
#     print("\nquit browser..")
#     browser.quit()