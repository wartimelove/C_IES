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
class PixlrFunctionTests(unittest.TestCase):

	NAME_CANCEL	= 'Cancel'
	NAME_ACCEPT	= 'I accept'
	NAME_FRESH	= 'Fresh'
	NAME_COLLAGE	= 'Collage'
	NAME_PHOTOS	= 'Photos'
	NAME_ES		= 'ES File Explorer'
	NAME_DONE	= 'Done'
	NAME_FINISH	= 'Finish' 
	NAME_CUSTOM	= 'Custom' 
	NAME_APPLY	= 'Apply'
	NAME_CLOSE	= 'Close'
	NAME_ADJUSTMENT	= 'Adjustment'
	NAME_ROTATE	= 'Rotate'
	
	DIR_TESTFILES	= 'TestFiles'
	FILE_IMG	= 'kno.jpg'

	TIME_PAGE	= 10

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'Baytrail_CR'
		desired_caps['appPackage'] = 'com.pixlr.oem.intel'
		desired_caps['appActivity'] = 'com.pixlr.express.StartupActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)
		
		#NOTE: may not encounter the "Cancel" button when launching
		try:
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_CANCEL).click()
		except:
			pass

		try:
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_ACCEPT).click()
		except:
			pass

		try:
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_FRESH)
		except:
			self._initPhotos()


	def tearDown(self):
		self.driver.quit()


	def testCollage(self):
		try:
			print 'click the button ', PixlrFunctionTests.NAME_COLLAGE, 'in the page'
			self.driver.find_element_by_id('com.pixlr.express:id/collage').click()

			print 'click the directory in the left navigation'
			self.driver.find_element_by_id('com.pixlr.express:id/text').click()

			print 'select the image'
			self.driver.find_elements_by_class_name('android.widget.ImageView')[1].click()

			print 'select the image again'
			self.driver.find_elements_by_class_name('android.widget.ImageView')[1].click()

			self.driver.find_element_by_name(PixlrFunctionTests.NAME_DONE).click()
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_FINISH).click()
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_CUSTOM).click()
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_APPLY).click()
			self.driver.find_element_by_id('android:id/customPanel')

			# wait to save the customized picture
			print 'wait to save the custom image'
			sleep(3 * PixlrFunctionTests.TIME_PAGE)

			self.driver.find_element_by_name(PixlrFunctionTests.NAME_CLOSE).click()

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testAddText(self):
		try:
			# click the cirle icon in the page
			self.driver.find_elements_by_class_name('android.widget.ImageView')[4].click()
			self.driver.find_element_by_name('Type').click()
			self.driver.find_element_by_name('Default').click()
			self.driver.find_element_by_id('com.pixlr.express:id/edit_box').send_keys('ppixlr\n')
			self.driver.find_element_by_id('com.pixlr.express:id/edit_box').send_keys('pppixlrr\n')
			self.driver.find_element_by_name('OK').click()

			self.driver.find_element_by_name('Color').click()		
			self.driver.find_element_by_id('com.pixlr.express:id/color_picker').click()
			self.driver.find_element_by_name('Left').click()
			self.driver.find_element_by_name('Center').click()
			self.driver.find_element_by_name('Right').click()
			self.driver.find_element_by_name('Apply').click()
			self.driver.find_element_by_name('Save')

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testAddBorders(self):
		try:
			# click the cirle icon in the page
			self.driver.find_elements_by_class_name('android.widget.ImageView')[4].click()
			self.driver.find_element_by_name('Borders').click()
			self.driver.find_element_by_name('Default').click()
			self.driver.find_element_by_name('Black').click()
			self.driver.find_element_by_name('Apply').click()
			self.driver.find_element_by_name('Save').click()
			self.driver.find_element_by_name('Current')

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testPhotoAdjustment(self):
		try:
			# click the cirle icon in the page
			self.driver.find_elements_by_class_name('android.widget.ImageView')[4].click()
			self.driver.find_element_by_name('Adjustment').click()
			self.driver.find_element_by_name('Rotate').click()
			self.driver.find_element_by_id('com.pixlr.express:id/rightRotate').click()
			self.driver.find_element_by_name('Apply').click()
			self.driver.find_element_by_name('Save').click()
			self.driver.find_element_by_name('Current')

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testTakeAndViewAPhoto(self):
		try:
			self.driver.find_element_by_id('com.pixlr.express:id/take').click()
			self.driver.find_element_by_id('com.pixlr.express:id/takePic').click()
			self.driver.find_element_by_id('com.pixlr.express:id/confirmOk').click()
			self.driver.find_element_by_name('Adjustment').click()
			self.driver.find_element_by_name('Rotate').click()
			self.driver.find_element_by_id('com.pixlr.express:id/rightRotate').click()
			self.driver.find_element_by_name('Apply').click()
			self.driver.find_element_by_name('Save').click()
			self.driver.find_element_by_name('Current')

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testEditModeAndEnterSuspend(self):
		try:
			print 'select the circle icon in the page'
			self.driver.find_elements_by_class_name('android.widget.ImageView')[4].click()

			print 'click the item', PixlrFunctionTests.NAME_ADJUSTMENT, 'in the page'
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_ADJUSTMENT).click()

			print 'click the item', PixlrFunctionTests.NAME_ROTATE, 'in the page'
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_ROTATE).click()

			self.driver.find_element_by_id('com.pixlr.express:id/rightRotate').click()

			self._suspendAndResume()
			
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_APPLY)

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testMainUIAndEnterSuspend(self):
		try:	
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_FRESH)
			self._suspendAndResume()
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_FRESH)

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testEditModeAndForceStop(self):
		try:
			print 'select the circle icon in the page'
			self.driver.find_elements_by_class_name('android.widget.ImageView')[4].click()

			print 'click the item', PixlrFunctionTests.NAME_ADJUSTMENT, 'in the page'
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_ADJUSTMENT).click()

			print 'click the item', PixlrFunctionTests.NAME_ROTATE, 'in the page'
			self.driver.find_element_by_name(PixlrFunctionTests.NAME_ROTATE).click()

			self.driver.find_element_by_id('com.pixlr.express:id/rightRotate').click()

			print 'kill the self\'s proc'
			os.system('pid=`adb shell ps | grep com.pixlr.oem.intel | awk \'{print $2}\'` && adb shell kill $pid')
			sleep(PixlrFunctionTests.TIME_PAGE)
			os.system('pid=`adb shell ps | grep com.pixlr.oem.intel | awk \'{print $2}\'` && adb shell kill $pid')
			sleep(PixlrFunctionTests.TIME_PAGE)
			self.driver.find_element_by_id('com.android.launcher:id/search_button_container')

			print 'restart the self\'s proc'
			os.system('adb shell am start com.pixlr.oem.intel/com.pixlr.express.StartupActivity')
			sleep(PixlrFunctionTests.TIME_PAGE)

			self.driver.find_element_by_name(PixlrFunctionTests.NAME_COLLAGE)


		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def _initPhotos(self):
		print 'click the item ', PixlrFunctionTests.NAME_PHOTOS, 'in the page'
		self.driver.find_element_by_id('com.pixlr.express:id/choose').click()

		print 'click the item', PixlrFunctionTests.NAME_ES, 'in the page'
		self.driver.find_element_by_name(PixlrFunctionTests.NAME_ES).click()

		print 'enter the directory', PixlrFunctionTests.DIR_TESTFILES
		self.driver.find_element_by_name(PixlrFunctionTests.DIR_TESTFILES).click()

		print 'select the image', PixlrFunctionTests.FILE_IMG
		self.driver.find_element_by_name(PixlrFunctionTests.FILE_IMG).click()

		print 'click the button', PixlrFunctionTests.NAME_CANCEL
		self.driver.find_element_by_name(PixlrFunctionTests.NAME_CLOSE).click()


	def _suspendAndResume(self):
		print 'suspend with the command \"adb shell \'echo mem >/sys/power/state\'\" '
		os.system('adb shell \'echo mem >/sys/power/state\'')

		print 'wait 10 seconds to suspend'
		sleep(10)

		print 'resume with the command \"adb shell \'echo on >/sys/power/state\'\" '
		os.system('adb shell \'echo on >/sys/power/state\'')

		print 'wait 10 seconds to resume'
		sleep(10)


if __name__ == '__main__':
	
	suite = unittest.TestSuite()

	#suite.addTest(PixlrFunctionTests('testCollage'))
	#suite.addTest(PixlrFunctionTests('testAddText'))
	#suite.addTest(PixlrFunctionTests('testAddBorders'))
	#suite.addTest(PixlrFunctionTests('testPhotoAdjustment'))
	#suite.addTest(PixlrFunctionTests('testTakeAndViewAPhoto'))
	#suite.addTest(PixlrFunctionTests('testEditModeAndEnterSuspend'))
	#suite.addTest(PixlrFunctionTests('testMainUIAndEnterSuspend'))
	suite.addTest(PixlrFunctionTests('testEditModeAndForceStop'))

	unittest.TextTestRunner(verbosity=2).run(suite)
