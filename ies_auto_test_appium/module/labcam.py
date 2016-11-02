import os,sys
import unittest
import traceback
import commands
#
from appium import webdriver
#from selenium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
#
from common.function import *
#
reload(sys)
sys.setdefaultencoding('utf8')

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LabcamFunctionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.labcam'
        desired_caps['appActivity'] = '.LabCamActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def testtimelapsefront(self):
	print "labcam timelapse front testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[0].click()
        sleep(3)       
        recording_btn = self.driver.find_element_by_class_name("android.widget.Button")
	recording_btn.click()
	sleep(5)
 	if check_camera("1") == "false":
		recording_btn.click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[2].click()
	status,video_orig = commands.getstatusoutput("adb shell ls /mnt/shell/emulated/0/LabCamera/TimeLapse | wc -l ")       
 
	sleep(40)
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	sleep(50)
	recording[2].click()
	sleep(3)
	play_btn = self.driver.find_elements_by_class_name("android.widget.Button")
	play_btn[1].click()
	sleep(5)

	status,video_now = commands.getstatusoutput("adb shell ls /mnt/shell/emulated/0/LabCamera/TimeLapse | wc -l ")       
	print video_orig, video_now
	if video_orig < video_now :
		 pass
        self.driver.press_keycode(3)


    def testkinematicsfront(self):
	print "labcam kinematics front testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[1].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[1].click()
	sleep(2)
 	if check_camera("1") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
	recording[2].click()
        sleep(5)
	recording_option = self.driver.find_elements_by_class_name("android.widget.Button")
	recording_option[7].click()
        self.driver.press_keycode(3)


    def testmicroscopefront(self):
	print "labcam microscope front testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[3].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[0].click()
	sleep(2)
 	if check_camera("1") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
	recording[8].click()
        sleep(5)
	recording[8].click()
	sleep(3)        
	os.system("adb shell rm /mnt/shell/emulated/0/LabCamera/Microscope/image.jpg")
	sleep(3)
        self.driver.press_keycode(3)


    def testuniversalloggerfront(self):
	print "labcam universallogger front testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[4].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
        sleep(5)
	recording[3].click()
 	if check_camera("1") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
        sleep(5)
	recording[3].click()
        sleep(5)
        recording[7].click() 
	sleep(5)
        recording[7].click() 
	sleep(5)
        self.driver.press_keycode(3)


    def testpathfinderfront(self):
	print "labcam pathfinder front testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[5].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[0].click()
        sleep(5)
 	if check_camera("1") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
	recording[4].click()
        sleep(5)
	recording[4].click()
#	Image_now[0].click()
	sleep(5)
	os.system("adb shell rm /mnt/shell/emulated/0/LabCamera/Pathfinder/image.jpg")
	sleep(3)
        self.driver.press_keycode(3)


    def testtimelapserear(self):
	print "labcam timelapse rear testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[0].click()
        sleep(3)       
        recording_btn = self.driver.find_element_by_class_name("android.widget.Button")
	recording_btn.click()
	sleep(5)
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[1].click()
	sleep(5)
 	if check_camera("0") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[2].click()
	status,video_orig = commands.getstatusoutput("adb shell ls /mnt/shell/emulated/0/LabCamera/TimeLapse | wc -l ")       
 
	sleep(40)
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	sleep(50)
	recording[2].click()
	sleep(3)
	play_btn = self.driver.find_elements_by_class_name("android.widget.Button")
	play_btn[1].click()
	sleep(5)

        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[3].click()
        sleep(3)	
	recording[1].click()	
	status,video_now = commands.getstatusoutput("adb shell ls /mnt/shell/emulated/0/LabCamera/TimeLapse | wc -l ")       
	if video_orig < video_now :
		 pass
	

        
	sleep(5)
        self.driver.press_keycode(3)


    def testkinematicsrear(self):
	print "labcam kinematics rear testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[1].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[1].click()
	sleep(2)
	recording[1].click()
	sleep(2)
 	if check_camera("0") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
	recording[2].click()
        sleep(5)
	recording_option = self.driver.find_elements_by_class_name("android.widget.Button")
	recording_option[7].click()
	sleep(3)
	recording[1].click()
	sleep(2)
        self.driver.press_keycode(3)



    def testmicroscoperear(self):
	print "labcam microscope rear testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[3].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[0].click()
	sleep(2)
	recording[1].click()
	sleep(2)
 	if check_camera("0") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
	recording[8].click()
        sleep(5)
	recording[8].click()
	sleep(3)        
	recording[1].click()
	os.system("adb shell rm /mnt/shell/emulated/0/LabCamera/Microscope/image.jpg")
	sleep(3)
        self.driver.press_keycode(3)


    def testuniversalloggerrear(self):
	print "labcam universallogger rear testing"
	os.system("adb logcat > /tmp/camera.log &")
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[4].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
        sleep(3)
	recording[0].click()
        sleep(5)
	recording[1].click()
        sleep(5)
 	if check_camera("0") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
	recording[3].click()
        sleep(5)
        recording[7].click() 
	sleep(5)
        recording[7].click() 
        sleep(3)
	recording[1].click()
	sleep(5)
        self.driver.press_keycode(3)

    def testpathfinderrear(self):
	sleep(3)
	print "labcam pathfinder rear testing"
	os.system("adb logcat > /tmp/camera.log &")
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[5].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[0].click()
        sleep(5)
	recording[1].click()
        sleep(5)
 	if check_camera("0") == "false":
		recording[1].click()
        	sleep(5)
	for i in range(1,5):
		os.system("kill `ps ax | grep logcat | grep adb |head -n 1 | awk '{printf $1}'`")
	recording[4].click()
        sleep(5)
	recording[4].click()
	sleep(5)
	recording[4].click()
        sleep(5)
	recording[1].click()
	sleep(5)
	os.system("adb shell rm /mnt/shell/emulated/0/LabCamera/Pathfinder/image.jpg")
	sleep(3)
        self.driver.press_keycode(3)


    def testtimelapsesuspend(self):
	print "labcam timelapse suspend testing"
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[0].click()
        sleep(3)       
        recording_btn = self.driver.find_element_by_class_name("android.widget.Button")
	recording_btn.click()
	sleep(5)
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[2].click()
    
	os.system("adb shell 'echo mem > /sys/power/state' && adb shell 'echo on > /sys/power/state'")	
	sleep(30)
        self.driver.press_keycode(3)


    def testkinematicssuspend(self):
	print "labcam kinematics suspend testing"
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[1].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[1].click()
	sleep(2)
	recording[2].click()
        sleep(5)
	recording_option = self.driver.find_elements_by_class_name("android.widget.Button")
	recording_option[7].click()
	os.system("adb shell 'echo mem > /sys/power/state' && adb shell 'echo on > /sys/power/state'")	
        sleep(3)
	self.driver.press_keycode(3)


    def testmicroscopesuspend(self):
	print "labcam microscope suspend testing"
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[3].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[0].click()
	sleep(2)
	recording[8].click()
        sleep(5)
	recording[8].click()
	sleep(3)        
	os.system("adb shell 'echo mem > /sys/power/state' && adb shell 'echo on > /sys/power/state'")	
	#os.system("adb shell rm /mnt/shell/emulated/0/LabCamera/Microscope/image.jpg")
	sleep(3)
        self.driver.press_keycode(3)


    def testuniversalloggersuspend(self):
	print "labcam universallogger suspend testing"
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[4].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
        sleep(5)
	recording[3].click()
        sleep(5)
	recording[3].click()
        sleep(5)
        recording[7].click() 
	sleep(5)
        recording[7].click() 
	os.system("adb shell 'echo mem > /sys/power/state' && adb shell 'echo on > /sys/power/state'")	
	sleep(5)
        self.driver.press_keycode(3)

    def testpathfindersuspend(self):
	print "labcam pathfinder suspend testing"
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[5].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[0].click()
        sleep(5)
	recording[4].click()
        sleep(5)
	recording[4].click()
	sleep(5)
	os.system("adb shell 'echo mem > /sys/power/state' && adb shell 'echo on > /sys/power/state'")	
	#os.system("adb shell rm /mnt/shell/emulated/0/LabCamera/Pathfinder/image.jpg")
	sleep(3)
        self.driver.press_keycode(3)


    def testtimelapseforcestop(self):
	print "labcam timelapse forcestop testing"
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[0].click()
        sleep(3)       
        recording_btn = self.driver.find_element_by_class_name("android.widget.Button")
	recording_btn.click()
	sleep(5)
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[2].click()
	status,video_orig = commands.getstatusoutput("adb shell ls /mnt/shell/emulated/0/LabCamera/TimeLapse | wc -l ")       
 
	sleep(40)
        self.driver.quit()
	kill_thread("labcam")
	self.setUp()
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[0].click()
        sleep(3)       
        self.driver.press_keycode(3)


    def testkinematicsforcestop(self):
	print "labcam kinematics forcestop testing"
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[1].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[1].click()
	sleep(2)
	recording[2].click()
        sleep(5)
	recording[3].click()
        sleep(20)
	recording[3].click()
        
	sleep(10)
        self.driver.quit()
	kill_thread("labcam")
	self.setUp()
	sleep(3)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[1].click()
        sleep(3)       
        self.driver.press_keycode(3)

