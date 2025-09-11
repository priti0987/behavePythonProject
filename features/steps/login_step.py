import time

from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@given("user is on the login page")
def step_impl(context):

    # Set up driver with WebDriverManager
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()

@when("user enters valid username and password")
def step_impl(context):
    context.driver.find_element(By.ID,"user-name").clear()
    context.driver.find_element(By.ID,"user-name").send_keys("standard_user")
    context.driver.find_element(By.ID,"password").clear()
    context.driver.find_element(By.ID,"password").send_keys("secret_sauce")

@when("user clicks on login button")
def step_impl(context):
    context.driver.find_element(By.ID,"login-button").click()


@then("user should navigated to the product page")
def then_validation(context):
    title = context.driver.find_element(By.CLASS_NAME,"title").text
    assert title == "Products",f"Expected 'Products' but got {title}"
    time.sleep(3)
    print("pass....")

@when("user enters invalid creadentials")
def step_impl(context):
    context.driver.find_element(By.ID,"user-name").clear()
    context.driver.find_element(By.ID,"user-name").send_keys("stan23dard_user")
    context.driver.find_element(By.ID,"password").clear()
    context.driver.find_element(By.ID,"password").send_keys("secret_11sauce")

@then("user should show error")
def errorPage(context):
    pass
    error_message = context.driver.find_element(By.XPATH,"//h3/text()").text
    assert error_message.__contains__("Epic sadface")