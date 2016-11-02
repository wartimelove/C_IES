#!/bin/python

import os
import time
from com.android.monkeyrunner import MonkeyRunner
from cpu_occupation import CPU_occupation, RunMonkey

class IES_CPU_occupation(CPU_occupation):
	
	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None):
		CPU_occupation.__init__(self, methodName, device, serialno, testResult)
		self.device = device
		self.serialno = serialno
		self.testResult = testResult

	def test_IES_Aviary(self):
		try:
			package = 'com.aviary.android.feather'
			self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_Aviary")
			print '\nTest Case: test_IES_Aviary'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			cpu_sum = 0
			for i in range(repeatTimes):
				cpu = self.calAverageVal()
				string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
				print string
				self.testResult.writeTestResult(string)
				cpu_sum = cpu_sum + cpu
			monkey_thread.stop()
			avg = round(cpu_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()


	def test_IES_ES_File_Explorer(self):
		try:
			package = 'com.estrongs.android.pop'
			self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_ES_File_Explorer")
			print '\nTest Case: test_IES_ES_File_Explorer'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			cpu_sum = 0
			for i in range(repeatTimes):
				cpu = self.calAverageVal()
				string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
				print string
				self.testResult.writeTestResult(string)
				cpu_sum = cpu_sum + cpu
			monkey_thread.stop()
			avg = round(cpu_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()


	def test_IES_RAR(self):
		try:
			package = 'com.rarlab.rar'
			self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_RAR")
			print '\nTest Case: test_IES_RAR'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			cpu_sum = 0
			for i in range(repeatTimes):
				cpu = self.calAverageVal()
				string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
				print string
				self.testResult.writeTestResult(string)
				cpu_sum = cpu_sum + cpu
			monkey_thread.stop()
			avg = round(cpu_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()


	def test_IES_Sparkvue(self):
		try:
			package = 'com.isbx.pasco.Spark'
			self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_Sparkvue")
			print '\nTest Case: test_IES_Sparkvue'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			cpu_sum = 0
			for i in range(repeatTimes):
				cpu = self.calAverageVal()
				string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
				print string
				self.testResult.writeTestResult(string)
				cpu_sum = cpu_sum + cpu
			monkey_thread.stop()
			avg = round(cpu_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()

	def test_IES_FluidMath(self):
		try:
			package = 'com.fluiditysoftware.fluidmath'
			self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_FluidMath")
			print '\nTest Case: test_IES_FluidMath'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			cpu_sum = 0
			for i in range(repeatTimes):
				cpu = self.calAverageVal()
				string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
				print string
				self.testResult.writeTestResult(string)
				cpu_sum = cpu_sum + cpu
			monkey_thread.stop()
			avg = round(cpu_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()



