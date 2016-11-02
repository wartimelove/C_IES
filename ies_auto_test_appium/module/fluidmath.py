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
#from common.function import *
#
reload(sys)
sys.setdefaultencoding('utf8')

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FluidmathFunctionTests(unittest.TestCase):
    def setUp(self):
	self.Connect_Wifi()
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.fluiditysoftware.fluidmathforintel'
        desired_caps['appActivity'] = '.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)


    def tearDown(self):
        self.driver.quit()

    def testswitchlanguage(self):
	sleep(8)
	self.driver.tap([(1225,100),])
	
	print self.driver.contexts	
	self.driver.switch_to.context("WEBVIEW_com.fluiditysoftware.fluidmathforintel")
	sleep(3)
	source = self.driver.page_source
	sleep(3)
	
	bar = self.driver.find_element_by_xpath("//*[@id='sidebar_handle']")
	touch_actions = TouchActions(self.driver)
	bar.click()
	option = self.driver.find_element_by_xpath("//*[@id='btn_options']")
	option.click()
	sleep(3)
	language = self.driver.find_element_by_xpath("//*[@id='a_language']")
	language.click()
	sleep(3)
	English = self.driver.find_element_by_xpath("//*[@id='options']/ul/li[2]/ul/li[1]/a")
	Espanol = self.driver.find_element_by_xpath("//*[@id='options']/ul/li[2]/ul/li[2]/a")
	Portuguese = self.driver.find_element_by_xpath("//*[@id='options']/ul/li[2]/ul/li[3]/a")
	Espanol.click()
	sleep(3)
	option.click()
	sleep(3)
	language.click()
	sleep(3)
	English.click()
	sleep(5)

	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)


    def testsuspend(self):
	sleep(8)
	self.driver.tap([(1225,100),])
	
	x = self.driver.get_window_size()['width']
	y = self.driver.get_window_size()['height']
	print x, y
	start_x = int(x*0.3)
	start_y = int(y*0.3)
	
	mid_x = int(x*0.5)
	mid_y = int(y*0.7)

	end_x = int(x*0.5)
	end_y = int(y*0.3)
	print start_x,start_y,mid_x,mid_y,end_x,end_y
	sleep(3)
	Point = TouchAction(self.driver)
	#Point.press(x=start_x,y=start_y).move_to(x=mid_x,y=mid_y).move_to(x=end_x,y=end_y).release().perform()
	Point.press(x=start_x,y=start_y).move_to(x=mid_x,y=mid_y).release().perform()
	sleep(3)	
	Point.press(x=start_x,y=start_y).move_to(x=end_x,y=end_y).release().perform()

	self.driver.switch_to.context("WEBVIEW_com.fluiditysoftware.fluidmathforintel")
	sleep(3)
	source = self.driver.page_source
	sleep(3)
	bar = self.driver.find_element_by_xpath("//*[@id='sidebar_handle']")
	touch_actions = TouchActions(self.driver)
	#touch_actions.tap(bar).perform()
	#sleep(3)
	#touch_actions.tap(bar).perform()
	bar.click()
	sleep(3)
	os.system("adb root && adb shell 'echo mem > /sys/power/state' && adb shell 'echo on > /sys/power/state'")	
	sleep(5)
	clear_button = self.driver.find_element_by_xpath("//*[@id='clearbutton']")
	clear_button.click()
#	isinstance(self.driver.page_source,"gbk")
	#source.decode("gb2312")
	#source.encode("ascii")	
#	print (self.driver.page_source.encode('ascii').decode('utf-8'))

	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

    def Connect_Wifi(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.wifi.WifiSettings'
    
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    
        sleep(5)
        Btn_Setting = self.driver.find_elements_by_class_name("android.widget.ImageButton")
        Btn_Setting[0].click()
        Add_Network = self.driver.find_elements_by_id("android:id/title")
        Add_Network[0].click()

	Security = self.driver.find_element_by_id("com.android.settings:id/security")
	Security.click()
	Security_option = self.driver.find_elements_by_class_name("android.widget.CheckedTextView")
	Security_option[2].click()
        T_SSID = self.driver.find_element_by_id("com.android.settings:id/ssid")
        T_SSID.send_keys("shz23f-wajoint-ap99-IES")
       	Password_In = self.driver.find_element_by_id("com.android.settings:id/password")
        Password_In.send_keys("ies+12345")
        Btn_Save = self.driver.find_element_by_id("android:id/button1")
        Btn_Save.click()
        #Wifi_List = self.driver.find_elements_by_id("android:id/title")
        #Wifi_List[0].click()
	#try:
        #	Password_In = self.driver.find_element_by_id("com.android.settings:id/password")
        #	Password_In.send_keys("ies+12345")
        #	Btn_Connect = self.driver.find_element_by_id("android:id/button1")
        #	Btn_Connect.click()
	#except :
	#	Btn_Done = self.driver.find_element_by_id("android:id/button2")
	#	Btn_Done.click()
        self.driver.quit()


    def testlogin(self):
	sleep(8)
	self.driver.tap([(1225,100),])
	
	self.driver.switch_to.context("WEBVIEW_com.fluiditysoftware.fluidmathforintel")
	source = self.driver.page_source
	sleep(3)
	bar = self.driver.find_element_by_xpath("//*[@id='sidebar_handle']")
	touch_actions = TouchActions(self.driver)
	bar.click()
	sleep(3)
	login = self.driver.find_element_by_xpath("//*[@id='loginlink']")
	login.click()
	sleep(3)
	user = self.driver.find_element_by_xpath("//*[@id='popup_username']")
	user.send_keys("wartimelove@gmail.com")
	password = self.driver.find_element_by_xpath("//*[@id='popup_password']")
	password.send_keys("fluidmath74")
	sleep(3)
	submit = self.driver.find_element_by_xpath("//*[@id='btn_login_submit']")
	submit.click()
	sleep(10)
	login = self.driver.find_element_by_xpath("//*[@id='loginlink']")
	login.click()
	sleep(3)
	btn_ok = self.driver.find_element_by_xpath("/html/body/div[8]/div/button[1]")
	btn_ok.click()
	sleep(5)
#	isinstance(self.driver.page_source,"gbk")
	#source.decode("gb2312")
	#source.encode("ascii")	
#	print (self.driver.page_source.encode('ascii').decode('utf-8'))

	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)


    def testtap(self):
	sleep(5)
	self.driver.tap([(1225,100),])
	
	x = self.driver.get_window_size()['width']
	y = self.driver.get_window_size()['height']
	print x, y
	start_x = int(x*0.3)
	start_y = int(y*0.3)
	
	mid_x = int(x*0.5)
	mid_y = int(y*0.7)

	end_x = int(x*0.8)
	end_y = int(y*0.2)
	sleep(3)
	Point = TouchAction(self.driver)
	Point.press(x=start_x,y=start_y).move_to(x=mid_x,y=mid_y).move_to(x=end_x,y=end_y).release().perform()
	
	self.driver.switch_to.context("WEBVIEW_com.fluiditysoftware.fluidmath")
	sleep(3)
	source = self.driver.page_source
	sleep(3)
	bar = self.driver.find_element_by_xpath("//*[@id='sidebar_handle']")
	touch_actions = TouchActions(self.driver)
	#touch_actions.tap(bar).perform()
	#sleep(3)
	#touch_actions.tap(bar).perform()
	bar.click()
	sleep(3)
	clear_button = self.driver.find_element_by_xpath("//*[@id='clearbutton']")
	clear_button.click()
#	isinstance(self.driver.page_source,"gbk")
	#source.decode("gb2312")
	#source.encode("ascii")	
#	print (self.driver.page_source.encode('ascii').decode('utf-8'))

	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)


    def testequation(self):
	sleep(5)
	self.driver.tap([(1225,100),])
	
	x = self.driver.get_window_size()['width']
	y = self.driver.get_window_size()['height']
	print x, y
	start_x = int(x*0.3)
	start_y = int(y*0.3)
	
	mid_x = int(x*0.5)
	mid_y = int(y*0.7)

	end_x = int(x*0.8)
	end_y = int(y*0.2)
	sleep(3)
	Point = TouchAction(self.driver)
	Point.press(x=start_x,y=start_y).move_to(x=mid_x,y=mid_y).move_to(x=end_x,y=end_y).release().perform()
	
	self.driver.switch_to.context("WEBVIEW_com.fluiditysoftware.fluidmath")
	sleep(3)
	source = self.driver.page_source
	sleep(3)
	bar = self.driver.find_element_by_xpath("//*[@id='sidebar_handle']")
	touch_actions = TouchActions(self.driver)
	#touch_actions.tap(bar).perform()
	#sleep(3)
	#touch_actions.tap(bar).perform()
	bar.click()
	sleep(3)
	clear_button = self.driver.find_element_by_xpath("//*[@id='clearbutton']")
	clear_button.click()
#	isinstance(self.driver.page_source,"gbk")
	#source.decode("gb2312")
	#source.encode("ascii")	
#	print (self.driver.page_source.encode('ascii').decode('utf-8'))

	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

