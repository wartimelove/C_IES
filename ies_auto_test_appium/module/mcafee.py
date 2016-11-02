#!/usr/bin/python

import os
import unittest 
import traceback 
from time import sleep
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

#NOTE: if not, show 'A new session could not be created' error
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class McafeeFunctionTests(unittest.TestCase): 
	NAME_SECURITY_SCAN	= 'Security scan'
	NAME_SCAN_NOW		= 'Scan now'
	NAME_SCAN_REPORT	= 'Security scan report'
	NAME_UPDATE_VIRUS	= 'Update virus definitions'
	NAME_AUTO_UPDATE	= 'Auto Update:?On'
	NAME_EVERY		= 'Every'
	NAME_DATY		= 'Day'
	NAME_AT			= 'At'
	NAME_OK			= 'OK'
	NAME_MCAFEE_SECURITY	= 'McAfee Mobile Security.'
	NAME_USB	 	= 'USB debugging connected'
	NAME_WELCOME		= 'Welcome to the ultimate in mobile protection.'
	NAME_START		= 'Start'
	
	TIMOUT_TIMES		= 5 # equals 5 x 5
	TIME_SCAN		= 3
	TIME_PAGE		= 10

	PROC_NAME		= 'com.wsandroid.suite.intelempg'

	def setUp(self):

		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'Baytrail_CR'
		desired_caps['appPackage'] = 'com.wsandroid.suite.intelempg'
		desired_caps['appActivity'] = 'com.mcafee.app.LauncherDelegateActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)

		try:
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_WELCOME)
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_START).click()
		except NoSuchElementException:
			pass

		#NOTE: clear the log for the alarm manager
		os.system('adb logcat -c')


	def tearDown(self):
		self.driver.quit()


	def testManualScanDevice(self):
		try:
			time = 0

			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN).click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_NOW).click()
			while True:
				try:
					self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_REPORT)
					break
				except NoSuchElementException:
					if time > McafeeFunctionTests.TIMOUT_TIMES :
						self.fail('cannot find the element')
					else:
						sleep(5)
						time = time + 1
						continue

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testManualScanDeviceAndTapBackButton(self):
		try:
			time = 0
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN).click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_NOW).click()
			sleep(3)
			self.driver.back()
			sleep(3)

			while True:
				try:
					self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_REPORT)
					break
				except NoSuchElementException:
					if time > McafeeFunctionTests.TIMOUT_TIMES :
						self.fail('cannot find the element')
					else:
						sleep(5)
						time = time + 1
						continue

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testManualScanDeviceAndTapHomeButton(self):
		try:
			time = 0
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN).click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_NOW).click()
			sleep(3)
			#NOTE: press the home button
			self.driver.press_keycode(3)
			sleep(3)

			while True:
				try:
					self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_REPORT)
					break
				except NoSuchElementException:
					if time > McafeeFunctionTests.TIMOUT_TIMES :
						self.fail('cannot find the element')
					else:
						sleep(15)
						time = time + 1
						continue

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testManualUpdateMcAfee(self):
		try:
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN).click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_UPDATE_VIRUS).click()
			el = self.driver.find_element_by_id('com.wsandroid.suite.intelempg:id/id_update_last_check_date')
			line = os.popen('adb shell date +%-m/%-d/%Y').readlines()[0]

			self.assertTrue(el.text.split(' ')[0] == line.split('\r\n')[0])

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testAutoUpdateMcAfee(self):
		try:
			self.driver.find_element_by_id('com.wsandroid.suite.intelempg:id/menu_settings').click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN).click()
			self.driver.find_elements_by_id('android:id/title')[3].click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_EVERY).click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_DATY).click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_AT).click()

			#NOTE: get the current time
			hour = os.popen('adb shell date +%-l').readlines()[0].split('\r\n')[0]

			el = self.driver.find_element_by_id('android:id/numberpicker_input')
			if hour != el.text:
				x = el.location['x'] + el.size['width'] //2
				y = el.location['y'] + el.size['height'] //2
				self.driver.tap([(x, y),], 3000)
				self._clearText(el.text)
				el.send_keys(hour)


			minute = int(os.popen('adb shell date +%-M').readlines()[0].split('\r\n')[0]) + 1

			el = self.driver.find_elements_by_id('android:id/numberpicker_input')[1]
			if str(minute) != el.text:
				x = el.location['x'] + el.size['width'] //2
				y = el.location['y'] + el.size['height'] //2
				self.driver.tap([(x, y),], 3000)
				self._clearText(el.text)
				el.send_keys(('%d' % minute))

			am = os.popen('adb shell date +%p').readlines()[0].split('\r\n')[0]
			el = self.driver.find_elements_by_id('android:id/numberpicker_input')[2]
			if am != el.text:
				x = el.location['x'] + el.size['width'] //2
				y = el.location['y'] + el.size['height'] //2
				self.driver.tap([(x, y),], 3000)
				self._clearText(el.text)
				el.send_keys(am)

			#NOTE: press the enter key
			self.driver.press_keycode(66)

			self.driver.find_element_by_name(McafeeFunctionTests.NAME_OK).click()

			
			now = 0
			while now <= minute:
				now = int(os.popen('adb shell date +%-M').readlines()[0].split('\r\n')[0])

				#NOTE: keep the session, otherwise would return to the home page
				self.driver.find_element_by_name(McafeeFunctionTests.NAME_EVERY)

				try:
					os.popen('adb logcat -d AlarmManager:V *:S | grep mcafee -i').readlines()[0]
					self.assertTrue('find the alarm from the mcafee')
					return 
				except (TypeError, IndexError):
					sleep(10)
					continue

			self.fail('could not find the alarm from the mcafee')
			
		except NoSuchElementException:
			self.fail(traceback.format_exc())
			pass

	def testManualScanDeviceAndEnterSuspend(self):
		try:
			time = 0

			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN).click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_NOW).click()
			sleep(3)

			os.system('adb shell \'echo mem >/sys/power/state\'')
			sleep(10)
			os.system('adb shell \'echo on >/sys/power/state\'')

			while True:
				try:
					self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_REPORT)
					break
				except NoSuchElementException:
					if time > McafeeFunctionTests.TIMOUT_TIMES :
						self.fail('cannot find the element')
					else:
						sleep(5)
						time = time + 1
						continue

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testManualUpdateMcafeeAndEnterSuspend(self):
		try:
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN).click()
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_UPDATE_VIRUS).click()
			sleep(3)

			os.system('adb shell \'echo mem >/sys/power/state\'')
			sleep(10)
			os.system('adb shell \'echo on >/sys/power/state\'')

			el = self.driver.find_element_by_id('com.wsandroid.suite.intelempg:id/id_update_last_check_date')
			line = os.popen('adb shell date +%-m/%-d/%Y').readlines()[0]

			self.assertTrue(el.text.split(' ')[0] == line.split('\r\n')[0])

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testManualScanDeviceAndForceStop(self):
		try:
			print 'click the button "', McafeeFunctionTests.NAME_SECURITY_SCAN, '"'
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN).click()

			print 'scan the device'
			sleep(McafeeFunctionTests.TIME_SCAN)

			print 'click the button "', McafeeFunctionTests.NAME_SCAN_NOW, '"'
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SCAN_NOW).click()

			print 'kill the self\'s proc'
			os.system('pid=`adb shell ps | grep com.wsandroid.suite.intelempg | awk \'{print $2}\'` && adb shell kill $pid')

			print 'wait'
			sleep(McafeeFunctionTests.TIME_PAGE)
			self.driver.find_element_by_id('com.android.launcher:id/search_button_container')

			print 'start the self\'s proc'
			os.system('adb shell am start com.wsandroid.suite.intelempg/com.mcafee.app.MainActivity')
			sleep(McafeeFunctionTests.TIME_PAGE)
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN)


		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testAutoLaunch(self):
		try:
			self.driver.find_element_by_name(McafeeFunctionTests.NAME_SECURITY_SCAN)

			print 'reboot'
			time = 3
			while time > 0:
				print time
				sleep(McafeeFunctionTests.TIME_PAGE)
				time -= 1
			os.system('adb reboot')

			time = 0
			while time < McafeeFunctionTests.TIMOUT_TIMES:
				print 'attempt to find the device in the', time, 'times'
				if os.popen('adb devices').read().find('device', 23) > 0:
					break
				sleep(McafeeFunctionTests.TIME_PAGE)
				time += 1

			print 'wait for the system\'s ready'
			sleep(2*McafeeFunctionTests.TIME_PAGE)
			line = os.popen(('adb shell ps | grep %s') % McafeeFunctionTests.PROC_NAME).read()
			self.assertTrue(line.find(McafeeFunctionTests.PROC_NAME) >= 0)

			try:
				os.system('adb root')

				desired_caps = {}
				desired_caps['platformName'] = 'Android'
				desired_caps['platformVersion'] = '5.0'
				desired_caps['deviceName'] = 'Baytrail_CR'
				desired_caps['appPackage'] = 'com.wsandroid.suite.intelempg'
				desired_caps['appActivity'] = 'com.mcafee.app.MainActivity'

				self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
				self.driver.implicitly_wait(15)

				el = self.driver.find_element_by_name(McafeeFunctionTests.NAME_USB)
				self.driver.swipe(el.location['x'] + 10, el.location['y'] + 10, \
					el.location['x'] + 10, el.location['y'] - 100)
			except:
				pass


		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def _clearText(self, text):
		self.driver.keyevent(123)
		for i in range(0, len(text)):
			self.driver.keyevent(67)

