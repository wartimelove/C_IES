import unittest
import os
import sys
import time
import datetime
#from common.wifi import Wifi
#from common.contacts import Contacts
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
#from common.camera import Camera

class App_launch_time(unittest.TestCase):

  def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None):
    unittest.TestCase.__init__(self, methodName)
    self.device = device
    self.serialno = serialno
    self.testResult = testResult

  def setUp(self):
    pass

  def tearDown(self):
    self.testResult.writeTestResult("="*50)
#    self.device.device.press('KEYCODE_HOME', 'DOWN_AND_UP') 

  def fetchTime(self,string):
    l = string.split()
    s = l[0].strip() + ' ' + l[1].strip()
    s2 = s.split('.')
    t1 = datetime.datetime.strptime(s2[0], '%m-%d %H:%M:%S')
    t2 = datetime.timedelta(milliseconds= int(s2[1]))
    t = t1 + t2
    return t
  
  def calLaunchTime(self, component, repeatTimes):
    timeSum = datetime.timedelta(0)
    for j in range(repeatTimes):
      self.device.reboot()
      time.sleep(60)
      self.device.rootDevice()
      #self.device.connectMonkeyDevice()
#      self.device.wakeup()
#      self.device.unlockScreen()
      os.system('adb -s %s logcat -c' %self.serialno)
      print "start to launch"
      print ('adb -s %s shell am start -n %s' %(self.serialno, component))
      lines = os.popen('adb -s %s shell am start  %s' %(self.serialno, component)).readlines()
      for i in range(len(lines)):
        if lines[i].find('Error') >= 0:
          raise Exception('Can not launch %s' %component)
      MonkeyRunner.sleep(6)
      line = os.popen('adb -s %s logcat -v time -d ActivityManager:I *:S | grep cmp=%s' %(self.serialno, component)).readlines()
      print line
      self.assertTrue(len(line) == 1)
      time1 = self.fetchTime(line[0])

      if component == 'com.isbx.pasco.Spark/com.isbx.sparksandboxui.LaunchActivity':
          print 'SPARKvue check another component'
	  MonkeyRunner.sleep(5)
          line = os.popen("adb -s %s logcat -v time -d ActivityManager:I *:S | grep 'Displayed com.isbx.pasco.Spark/com.isbx.sparksandboxui.SparkActivity'" %(self.serialno)).readlines()
	  print line
      elif component == 'com.kno.textbooks/kno.textbooks.SplashActivity':
	  print 'kno check another component'
          line = os.popen("adb -s %s logcat -v time -d ActivityManager:I *:S | grep 'Displayed com.kno.textbooks/kno.textbooks.SplashActivity'" %(self.serialno)).readlines()
          #line = os.popen("adb -s %s logcat -v time -d ActivityManager:I *:S | grep 'Displayed com.kno.textbooks/kno.textbooks.coursemanager.CourseListActivity'" %(self.serialno)).readlines()
      else :
          line = os.popen("adb -s %s logcat -v time -d ActivityManager:I *:S | grep 'Displayed %s'" %(self.serialno, component)).readlines()
      print "launch completely"
      MonkeyRunner.sleep(6)
      #line = os.popen('adb -s %s logcat -v time -d ActivityManager:I *:S | grep cmp=%s' %(self.serialno, component)).readlines()
      self.assertTrue(len(line) == 1)
      time2 = self.fetchTime(line[0])
      #if component == 'com.isbx.pasco.Spark/com.isbx.sparksandboxui.LaunchActivity':
          #print 'SPARKvue: launch time add 0.5s'
          #time2 += datetime.timedelta(milliseconds=500)
      print time1, time2
      string = time.ctime() + '\t#%s Launch Time: %0.3f' %(str(j+1), float(str(time2 - time1)[6:11]))
      print string
      self.testResult.writeTestResult(string)
      timeSum = timeSum + (time2 -time1)
      MonkeyRunner.sleep(5)

    avgTime = timeSum / repeatTimes
    string = time.ctime() + "\tAverage time: %0.3f" %float(str(avgTime)[6:11])
    print string
    self.testResult.writeTestResult(string)
    
  def test_LT_Music(self):
    lines = os.popen("adb -s %s shell ls /sdcard/Music/" %self.serialno).readlines()
    if len(lines) != 0:
      print "Delete all audio files in /sdcard/Music."
      os.system("adb -s %s shell rm -r /sdcard/Music/*" %self.serialno)
    component = 'com.google.android.music/com.android.music.activitymanagement.TopLevelActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Music")
    print time.ctime() + '\tRunning test_LT_Music...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_WebBrowser(self):
    component = 'com.android.browser/.BrowserActivity'
    browserSettingsPage = 'com.android.browser/.BrowserPreferencesPage'
    #ap = 'shz23f-wajoint-ap04-androidtable'
    #passwd = '1223334445'
    print time.ctime() + '\tRunning test_LT_WebBrowser...'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_WebBrowser")
    labWifi = Wifi(self.device, self.serialno, self.testResult)
    labWifi.openWifiSettings()
    if labWifi.turnOnWifi() == False:
        raise Exception("test_LT_WebBrowser: Turn on wifi failed") 
    if labWifi.connectAP() == False:
        raise Exception("test_LT_WebBowser: Connect AP failed")
    #set the homepage as "Blank page"
    lines = os.popen('adb -s %s shell am start -n %s' %(self.serialno, browserSettingsPage)).readlines()
    for i in range(len(lines)):
      if lines[i].find('Error') >= 0:
        raise Exception('Can not launch %s' %browserSettingsPage)
    MonkeyRunner.sleep(1)
    self.device.device.touch(800,115,'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    self.device.device.touch(800,345,'DOWN_AND_UP')
    MonkeyRunner.sleep(1)
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)
    labWifi.openWifiSettings()
    labWifi.turnOffWifi()

  def test_LT_Contacts(self):
    component = "com.android.contacts/.activities.PeopleActivity"
    waContacts = Contacts(self.device, self.serialno)
    waContacts.addContact("WAtest")
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Contacts")
    print time.ctime() + '\tRunning test_LT_Contacts...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)
        
  def test_LT_Gallery(self):
    lines = os.popen("adb -s %s shell ls /sdcard/DCIM/Camera/" %self.serialno).readlines()
    if len(lines) != 0:
      print "Delete all media files in /sdcard/DCIM/Camera."
      os.system("adb -s %s shell rm -r /sdcard/DCIM/Camera/*" %self.serialno)
    lines = os.popen("adb -s %s shell ls /sdcard/Movies/" %self.serialno).readlines()
    if len(lines) != 0:
      print "Delete all media files in /sdcard/Movies."
      os.system("adb -s %s shell rm -r /sdcard/Movies/*" %self.serialno)
    lines = os.popen("adb -s %s shell ls /sdcard/Pictures/" %self.serialno).readlines()
    if len(lines) != 0:
      print "Delete all pictures in /sdcard/Pictures."
      os.system("adb -s %s shell rm -r /sdcard/Pictures/*" %self.serialno)

    #camera = Camera(self.device, self.serialno)
    #component = camera.package + '/.app.Gallery'
    component = 'com.android.gallery3d/.app.GalleryActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Gallery")
    print time.ctime() + '\tRunning test_LT_Gallery...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_Settings(self):
    component = 'com.android.settings/.Settings'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Settings")
    print time.ctime() + '\tRunning test_LT_Settings...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_Camera(self):
    camera = Camera(self.device, self.serialno)
    component = camera.component
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Camera")
    print time.ctime() + '\tRunning test_LT_Camera...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_CLM(self):
    component = 'mythware.classroom.client/mythware.ux.student.form.MainActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_CLM")
    print time.ctime() + '\tRunning test_LT_CLM...'
    os.system('adb -s %s shell am start -n %s' %(self.serialno, component))
    time.sleep(5)
    self.device.device.touch(912,730, 'DOWN_AND_UP')
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_TD(self):
    component = 'com.intel.cmpc.td.agent/com.intel.cmpc.td.ui.MainActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_TD")
    print time.ctime() + '\tRunning test_LT_TD...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)
    
  def test_LT_LabCam(self):
    component = 'com.labcam/.LabCamActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_LabCam")
    print time.ctime() + '\tRunning test_LT_LabCam...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_MediaCam(self):
    component = 'com.mediacam/.MediaCamActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_MediaCam")
    print time.ctime() + '\tRunning test_LT_MediaCam...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_Kno(self):
    #component = 'com.kno.textbooks/kno.textbooks.SplashActivity'
    component = 'com.kno.textbooks/md5c6fc437aecb30701f36d1ffb4d673fe3.SplashActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Kno")
    print time.ctime() + '\tRunning test_LT_Kno...'

    MonkeyRunner.sleep(20)
    #discard 1st value since it is always longer than any others due to some initialzation work
    lines = os.popen('adb -s %s shell am start -n %s' %(self.serialno, component)).readlines()
    for i in range(len(lines)):
        if lines[i].find('Error') >= 0:
            raise Exception('Can not launch %s' %component)
    MonkeyRunner.sleep(5)
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_Foxit(self):
    component = 'com.foxit.mobile.pdf.lite/com.foxit.filemanager.FM_MainActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Foxit")
    print time.ctime() + '\tRunning test_LT_Foxit...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_SPARKvue(self):
    component = 'com.isbx.pasco.Spark/com.isbx.sparksandboxui.LaunchActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_SPARKvue")
    print time.ctime() + '\tRunning test_LT_SPARKvue...'
    # Discard first launch, because SPARKvue need update resources
    os.system('adb -s %s logcat -c' %self.serialno)
    lines = os.popen('adb -s %s shell am start -n %s' %(self.serialno, component)).readlines()
    for i in range(len(lines)):
        if lines[i].find('Error') >= 0:
            raise Exception('Can not launch %s' %component)
    MonkeyRunner.sleep(5)
    line = os.popen("adb -s %s logcat -d ActivityManager:I *:S | grep 'Displayed %s'" %(self.serialno, component)).readlines()
    if len(line) == 1:
        MonkeyRunner.sleep(20)
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_NoteTaker(self):
    component = 'com.visionobjects.notesmobile_int/.NotesMobileActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_NoteTaker")
    print time.ctime() + '\tRunning test_LT_NoteTaker...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_PenInput(self):
    component = 'com.visionobjects.stylusmobile_int/com.visionobjects.stylusmobile.StylusMainActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_PenInput")
    print time.ctime() + '\tRunning test_LT_PenInput...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_Artrage(self):
    component = 'com.ambientdesign.artrage/.MainActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Artrage")
    print time.ctime() + '\tRunning test_LT_Artrage...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_VLC(self):
    component = 'org.videolan.vlc/.gui.MainActivity'
    #component = 'org.videolan.vlc.betav7neon/.gui.MainActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_VLC")
    print time.ctime() + '\tRunning test_LT_VLC...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)
    
  def test_LT_McAfee(self):
    component = 'com.wsandroid.suite.intelempg/com.mcafee.app.SplashActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_McAfee")
    print time.ctime() + '\tRunning test_LT_McAfee...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_Pixlr(self):
    component = 'com.pixlr.oem.intel/com.pixlr.express.StartupActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_Pixlr")
    print time.ctime() + '\tRunning test_LT_Pixlr...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_SketchBook(self):
    component = 'com.adsk.sketchbook.oem.intel/com.adsk.sketchbook.SketchBook'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_SketchBook")
    print time.ctime() + '\tRunning test_LT_SketchBook...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_AdobeReader(self):
    component = 'com.adobe.reader/.AdobeReader'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_AdobeReader")
    print time.ctime() + '\tRunning test_LT_AdobeReader...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_IER(self):
    component = 'com.intel.ipls.ierbundle/.SplashScreen_Activity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_IER")
    print time.ctime() + '\tRunning test_LT_IER...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_WPS(self):
    component = 'cn.wps.moffice_eng/cn.wps.moffice.main.local.home.PadHomeActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_WPS")
    print time.ctime() + '\tRunning test_LT_WPS...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_NetSupportstudent(self):
    component = 'com.netsupportsoftware.school.student.oem.intel/.IntelCheckActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_NetSupportstudent")
    print time.ctime() + '\tRunning test_LT_NetSupportstudent...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_NetSupporttutor(self):
    component = 'com.netsupportsoftware.school.tutor.oem.intel/com.netsupportsoftware.school.tutor.activity.IntelSplashActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_NetSupporttutor")
    print time.ctime() + '\tRunning test_LT_NetSupporttutor...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

  def test_LT_FluidMath(self):
    component = 'com.fluiditysoftware.fluidmath/.MainActivity'
    self.testResult.writeTestResult("Test Case: Application Launch Time\nTest Method: test_LT_FluidMath")
    print time.ctime() + '\tRunning test_LT_FluidMath...'
    repeatTimes = 3
    self.calLaunchTime(component, repeatTimes)

if __name__ == '__main__':
  unittest.main()
