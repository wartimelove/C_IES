#!/usr/bin/python

import time
from app_launch_time import App_launch_time

class IES_App_launch_time(App_launch_time):

	def __init__(self, methodName='runtest', device=None, serialno=None, testResult=None):
		App_launch_time.__init__(self, methodName, device, serialno, testResult)
		self.device = device
		self.serialno = serialno
		self.testResult = testResult
		
	def test_LT_Aviary(self):
		component = 'com.aviary.android.feather/.GridActivity'
		self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Aviary")
		print time.ctime() + '\tRunning test_LT_Aviary...'
		repeatTimes = 3
		self.calLaunchTime(component, repeatTimes)
		
	def test_LT_ES_File_Explorer(self):
		component = 'com.estrongs.android.pop/.view.FileExplorerActivity'
		self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_ES_File_Explorer")
		print time.ctime() + '\tRunning test_LT_ES_File_Explorer...'
		repeatTimes = 3
		self.calLaunchTime(component, repeatTimes)
		
	def test_LT_RAR(self):
		component = 'com.rarlab.rar/.MainActivity'
		self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_RAR")
		print time.ctime() + '\tRunning test_LT_RAR...'
		repeatTimes = 3
		self.calLaunchTime(component, repeatTimes)
		
