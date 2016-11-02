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

class TutorTestCase(unittest.TestCase):

	NAME_START_ROOM		= 'Start Room'
	NAME_ETNER_ROOM		= 'Enter Room'
	NAME_ROOM		= 'New Room 1'
	NAME_STUDENT		= 'netsupport'
	NAME_START_SURVEY	= 'Start Survey'
	NAME_LOCK		= 'Lock'
	NAME_UNLOCK		= 'Unlock'
	NAME_TUTOR		= 'netsupport'
	NAME_LESSON		= 'netsupport'
	NAME_LEAVE_ROOM		= 'Leave Room'
	NAME_OK			= 'OK'
	NAME_SEND		= 'Send'
	NAME_NO_ACTIVE_FILE	= 'No active file transfers'
	NAME_DISCONNECTED	= 'Disconnected'

	TIME_PAGE	= 10
	TEXT_QUESTION	= 'Am I OK?'
	TEXT_CHAT	= '1'
	TEXT_OK		= 'OK'
	TIMES_ATTEMPT	= 5

	FILE_TRANSFER	= 'C'

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'Baytrail_CR'
		desired_caps['appPackage'] = 'com.netsupportsoftware.school.tutor.oem.intel'
		desired_caps['appActivity'] = 'com.netsupportsoftware.school.tutor.activity.IntelSplashActivity'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)
		

	def tearDown(self):
		self.driver.quit()


	def testStartRoom(self):
		try:
			self._enterRoom()
			self._leaveRoom()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testChatWithTutor(self):
		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)

			print 'wait for the student "', TutorTestCase.NAME_STUDENT, '"'
			sleep(TutorTestCase.TIME_PAGE)

			time = 0
			while time < TutorTestCase.TIMES_ATTEMPT:

				try:
					print 'attempt to find the message in the ', time, 'times'
					self.driver.find_element_by_name(TutorTestCase.TEXT_CHAT).click()

					print 'click the student"', TutorTestCase.NAME_STUDENT, '"'
					self.driver.find_element_by_name(TutorTestCase.NAME_STUDENT).click()
					print 'find the question"', TutorTestCase.TEXT_QUESTION, '"'
					self.driver.find_element_by_name(TutorTestCase.TEXT_QUESTION)

					print 'answer with the string"', TutorTestCase.TEXT_OK, '"'
					self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/chatBox').send_keys(TutorTestCase.TEXT_OK)


					print 'click the button"', TutorTestCase.NAME_SEND, '"'
					self.driver.find_element_by_name(TutorTestCase.NAME_SEND).click()

					print 'wait for the student'
					sleep(TutorTestCase.TIME_PAGE)

					break

				except NoSuchElementException:
					self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/thumbnails').click()
					sleep(TutorTestCase.TIME_PAGE)
					self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/icons').click()

					time += 1

			self._leaveRoom()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testDisconnectFromTutor(self):
		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)
			self._leaveRoom()

		except NoSuchElementException:
				self.fail(traceback.format_exc())

	def testSurveyMode(self):
		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)

			print 'click the button survey'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/survey').click()

			print 'click the button', TutorTestCase.NAME_START_SURVEY
			self.driver.find_element_by_name(TutorTestCase.NAME_START_SURVEY).click()

			sleep(TutorTestCase.TIME_PAGE)

			print 'input the question "', TutorTestCase.TEXT_QUESTION, '"'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/questionVal').send_keys(TutorTestCase.TEXT_QUESTION)
			self.driver.press_keycode(66)

			print 'click the button OK'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/go').click()

			time = 0
			while time < TutorTestCase.TIMES_ATTEMPT:
				try:
					print 'attempt to find the result in the ', time, ' times'
					self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/badgeIcon')
					sleep(TutorTestCase.TIME_PAGE)
					time += 1

				except NoSuchElementException:
					break

			self._leaveRoom()


		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testLockAndUnlock(self):
		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)

			print 'wait for the student'
			sleep(2*TutorTestCase.TIME_PAGE)

			print 'click the button"', TutorTestCase.NAME_LOCK, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_LOCK).click()

			sleep(3*TutorTestCase.TIME_PAGE)

			print 'click the button"', TutorTestCase.NAME_UNLOCK, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_UNLOCK).click()

			self._leaveRoom()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testStudentDisableWifiWhenConnectToTutor(self):
		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)
			self._leaveRoom1()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testStudentDisableWifiWhenSurvey(self):

		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)

			print 'click the button survey'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/survey').click()

			print 'click the button "', TutorTestCase.NAME_START_SURVEY, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_START_SURVEY).click()

			sleep(TutorTestCase.TIME_PAGE)

			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/questionVal').send_keys(TutorTestCase.TEXT_QUESTION)
			self.driver.press_keycode(66)

			print 'click the button OK'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/go').click()
			self._leaveRoom1()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testEnterSuspendWhileSurvey(self):

		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)

			print 'click the button survey'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/survey').click()

			print 'click the button "', TutorTestCase.NAME_START_SURVEY, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_START_SURVEY).click()

			sleep(TutorTestCase.TIME_PAGE)

			print 'input the question "', TutorTestCase.TEXT_QUESTION, '"'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/questionVal').send_keys(TutorTestCase.TEXT_QUESTION)
			self.driver.press_keycode(66)

			print 'click the button OK'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/go').click()
			self._leaveRoom()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testFileTransfer(self):
		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)

			print 'click the button to transfer files'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/filetransfer').click()

			print 'select the file "', TutorTestCase.FILE_TRANSFER, '"'
			self.driver.find_element_by_name(TutorTestCase.FILE_TRANSFER).click()

			print 'click the button "', TutorTestCase.NAME_SEND, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_SEND).click()

			print 'select the student "', TutorTestCase.NAME_STUDENT, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_STUDENT).click()

			print 'click the button to transfer files'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/send').click()

			time = 0
			while time < TutorTestCase.TIMES_ATTEMPT:
				try:
					print 'attempt to find the dialog in the ', time, 'times'
					self.driver.find_element_by_name(TutorTestCase.NAME_NO_ACTIVE_FILE)
					break
				except:
					sleep(TutorTestCase.TIME_PAGE)
					time += 1

			self._leaveRoom()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testFileTransferAndForceStop(self):
		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)

			print 'click the button to transfer files'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/filetransfer').click()

			print 'select the file "', TutorTestCase.FILE_TRANSFER, '"'
			self.driver.find_element_by_name(TutorTestCase.FILE_TRANSFER).click()

			print 'click the button "', TutorTestCase.NAME_SEND, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_SEND).click()

			print 'select the student "', TutorTestCase.NAME_STUDENT, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_STUDENT).click()

			print 'click the button to send files'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/send').click()

			time = 0
			while time < TutorTestCase.TIMES_ATTEMPT:
				try:
					print 'attempt to find the dialog in the ', time, 'times'
					self.driver.find_element_by_name(TutorTestCase.NAME_DISCONNECTED)
					self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/ok').click()
					self.driver.find_element_by_name(TutorTestCase.NAME_NO_ACTIVE_FILE)
					break
				except:
					sleep(TutorTestCase.TIME_PAGE)
					time += 1

			self._leaveRoom1()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testStudentDisableWifiWhenFileTransfer(self):
		
		try:
			self._enterRoom()
			self._findStudent(TutorTestCase.NAME_STUDENT)

			print 'click the button to transfer files'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/filetransfer').click()

			print 'select the file "', TutorTestCase.FILE_TRANSFER, '"'
			self.driver.find_element_by_name(TutorTestCase.FILE_TRANSFER).click()

			print 'click the button "', TutorTestCase.NAME_SEND, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_SEND).click()

			print 'select the student "', TutorTestCase.NAME_STUDENT, '"'
			self.driver.find_element_by_name(TutorTestCase.NAME_STUDENT).click()

			print 'click the button to transfer files'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/send').click()

			time = 0
			while time < TutorTestCase.TIMES_ATTEMPT:
				try:
					print 'attempt to find the disconnected dialog in ', time, 'times'
					self.driver.find_element_by_name(TutorTestCase.NAME_DISCONNECTED)
					self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/ok').click()
					self.driver.find_element_by_name(TutorTestCase.NAME_NO_ACTIVE_FILE)
					break
				except:
					sleep(TutorTestCase.TIME_PAGE)
					time += 1

			self._leaveRoom()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def _enterRoom(self):

		try:
			self.driver.find_element_by_name(TutorTestCase.NAME_ROOM)

		except NoSuchElementException:
			
			print 'create the room', TutorTestCase.NAME_ROOM
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/addRoom').click()

			el = self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/roomName')
			print 'room\'s name: ', el.text
			if el.text != TutorTestCase.NAME_ROOM:
				el.click()
				self._clearText(el.text)
				el.send_keys(TutorTestCase.NAME_ROOM)
				self.driver.back()


		print 'click the button "', TutorTestCase.NAME_START_ROOM, '"'
		self.driver.find_element_by_name(TutorTestCase.NAME_START_ROOM).click()

		el = self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/tutorName')
		print 'Tutor Name:', el.text

		if el.text != TutorTestCase.NAME_TUTOR:
			el.click()
			self._clearText(el.text)
			el.send_keys(TutorTestCase.NAME_TUTOR)
			self.driver.back()

		el = self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/lessonTitle')
		print 'Lesson Title:', el.text

		if el.text != TutorTestCase.NAME_LESSON:
			el.click()
			self._clearText(el.text)
			el.send_keys(TutorTestCase.NAME_LESSON)
			self.driver.back()

		print 'click the button "', TutorTestCase.NAME_ETNER_ROOM, '"'
		self.driver.find_element_by_name(TutorTestCase.NAME_ETNER_ROOM).click()

	def _leaveRoom(self):

		time = 0
		while time < 2*TutorTestCase.TIMES_ATTEMPT:
			try:
				self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/thumbnails').click()
				sleep(TutorTestCase.TIME_PAGE)
				self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/icons').click()
				print 'find the student "', TutorTestCase.NAME_STUDENT, '"'
				self.driver.find_element_by_name(TutorTestCase.NAME_STUDENT)

			except NoSuchElementException:
				break

		print 'click the button "', TutorTestCase.NAME_ROOM, '"'
		self.driver.find_element_by_name(TutorTestCase.NAME_ROOM).click()

		print 'click the button "', TutorTestCase.NAME_LEAVE_ROOM, '"'
		self.driver.find_element_by_name(TutorTestCase.NAME_LEAVE_ROOM).click()


	def _leaveRoom1(self):

		time = 0
		while time < 2*TutorTestCase.TIMES_ATTEMPT:
			try:
				self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/icons').click()
				sleep(TutorTestCase.TIME_PAGE)
				self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/thumbnails').click()

				print 'attempt to find the battery in ', time, 'times'
				self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/batteryIndicator')

				time += 1

			except NoSuchElementException:
				break

		print 'click the button "', TutorTestCase.NAME_ROOM, '"'
		self.driver.find_element_by_name(TutorTestCase.NAME_ROOM).click()

		print 'click the button "', TutorTestCase.NAME_LEAVE_ROOM, '"'
		self.driver.find_element_by_name(TutorTestCase.NAME_LEAVE_ROOM).click()


	def _findStudent(self, name):

		while True:
			print 'click the button thumbnail'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/thumbnails').click()
			sleep(TutorTestCase.TIME_PAGE)

			print 'click the button icon'
			self.driver.find_element_by_id('com.netsupportsoftware.school.tutor.oem.intel:id/icons').click()
			sleep(TutorTestCase.TIME_PAGE)

			try:
				print 'find the student', name
				self.driver.find_element_by_name(name)
				break

			except NoSuchElementException:
				continue

	def _clearText(self, text):
		print 'clear the text "', text, '"'
		self.driver.keyevent(123)
		for i in range(0, len(text)):
			self.driver.keyevent(67)


if __name__ == '__main__':
	
	suite = unittest.TestSuite()

	#suite.addTest(TutorTestCase('testChatWithTutor'))
	#suite.addTest(TutorTestCase('testDisconnectFromTutor'))
	#suite.addTest(TutorTestCase('testSurveyMode'))
	#suite.addTest(TutorTestCase('testLockAndUnlock'))
	#suite.addTest(TutorTestCase('testStudentDisableWifiWhenConnectToTutor'))
	#suite.addTest(TutorTestCase('testStudentDisableWifiWhenSurvey'))
	#suite.addTest(TutorTestCase('testFileTransfer'))
	#suite.addTest(TutorTestCase('testStudentDisableWifiWhenFileTransfer'))
	#suite.addTest(TutorTestCase('testEnterSuspendWhileSurvey'))
	suite.addTest(TutorTestCase('testFileTransferAndForceStop'))

	unittest.TextTestRunner(verbosity=2).run(suite)
