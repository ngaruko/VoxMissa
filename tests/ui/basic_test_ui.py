import re
from playwright.sync_api import Page, expect
import pytest
import logging
import boto3
from botocore.exceptions import ClientError

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.on("console", lambda msg: print(msg.text))
    logging.info("before the test runs")
    

    # Go to the starting url before each test.
    # page.goto("https://playwright.dev/")
    yield
    
    print("after the test runs")

def test_has_title(page: Page):
    
    print("starting test runs...")
    page.goto("http://127.0.0.1:8000/admin/")
    page.screenshot(path='screenshot.png', full_page=True)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Log in | Django site admin"))

# def test_admin_login(page: Page):
#     page.goto("http://127.0.0.1:8000/admin")

#     # login with valid admin creds
#     page.get_by_role("textbox", name="username").fill("admin")
#     page.get_by_role("textbox", name="password").fill("pass")
#     page.get_by_text("Log in").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Site administration")).to_be_visible()

def test_upload_file():
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file('screenshot.png', 'bedebucket2', 'screenshot.png')
    except ClientError as e:
        logging.error(e)
