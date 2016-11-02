import os,sys
import unittest
import traceback
import commands
#
from appium import webdriver
#from selenium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
#
from common.function import *
#
reload(sys)
sys.setdefaultencoding('utf8')

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SparkvueFunctionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.isbx.pasco.Spark'
        desired_caps['appActivity'] = 'com.isbx.sparksandboxui.LaunchActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)
	



    def tearDown(self):
        self.driver.quit()

    def testforcestop(self, testResult=None):
	self.testResult = testResult
	sleep(15)
	try:
        	Page = self.driver.find_element_by_class_name("android.webkit.WebView")
		sleep(3)
	except:
		sleep(15)
        	Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	        sleep(3)
	
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-0']/ul/li")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[3]/div[1]/div/a[1]")
	btn.click()
	sleep(3)
        self.driver.quit()
	kill_thread("Spark")
	self.setUp()
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[3]/div[1]/div/a[1]")
	btn.click()
	sleep(3)
	
	try:
		No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
		No_btn.click()
		sleep(3)
	except:
		pass
		
	home_btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[1]/div[1]/a[1]")
	home_btn.click()
	sleep(3)
	No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
	No_btn.click()
	sleep(3)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

    def testlaunch(self):
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-2']/ul/li[3]")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[3]/div[1]/div/a[1]")
	btn.click()
	sleep(10)
	home_btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[1]/div[1]/a[1]")
	home_btn.click()
	sleep(3)
	No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
	No_btn.click()
	sleep(3)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

    def testsuspenddata(self):
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-0']/ul/li")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[3]/div[1]/div/a[1]")
	btn.click()
	sleep(60)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

    def testsuspendmainui(self):
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-0']/ul/li")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	sleep(3)
	os.system("adb shell 'echo mem > /sys/power/state' && adb shell 'echo on > /sys/power/state'")	
	sleep(10)
	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(3)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[3]/div[1]/div/a[1]")
	btn.click()
	sleep(5)
	home_btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[1]/div[1]/a[1]")
	home_btn.click()
	sleep(3)
	No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
	No_btn.click()
	sleep(3)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

    def testfrontcamera(self):
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.swipe(1000,540,1000,360)
	sleep(3)
	self.driver.swipe(1000,540,1000,360)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-5']/ul/li")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[2]/div[2]/div")
	touch_actions_open = TouchActions(self.driver)
	touch_actions_open.tap(btn).perform()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[2]/div[2]/div")
	touch_actions_open = TouchActions(self.driver)
	touch_actions_open.tap(btn).perform()
	sleep(5)
	home_btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[1]/div[1]/a[1]")
	home_btn.click()
	sleep(3)
	No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
	No_btn.click()
	sleep(5)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

    def testrearcamera(self):
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.swipe(1000,540,1000,360)
	sleep(3)
	self.driver.swipe(1000,540,1000,360)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-4']/ul/li")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[2]/div[2]/div")
	touch_actions_open = TouchActions(self.driver)
	touch_actions_open.tap(btn).perform()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[2]/div[2]/div")
	touch_actions_open = TouchActions(self.driver)
	touch_actions_open.tap(btn).perform()
	sleep(5)
	home_btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[1]/div[1]/a[1]")
	home_btn.click()
	sleep(3)
	No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
	No_btn.click()
	sleep(5)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

    def testlight(self):
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-1']/ul/li")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[3]/div[1]/div/a[1]")
	btn.click()
	sleep(10)
	home_btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[1]/div[1]/a[1]")
	home_btn.click()
	sleep(3)
	No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
	No_btn.click()
	sleep(3)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

    def testsound(self):
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.swipe(1000,540,1000,360)
	sleep(3)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-3']/ul/li[1]")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[3]/div[1]/div/a[1]")
	btn.click()
	sleep(10)
	home_btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[1]/div[1]/a[1]")
	home_btn.click()
	sleep(3)
	No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
	No_btn.click()
	sleep(3)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

