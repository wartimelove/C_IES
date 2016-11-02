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

class ESFunctionTests(unittest.TestCase):

	NAME_HOME 	= 'Home'
	NAME_NEW	= 'New'
	NAME_FILE	= 'File'
	NAME_OK		= 'OK'
	NAME_TEXT	= 'Text'
	NAME_ES_EDITOR	= 'ES Note Editor'
	NAME_EDIT	= 'Edit'
	NAME_YES	= 'Yes'
	NAME_DELETE	= 'Delete'
	NAME_CUT	= 'Cut'
	NAME_PASTE	= 'Paste'
	NAME_SHOW_HIDE	= 'Show hidden files'
	NAME_TOOLS	= 'Tools'
	NAME_HIDE	= 'Hide'
	NAME_MORE	= 'More'
	NAME_HIDE_LIST	= 'Hide List'
	NAME_RESTORE	= 'Restore'
	NAME_REFRESH	= 'Refresh'
	NAME_DESKTOP	= 'Add to desktop'
	NAME_HOMEPAGE	= 'Homepage'
	NAME_APP	= 'APP'
	NAME_UNLOCK	= 'Unlock'
	NAME_BACKUP	= 'Backup'
	NAME_LOCAL	= 'Local'

	DIRECTORY_TEST	= 'TestFiles'
	DIRECTORY_BACKUP= 'backups'
	DIRECTORY_APPS	= 'apps'
	FILE_TEST	= 'test'
	CONTENT_TEST	= '12ab'

	TIME_PAGE	= 10

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'Baytrail_CR'
		desired_caps['appPackage'] = 'com.estrongs.android.pop'
		desired_caps['appActivity'] = '.view.FileExplorerActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)
		

	def tearDown(self):
		self.driver.quit()
		pass

	def testReadDocument(self):
		try:
			try:
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)
			except:
				self.driver.find_elements_by_id('com.estrongs.android.pop:id/indicator')[1].click()
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)

			self.driver.find_element_by_name(ESFunctionTests.DIRECTORY_TEST).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_NEW).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_FILE).click() 
			el = self.driver.find_element_by_class_name('android.widget.EditText')
			self._clearText(el.text)
			el.send_keys(ESFunctionTests.FILE_TEST)
			self.driver.find_element_by_name(ESFunctionTests.NAME_OK).click()

			self.driver.find_element_by_name(ESFunctionTests.FILE_TEST).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_TEXT).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_ES_EDITOR).click()
			self.driver.find_element_by_name(ESFunctionTests.FILE_TEST)

			self.driver.find_element_by_id('com.estrongs.android.pop:id/menu').click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_EDIT).click()

			#NOTE: input the string '12ab'
			self.driver.press_keycode(8)
			self.driver.press_keycode(9)
			self.driver.press_keycode(29)
			self.driver.press_keycode(30)

			#NOTE: keycode 4 is the back event
			self.driver.press_keycode(4)
			self.driver.press_keycode(4)
			self.driver.find_element_by_name(ESFunctionTests.NAME_YES).click()
			self.driver.press_keycode(4)

			self.driver.find_element_by_name(ESFunctionTests.FILE_TEST).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_TEXT).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_ES_EDITOR).click()
			self.driver.find_element_by_name(ESFunctionTests.FILE_TEST)

			el = self.driver.find_element_by_id('com.estrongs.android.pop:id/text_show')

			self.assertEqual(el.text, ESFunctionTests.CONTENT_TEST)

			self.driver.press_keycode(4)

			el = self.driver.find_element_by_name(ESFunctionTests.FILE_TEST)
			self.driver.tap([(el.location['x']+10, el.location['y']+10),], 10000)
			self.driver.find_element_by_name(ESFunctionTests.NAME_DELETE).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_OK).click()
				
		except NoSuchElementException:
			self.fail(traceback.format_exc())
		pass


	def testCopyCutFunction(self):
		try:
			try:
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)
			except:
				self.driver.find_elements_by_id('com.estrongs.android.pop:id/indicator')[1].click()
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)

			self.driver.find_element_by_name(ESFunctionTests.DIRECTORY_TEST).click()

			self._createFile()

			el = self.driver.find_element_by_name(ESFunctionTests.FILE_TEST)
			self.driver.tap([(el.location['x']+10, el.location['y']+10),], 10000)
			self.driver.find_element_by_name(ESFunctionTests.NAME_CUT).click()

			self.driver.press_keycode(4)
			self.driver.find_element_by_name(ESFunctionTests.NAME_PASTE).click()
			self.driver.find_element_by_name(ESFunctionTests.FILE_TEST)
			self._removeFile()

		except NoSuchElementException:
			self.fail(traceback.format_exc())
		pass

	def testShowHideFile(self):
		try:
			try:
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)
			except:
				self.driver.find_elements_by_id('com.estrongs.android.pop:id/indicator')[1].click()
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)

			self.driver.find_element_by_name(ESFunctionTests.DIRECTORY_TEST).click()

			self._createFile()
			
			el = self.driver.find_element_by_name(ESFunctionTests.FILE_TEST)
			self.driver.tap([(el.location['x']+10, el.location['y']+10),], 10000)
			self.driver.find_element_by_name(ESFunctionTests.NAME_MORE).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_HIDE).click()

			try:
				self.driver.find_element_by_name(ESFunctionTests.NAME_HIDE_LIST).click()
			except:
				self.driver.find_element_by_name(ESFunctionTests.NAME_TOOLS).click()
				self.driver.find_element_by_name(ESFunctionTests.NAME_HIDE_LIST).click()

			self.driver.find_element_by_name(ESFunctionTests.NAME_RESTORE).click()
			self.driver.find_element_by_id('com.estrongs.android.pop:id/tool_return').click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_REFRESH).click()
			self.driver.find_element_by_name(ESFunctionTests.FILE_TEST)

			self._removeFile()
			
		except NoSuchElementException:
			self.fail(traceback.format_exc())
		pass
	

	def testLocalFilesShow(self):
		try:
			try:
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)
			except:
				self.driver.find_elements_by_id('com.estrongs.android.pop:id/indicator')[1].click()
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)

			self.driver.find_element_by_name(ESFunctionTests.DIRECTORY_TEST)

		except NoSuchElementException:
			self.fail(traceback.format_exc())
			pass


	def testAddShortcutIcontoHomeScreen(self):
		try:
			try:
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)
			except:
				self.driver.find_elements_by_id('com.estrongs.android.pop:id/indicator')[1].click()
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)

			el = self.driver.find_element_by_name(ESFunctionTests.DIRECTORY_TEST)
			self.driver.tap([(el.location['x']+10, el.location['y']+10)], 10000)
			self.driver.find_element_by_name(ESFunctionTests.NAME_MORE).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_DESKTOP).click()
			
			#NOTE: press the home button on the screen
			self.driver.press_keycode(4)
			sleep(3)
			self.driver.press_keycode(4)

			el0 = self.driver.find_element_by_id('com.android.launcher:id/search_button_container')
			el1 = self.driver.find_element_by_name(ESFunctionTests.DIRECTORY_TEST)
			self.driver.swipe(el1.location['x']+10, el1.location['y']+10, \
				el0.location['x'] + el0.size['width']//2, el0.location['y'] + el0.size['height']//2, 30000)
			

		except NoSuchElementException:
			self.fail(traceback.format_exc())
			pass

	def testMainUIAndEnterSuspend(self):
		try:
			try:
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)
			except:
				self.driver.find_elements_by_id('com.estrongs.android.pop:id/indicator')[1].click()
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)

			self._suspendAndResume()

			self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testMainUIAndForceStop(self):
		try:
			self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)

			print 'kill the self\'s proc'
			os.system('pid=`adb shell ps | grep com.estrongs.android.pop | awk \'{print $2}\'` && adb shell kill $pid')
			sleep(10) 
			self.driver.find_element_by_id('com.android.launcher:id/search_button_container') 

			print 'start the self\'s proc'
			os.system('adb shell am start com.estrongs.android.pop/.view.FileExplorerActivity') 
			self.driver.find_element_by_name(ESFunctionTests.NAME_HOME)


		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testBackupApp(self):
		try:
			try:
				print 'click the item "', ESFunctionTests.NAME_HOMEPAGE, '"'
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOMEPAGE).click()

			except NoSuchElementException:
				print 'click the item "', ESFunctionTests.NAME_LOCAL, '"'
				self.driver.find_element_by_name(ESFunctionTests.NAME_LOCAL).click()

				print 'click the item "', ESFunctionTests.NAME_HOMEPAGE, '" again'
				self.driver.find_element_by_name(ESFunctionTests.NAME_HOMEPAGE).click()

			print 'click the icon "', ESFunctionTests.NAME_APP, '"'
			self.driver.find_element_by_name(ESFunctionTests.NAME_APP).click()

			el = self.driver.find_element_by_name(ESFunctionTests.NAME_UNLOCK)
			self.driver.tap([(el.location['x'] + el.size['width'] // 2, el.location['y'] - 30),], 5000)

			print 'click the item "', ESFunctionTests.NAME_BACKUP, '"'
			self.driver.find_element_by_name(ESFunctionTests.NAME_BACKUP).click()

			print 'click the item "', ESFunctionTests.NAME_HOME, '"'
			self.driver.find_element_by_name(ESFunctionTests.NAME_HOME).click()

			print 'enter the directory "', ESFunctionTests.DIRECTORY_BACKUP, '"'
			self.driver.find_element_by_name(ESFunctionTests.DIRECTORY_BACKUP).click()

			print 'enter the directory "', ESFunctionTests.DIRECTORY_APPS, '"'
			self.driver.find_element_by_name(ESFunctionTests.DIRECTORY_APPS).click()

			el = self.driver.find_element_by_id('com.estrongs.android.pop:id/message')
			print el.text
			self.assertTrue(el.text.find(ESFunctionTests.NAME_UNLOCK) == 0)
			self.driver.tap([(el.location['x'], el.location['y']),], 5000)

			print 'click the button "', ESFunctionTests.NAME_DELETE, '"'
			self.driver.find_element_by_name(ESFunctionTests.NAME_DELETE).click()
			self.driver.find_element_by_name(ESFunctionTests.NAME_OK).click()


		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def _suspendAndResume(self):
		print 'suspend with the command \"adb shell \'echo mem >/sys/power/state\'\" '
		os.system('adb shell \'echo mem >/sys/power/state\'')

		print 'wait 10 seconds to suspend'
		sleep(10)

		print 'resume with the command \"adb shell \'echo on >/sys/power/state\'\" '
		os.system('adb shell \'echo on >/sys/power/state\'')

		print 'wait 10 seconds to resume'
		sleep(10)

	def _clearText(self, text):
		self.driver.keyevent(123)
		for i in range(0, len(text)):
			self.driver.keyevent(67)


	def _createFile(self):
		self.driver.find_element_by_name(ESFunctionTests.NAME_NEW).click()
		self.driver.find_element_by_name(ESFunctionTests.NAME_FILE).click()

		el = self.driver.find_element_by_class_name('android.widget.EditText')
		self._clearText(el.text)
		el.send_keys(ESFunctionTests.FILE_TEST)
		self.driver.find_element_by_name(ESFunctionTests.NAME_OK).click()
		

	def _removeFile(self):
		el = self.driver.find_element_by_name(ESFunctionTests.FILE_TEST)
		self.driver.tap([(el.location['x']+10, el.location['y']+10),], 10000)
		self.driver.find_element_by_name(ESFunctionTests.NAME_DELETE).click()
		self.driver.find_element_by_name(ESFunctionTests.NAME_OK).click()
		

if __name__ == '__main__':
	
	suite = unittest.TestSuite()
	#suite.addTest(ESFunctionTests('testReadDocument'))
	#suite.addTest(ESFunctionTests('testCopyCutFunction'))
	#suite.addTest(ESFunctionTests('testShowHideFile'))
	#suite.addTest(ESFunctionTests('testLocalFilesShow'))
	#suite.addTest(ESFunctionTests('testAddShortcutIcontoHomeScreen'))
	#suite.addTest(ESFunctionTests('testMainUIAndEnterSuspend'))
	#suite.addTest(ESFunctionTests('testMainUIAndForceStop'))
	suite.addTest(ESFunctionTests('testBackupApp'))

	unittest.TextTestRunner(verbosity=2).run(suite)
