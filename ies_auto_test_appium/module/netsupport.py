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

class NetsupportFunctionTests(unittest.TestCase):
	
	TIME_PAGE		= 15
	TIME_ATTEMPT		= 5
	TIMES_ATTEMPT		= 5

	NAME_ROOM		= 'New Room 1'
	NAME_SIGN_IN		= 'Sign In'
	NAME_SIGN_OUT		= 'Sign Out'
	NAME_OK			= 'OK'
	NAME_NAME		= 'netsupport'
	NAME_LESSON_TITLE	= 'Lesson Title'
	NAME_CHAT_WITH_TUTOR	= 'Chat with Tutor'
	NAME_YES		= 'Yes'
	NAME_SEND		= 'Send'
	NAME_QUESTION		= 'Am I OK?'
	NAME_FILE_EXPLORER	= 'File Explorer'
	NAME_BACK		= 'Back'
	NAME_DELETE		= 'Delete'

	TEXT_QUESTION		= 'Am I OK?'
	TEXT_OK			= 'OK'

	FILE_TRANSFER		= 'C'
	FILE_TEMP		= 'TEMPFILE.$$$.UDP'

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'CHTT2D18403F'
		desired_caps['appPackage'] = 'com.netsupportsoftware.school.student.oem.intel'
		desired_caps['appActivity'] = '.IntelCheckActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)


	def tearDown(self):

		try:
			self.driver.find_element_by_name(NetsupportFunctionTests.NAME_SIGN_OUT).click()
			self.driver.find_element_by_name(NetsupportFunctionTests.NAME_OK).click()

		except NoSuchElementException:
			pass

		self.driver.quit()
		sleep(2*NetsupportFunctionTests.TIME_PAGE)


	def testChatWithTutor(self):

		try:
			self._signIn()


			print 'click the button', NetsupportFunctionTests.NAME_CHAT_WITH_TUTOR
			self.driver.find_element_by_name(NetsupportFunctionTests.NAME_CHAT_WITH_TUTOR).click()
			
			print 'wait'
			sleep(NetsupportFunctionTests.TIME_PAGE)

			el = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
			print el.text
			self.assertEqual(el.text.find('Chat started at'), 0)

			el = self.driver.find_elements_by_class_name('android.widget.TextView')[3]
			print el.text
			self.assertEqual(el.text, NetsupportFunctionTests.NAME_NAME + ' has joined')

			el = self.driver.find_element_by_id('com.netsupportsoftware.school.student.oem.intel:id/chatBox')
			print 'input the question', NetsupportFunctionTests.TEXT_QUESTION
			el.send_keys(NetsupportFunctionTests.TEXT_QUESTION)

			print 'click the button "', NetsupportFunctionTests.NAME_SEND, '"'
			self.driver.find_element_by_name(NetsupportFunctionTests.NAME_SEND).click()

			print 'wait for the techer\'s answer'
			sleep(NetsupportFunctionTests.TIME_PAGE)

			print 'find the answer', NetsupportFunctionTests.TEXT_OK
			self.driver.find_element_by_name(NetsupportFunctionTests.TEXT_OK)
			self.driver.back()

			print 'return to the main page'
			self.driver.back()

			self._signOut()


		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testDisconnectFromTutor(self):
		try:
			self._signIn()
			self._signOut()

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testSurveyMode(self):
		try:
			self._signIn()

			time = 0
			while time < NetsupportFunctionTests.TIMES_ATTEMPT:
				try:
					print 'attempt to find the question in the ', time, ' times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_QUESTION)
					break

				except NoSuchElementException:
					sleep(NetsupportFunctionTests.TIME_PAGE)
					time += 1

			print 'click the button"', NetsupportFunctionTests.NAME_YES, '"'
			self.driver.find_element_by_name(NetsupportFunctionTests.NAME_YES).click()

			print 'wait for the teacher'
			sleep(2*NetsupportFunctionTests.TIME_PAGE)
			
			self._signOut()


		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testLockAndUnlock(self):
		try:
			self._signIn()

			time = 0
			while time<NetsupportFunctionTests.TIMES_ATTEMPT:
				try:
					print 'attempt to find the title in the ', time, 'times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_LESSON_TITLE)
					sleep(NetsupportFunctionTests.TIME_PAGE)
					time += 1

				except NoSuchElementException:
					break

			els = self.driver.find_elements_by_class_name('android.view.View')
			print 'get the number of the view', len(els)
			self.assertEqual(len(els), 1)

			time = 0
			while time<NetsupportFunctionTests.TIMES_ATTEMPT:
				try:
					print 'attempt to find the button in the ', time, 'times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_SIGN_OUT)
					break

				except NoSuchElementException:
					sleep(NetsupportFunctionTests.TIME_PAGE)
					time += 1

			self._signOut()

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testStudentDisableWifiWhenConnectToTutor(self):
		try:
			self._signIn()

			self._disableWifi()

			sleep(NetsupportFunctionTests.TIME_PAGE)
			self.driver.find_element_by_name(NetsupportFunctionTests.NAME_SIGN_OUT)

			self._enableWifi()

			self._signOut()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testStudentDisableWifiWhenSurvey(self):
		
		try:
			self._signIn()

			time = 0
			while time < NetsupportFunctionTests.TIMES_ATTEMPT:

				try:
					print 'attempt to find the question in the ', time, 'times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_QUESTION)

					self._disableWifi()

					print 'wait to disable the wifi'
					sleep(NetsupportFunctionTests.TIME_PAGE)

					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_SIGN_OUT)

					self._enableWifi()

					break

				except NoSuchElementException:
					sleep(NetsupportFunctionTests.TIME_PAGE)
					time += 1


			self._signOut()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testEnterSuspendWhileSurvey(self):

		try:
			self._signIn()

			time = 0
			while time < NetsupportFunctionTests.TIMES_ATTEMPT:

				try:
					print 'attempt to find the survey in ', time, 'times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_QUESTION)

					self._suspend()

					print 'wait to suspend'
					sleep(2*NetsupportFunctionTests.TIME_PAGE)

					self._resume()

					break

				except NoSuchElementException:
					sleep(NetsupportFunctionTests.TIME_PAGE)
					time += 1

			time = 0
			while time < NetsupportFunctionTests.TIMES_ATTEMPT:

				try:
					print 'attemp to find the question in the ', time, 'times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_QUESTION)

					print 'click the button "', NetsupportFunctionTests.NAME_YES, '"'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_YES).click()

					break

				except NoSuchElementException:
					sleep(NetsupportFunctionTests.TIME_PAGE)
					time += 1


			self._signOut()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testFileTransfer(self):
		try:
			self._signIn()
			
			time = 0
			while time < NetsupportFunctionTests.TIMES_ATTEMPT:
				try:
					print 'attempt to find the file in the ', time, 'times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_FILE_EXPLORER).click()
					self.driver.find_element_by_name(NetsupportFunctionTests.FILE_TRANSFER)

					print 'select the file "', NetsupportFunctionTests.FILE_TRANSFER, '"'
					self.driver.find_element_by_name(NetsupportFunctionTests.FILE_TRANSFER).click()

					print 'click the button "', NetsupportFunctionTests.NAME_DELETE, '"'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_DELETE).click()
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_OK).click()
					self.driver.back()

					break

				except NoSuchElementException:
					sleep(NetsupportFunctionTests.TIME_PAGE)
					self.driver.back()
					time += 1

			if time == NetsupportFunctionTests:
				self.fail('fail to transfer the file')

			self._signOut()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testStudentDisableWifiWhenFileTransfer(self):

		try:
			self._signIn()
			
			time = 0
			while time < NetsupportFunctionTests.TIMES_ATTEMPT:
				try:
					print 'attempt to find the temp file in the ', time, 'times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_FILE_EXPLORER).click()
					self.driver.find_element_by_name(NetsupportFunctionTests.FILE_TEMP)

					self._disableWifi()
					
					print 'wait'
					sleep(NetsupportFunctionTests.TIME_PAGE)

					self._enableWifi()

					try:
						print 'find the file"', NetsupportFunctionTests.FILE_TEMP, '"'
						self.driver.find_element_by_name(NetsupportFunctionTests.FILE_TEMP)

					except NoSuchElementException:
						self.driver.back()
						break

				except NoSuchElementException:
					sleep(NetsupportFunctionTests.TIME_PAGE)
					self.driver.back()
					time += 1


			self._signOut()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testFileTransferAndForceClose(self):

		try:
			self._signIn()
			
			time = 0
			while time < NetsupportFunctionTests.TIMES_ATTEMPT:
				try:
					print 'attempt to find the temp file in the ', time, 'times'
					self.driver.find_element_by_name(NetsupportFunctionTests.NAME_FILE_EXPLORER).click()
					self.driver.find_element_by_name(NetsupportFunctionTests.FILE_TEMP)

					print 'kill the self\'s proc'	
					os.system('pid=`adb shell ps | grep netsupportsoftware | awk \'{print $2}\'` && adb shell kill $pid')
					sleep(NetsupportFunctionTests.TIME_PAGE)
					self.driver.find_element_by_id('com.android.launcher:id/search_button_container')

					print 'wait'
					sleep(NetsupportFunctionTests.TIME_PAGE)

					print 'start the self\'s proc'
					os.system('adb shell am start com.netsupportsoftware.school.student.oem.intel/.IntelCheckActivity')
					sleep(NetsupportFunctionTests.TIME_PAGE)
					break

					
				except NoSuchElementException:
					sleep(NetsupportFunctionTests.TIME_PAGE)
					self.driver.back()
					time += 1


			self.driver.find_element_by_name(NetsupportFunctionTests.NAME_SIGN_IN)

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def _clearText(self, text):
		self.driver.keyevent(123)
		for i in range(0, len(text)):
			self.driver.keyevent(67)


	def _signIn(self):

		print 'input the name of the room'
		self.driver.find_element_by_id('com.netsupportsoftware.school.student.oem.intel:id/roomEditTextValue')\
			.send_keys(NetsupportFunctionTests.NAME_ROOM) 

		el = self.driver.find_element_by_id('com.netsupportsoftware.school.student.oem.intel:id/roomNameValue')
		if el.text != NetsupportFunctionTests.NAME_NAME:
			print 'clear the name'
			el.click()
			self._clearText(el.text)

			print 'input the name of the Name'
			el.send_keys(NetsupportFunctionTests.NAME_NAME)
			self.driver.back()

		print 'click the button Sign In'
		self.driver.find_element_by_id('com.netsupportsoftware.school.student.oem.intel:id/signInButton')\
			.click()

		time = 0
		while time<NetsupportFunctionTests.TIMES_ATTEMPT:
			try:
				print 'attempt to connect the teacher in ', time, 'times'
				self.driver.find_element_by_name(NetsupportFunctionTests.NAME_LESSON_TITLE)
				break
			except NoSuchElementException:
				sleep(NetsupportFunctionTests.TIME_ATTEMPT)
				time += 1

		self.driver.find_element_by_name(NetsupportFunctionTests.NAME_LESSON_TITLE)


	def _signOut(self):

		print 'click the button Sign Out'
		self.driver.find_element_by_name(NetsupportFunctionTests.NAME_SIGN_OUT).click()

		print 'click the button OK'
		self.driver.find_element_by_name(NetsupportFunctionTests.NAME_OK).click()

		print 'find the title Sign In'
		self.driver.find_element_by_name(NetsupportFunctionTests.NAME_SIGN_IN)


	def _enableWifi(self):

		print 'enable the wifi'
		os.system('adb shell svc wifi enable')


	def _disableWifi(self):

		print 'disable the wifi'
		os.system('adb shell svc wifi disable')

	def _suspend(self):

		print 'suspend with the command \"adb shell \'echo mem >/sys/power/state\'\" '
		os.system('adb shell \'echo mem >/sys/power/state\'')


	def _resume(self):

		print 'resume with the command \"adb shell \'echo on >/sys/power/state\'\" '
		os.system('adb shell \'echo on >/sys/power/state\'')


if __name__ == '__main__':
	
	suite = unittest.TestSuite()
	#suite.addTest(NetsupportFunctionTests('testChatWithTutor'))
	#suite.addTest(NetsupportFunctionTests('testDisconnectFromTutor'))
	#suite.addTest(NetsupportFunctionTests('testSurveyMode'))
	#suite.addTest(NetsupportFunctionTests('testLockAndUnlock'))
	#suite.addTest(NetsupportFunctionTests('testStudentDisableWifiWhenConnectToTutor'))
	#suite.addTest(NetsupportFunctionTests('testStudentDisableWifiWhenSurvey'))
	#suite.addTest(NetsupportFunctionTests('testFileTransfer'))
	#suite.addTest(NetsupportFunctionTests('testStudentDisableWifiWhenFileTransfer'))
	#suite.addTest(NetsupportFunctionTests('testEnterSuspendWhileSurvey'))
	suite.addTest(NetsupportFunctionTests('testFileTransferAndForceClose'))

	unittest.TextTestRunner(verbosity=2).run(suite)
