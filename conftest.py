import pytest
import pytest_html
import requests
from utils.data_reader import load_config
from db_clients.db_helper import MySQLClient
import os

# --- Load config globally once ---
@pytest.fixture(scope="session")
def config():
    return load_config()

# --- API Client Fixture ---
@pytest.fixture(scope="session")
def api_client(config):
    session = requests.Session()
    session.headers.update({'Content-Type': 'application/json'})
    session.base_url = config['api_base_url']  # Custom attribute
    return session

# --- Database Fixture ---
@pytest.fixture(scope="session")
def db_client():
    client = MySQLClient()
    yield client
    client.close()

# --- Playwright (Web) Browser Setup with Resolution Handling ---
from playwright.sync_api import sync_playwright

def get_resolutions():
    return [
        {"width": 1920, "height": 1080},
        {"width": 1366, "height": 768},
        {"width": 414, "height": 896}  # iPhone XR like
    ]

@pytest.fixture(params=get_resolutions(), scope="function")
def browser_context(request):
    resolution = request.param
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport=resolution,
            ignore_https_errors=True
        )
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(browser_context):
    return browser_context.new_page()


# Attach screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            page.screenshot(path=screenshot_path, full_page=True)

            if hasattr(item.config, "_html"):
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                rep.extra = extra

def pytest_configure(config):
    if hasattr(config, '_metadata'):  # ✅ check if pytest-html is enabled
        config._metadata['Project Name'] = 'Playwright Hybrid QA Framework'
        config._metadata['Tested By'] = 'QA Automation'
        config._metadata['Base URL'] = load_config().get('base_url', 'N/A')

