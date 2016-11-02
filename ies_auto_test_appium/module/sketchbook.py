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

class SketchBookFunctionTests(unittest.TestCase):
	
	POINT_INFO_X			= 700
	POINT_INFO_Y			= 130
	TIME_PAGE			= 10

	DIR_SKETCHBOOK			= '/sdcard/Autodesk/SketchBook3/SketchBookPreview'

	NAME_SAVE_CURRENT_SKETCH	= 'Save current sketch'
	NAME_GALLERY			= 'Gallery'
	NAME_TESTFILES			= 'TestFiles'

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'Baytrail_CR'
		desired_caps['appPackage'] = 'com.adsk.sketchbook.oem.intel'
		desired_caps['appActivity'] = 'com.adsk.sketchbook.SketchBook'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)

		try:
			self.driver.find_element_by_name('I accept').click()	
		except:
			pass

		try:
			self.driver.switch_to_alert().accept()
		except:
			pass

		print 'wait to load the main page'
		sleep(SketchBookFunctionTests.TIME_PAGE)

		print 'click the "OK" button in the information dialog'
		self.driver.tap([(SketchBookFunctionTests.POINT_INFO_X, SketchBookFunctionTests.POINT_INFO_Y),])

		print 'remove the files in the directory', SketchBookFunctionTests.DIR_SKETCHBOOK
		os.system('adb shell rm ' + SketchBookFunctionTests.DIR_SKETCHBOOK + '/*.png')

	def tearDown(self):
		self.driver.quit()


	def testImportImage(self):
		try:
			self.driver.find_elements_by_class_name('android.widget.ImageView')[3].click()
			self.driver.find_element_by_name('Import Image').click()

			print 'select the item gallery'
			self.driver.find_element_by_name(SketchBookFunctionTests.NAME_GALLERY).click()

			print 'wait'
			sleep(SketchBookFunctionTests.TIME_PAGE)

			print 'select the item TestFiles'
			x = self.driver.get_window_size()['width'] // 2
			y = self.driver.get_window_size()['height'] // 4 * 3
			self.driver.tap([(x, y)])


			print 'wait'
			sleep(SketchBookFunctionTests.TIME_PAGE)

			print 'tap the middle point of the screen'
			x = self.driver.get_window_size()['width'] // 2
			y = self.driver.get_window_size()['height'] // 2
			self.driver.tap([(x, y)])

			print 'wait'
			sleep(SketchBookFunctionTests.TIME_PAGE)
			
			print 'click the icon done for importing the image'
			self.driver.find_element_by_id('com.adsk.sketchbook.oem.intel:id/toolDoneButton').click()
			

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testNewSketch(self):
		try:
			els = self.driver.find_elements_by_class_name('android.widget.FrameLayout')

			startx = els[0].size['width'] // 2 - 50
			starty = 0
			endx = els[0].size['width'] // 2 + 50
			endy = starty

			print 'draw the line on the screen'
			self.driver.swipe(startx, starty, endx, endy, 0)

			self.driver.find_elements_by_class_name('android.widget.ImageView')[0].click()
			self.driver.find_element_by_id('com.adsk.sketchbook.oem.intel:id/mm_new_sketch').click()
			self.driver.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()

			print 'save the current sketch'
			self.driver.find_element_by_name(SketchBookFunctionTests.NAME_SAVE_CURRENT_SKETCH).click()
			sleep(SketchBookFunctionTests.TIME_PAGE)

			try:
				img = os.popen('adb shell ls ' + SketchBookFunctionTests.DIR_SKETCHBOOK).readlines()[0]
				print img.split('\n')[0]
				self.assertTrue('find the file')

			except IndexError:
				self.fail('not found the file')

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testDrawAndSave(self):
		try:
			els = self.driver.find_elements_by_class_name('android.widget.FrameLayout')

			startx = els[0].size['width'] // 2 - 50
			starty = 0
			endx = els[0].size['width'] // 2 + 50
			endy = starty
			self.driver.swipe(startx, starty, endx, endy, 0)

			print 'select the bottom icon on the right bar'
			el = self.driver.find_elements_by_class_name('android.widget.ImageView')[23]
			el.click() 

			print 'choose the color of the background'
			self.driver.tap([(el.location['x'] - 100, el.location['y'])])

			print 'clear the popup menu'
			x = self.driver.get_window_size()['width'] // 2
			y = self.driver.get_window_size()['height'] // 2
			self.driver.tap([(x, y)])

			print 'draw the line on the screen'
			self.driver.swipe(startx, starty+100, endx, endy+100, 0)

			self.driver.back()
			self.driver.find_element_by_name('Save and Exit').click()


			print 'wait to save the picture'
			sleep(SketchBookFunctionTests.TIME_PAGE)
			
			try:
				img = os.popen('adb shell ls ' + SketchBookFunctionTests.DIR_SKETCHBOOK).readlines()[0]
				print img.split('\n')[0]
				self.assertTrue('find the file')

			except IndexError:
				self.fail('not found the file')

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testNewFromCamera(self):
		try:
			self.driver.find_elements_by_class_name('android.widget.ImageView')[0].click()
			self.driver.find_element_by_name('Gallery').click()
			el = self.driver.find_elements_by_class_name('android.widget.ImageView')[3]
			el.click()
			self.driver.tap([(el.location['x'], el.location['y'] - 15),])
			self.driver.find_element_by_id('com.android.camera2:id/shutter_button').click()
			self.driver.find_element_by_id('com.android.camera2:id/cancel_button')

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testAddAndHideTheLayer(self):
		try:
			els = self.driver.find_elements_by_class_name('android.widget.FrameLayout')
			startx = els[0].size['width'] // 2 - 50
			starty = 0
			endx = els[0].size['width'] // 2 + 50
			endy = starty
			self.driver.swipe(startx, starty, endx, endy, 0)

			els0 = self.driver.find_elements_by_class_name('android.view.View')
			# click the '+' icon on the right panel
			self.driver.find_elements_by_class_name('android.widget.ImageView')[10].click()
			els1 = self.driver.find_elements_by_class_name('android.view.View')
			self.assertTrue(len(els0) + 2 == len(els1))

			els = self.driver.find_elements_by_class_name('android.widget.FrameLayout')
			startx = els[0].size['width'] // 2 
			starty = 0
			endx = els[0].size['width'] // 2 
			endy = 50
			self.driver.swipe(startx, starty, endx, endy, 0)

			els = self.driver.find_elements_by_class_name('android.widget.ImageView')
			# click the eye icon on the right panel
			self.driver.find_elements_by_class_name('android.widget.ImageView')[11].click()

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testEditModeAndEnterSuspend(self):
		try: 
			els = self.driver.find_elements_by_class_name('android.widget.FrameLayout')
			startx = els[0].size['width'] // 2 - 50
			starty = 0
			endx = els[0].size['width'] // 2 + 50
			endy = starty
			self.driver.swipe(startx, starty, endx, endy, 0)

			self._suspendAndResume()

			self.driver.find_element_by_id('com.adsk.sketchbook.oem.intel:id/top_bar_undo')

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testMainUIAndSuspend(self):
		try:
			self._suspendAndResume()
			self.driver.find_element_by_id('com.adsk.sketchbook.oem.intel:id/top_bar_undo')

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testEditModeAndForceStop(self):
		try:
			print 'draw the line in the page'
			els = self.driver.find_elements_by_class_name('android.widget.FrameLayout')
			startx = els[0].size['width'] // 2 - 50
			starty = 0
			endx = els[0].size['width'] // 2 + 50
			endy = starty
			self.driver.swipe(startx, starty, endx, endy, 0)

			print 'kill the self\'s proc'
			os.system('pid=`adb shell ps | grep com.adsk.sketchbook.oem.intel | awk \'{print $2}\'` && adb shell kill $pid')
			sleep(SketchBookFunctionTests.TIME_PAGE)
			self.driver.find_element_by_id('com.android.launcher:id/search_button_container')

			print 'restart the self\'s proc'
			os.system('adb shell am start com.adsk.sketchbook.oem.intel/com.adsk.sketchbook.SketchBook')
			sleep(SketchBookFunctionTests.TIME_PAGE)

			self.driver.find_element_by_id('com.adsk.sketchbook.oem.intel:id/top_bar_main_menu')

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


if __name__ == '__main__':

	suite = unittest.TestSuite()
	#suite.addTest(SketchBookFunctionTests('testImportImage'))
	#suite.addTest(SketchBookFunctionTests('testNewSketch'))
	#suite.addTest(SketchBookFunctionTests('testDrawAndSave'))
	#suite.addTest(SketchBookFunctionTests('testNewFromCamera'))
	#suite.addTest(SketchBookFunctionTests('testAddAndHideTheLayer'))
	#suite.addTest(SketchBookFunctionTests('testEditModeAndEnterSuspend'))
	#suite.addTest(SketchBookFunctionTests('testMainUIAndSuspend'))
	suite.addTest(SketchBookFunctionTests('testEditModeAndForceStop'))

        unittest.TextTestRunner(verbosity=2).run(suite)

