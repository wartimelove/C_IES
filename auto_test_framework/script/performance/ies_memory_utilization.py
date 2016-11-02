#!/bin/python

import os
import time
from com.android.monkeyrunner import MonkeyRunner
from cpu_occupation import CPU_occupation, RunMonkey
from memory_utilization import Memory_utilization, RunMonkey

class IES_Memory_utilization(Memory_utilization):
	
	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None):
		Memory_utilization.__init__(self, methodName, device, serialno, testResult)
		self.device = device
		self.serialno = serialno
		self.testResult = testResult

	def test_MEM_Aviary(self):
		try:
			package = 'com.aviary.android.feather'
			self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_Aviary")
			print '\nTest Case: test_MEM_Aviary'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			memory_sum = 0
			for i in range(repeatTimes):
				memory = self.calAverageVal()
				string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
				print string
				self.testResult.writeTestResult(string)
				memory_sum = memory_sum + memory
			monkey_thread.stop()
			avg = round(memory_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()


	def test_MEM_ES_File_Explorer(self):
		try:
			package = 'com.estrongs.android.pop'
			self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_ES_File_Explorer")
			print '\nTest Case: test_MEM_ES_File_Explorer'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			memory_sum = 0
			for i in range(repeatTimes):
				memory = self.calAverageVal()
				string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
				print string
				self.testResult.writeTestResult(string)
				memory_sum = memory_sum + memory
			monkey_thread.stop()
			avg = round(memory_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()


	def test_MEM_RAR(self):
		try:
			package = 'com.rarlab.rar'
			self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_RAR")
			print '\nTest Case: test_MEM_RAR'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			memory_sum = 0
			for i in range(repeatTimes):
				memory = self.calAverageVal()
				string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
				print string
				self.testResult.writeTestResult(string)
				memory_sum = memory_sum + memory
			monkey_thread.stop()
			avg = round(memory_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()


	def test_MEM_Sparkvue(self):
		try:
			package = 'com.isbx.pasco.Spark'
			self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_Sparkvue")
			print '\nTest Case: test_MEM_Sparkvue'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			memory_sum = 0
			for i in range(repeatTimes):
				memory = self.calAverageVal()
				string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
				print string
				self.testResult.writeTestResult(string)
				memory_sum = memory_sum + memory
			monkey_thread.stop()
			avg = round(memory_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()

	def test_MEM_FluidMath(self):
		try:
			package = 'com.fluiditysoftware.fluidmath/.MainActivity'
			self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_FluidMath")
			print '\nTest Case: test_MEM_FluidMath'

			monkey_thread = RunMonkey(package, self.serialno)
			monkey_thread.start()
			repeatTimes = 3
			memory_sum = 0
			for i in range(repeatTimes):
				memory = self.calAverageVal()
				string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
				print string
				self.testResult.writeTestResult(string)
				memory_sum = memory_sum + memory
			monkey_thread.stop()
			avg = round(memory_sum / repeatTimes, 2)
			os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
			MonkeyRunner.sleep(3)
			string = time.ctime() + '\tAverage value = ' + str(avg)
			print string
			self.testResult.writeTestResult(string)
		except BaseException,e:
			print e
			line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" 
							%(self.serialno, self.serialno)).readlines()


