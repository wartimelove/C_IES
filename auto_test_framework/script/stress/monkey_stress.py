import unittest
import os,sys
import time
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
sys.path.append('..')
from common.general import Log,DeviceInfo,SIMonkeyDevice,DevicesList,TestResult 


global serailno
serialno = DevicesList().getFirstDeviceNo().strip()
path=os.popen("pwd").read().strip('\n')

class MonkeyStress(unittest.TestCase):
    file_path = os.path.dirname(__file__) 
    global resourcePath
    resourcePath = file_path + '/../../resource_files/stress/'
    global repeattimes
    repeattimes = 10000
   
    def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None):
        unittest.TestCase.__init__(self, methodName)
        self.device = device
        self.serialno = serialno
        self.testResult = testResult
	self.log = Log(serialno,self.testResult,'media',self.device)

    def setUp(self):
       pass

    def tearDown(self):
        self.testResult.writeTestResult("="*50)
        self.device.device.press('KEYCODE_HOME', 'DOWN_AND_UP')

    def test_stress_monkey_WebBrowser(self):
        print time.ctime()+"    Test Case: Test_stress_monkey_test"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_WebBrowser")
        apk = 'com.android.browser'
             
        
        try:            
            #self.testResult.writeTestResult('Monkey_test:'+apk)
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()
            #for j in lines:
             #   self.testResult.writeTestResult(j)

            if lines[-1].strip() == "// Monkey finished":
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
             #   self.testResult.writeTestResult( '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes))
            else:
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
              #  self.testResult.writeTestResult( '%s %s: %d times\nFail.' %(self.serialno,apk,repeattimes))
                raise Exception("Monkey not finished ")
            self.testResult.writeTestResult("Pass")  
	    os.system("adb -s '%s' shell am force-stop '%s'" % (self.serialno,apk)) 
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_CLM(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_CLM"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_CLM")
        apk ='mythware.classroom.client'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s'  --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_CLM", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_CLM", path, lines)
	    	self.log._getAndSaveActResult("test_stress_monkey_IES_CLM")
	        self.log.get_cpu_usage("test_stress_monkey_IES_CLM")
	        self.log.get_mem_usage("test_stress_monkey_IES_CLM")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_CLM")
	    self.log.get_cpu_usage("test_stress_monkey_IES_CLM")
	    self.log.get_mem_usage("test_stress_monkey_IES_CLM")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_LabCam(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_LabCam"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_LabCam")
        apk = 'com.labcam'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_LabCam", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_LabCam", path, lines)
	    	self.log._getAndSaveActResult("test_stress_monkey_IES_LabCam")
	        self.log.get_cpu_usage("test_stress_monkey_IES_LabCam")
	        self.log.get_mem_usage("test_stress_monkey_IES_LabCam")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_LabCam")
	    self.log.get_cpu_usage("test_stress_monkey_IES_LabCam")
	    self.log.get_mem_usage("test_stress_monkey_IES_LabCam")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")


    def test_stress_monkey_IES_MediaCam(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_MediaCam"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_MediaCam")
        apk = 'com.mediacam'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_MediaCam", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_MediaCam", path, lines)
	    	self.log._getAndSaveActResult("test_stress_monkey_IES_MediaCam")
	        self.log.get_cpu_usage("test_stress_monkey_IES_MediaCam")
	        self.log.get_mem_usage("test_stress_monkey_IES_MediaCam")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_MediaCam")
	    self.log.get_cpu_usage("test_stress_monkey_IES_MediaCam")
	    self.log.get_mem_usage("test_stress_monkey_IES_MediaCam")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")


    def test_stress_monkey_IES_Kno(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_Kno"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_Kno")
        apk = 'com.kno.textbooks'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_Kno", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_Kno", path, lines)
            	self.log._getAndSaveActResult("test_stress_monkey_IES_Kno")
	        self.log.get_cpu_usage("test_stress_monkey_IES_Kno")
	        self.log.get_mem_usage("test_stress_monkey_IES_Kno")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
            self.log._getAndSaveActResult("test_stress_monkey_IES_Kno")
	    self.log.get_cpu_usage("test_stress_monkey_IES_Kno")
	    self.log.get_mem_usage("test_stress_monkey_IES_Kno")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_SPARKvue(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_SPARKvue"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_SPARKvue")
        apk = 'com.isbx.pasco.Spark'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()
            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_SPARKvue", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_SPARKvue", path, lines)
	    	self.log._getAndSaveActResult("test_stress_monkey_IES_SPARKvue")
	        self.log.get_cpu_usage("test_stress_monkey_IES_SPARKvue")
	        self.log.get_mem_usage("test_stress_monkey_IES_SPARKvue")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_SPARKvue")
	    self.log.get_cpu_usage("test_stress_monkey_IES_SPARKvue")
	    self.log.get_mem_usage("test_stress_monkey_IES_SPARKvue")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_Qwizdom(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_Qwizdom"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_Qwizdom")
        apk = 'com.Qwizdom.WT5'
               
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s'  -v %d" %(self.serialno,apk,repeattimes)).readlines()
            if lines[-1].strip() == "// Monkey finished":
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_Foxit(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_Foxit"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_Foxit")
        apk = 'com.foxit.mobile.pdf.lite'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_Foxit", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_Foxit", path, lines)
	    	self.log._getAndSaveActResult("test_stress_monkey_IES_Foxit")
	        self.log.get_cpu_usage("test_stress_monkey_IES_Foxit")
	        self.log.get_mem_usage("test_stress_monkey_IES_Foxit")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_Foxit")
	    self.log.get_cpu_usage("test_stress_monkey_IES_Foxit")
	    self.log.get_mem_usage("test_stress_monkey_IES_Foxit")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_Artrage(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_Artrage"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_Artrage")
        apk = 'com.ambientdesign.artrage'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_Artrage", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_Artrage", path, lines)
	    	self.log._getAndSaveActResult("test_stress_monkey_IES_Artrage")
	        self.log.get_cpu_usage("test_stress_monkey_IES_Artrage")
	        self.log.get_mem_usage("test_stress_monkey_IES_Artrage")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_Artrage")
	    self.log.get_cpu_usage("test_stress_monkey_IES_Artrage")
	    self.log.get_mem_usage("test_stress_monkey_IES_Artrage")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_TD(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_TD"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_TD")
        apk = 'com.intel.cmpc.td.agent'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_TD", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_TD", path, lines)
	    	self.log._getAndSaveActResult("test_stress_monkey_IES_TD")
	        self.log.get_cpu_usage("test_stress_monkey_IES_TD")
	        self.log.get_mem_usage("test_stress_monkey_IES_TD")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_TD")
	    self.log.get_cpu_usage("test_stress_monkey_IES_TD")
	    self.log.get_mem_usage("test_stress_monkey_IES_TD")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_RAR(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_RAR"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_RAR")
        apk = 'com.rarlab.rar'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_RAR", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_RAR", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_RAR")
	        self.log.get_cpu_usage("test_stress_monkey_IES_RAR")
	        self.log.get_mem_usage("test_stress_monkey_IES_RAR")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_RAR")
	    self.log.get_cpu_usage("test_stress_monkey_IES_RAR")
	    self.log.get_mem_usage("test_stress_monkey_IES_RAR")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_McAfee(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_McAfee"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_McAfee")
        apk = 'com.wsandroid.suite.intelempg'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_McAfee", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_McAfee", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_McAfee")
	        self.log.get_cpu_usage("test_stress_monkey_IES_McAfee")
	        self.log.get_mem_usage("test_stress_monkey_IES_McAfee")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_McAfee")
	    self.log.get_cpu_usage("test_stress_monkey_IES_McAfee")
	    self.log.get_mem_usage("test_stress_monkey_IES_McAfee")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_Aviary(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_Aviary"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_Aviary")
        apk = 'com.aviary.android.feather'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_Aviary", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_Aviary", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_Aviary")
	        self.log.get_cpu_usage("test_stress_monkey_IES_Aviary")
	        self.log.get_mem_usage("test_stress_monkey_IES_Aviary")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_Aviary")
	    self.log.get_cpu_usage("test_stress_monkey_IES_Aviary")
	    self.log.get_mem_usage("test_stress_monkey_IES_Aviary")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_ESFileexplorer(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_ESFileexplorer"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_ESFileexplorer")
        apk = 'com.estrongs.android.pop'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_ESFileexplorer", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_ESFileexplorer", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_ESFileexplorer")
	        self.log.get_cpu_usage("test_stress_monkey_IES_ESFileexplorer")
	        self.log.get_mem_usage("test_stress_monkey_IES_ESFileexplorer")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_ESFileexplorer")
	    self.log.get_cpu_usage("test_stress_monkey_IES_ESFileexplorer")
	    self.log.get_mem_usage("test_stress_monkey_IES_ESFileexplorer")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    def test_stress_monkey_IES_VLC(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_VLC"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_VLC")
        #apk = 'org.videolan.vlc.betav7neon'
        apk = 'org.videolan.vlc'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()
            #lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 1000 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_VLC", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_VLC", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_VLC")
	        self.log.get_cpu_usage("test_stress_monkey_IES_VLC")
	        self.log.get_mem_usage("test_stress_monkey_IES_VLC")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_VLC")
	    self.log.get_cpu_usage("test_stress_monkey_IES_VLC")
	    self.log.get_mem_usage("test_stress_monkey_IES_VLC")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_Pixlr(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_Pixlr"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_Pixlr")
        apk = 'com.pixlr.oem.intel'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_Pixlr", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_Pixlr", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_Pixlr")
	        self.log.get_cpu_usage("test_stress_monkey_IES_Pixlr")
	        self.log.get_mem_usage("test_stress_monkey_IES_Pixlr")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_Pixlr")
	    self.log.get_cpu_usage("test_stress_monkey_IES_Pixlr")
	    self.log.get_mem_usage("test_stress_monkey_IES_Pixlr")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_SketchBook(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_SketchBook"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_SketchBook")
        apk = 'com.adsk.sketchbook.oem.intel'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_SketchBook", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_SketchBook", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_SketchBook")
	        self.log.get_cpu_usage("test_stress_monkey_IES_SketchBook")
	        self.log.get_mem_usage("test_stress_monkey_IES_SketchBook")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_SketchBook")
	    self.log.get_cpu_usage("test_stress_monkey_IES_SketchBook")
	    self.log.get_mem_usage("test_stress_monkey_IES_SketchBook")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_AdobeReader(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_AdobeReader"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_AdobeReader")
        apk = 'com.adobe.reader'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_AdobeReader", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_AdobeReader", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_AdobeReader")
	        self.log.get_cpu_usage("test_stress_monkey_IES_AdobeReader")
	        self.log.get_mem_usage("test_stress_monkey_IES_AdobeReader")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_AdobeReader")
	    self.log.get_cpu_usage("test_stress_monkey_IES_AdobeReader")
	    self.log.get_mem_usage("test_stress_monkey_IES_AdobeReader")
            self.testResult.writeTestResult("Pass")   
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_IER(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_IER"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_IER")
        apk = 'com.intel.ipls.ierbundle'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_IER", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_IER", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_IER")
	        self.log.get_cpu_usage("test_stress_monkey_IES_IER")
	        self.log.get_mem_usage("test_stress_monkey_IES_IER")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_IER")
	    self.log.get_cpu_usage("test_stress_monkey_IES_IER")
	    self.log.get_mem_usage("test_stress_monkey_IES_IER")
            self.testResult.writeTestResult("Pass")  
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_WPS(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_WPS"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_WPS")
        apk = 'cn.wps.moffice_eng'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_WPS", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_WPS", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_WPS")
	        self.log.get_cpu_usage("test_stress_monkey_IES_WPS")
	        self.log.get_mem_usage("test_stress_monkey_IES_WPS")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_WPS")
	    self.log.get_cpu_usage("test_stress_monkey_IES_WPS")
	    self.log.get_mem_usage("test_stress_monkey_IES_WPS")
            self.testResult.writeTestResult("Pass")  
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
    
    def test_stress_monkey_IES_NetSupportstudent(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_NetSupportstudent"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_NetSupportstudent")
        apk = 'com.netsupportsoftware.school.student.oem.intel'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_NetSupportstudent", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_NetSupportstudent", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_NetSupportstudent")
	        self.log.get_cpu_usage("test_stress_monkey_IES_NetSupportstudent")
	        self.log.get_mem_usage("test_stress_monkey_IES_NetSupportstudent")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_NetSupportstudent")
	    self.log.get_cpu_usage("test_stress_monkey_IES_NetSupportstudent")
	    self.log.get_mem_usage("test_stress_monkey_IES_NetSupportstudent")
            self.testResult.writeTestResult("Pass")  
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_NetSupporttutor(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_NetSupporttutor"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_NetSupporttutor")
        apk = 'com.netsupportsoftware.school.tutor.oem.intel'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_NetSupporttutor", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_NetSupporttutor", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_NetSupporttutor")
	        self.log.get_cpu_usage("test_stress_monkey_IES_NetSupporttutor")
	        self.log.get_mem_usage("test_stress_monkey_IES_NetSupporttutor")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_NetSupporttutor")
	    self.log.get_cpu_usage("test_stress_monkey_IES_NetSupporttutor")
	    self.log.get_mem_usage("test_stress_monkey_IES_NetSupporttutor")
            self.testResult.writeTestResult("Pass")  
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")

    def test_stress_monkey_IES_FluidMath(self):
        print time.ctime()+"    Test Case: test_stress_monkey_IES_FluidMath"
        self.testResult.writeTestResult("Test Case: Monkey Stress\nTest Method: test_stress_monkey_IES_FluidMath")
        apk = 'com.fluiditysoftware.fluidmath'
        
        try:            
            lines = os.popen("adb -s '%s' shell monkey -p '%s' --throttle 500 -v %d" %(self.serialno,apk,repeattimes)).readlines()

            if lines[-1].strip() == "// Monkey finished":
		self.log.captureLog("test_stress_monkey_IES_FluidMath", path, lines)
                print '%s %s: %d times\nPass' %(self.serialno,apk,repeattimes)
            else:
		self.log.captureLog("test_stress_monkey_IES_FluidMath", path, lines)
		self.log._getAndSaveActResult("test_stress_monkey_IES_FluidMath")
	        self.log.get_cpu_usage("test_stress_monkey_IES_FluidMath")
	        self.log.get_mem_usage("test_stress_monkey_IES_FluidMath")
                print '%s %s: %d times\nFail. Check log file for more information' %(self.serialno,apk,repeattimes)
                raise Exception("Monkey not finished ")
	    self.log._getAndSaveActResult("test_stress_monkey_IES_FluidMath")
	    self.log.get_cpu_usage("test_stress_monkey_IES_FluidMath")
	    self.log.get_mem_usage("test_stress_monkey_IES_FluidMath")
            self.testResult.writeTestResult("Pass")  
            self.device.device.press('KEYCODE_HOME','DOWN_AND_UP')
        except Exception,e:
            print e
            self.testResult.writeTestResult("Fail")
