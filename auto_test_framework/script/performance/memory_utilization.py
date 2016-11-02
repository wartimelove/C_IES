import unittest
import os
import sys
import time
import threading
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
#from common.camera import Camera
#from common.wifi import Wifi
import shlex
import subprocess,commands

class Memory_utilization(unittest.TestCase):
    
    file_path = os.path.dirname(__file__) 
    global resourcePath
    resourcePath = file_path + '/../../resource_files/performance/Memory/'
    
    def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None):
        unittest.TestCase.__init__(self, methodName)
        self.device = device
        self.serialno = serialno
        self.testResult = testResult

    def setUp(self):
        print '\n'
        appmonPath = resourcePath + 'appmon'
        lines = os.popen("adb -s %s shell ls /data | grep 'appmon'" %self.serialno).readlines()
        if len(lines) == 0:
            os.system("adb -s %s push %s /data" %(self.serialno,appmonPath))
            os.system("adb -s %s shell chmod 770 /data/appmon" %self.serialno)
        else:
            pass
        
    def tearDown(self):
        self.testResult.writeTestResult("="*50)
        appmonLogName = "appmon_" + self.serialno + ".log"
        os.system("rm -f %s" %appmonLogName)
        self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')

    def calAverageVal(self):
        memory = 0
        cnt = 0
        memoryLogName = "memory_" + self.serialno + ".log"
	count = 0 
	avg_sum = 0 
	for count in range(5):
        	os.system("adb -s %s shell dumpsys meminfo | grep RAM > %s" %(self.serialno,memoryLogName))
		count = count + 1

        	lines = os.popen("cat %s" %memoryLogName).readlines()
        	for i in range(len(lines)):
                	idle_index = lines[i].find("Free")
                	total_index = lines[i].find("Total")
                	if idle_index >= 0:
                    		(status,idle) = commands.getstatusoutput("cat %s  | grep Free | awk '{printf $3}'" % memoryLogName)
			elif total_index >= 0:
                    		total = int(lines[i][total_index+11:lines[i].find(" kB") - len(lines[i])])
			else:
		    		continue
		
		avg_orig = 100*(total-int(idle))/float(total)
		avg_sum = avg_sum + avg_orig
		time.sleep(1)
	avg_orig = avg_sum/float(count)
	print 'total=', total, 'avg_orig=', avg_orig, 'avg_sum=', avg_sum
	avg = round(avg_orig,2)
        return avg

    def test_system_idle(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_system_idle")
        print 'Test Case: test_system_idle'
        self.device.device.press('KEYCODE_HOME', 'DOWN_AND_UP')
        MonkeyRunner.sleep(6)

        repeatTimes = 3
        memory_sum = 0
        for i in range(repeatTimes):
            memory = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(memory)
            print string
            self.testResult.writeTestResult(string)                                        
            memory_sum = memory_sum + memory
        avg = round(memory_sum / repeatTimes, 2)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)

    def launch_McAfee(self):
        component = 'com.wsandroid.suite.intelempg/com.mcafee.app.SplashActivity'
        package = 'com.wsandroid.suite.intelempg'

        os.system('adb -s %s logcat -c' %self.serialno)
        MonkeyRunner.sleep(3)

        lines = os.popen('adb -s %s shell am start -n %s' %(self.serialno, component)).readlines()
        for j in range(len(lines)):
            if lines[j].find('Error') >= 0:
                raise Exception("Can not launch McAfee")
        MonkeyRunner.sleep(10)
        line = os.popen('adb -s %s logcat -d -s ActivityManager:* | grep "Displayed com.wsandroid.suite.intelempg/com.mcafee.activation"' %self.serialno).readlines()
        if len(line) == 1:
            print 'license agreement'
            MonkeyRunner.sleep(15)
            print 'accept'
            self.device.device.touch(500, 550, 'DOWN_AND_UP')
            MonkeyRunner.sleep(5)
            print time.ctime()
	    count = 0
            while True:
                time.sleep(10)
                line = os.popen('adb -s %s logcat -d -s ActivityManager:* | grep "com.wsandroid.suite.intelempg/com.mcafee.vsmandroid.OdsSummary:"' %self.serialno).readlines()
                if len(line) == 1:
                    print time.ctime()
                    print line
                    break
		count = count + 1
		if count == 6:
		    print 60
		    break

            self.device.device.touch(648, 218, 'DOWN_AND_UP')
            MonkeyRunner.sleep(10)


    def test_MEM_McAfee_background(self):
        self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_McAfee_background")
        print '\nTest Case: test_MEM_McAfee_background'
        package = 'com.wsandroid.suite.intelempg'
              

        self.launch_McAfee()
        self.device.device.press('KEYCODE_HOME', 'DOWN_AND_UP')

        repeatTimes = 3
        memory_sum = 0
        for i in range(repeatTimes):
            memory = self.calAverageVal()
            string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
            print string
            self.testResult.writeTestResult(string)
            memory_sum = memory_sum + memory
        avg = round(memory_sum / repeatTimes, 2)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(5)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)

    def test_MEM_McAfee_scan(self):
        self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_McAfee_scan")
        print '\nTest Case: test_MEM_McAfee_scan'
        package = 'com.wsandroid.suite.intelempg'

        repeatTimes = 3
        memory_sum = 0
        for i in range(repeatTimes):

            self.launch_McAfee()
            MonkeyRunner.sleep(3)

            self.device.device.touch(648, 248, 'DOWN_AND_UP')
            MonkeyRunner.sleep(3)
            self.device.device.touch(648, 288, 'DOWN_AND_UP')
            MonkeyRunner.sleep(2)
            memory = self.calAverageVal()
            string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
            print string
            self.testResult.writeTestResult(string)
            memory_sum = memory_sum + memory
            os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
            MonkeyRunner.sleep(5)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        avg = round(memory_sum / repeatTimes, 2)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)

    def test_build_in_WebBrowser(self):
        component = 'com.android.browser/.BrowserActivity'
        package = 'com.android.browser'
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_build_in_WebBrowser")
        print '\nTest Case: test_build_in_WebBrowser'

        labWifi = Wifi(self.device, self.serialno, self.testResult)
        labWifi.openWifiSettings()
        if labWifi.turnOnWifi() == False:
            raise Exception("test_LT_WebBrowser: Turn on wifi failed")
        if labWifi.connectAP() == False:
            raise Exception("test_LT_WebBowser: Connect AP failed")

        lines = os.popen("adb -s %s shell am start -n %s -d http://www.intel.com -a 'android.intent.action.VIEW'" %(self.serialno, component)).readlines()
        for j in range(len(lines)):
            if lines[j].find('Error') >= 0:
                raise Exception("Can not play video")

        repeatTimes = 3
        memory_sum = 0
        for i in range(repeatTimes):
            memory = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(memory)
            print string
            self.testResult.writeTestResult(string)
            memory_sum = memory_sum + memory
        avg = round(memory_sum / repeatTimes, 2)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(3)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)
        labWifi.turnOffWifi()


    def test_MEM_Foxit(self):
        try:
              package = 'com.foxit.mobile.pdf.lite'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_Foxit")
              print '\nTest Case: test_MEM_Foxit'
              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              repeatTimes = 3
              memory_sum = 0
              for i in range(repeatTimes):
                  memory = self.calAverageVal()
                  string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
                  print string
                  self.testResult.writeTestResult(string)
                  memory_sum = memory_sum + memory
              self.device.device.touch(1240, 153, 'DOWN_AND_UP')
              monkey_thread.stop()
              self.device.device.touch(1240, 154, 'DOWN_AND_UP')
              avg = round(memory_sum / repeatTimes, 2)
              os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
              MonkeyRunner.sleep(3)
              string = time.ctime() + '\tAverage value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
        except BaseException,e:
          print 'there is an exception ', e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()


    def test_MEM_TD(self):
      try:
              package = 'com.intel.cmpc.td.agent'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_TD")
              print '\nTest Case: test_MEM_TD'

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
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_MEM_LabCam(self):
        self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_LabCam")
        print '\nTest Case: test_MEM_LabCam'
        component = 'com.labcam/.LabCamActivity'
        package = 'com.labcam'

        lines = os.popen("adb -s %s shell am start -n %s" %(self.serialno, component)).readlines()
        for j in range(len(lines)):
            if lines[j].find('Error') >= 0:
                raise Exception("Can not launch labcam")
        MonkeyRunner.sleep(5)
        # Enter into "Time Lapse" module, then start recording
        self.device.device.touch(330,300,'DOWN_AND_UP')
        MonkeyRunner.sleep(15)
        self.device.device.touch(430,540,'DOWN_AND_UP')
        MonkeyRunner.sleep(5)
        self.device.device.touch(430,695,'DOWN_AND_UP')
        MonkeyRunner.sleep(5)

        repeatTimes = 3
        memory_sum = 0
        for i in range(repeatTimes):
            memory = self.calAverageVal()
            string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
            print string
            self.testResult.writeTestResult(string)
            memory_sum = memory_sum + memory
        avg = round(memory_sum / repeatTimes, 2)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(3)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)


    def test_MEM_MediaCam(self):
        self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_MediaCam")
        print '\nTest Case: test_MEM_MediaCam'
        component = 'com.mediacam/.MediaCamActivity'
        package = 'com.mediacam'

        lines = os.popen("adb -s %s shell am start -n %s" %(self.serialno, component)).readlines()
        for j in range(len(lines)):
            if lines[j].find('Error') >= 0:
                raise Exception("Can not launch mediacam")
        MonkeyRunner.sleep(5)
        # Enter into "Recorder" module, then start recording
        self.device.device.touch(516,412,'DOWN_AND_UP')
        MonkeyRunner.sleep(10)
        self.device.device.touch(490,540,'DOWN_AND_UP')
        MonkeyRunner.sleep(5)
        self.device.device.touch(490,700,'DOWN_AND_UP')
        MonkeyRunner.sleep(5)

        repeatTimes = 3
        memory_sum = 0
        for i in range(repeatTimes):
            memory = self.calAverageVal()
            string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
            print string
            self.testResult.writeTestResult(string)
            memory_sum = memory_sum + memory
        avg = round(memory_sum / repeatTimes, 2)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(3)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)


    def test_MEM_CLM(self):
        try:
              package = 'mythware.classroom.client'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_CLM")
              print '\nTest Case: test_MEM_CLM' 
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
          print 'there is an exception ', e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()


    def test_MEM_Kno(self):
        try:
              package = 'com.kno.textbooks'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_Kno")
              print '\nTest Case: test_MEM_Kno'

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
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()



    def test_MEM_Artrage(self):
      try:
              package = 'com.ambientdesign.artrage'
	      lines = 0
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_Artrage")
              print '\nTest Case: test_MEM_Artrage'

              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
			
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
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_MEM_VLC(self):
      try:
              package = 'org.videolan.vlc'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_VLC")
              print '\nTest Case: test_MEM_VLC'

              monkey_thread = RunMonkey(package, self.serialno)
#              monkey_thread.start()
#	      MonkeyRunner.sleep(10)
#	      isAlive=monkey_thread.isAlive()
#	      if isAlive == False:
 #             		raise Exception("Can not launch package")
 #             
	      repeatTimes = 3
              memory_sum = 0
              for i in range(repeatTimes):
                  memory = self.calAverageVal()
                  string = time.ctime() + '\t#%s Memory Utilization is: ' %str(i+1) + str(memory)
                  print string
                  self.testResult.writeTestResult(string)
                  memory_sum = memory_sum + memory
#              monkey_thread.stop()
              avg = round(memory_sum / repeatTimes, 2)
              os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
              MonkeyRunner.sleep(3)
              string = time.ctime() + '\tVLC value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_MEM_Pixlr(self):
      try:
              package = 'com.pixlr.oem.intel'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_Pixlr")
              print '\nTest Case: test_MEM_Pixlr'

              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              
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
              string = time.ctime() + '\tPixlr value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_MEM_SketchBook(self):
      try:
              package = 'com.adsk.sketchbook.oem.intel'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_SketchBook")
              print '\nTest Case: test_MEM_SketchBook'

              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              
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
              string = time.ctime() + '\tSketchBook value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_MEM_AdobeReader(self):
      try:
              package = 'com.adobe.reader'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_AdobeReader")
              print '\nTest Case: test_MEM_AdobeReader'

              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              
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
              string = time.ctime() + '\tAdobeReader value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def launch_IER(self):
        component = 'com.intel.ipls.ierbundle/.SplashScreen_Activity'
        package = 'com.intel.ipls.ierbundle'

        os.system('adb -s %s logcat -c' %self.serialno)
        MonkeyRunner.sleep(3)

        lines = os.popen('adb -s %s shell am start -n %s' %(self.serialno, component)).readlines()
        for j in range(len(lines)):
            if lines[j].find('Error') >= 0:
                raise Exception("Can not launch IERBundle")
        MonkeyRunner.sleep(10)
        line = os.popen('adb -s %s logcat -d -s ActivityManager:* | grep "Displayed com.intel.ipls.ierbundle/.WebContent_Activity"' %self.serialno).readlines()
        if len(line) == 1:
            print 'license agreement'
            MonkeyRunner.sleep(15)
            print 'accept'
	    for i in range(1,5):
		self.device.device.drag((100,730),(100,130),0.1,1)
                MonkeyRunner.sleep(3)
		print i
            self.device.device.touch(1080, 704, 'DOWN_AND_UP')
            MonkeyRunner.sleep(5)
	    count = 0
            print time.ctime()
            while True:
                time.sleep(10)
                line = os.popen('adb -s %s logcat -d -s ActivityManager:* | grep "com.intel.ipls.ierbundle"' %self.serialno).readlines()
                if len(line) == 1:
                    print time.ctime()
                    print line
                    break
		count = count + 1
		if count == 1:
		    print 60
		    break
			
            MonkeyRunner.sleep(3)


    def test_MEM_IER(self):
      try:
              package = 'com.intel.ipls.ierbundle'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_IER")
              print '\nTest Case: test_MEM_IER'
		
	      self.launch_IER()
              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              
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
              string = time.ctime() + '\tIER value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def launch_WPS(self):
        component = 'cn.wps.moffice_eng/cn.wps.moffice.main.local.home.PadHomeActivity'
        package = 'cn.wps.moffice_eng'

        os.system('adb -s %s logcat -c' %self.serialno)
        MonkeyRunner.sleep(3)

        lines = os.popen('adb -s %s shell am start -n %s' %(self.serialno, component)).readlines()
        for j in range(len(lines)):
            if lines[j].find('Error') >= 0:
                raise Exception("Can not launch WPS")
        MonkeyRunner.sleep(10)
        line = os.popen('adb -s %s logcat -d -s ActivityManager:* | grep "Displayed cn.wps.moffice_eng/cn.wps.moffice.main.local.home.PadHomeActivity"' %self.serialno).readlines()
        if len(line) == 1:
            print 'license agreement'
            self.device.device.touch(700, 560, 'DOWN_AND_UP')
            MonkeyRunner.sleep(15)
            print 'accept'
            self.device.device.touch(1080, 704, 'DOWN_AND_UP')
            MonkeyRunner.sleep(5)
	    count = 0
            print time.ctime()
            while True:
                time.sleep(10)
                line = os.popen('adb -s %s logcat -d -s ActivityManager:* | grep "cn.wps.moffice_eng"' %self.serialno).readlines()
                if len(line) == 1:
                    print time.ctime()
                    print line
                    break
		count = count + 1
		if count == 1:
		    print 60
		    break
			
            MonkeyRunner.sleep(3)

    def test_MEM_WPS(self):
      try:
              package = 'cn.wps.moffice_eng'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_WPS")
              print '\nTest Case: test_MEM_WPS'
		
	      self.launch_WPS()
              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              
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
              string = time.ctime() + '\tIER value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_MEM_NetSupportstudent(self):
      try:
              package = 'com.netsupportsoftware.school.student.oem.intel'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_NetSupportstudent")
              print '\nTest Case: test_MEM_NetSupportstudent'

              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              
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
              string = time.ctime() + '\tNetSupport student value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_MEM_NetSupporttutor(self):
      try:
              package = 'com.netsupportsoftware.school.tutor.oem.intel'
              self.testResult.writeTestResult("Test Case: Memory Utilization\nTest Method: test_MEM_NetSupporttutor")
              print '\nTest Case: test_MEM_NetSupporttutor'

              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              
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
              string = time.ctime() + '\tNetSupport tutor value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()


class RunMonkey(threading.Thread):
  def __init__(self, package, serialno):
      threading.Thread.__init__(self)
      self.package = package
      self.serialno = serialno
      self.pid = None

  def run(self):
      print 'start monkey ------------------------------'
      self.pidList1 = os.popen("adb -s %s shell ps | grep 'com.android.commands.monkey' | awk '{print $2}'" %self.serialno).readlines()
      print self.pidList1
      
      lines = os.popen("adb -s '%s' shell monkey -p '%s'  --throttle 500 -v 100000" %(self.serialno,self.package)).readlines()
      for j in range(len(lines)):
           	if lines[j].find('aborted') >= 0:
              		raise Exception("Can not launch package")
      #command = "adb -s '%s' shell monkey -p '%s' --throttle 1000 -v 100000" %(self.serialno,self.package)
      #args = shlex.split(command)
      #print args
      #subprocess.Popen(args)
      #MonkeyRunner.sleep(5)

  def stop(self):
      self.pidList2 = os.popen("adb -s %s shell ps | grep 'com.android.commands.monkey' | awk '{print $2}'" %self.serialno).readlines()
      print self.pidList2
      pidList = list(set(self.pidList2).difference(set(self.pidList1)))
      print pidList
      if(len(pidList)==1):
          self.pid = pidList[0].strip()

          line = os.popen('adb -s %s shell ps | grep %s' %(self.serialno, self.pid)).readlines()
          if len(line) == 0:
              print 'monkey has finished!!!!'
          else:
              os.system('adb -s %s shell kill %s'  %(self.serialno, self.pid))
              print 'kill monkey----------------------'
              #line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

      else:
          #raise Exception("can not find the pid of monkey")
          print 'can not find the pid of monkey'




class CapturePhoto(threading.Thread):
  def __init__(self, device):
    threading.Thread.__init__(self)
    print '================ thread init ================'
    self.dev = device
    self.thread_stop = False

  def run(self):
    while not self.thread_stop:
      print time.ctime(), '\tcapture'
      self.dev.touch(1216, 372, 'DOWN_AND_UP')
      MonkeyRunner.sleep(10)

  def stop(self):
    print '================ thread stop ================'
    self.thread_stop = True


if __name__ == '__main__':
    unittest.main()

