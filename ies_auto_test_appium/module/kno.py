#!/usr/bin/python

import os
import sys
import unittest 
import traceback

from time import sleep
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

#NOTE: if not, show 'A new session could not be created' error
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class KnoFunctionTests(unittest.TestCase):
	ACCOUNT 		= 'inteltest@kno.com'
	PASSWORD 		= '123456'
	DIR_TESTFILES		= 'TestFiles'
	FILE_SCREEN 		= 'screen.png'
	FILE_HIGHLIGHT 		= 'highlight.png'
	FILE_IMG		= 'kno.jpg'
	PAGE_SLEEP_TIME 	= 10

	NAME_BOOK 		= 'Sample: Biology'
	NAME_STORE		= 'Store'
	NAME_ADD_NOTE		= 'Add Note'
	NAME_SELECT_PICTURE	= 'Select a picture'
	NAME_ES			= 'ES File Explorer'
	NAME_PICTURES		= 'Pictures'
	
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'Baytrail_CR'
		desired_caps['appPackage'] = 'com.kno.textbooks'
		desired_caps['appActivity'] = 'md5c6fc437aecb30701f36d1ffb4d673fe3.SplashActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)
		
		#NOTE: may not encounter the "Cancel" button when launching
		try:
			self.driver.find_element_by_name('Cancel').click()
		except:
			pass


	def tearDown(self):
		self.driver.quit()


	def testSignIn(self):
		try:
			print 'click the top-right icon in the home page'
			self.driver.find_element_by_class_name('android.widget.ImageButton').click()
			
			print 'click the "Sign in" menu item'
			self.driver.find_element_by_name('Sign In').click()

			self.driver.find_element_by_id('com.kno.textbooks:id/signin_email_text').send_keys(KnoFunctionTests.ACCOUNT)
			self.driver.find_element_by_id('com.kno.textbooks:id/signin_password_text').send_keys(KnoFunctionTests.PASSWORD) 
			self.driver.find_element_by_name('Sign In').click()

			#NOTE: wait to enter the home page when clicking the "Sign In" button			
			sleep(30)

			self.driver.find_element_by_class_name('android.widget.ImageButton').click()

			el = None
			try:
				el = self.driver.find_element_by_name('Sign In')
			except:
				pass

			self.assertTrue(None == el);

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testViewNexPagePreviousPage(self):
		try:
			self.driver.find_element_by_id('com.kno.textbooks:id/bookCover').click()
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			el = self.driver.find_element_by_id('android:id/action_bar_title')
			self.assertEqual(el.text, KnoFunctionTests.NAME_BOOK)

			el = self.driver.find_element_by_id('com.kno.textbooks:id/reader_page_hint')
			self.assertEqual(el.text, 'Chapter 4, page 59')

			el = self.driver.find_element_by_id('com.kno.textbooks:id/overlay_layer')
			start_x =  el.location['x'] + el.size['width'] * 3// 4
			end_x = el.location['x'] + el.size['width'] // 4
			start_y = end_y = el.location['y'] + el.size['height'] // 2
			self.driver.swipe(start_x, start_y, end_x, end_y)	

			#NOTE: wait to load the corresponding page
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			el = self.driver.find_element_by_id('com.kno.textbooks:id/reader_page_hint')
			self.assertEqual(el.text, 'Chapter 4, page 60')

			self.driver.swipe(end_x, end_y, start_x, start_y)	

			#NOTE: wait to load the corresponding page
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			el = self.driver.find_element_by_id('com.kno.textbooks:id/reader_page_hint')
			self.assertEqual(el.text, 'Chapter 4, page 59')

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	
	def testHighlightText(self):
		try:
			self.driver.find_element_by_id('com.kno.textbooks:id/bookCover').click()
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			el = self.driver.find_element_by_id('android:id/action_bar_title')
			self.assertEqual(el.text, KnoFunctionTests.NAME_BOOK)

			el = self.driver.find_element_by_id('com.kno.textbooks:id/overlay_layer')
			x =  el.location['x'] + el.size['width'] // 2
			y = el.location['y'] + el.size['height'] // 2
			self.driver.tap([(x, y),], 3000)

			el = self.driver.find_element_by_id('com.kno.textbooks:id/reader_menu_highlight_selected_color')
			self.assertIsNotNone(el)
			el.click()

			el = self.driver.find_element_by_name('Needs Clarification')
			el.click()

			self.driver.find_element_by_class_name('android.widget.ImageButton').click()
			
			el = self.driver.find_element_by_name('Delete Highlight')
			el.click()

			el = self.driver.find_element_by_name(KnoFunctionTests.NAME_BOOK)
			self.assertIsNotNone(el)


		except NoSuchElementException:
			self.fail(traceback.format_exc())

	
	def testAddNote(self):
		try:
			self.driver.find_element_by_id('com.kno.textbooks:id/bookCover').click()
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			self.driver.find_element_by_id('com.kno.textbooks:id/reader_menu_add_sticky_note').click()

			el = self.driver.find_element_by_id('com.kno.textbooks:id/sticky_text')
			self.assertIsNotNone(el)
			el.send_keys(KnoFunctionTests.NAME_BOOK)
			self.assertEqual(el.text, KnoFunctionTests.NAME_BOOK)

			self.driver.find_element_by_id('com.kno.textbooks:id/sticky_minimize_button').click()

			el = self.driver.find_element_by_id('com.kno.textbooks:id/docked_global_sticky')
			self.assertIsNotNone(el)
			el.click()

			el = self.driver.find_element_by_id('com.kno.textbooks:id/sticky_text')
			self.assertEqual(el.text, KnoFunctionTests.NAME_BOOK)

			self.driver.find_element_by_id('com.kno.textbooks:id/sticky_delete_button').click()
			self.driver.find_element_by_id('android:id/button1').click()
			
		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testEnterIntoTheKNOStore(self):
		try:
			print 'click the item on top bar'
			self.driver.find_element_by_class_name('android.widget.ImageButton').click()

			print 'click the menu item'
			el = self.driver.find_element_by_id('android:id/title')
			self.assertEqual(el.text, 'Store')
			el.click()

			#NOTE: enter the Store page
			times = 0
			el = None

			while times<6:
				print 'attempt to check the tilte of the page store in', times, 'times'
				el = self.driver.find_element_by_name(KnoFunctionTests.NAME_STORE)
				sleep(KnoFunctionTests.PAGE_SLEEP_TIME)
				times = times + 1

			self.assertTrue(el.text == KnoFunctionTests.NAME_STORE)	

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testCheckCoversInMainUI(self):
		try:
			els = self.driver.find_elements_by_id('com.kno.textbooks:id/bookCover')
			self.assertIsNotNone(els)

			print 'wait to load books'
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			#NOTE: 2 is the number of the default book
			print 'get', len(els), ' books'
			self.assertGreater(len(els), 2)
			
		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testInsertPictureOrVideoNotesFromES(self):
		try:
			print 'open the book'
			self.driver.find_element_by_id('com.kno.textbooks:id/bookCover').click()

			print 'wait to load the book'
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			el = self.driver.find_element_by_id('android:id/action_bar_title')
			self.assertEqual(el.text, KnoFunctionTests.NAME_BOOK)

			self.driver.find_element_by_id('com.kno.textbooks:id/reader_menu_add_sticky_note').click()
			el = self.driver.find_element_by_id('com.kno.textbooks:id/sticky_text')
			el.send_keys(KnoFunctionTests.NAME_BOOK)

			self.driver.find_element_by_id('com.kno.textbooks:id/reader_menu_journal').click()

			print 'add the note'
			self.driver.find_element_by_name(KnoFunctionTests.NAME_ADD_NOTE).click()

			print 'insert the picture'
			self.driver.find_element_by_name(KnoFunctionTests.NAME_SELECT_PICTURE).click()
	
			#NOTE: load image
			sleep(25)

			print 'select the \'ES File Explore\''
			self.driver.find_element_by_name(KnoFunctionTests.NAME_ES).click()

			print 'select the directory \'TestFiles\' '
			self.driver.find_element_by_name(KnoFunctionTests.DIR_TESTFILES).click()

			self.driver.find_element_by_name(KnoFunctionTests.FILE_IMG).click()
			self.driver.find_element_by_id('com.kno.textbooks:id/journal_photovideonote_edittext').send_keys(KnoFunctionTests.NAME_BOOK)
			self.driver.back()

			print 'save the note'
			self.driver.find_element_by_name('Save').click()
			el = self.driver.find_element_by_id('com.kno.textbooks:id/journal_photovideonote_text')
			self.assertEqual(el.text, KnoFunctionTests.NAME_BOOK + '\n\n')

			#NOTE: delete the previously created note
			print 'delete the note'
			self.driver.find_element_by_id('android:id/up').click()		
			self.driver.find_element_by_id('com.kno.textbooks:id/docked_global_sticky').click()
			self.driver.find_element_by_id('com.kno.textbooks:id/sticky_delete_button').click()
			self.driver.find_element_by_name('Delete').click()

		except	NoSuchElementException:
			sleep(30)
			self.fail(traceback.format_exc())

	def testKnoWillCrashWhenSelectTextAndSearch(self):
		try:
			self.driver.find_element_by_id('com.kno.textbooks:id/bookCover').click()
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			el = self.driver.find_element_by_id('android:id/action_bar_title')
			self.assertEqual(el.text, KnoFunctionTests.NAME_BOOK)

			el = self.driver.find_element_by_id('com.kno.textbooks:id/overlay_layer')
			x =  el.location['x'] + el.size['width'] // 2
			y = el.location['y'] + el.size['height'] // 2
			self.driver.tap([(x, y),], 3000)

			self.driver.find_element_by_id('com.kno.textbooks:id/reader_menu_highlight_selected_search').click()
			self.driver.find_element_by_name('This Book').click()

			self.driver.implicitly_wait(15)

			el = self.driver.find_element_by_id('com.kno.textbooks:id/advancedSearchTitle')
			self.assertEqual(el.text, 'Advanced Search')

			self.driver.back()
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			self.driver.tap([(x,y - 20)])
			self.driver.find_element_by_class_name('android.widget.ImageButton').click()
			self.driver.find_element_by_name('Delete Highlight').click()

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testReadBookAndEnterSuspend(self):
		try:
			print 'open the book'
			self.driver.find_element_by_id('com.kno.textbooks:id/bookCover').click()
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			self._suspendAndResume()

			print 'find out the book'
			self.driver.find_element_by_name(KnoFunctionTests.NAME_BOOK)
			
		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testMainUIAndEnterSuspend(self):
		try:
			els = self.driver.find_elements_by_id('com.kno.textbooks:id/bookCover')

			print "the total of books is" , len(els)

			self.assertIsNotNone(els)

			#NOTE: 2 is the number of the default book
			self.assertGreater(len(els), 2)


			self._suspendAndResume()

			els1 = self.driver.find_elements_by_id('com.kno.textbooks:id/bookCover')

			self.assertEqual(len(els), len(els1))


		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testReadBookAndForceStop(self):

		try:
			print 'open the book'
			self.driver.find_element_by_id('com.kno.textbooks:id/bookCover').click()
			
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			print 'kill the self\'s proc'
			os.system('pid=`adb shell ps | grep com.kno.textbooks | awk \'{print $2}\'` && adb shell kill $pid')
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)
			os.system('pid=`adb shell ps | grep com.kno.textbooks | awk \'{print $2}\'` && adb shell kill $pid')
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			self.driver.find_element_by_id('com.android.launcher:id/search_button_container')

			print 'restart the self\'s proc'
			os.system('adb shell am start com.kno.textbooks/md5c6fc437aecb30701f36d1ffb4d673fe3.SplashActivity' )
			sleep(KnoFunctionTests.PAGE_SLEEP_TIME)

			print 'open the book again'
			self.driver.find_element_by_id('com.kno.textbooks:id/bookCover').click()

			self.driver.find_element_by_name(KnoFunctionTests.NAME_BOOK)

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


