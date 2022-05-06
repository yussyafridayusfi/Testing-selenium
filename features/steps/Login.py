import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
# driver = webdriver.Chrome(ChromeDriverManager().install())
service = Service('D:/Playground/Testing-automation/Driver/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)


@given(u'I open the login page')
def step_impl(context):
    driver.get('https://www.psegameshop.com/my-account/')


@when(u'I enter valid email')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("horaw43849@angeleslid.com")


@when(u'I enter valid password')
def step_impl(context):
    passw = 'TW!peR633gsVN7C'
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(passw)

@when(u'I click login button')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/div/form/p[3]/button').click()

@then(u'Successfully login')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="my-account-nav"]/li[3]/a').click()
    driver.close()