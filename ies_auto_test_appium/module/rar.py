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

class RARFunctionTests(unittest.TestCase):

	NAME_YES		= 'Yes'
	NAME_SET_PASSWORD	= 'Set password...'
	NAME_ENTER_PASSWORD	= 'Enter password'
	NAME_OK			= 'OK'
	NAME_ZIP		= 'ZIP'
	NAME_RAR4X		= 'RAR 4.x'
	NAME_DELETE_FILES	= 'Delete files after archiving'

	FILE_TEST_ZIP		= 'test.zip'
	FILE_TEST_RAR		= 'test.rar'
	FILE_TEST4X_RAR		= 'test4x.rar'
	FILE_A			= 'A'
	FILE_B			= 'B'
	FILE_TESTFILES_RAR	= 'TestFiles.rar'
	FILE_TESTFILES_ZIP	= 'TestFiles.zip'

	DIRECTORY_ZIP		= 'test'
	DIRECTORY_RAR4X		= 'test4x'
	DIRECTORY_TESTFILES	= 'TestFiles'

	PASSWORD	= '123'

	TIME_PAGE	= 10

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'Baytrail_CR'
		desired_caps['appPackage'] = 'com.rarlab.rar'
		desired_caps['appActivity'] = '.MainActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)
		

	def tearDown(self):
		self.driver.quit()
		pass

	def testExtracttheArchive(self):
		try:
			try:
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()
			except NoSuchElementException:
				w = self.driver.get_window_size()['width']
				h = self.driver.get_window_size()['height']

				x = w // 2;
				y = h // 2;
				self.driver.swipe(x, y + y//2, x, y - y//3*2, 0)
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()

			#NOTE: check the zip format
			self.driver.find_element_by_name(RARFunctionTests.FILE_TEST_ZIP).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_extract').click()
			self.driver.find_element_by_id('com.rarlab.rar:id/btnok').click()
			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_ZIP).click()
			self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			self.driver.find_element_by_name(RARFunctionTests.FILE_B)
			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self._deleteUnzipDirectory()

			#NOTE: check the rar format
			self.driver.find_element_by_name(RARFunctionTests.FILE_TEST_RAR).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_extract').click()
			self.driver.find_element_by_id('com.rarlab.rar:id/btnok').click()
			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_ZIP).click()
			self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			self.driver.find_element_by_name(RARFunctionTests.FILE_B)
			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self._deleteUnzipDirectory()
				
			#NOTE: check the rar 4.X format
			self.driver.find_element_by_name(RARFunctionTests.FILE_TEST4X_RAR).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_extract').click()
			self.driver.find_element_by_id('com.rarlab.rar:id/btnok').click()
			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_RAR4X).click()
			self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			self.driver.find_element_by_name(RARFunctionTests.FILE_B)
			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self._deleteUnzipDirectory(RARFunctionTests.DIRECTORY_RAR4X)

		except NoSuchElementException:
			self.fail(traceback.format_exc())
		pass

	def testZipFormat(self):
		try:
			try:
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()
			except NoSuchElementException:
				w = self.driver.get_window_size()['width']
				h = self.driver.get_window_size()['height']

				x = w // 2;
				y = h // 2;
				self.driver.swipe(x, y + y//2, x, y - y//3*2, 0)
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()

			elA = self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			elB = self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			#NOTE: tick the files A and B
			xA = elA.location['x'] + elA.size['width'] + 3
			yA = elA.location['y'] + elA.size['height'] + 3
			xB = elB.location['x'] + elB.size['width'] + 3
			yB = elB.location['y'] + elB.size['height'] + 3
			self.driver.tap([(xA, yA),])
			self.driver.tap([(xB, yB),])

			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_add').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_ZIP).click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_SET_PASSWORD).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/getpsw_edit').send_keys(RARFunctionTests.PASSWORD)
			#NOTE: hide the keyboard
			self.driver.press_keycode(4)
			#NOTE: the first is to set the password, the second is to confirm the compress dialog
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()

			self.driver.find_element_by_name(RARFunctionTests.FILE_TESTFILES_ZIP).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_extract').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/getpsw_edit').send_keys(RARFunctionTests.PASSWORD)
			#NOTE: hide the keyboard
			self.driver.press_keycode(4)
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self._deleteUnzipDirectory(RARFunctionTests.DIRECTORY_TESTFILES)
			#NOTE: wait for the ready of the files
			sleep(3)
			self._deleteUnzipDirectory(RARFunctionTests.FILE_TESTFILES_ZIP)


		except NoSuchElementException:
			self.fail(traceback.format_exc())
			pass

	def testRarFormat(self):
		try:
			try:
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()
			except NoSuchElementException:
				w = self.driver.get_window_size()['width']
				h = self.driver.get_window_size()['height']

				x = w // 2;
				y = h // 2;
				self.driver.swipe(x, y + y//2, x, y - y//3*2, 0)
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()

			elA = self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			elB = self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			#NOTE: tick the files A and B
			xA = elA.location['x'] + elA.size['width'] + 3
			yA = elA.location['y'] + elA.size['height'] + 3
			xB = elB.location['x'] + elB.size['width'] + 3
			yB = elB.location['y'] + elB.size['height'] + 3
			self.driver.tap([(xA, yA),])
			self.driver.tap([(xB, yB),])

			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_add').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_SET_PASSWORD).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/getpsw_edit').send_keys(RARFunctionTests.PASSWORD)
			#NOTE: hide the keyboard
			self.driver.press_keycode(4)
			#NOTE: the first is to set the password, the second is to confirm the compress dialog
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()

			self.driver.find_element_by_name(RARFunctionTests.FILE_TESTFILES_RAR).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_extract').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/getpsw_edit').send_keys(RARFunctionTests.PASSWORD)
			#NOTE: hide the keyboard
			self.driver.press_keycode(4)
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self._deleteUnzipDirectory(RARFunctionTests.DIRECTORY_TESTFILES)
			#NOTE: wait for the ready of the files
			sleep(3)
			self._deleteUnzipDirectory(RARFunctionTests.FILE_TESTFILES_RAR)


		except NoSuchElementException:
			self.fail(traceback.format_exc())
			pass

	def testRar4xFormat(self):
		try:
			try:
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()
			except NoSuchElementException:
				w = self.driver.get_window_size()['width']
				h = self.driver.get_window_size()['height']

				x = w // 2;
				y = h // 2;
				self.driver.swipe(x, y + y//2, x, y - y//3*2, 0)
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()

			elA = self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			elB = self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			#NOTE: tick the files A and B
			xA = elA.location['x'] + elA.size['width'] + 3
			yA = elA.location['y'] + elA.size['height'] + 3
			xB = elB.location['x'] + elB.size['width'] + 3
			yB = elB.location['y'] + elB.size['height'] + 3
			self.driver.tap([(xA, yA),])
			self.driver.tap([(xB, yB),])

			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_add').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_RAR4X).click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_SET_PASSWORD).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/getpsw_edit').send_keys(RARFunctionTests.PASSWORD)
			#NOTE: hide the keyboard
			self.driver.press_keycode(4)
			#NOTE: the first is to set the password, the second is to confirm the compress dialog
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()

			self.driver.find_element_by_name(RARFunctionTests.FILE_TESTFILES_RAR).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_extract').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_id('com.rarlab.rar:id/getpsw_edit').send_keys(RARFunctionTests.PASSWORD)
			#NOTE: hide the keyboard
			self.driver.press_keycode(4)
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()
			self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			self.driver.find_element_by_id('com.rarlab.rar:id/filelist_icon').click()
			self._deleteUnzipDirectory(RARFunctionTests.DIRECTORY_TESTFILES)
			#NOTE: wait for the ready of the files
			sleep(3)
			self._deleteUnzipDirectory(RARFunctionTests.FILE_TESTFILES_RAR)


		except NoSuchElementException:
			self.fail(traceback.format_exc())
			pass

	def testDeleteFileAfterArchiving(self):
		try:
			try:
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()
			except NoSuchElementException:
				w = self.driver.get_window_size()['width']
				h = self.driver.get_window_size()['height']

				x = w // 2;
				y = h // 2;
				self.driver.swipe(x, y + y//2, x, y - y//3*2, 0)
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()

			elA = self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			elB = self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			#NOTE: tick the files A and B
			xA = elA.location['x'] + elA.size['width'] + 3
			yA = elA.location['y'] + elA.size['height'] + 3
			xB = elB.location['x'] + elB.size['width'] + 3
			yB = elB.location['y'] + elB.size['height'] + 3
			self.driver.tap([(xA, yA),])
			self.driver.tap([(xB, yB),])

			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_add').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_DELETE_FILES).click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()

			try:
				self.driver.find_element_by_name(RARFunctionTests.FILE_A)
				self.fail('do not delete the file')
			except NoSuchElementException:
				pass

			try:
				self.driver.find_element_by_name(RARFunctionTests.FILE_B)
				self.fail('do not delete the file')
			except NoSuchElementException:
				pass

			self._deleteUnzipDirectory(RARFunctionTests.FILE_TESTFILES_RAR)

		except NoSuchElementException:
			self.fail(traceback.format_exc())
			pass

	def testArchiveFileAndEnterSuspend(self):
		try:
			try:
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()
			except NoSuchElementException:
				w = self.driver.get_window_size()['width']
				h = self.driver.get_window_size()['height']

				x = w // 2;
				y = h // 2;
				self.driver.swipe(x, y + y//2, x, y - y//3*2, 0)
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()

			elA = self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			elB = self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			#NOTE: tick the files A and B
			xA = elA.location['x'] + elA.size['width'] + 3
			yA = elA.location['y'] + elA.size['height'] + 3
			xB = elB.location['x'] + elB.size['width'] + 3
			yB = elB.location['y'] + elB.size['height'] + 3
			self.driver.tap([(xA, yA),])
			self.driver.tap([(xB, yB),])

			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_add').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_ZIP).click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()

			print 'wait to zip the files'
			sleep(3)

			self._suspendAndResume()

			self._deleteUnzipDirectory(RARFunctionTests.FILE_TESTFILES_ZIP)


		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testArchiveFilesAndForceStop(self):
		try:
			try:
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()
			except NoSuchElementException:
				w = self.driver.get_window_size()['width']
				h = self.driver.get_window_size()['height']

				x = w // 2;
				y = h // 2;
				self.driver.swipe(x, y + y//2, x, y - y//3*2, 0)
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()

			elA = self.driver.find_element_by_name(RARFunctionTests.FILE_A)
			elB = self.driver.find_element_by_name(RARFunctionTests.FILE_B)

			#NOTE: tick the files A and B
			xA = elA.location['x'] + elA.size['width'] + 3
			yA = elA.location['y'] + elA.size['height'] + 3
			xB = elB.location['x'] + elB.size['width'] + 3
			yB = elB.location['y'] + elB.size['height'] + 3
			self.driver.tap([(xA, yA),])
			self.driver.tap([(xB, yB),])

			self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_add').click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_ZIP).click()
			self.driver.find_element_by_name(RARFunctionTests.NAME_OK).click()

			print 'wait to zip the files'
			sleep(3)

			print 'kill the self\'s proc'
			os.system('pid=`adb shell ps | grep com.rarlab.rar | awk \'{print $2}\'` && adb shell kill $pid')
			sleep(RARFunctionTests.TIME_PAGE)
			self.driver.find_element_by_id('com.android.launcher:id/search_button_container')

			print 'kill start self\'s proc'
			os.system('adb shell am start com.rarlab.rar/.MainActivity')
			sleep(RARFunctionTests.TIME_PAGE)

			print 'delete the file "', RARFunctionTests.FILE_TESTFILES_ZIP, '"'
			try:
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()
			except NoSuchElementException:
				w = self.driver.get_window_size()['width']
				h = self.driver.get_window_size()['height']

				x = w // 2;
				y = h // 2;
				self.driver.swipe(x, y + y//2, x, y - y//3*2, 0)
				self.driver.find_element_by_name(RARFunctionTests.DIRECTORY_TESTFILES).click()

			self._deleteUnzipDirectory(RARFunctionTests.FILE_TESTFILES_ZIP)

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


	def _deleteUnzipDirectory(self, name='test'):
		#NOTE: delete the test directory from the test.zip
		el = self.driver.find_element_by_name(name)
		x = el.location['x'] + el.size['width'] + 3
		y = el.location['y'] + el.size['height'] + 3
		self.driver.tap([(x,y),])
		self.driver.find_element_by_id('com.rarlab.rar:id/maincmd_delete').click()
		self.driver.find_element_by_name(RARFunctionTests.NAME_YES).click()
		

