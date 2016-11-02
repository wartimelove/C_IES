import unittest
import os
import sys
import time
import datetime
#from common.wifi import Wifi
#from common.contacts import Contacts
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

class Time_others(unittest.TestCase):
  file_path = os.path.dirname(__file__) 
  global resourcePath
  resourcePath = file_path + '/../../resource_files/performance/Time/'
    
  def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None):
    unittest.TestCase.__init__(self, methodName)
    self.device = device
    self.serialno = serialno
    self.testResult = testResult

  def setUp(self):
    pass

  def tearDown(self):
    os.system("adb -s %s shell am force-stop com.example.orientationtest" %self.serialno)
    self.testResult.writeTestResult("="*50)
    self.device.device.press('KEYCODE_HOME', 'DOWN_AND_UP') 

  def fetchTime(self,string):
    l = string.split()
    s = l[0].strip() + ' ' + l[1].strip()
    s2 = s.split('.')
    t1 = datetime.datetime.strptime(s2[0], '%m-%d %H:%M:%S')
    t2 = datetime.timedelta(milliseconds= int(s2[1]))
    t = t1 + t2
    return t

  def calRotationTime(self,i,x,y):
    os.system('adb -s %s logcat -c' %self.serialno)
    lines = os.popen("adb -s %s shell input touchscreen tap %s %s" %(self.serialno,x,y)).readlines()
    time.sleep(5)
    lines = os.popen("adb -s %s logcat -v time -d WindowManager:V *:S | grep 'save mTransitionAnimationScaleOld=1.0'" %self.serialno).readlines()
    print lines
    self.assertTrue(len(lines) == 1)
    time1 = self.fetchTime(lines[0])
    lines = os.popen("adb -s %s logcat -v time -d WindowManager:V *:S | grep 'restore mTransitionAnimationScale=1.0'" %self.serialno).readlines()
    print lines
    self.assertTrue(len(lines) == 1)
    time2 = self.fetchTime(lines[0])
    string = time.ctime() + '\t#%s Rotation Time: %s' %(i,str(time2 - time1)[6:11])
    print string
    self.testResult.writeTestResult(string)
    deltaTime = time2 - time1
    return deltaTime
    
  def test_time_screen_rotation(self):
    apkName = resourcePath + 'orientationTest.apk'
    component = "com.example.orientationtest/.MainActivity"
    self.testResult.writeTestResult("Test Case: Others\nTest Method: test_time_screen_rotation")
    print time.ctime() + '\tRunning test_Time_ScreenRotation...'
    lines = os.popen("adb -s %s shell pm list packages | grep com.example.orientationtest" %self.serialno).readlines()
    if len(lines) == 0:
      print "installing orientation test apk..."
      os.system("adb -s %s install %s" %(self.serialno,apkName))
    else:
      print "orientation test apk is already installed"
    os.system("adb -s %s shell am start -n %s" %(self.serialno,component))
    time.sleep(2)
    
    repeatTimes = 3
    timeSum = datetime.timedelta(0)

    #90 degree rotation
    timeSum += self.calRotationTime(1,70,155)
    #180 degree rotation
    timeSum += self.calRotationTime(2,70,190)
    #270 degree rotation
    timeSum += self.calRotationTime(3,70,260)
    #0 degree rotation
#   timeSum += self.calRotationTime(4,70,105)

    avgTime = timeSum / repeatTimes
    string = time.ctime() + "\tAverage time: %s" %str(avgTime)[6:11] 
    print string
    self.testResult.writeTestResult(string)

    
if __name__ == '__main__':
  unittest.main()
