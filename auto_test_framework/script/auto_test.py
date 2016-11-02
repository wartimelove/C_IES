import unittest
import getopt
import sys
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from common.general import DevicesList, TestResult, SIMonkeyDevice
from performance.performance import performanceSuite
from stress.stress import stressSuite
from version.ies import ies_apps_suite

def start(argv=None):
    short_opt = 'c:hn:d'
    long_opt = ['version=','performance=','stress=']
    opts, args = getopt.getopt(sys.argv[1:], short_opt, long_opt)
    global serialno
    global mdev
    global testResult
    global outputDir
#Flag to indicate devlopment or execution
    global debugFlag
    serialno = DevicesList().getFirstDeviceNo().strip()
    outputDir = os.path.dirname(__file__) + "/../"
    debugFlag = True
    count = 1
    suite = 'all'
    dict = {}
    for op, value  in opts:
        if op == '-n':
            serialno = value
	if op in ['--version','--performance','--stress']:
	    count = value
	    suite = op[2:]
	    dict.setdefault(suite,count)
        if op == '-d':
            outputDir = value
            debugFlag = False
        if op == '-h':
            print 'help info'
            os._exit(0)
    mdev = SIMonkeyDevice(serialno)
    mdev.connectMonkeyDevice()
    testResult = TestResult(outputDir, serialno)
    testResult.initTestResult()
    alltests = unittest.TestSuite()
   
    for suite in dict:
	count = dict[suite]
    #	alltests = unittest.TestSuite()
	count = int(count) + 1
        for step in range(1,count):
                print step
    		if suite == 'version':
	    		alltests.addTests(ies_apps_suite(mdev, outputDir, debugFlag, serialno, testResult))
    		elif suite == 'performance':
	    		alltests.addTests(performanceSuite(mdev, outputDir, debugFlag, serialno, testResult))
    		elif suite == 'stress':
    	    		alltests.addTests(stressSuite(mdev, outputDir, debugFlag, serialno, testResult))
    if suite == 'all':
	    		print "all"
	    		alltests.addTests(ies_apps_suite(mdev, outputDir, debugFlag, serialno, testResult))
	    		alltests.addTests(performanceSuite(mdev, outputDir, debugFlag, serialno, testResult))
    	    		alltests.addTests(stressSuite(mdev, outputDir, debugFlag, serialno, testResult))
    #alltests.addTests(imageBATSuite(mdev, outputDir, debugFlag, serialno, testResult))
    #alltests.addTests(os_BehaviorSuite(mdev, outputDir, debugFlag, serialno, testResult))
    #alltests.addTests(builtinAppsSuite(mdev, outputDir, debugFlag, serialno, testResult))
    #alltests.addTests(ACTSSuite(mdev, outputDir, debugFlag, serialno, testResult))
    #alltests.addTests(CTSSuite(mdev, outputDir, debugFlag, serialno, testResult))

    mdev.wakeup()
    mdev.unlockScreen()
    mdev.rootDevice()
    mdev.prepareForTest()
    runner = unittest.TextTestRunner()
    runner.run(alltests) 
    testResult.closeTestResult()
    testResult.openTestResult('r')
    testResult.generateHTMLTestReport()
    testResult.closeTestResult()


