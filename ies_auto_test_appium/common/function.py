import os,sys
import unittest
import traceback
import commands

from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains


reload(sys)
sys.setdefaultencoding('utf8')

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def getFirstDeviceNo():
        """get current devices and return first dev"""
        dev = os.popen("adb devices | grep 'device' |awk '{print $1}'").readlines()
        if len(dev) < 2:
            print 'have no device'
            os._exit(1)
        return dev[1]

def getDate():
        """get current Date info"""
        dev = os.popen("date +%Y%m%d%H%M | awk '{printf $0}'" ).readline()
        return dev


def check_camera(info):
#	os.system("adb logcat > /tmp/camera.log &")
	sleep(10)
	status, camera_id = commands.getstatusoutput("cat /tmp/camera.log | grep Camera | grep Opened | tail -n 1 | cut -d ':' -f 2 | awk '{printf $2}'")
	if camera_id == info:
		return "ture"
	else:
		return "false"

def usage():
    print '''1.support module as arguments;
2.support mult arguments to run the cases;
3.module list: kno,sparkvue,fluidmath,vlc,labcam,'''

def set_sleep():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0'
    desired_caps['deviceName'] = 'Bytrail_CR'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.DisplaySettings'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    os.system("adb root")
    sleep(10)
    Sleep_Setting = driver.find_elements_by_class_name("android.widget.RelativeLayout")
    Sleep_Setting[3].click()
    TimeSet = driver.find_elements_by_class_name("android.widget.CheckedTextView")
    TimeSet[6].click()

    driver.quit()

def check_appium_server():
    status, pid = commands.getstatusoutput("ps ax | grep appium | wc -l")
    os.system("ps ax | grep appium ")
    print pid
    if pid == "2":
		print "appium server is not running"
		os.system("appium | tee appium.log &")
		sleep(5)
    else:
		print "appium server is  running"

def kill_thread(key):
	status, thread_id = commands.getstatusoutput("adb shell ps | grep %s | awk '{printf $2}'" % (key))
	os.system("adb root && adb shell kill %s" % (thread_id))

