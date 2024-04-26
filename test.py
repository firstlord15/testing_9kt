import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.action_helpers import ActionHelpers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appActivity='.Settings',
    language='en',
    locale='US'
)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )

        self.action_helpers = ActionHelpers
        self.wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)


    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def my_tap(self, arr, timeInt=0):
        time.sleep(timeInt)
        self.driver.tap(arr)

    def my_click(self, type, locator, timeInt=0):
        time.sleep(timeInt)
        self.wait.until(EC.presence_of_element_located((type, locator)))
        self.driver.find_element(type, locator).click()

    def my_send_keys(self, type, locator, value, timeInt=0):
        self.wait.until(EC.presence_of_element_located((type, locator)))
        self.driver.find_element(type, locator).send_keys(value)

    def exit(self, timeInt=1):
        self.driver.swipe(10, 1300, 400, 1300)
        time.sleep(timeInt)

    def enter(self):
        self.driver.press_keycode(66)

    def home(self, timeInt=1):
        type = AppiumBy.ANDROID_UIAUTOMATOR
        locator = home

        while(True):
            try:
                WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((type, locator)))
                self.driver.find_element(type, locator).click()
                break
            except:
                self.exit(timeInt=timeInt)

    def first(self):
        try:
            self.my_click(AppiumBy.ANDROID_UIAUTOMATOR, button_search)
            self.my_send_keys(AppiumBy.ANDROID_UIAUTOMATOR, input_search, "Marko developer")
            self.enter()

            time.sleep(1)
            self.my_tap([[500, 1000]], timeInt=1)
            self.my_click(AppiumBy.XPATH, like_xpath, timeInt=1)
        except Exception as e:
            print(e)
        finally:
            self.home()
    
    def second(self):
        try:
            el1 = self.driver.find_element(AppiumBy.ID, toolbar)
            el2 = self.driver.find_element(AppiumBy.ID, navbar)
            self.action_helpers.scroll(self.driver, el1, el2)

            self.my_click(AppiumBy.ACCESSIBILITY_ID, newtablet)
            self.my_send_keys(AppiumBy.ID, browser_search, youtube)
            self.enter()

        except Exception as e:
            print(e)
        finally:
            self.home()

    # def test_third(self):
    #     try:
            
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         self.home()

        

if __name__ == '__main__':
    unittest.main()
