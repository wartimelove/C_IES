#!/usr/bin/python

import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from performance.cpu_occupation import RunMonkey


class IESTestCase(unittest.TestCase):
	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, 
				className=None, appName=None,
				resourcePath=os.path.dirname(__file__) + '/../../resource_files/ies'):
		unittest.TestCase.__init__(self, methodName)
		self.device = device
		self.serialno = serialno
		self.testResult = testResult
		self.resourcePath = resourcePath + os.sep + appName
		self.className = className
		self.appName = appName


	def setUp(self):
		os.system('adb -s %s shell am start -n %s' % (self.serialno, self.className))
		pass


	def tearDown(self):
		os.system('adb -s %s shell am force-stop %s' % (self.serialno, self.className.split('/')[0]))
		pass


	def test_version(self):
		self.testResult.writeTestResult('test case: %s ies apps\ntest version' % self.appName)
		print 'test case: test_version'

		command = 'adb -s %s shell dumpsys package %s | grep versionName=' \
		% (self.serialno, self.className.split('/')[0])
		print command
		version = os.popen(command).readlines()

		assert len(version) == 1
		assert version[0].split('=')[1].split('\r\n')[0]

		print version[0]

		command = 'cat %s/versions.txt | grep ^%s=' % (os.path.dirname(__file__), self.appName)
		print command
		expect = os.popen(command).readlines()

		assert len(expect) == 1
		assert expect[0].split('=')[1].split('\n')[0]

		print expect[0]

		#if version[0].split('=')[1].split('\r\n')[0] == expect[0].split('=')[1].split('\n')[0] :
		#	self.testResult.writeTestResult(version[0].split('=')[1].split('\r\n')[0])
		#else:
		self.testResult.writeTestResult(version[0].split('=')[1].split('\r\n')[0])




	def _getAndSaveActResult(self, filename):
		logPath = self.testResult.curTestResultPath + os.sep + self.appName
		print logPath
		if not os.path.exists(logPath):
			os.mkdir(logPath)

		pathfilename = logPath + os.sep + filename
		result = self.device.device.takeSnapshot()
		result = result.getSubImage((0,0,1280,750))
		result.writeToFile(pathfilename,'png')
		return result
		

	def _loadExpResult(self, filename):
		pathfilename = self.resourcePath + os.sep + filename
		expect = MonkeyRunner.loadImageFromFile(pathfilename, 'png')
		return expect


	def _isAlive(self):
		lines = os.popen('adb -s %s shell procrank | grep %s | awk \'{print $6}\'' % (self.serialno, self.className.split('/')[0])).readlines()
		
		assert len(lines) == 1

		if self.className.split('/')[0] == lines[0].split('\r\n')[0]:
			return True

		return False


