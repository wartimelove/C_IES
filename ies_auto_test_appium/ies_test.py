import os,sys,getopt
import unittest
import traceback
import commands

from appium import webdriver
#from selenium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains

from common.function import *
from common.HTMLTestRunner import *
from module.bat import *
from module.sparkvue import *
from module.labcam import *
from module.fluidmath import *
from module.case_list import *
from module.es import *
from module.kno import *
from module.mcafee import *
from module.vlc import *
from module.rar import *
from module.pixlr import *
from module.sketchbook import *

reload(sys)
sys.setdefaultencoding('utf8')

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


if __name__ == '__main__':
#    outputDir = os.path.dirname(__file__) + "/log/"
#    serialno = DevicesList().getFirstDeviceNo().strip()
#
#    testResult = TestResult(outputDir, serialno)
#    testResult.initTestResult()

    serialno = getFirstDeviceNo().strip()
    date = getDate()

    opts,arg= getopt.getopt(sys.argv[1:],"hi:o:")
    module_list=["labcam","sparkvue","fluidmath","kno","vlc","es","mcafee","rar","netsupport","bat","pixlr", "sketchbook"]
    testcases=[]
    os.system("mkdir -p ./log/test_results/")
    result="./log/test_results/"+serialno+"_"+date+".html"
    print result
    fp = file(result,'wb')
    runner = HTMLTestRunner(stream=fp,title='IES_Report',verbosity=2,description='auto test report for ies')

    set_sleep()
    try: 
	for module in arg:
		if module in module_list:
			print "module =",module
			if module == "sparkvue":
				testcases.append(sparkvue)

			elif module == "labcam":
				testcases.append(labcam)

			elif module == "fluidmath":
				testcases.append(fluidmath)
		
			elif module == "kno":
				testcases.append(kno)

			elif module == "mcafee":
				testcases.append(mcafee)

			elif module == "es":
				testcases.append(es)

			elif module == "vlc":
				testcases.append(vlc)

			elif module == "rar":
				testcases.append(rar)

			elif module == "netsupport":
				testcases.append(netsupport)

			elif module == "pixlr":
				testcases.append(pixlr)

			elif module == "sketchbook":
				testcases.append(sketchbook)

			elif module == "bat":
				testcases.append(bat)

		else:
			print "Not support",module,"now,please check your input or contact the developer!"
		
	runner.run(unittest.TestSuite(testcases))
    except getopt.GetoptError,err:
	print str(err)
	usage()
	sys.exit(2)

#    testResult.closeTestResult()
#    testResult.openTestResult('r')
#    testResult.generateHTMLTestReport()
#    testResult.closeTestResult()


