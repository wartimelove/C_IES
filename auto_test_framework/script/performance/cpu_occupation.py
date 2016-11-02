import unittest
import os
import sys
import time
import threading
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
#from common.camera import Camera
#from common.wifi import Wifi
import shlex
import subprocess


class CPU_occupation(unittest.TestCase):
    
    file_path = os.path.dirname(__file__) 
    global resourcePath
    resourcePath = file_path + '/../../resource_files/performance/CPU/'
    
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
        cpu = 0
        cnt = 0
        appmonLogName = "appmon_" + self.serialno + ".log"
        os.system("adb -s %s shell /data/appmon -c 10 -p 1 > %s" %(self.serialno,appmonLogName))
        lines = os.popen("cat %s" %appmonLogName).readlines()
        for i in range(len(lines)):
            if lines[i].find("[cpu") >= 0:
                idle_index = lines[i].find("idle")
                total_index = lines[i].find("total")
                if idle_index < 0 or total_index < 0:
                    print "Can't find idle/total items"
                else:
                    idle = int(lines[i][idle_index+6:total_index-1])
                    total = int(lines[i][total_index+7:-1])
                    cpu += 100*(total-idle)/float(total)
                    cnt += 1
        avg = round(cpu/cnt,2)
        return avg
   

    def fetchBright(self):
        backlight = os.popen("adb -s %s shell cat '/sys/class/backlight/psb-bl/brightness'" %self.serialno).readlines()
        if len(backlight) < 0 :
            raise Exception('fail to fetch the screen brightness')
        else :
            print time.ctime() + '\tscreen brightness is : ' + backlight[0].strip()
            return  backlight[0].strip()

      
    def test_video_playback_1080p(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_video_playback_1080p")
        print 'Test Case: test_video_playback_1080p'
        component = 'com.android.gallery3d/.app.MovieActivity'
        package = 'com.android.gallery3d'
        #camera = Camera(self.device, self.serialno)
        #component = package + '/.app.MovieActivity'
        #package = camera.package
        videoName = 'video_h264_1080p.mp4'
        videoPath = resourcePath + videoName
        repeatTimes = 3
        cpu = 0
        lines = os.popen("adb -s %s shell ls /sdcard/Movies | grep '%s'" %(self.serialno,videoName)).readlines()
        if len(lines) == 0:
            os.system("adb -s %s push %s /sdcard/Movies" %(self.serialno,videoPath))
        else:
            pass

        cpu_sum = 0
        for i in range(repeatTimes):
            lines = os.popen("adb -s %s shell am start -n %s -d file:///sdcard/Movies/%s -t video/mp4" %(self.serialno, component, videoName)).readlines()
            for j in range(len(lines)):
                if lines[j].find('Error') >= 0:
                   raise Exception("Can not play video")
            time.sleep(2)
            cpu  = self.calAverageVal()
            cpu_sum = cpu_sum + cpu
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)
            os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
            time.sleep(3)
        avg = round(cpu_sum / repeatTimes, 2)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)

    def test_video_playback_720p(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_video_playback_720p")
        print 'Test Case: test_video_playback_720p'
        component = 'com.android.gallery3d/.app.MovieActivity'
        package = 'com.android.gallery3d'
        #camera = Camera(self.device, self.serialno)
        #component = camera.package + '/com.android.gallery3d.app.MovieActivity'
        #package = camera.package

        videoName = 'video_h264_720p.mp4'
        videoPath = resourcePath + videoName
        repeatTimes = 3
        cpu = 0
        cpu_sum = 0
        lines = os.popen("adb -s %s shell ls /sdcard/Movies | grep '%s'" %(self.serialno,videoName)).readlines()
        if len(lines) == 0:
            os.system("adb -s %s push %s /sdcard/Movies" %(self.serialno,videoPath))
        else:
            pass

        for i in range(repeatTimes):
            lines = os.popen("adb -s %s shell am start -n %s -d file:///sdcard/Movies/%s -t video/mp4" %(self.serialno, component, videoName)).readlines()
            for j in range(len(lines)):
                if lines[j].find('Error') >= 0:
                   raise Exception("Can not play video")

            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)                                        
            cpu_sum = cpu_sum + cpu
            os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
            time.sleep(3)
        avg = round(cpu_sum / repeatTimes, 2)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)

    def test_system_idle(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_system_idle")
        print 'Test Case: test_system_idle'
        self.device.device.press('KEYCODE_HOME', 'DOWN_AND_UP')
        MonkeyRunner.sleep(6)

        repeatTimes = 3
        cpu_sum = 0
        for i in range(repeatTimes):
            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)                                        
            cpu_sum = cpu_sum + cpu
        avg = round(cpu_sum / repeatTimes, 2)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)



    def test_build_in_Gallery(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_build_in_Gallery")
        print 'Test Case: test_build_in_Gallery'
        #picPath = resourcePath + 'Pic/'
        gallery_component = 'com.android.gallery3d/.app.GalleryActivity'
        gallery_package = 'com.android.gallery3d'
        c = Camera(self.device, self.serialno)

        camera_component = c.component
        camera_package = c.package
        #gallery = c.package + '/com.android.gallery3d.app.Gallery'
        
        lines = os.popen('adb -s %s shell am start -n %s' %(self.serialno, camera_component)).readlines()
        for i in range(len(lines)):
            if lines[i].find('Error') >= 0:
                raise Exception('Can not launch camera')
        MonkeyRunner.sleep(5)         
        self.device.device.touch(1225, 525, 'DOWN_AND_UP')
        MonkeyRunner.sleep(5)
        self.device.device.touch(1225, 520, 'DOWN_AND_UP') #Make sure the camera is on photo module
        MonkeyRunner.sleep(5)
        self.device.device.touch(1225, 400, 'DOWN_AND_UP')
        MonkeyRunner.sleep(5)
        self.device.device.touch(1225, 400, 'DOWN_AND_UP') #Capture two pictures
        MonkeyRunner.sleep(5)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, camera_package))

        
        lines = os.popen('adb -s %s shell am start -n %s' %(self.serialno, gallery_component)).readlines()
        for i in range(len(lines)):
            if lines[i].find('Error') >= 0:
                raise Exception('Can not launch Gallery')

        MonkeyRunner.sleep(5)         
        self.device.device.touch(135, 35, 'DOWN_AND_UP')
        MonkeyRunner.sleep(3)
        
        self.device.device.touch(140, 275, 'DOWN_AND_UP')     #choose tags option
        MonkeyRunner.sleep(3)
        #self.device.device.touch(600, 400, 'DOWN')
        os.system('adb -s %s shell input touchscreen tap 650 400' %self.serialno)
        MonkeyRunner.sleep(3)
        self.device.device.touch(1240, 35, 'DOWN_AND_UP')
        MonkeyRunner.sleep(3)
        self.device.device.touch(1190, 80, 'DOWN_AND_UP')
        MonkeyRunner.sleep(3)

        '''
        print 'drag'
        self.device.device.drag((900,400),(300,400))
        MonkeyRunner.sleep(3)
        print 'menu'
        self.device.device.press('KEYCODE_MENU', 'DOWN_AND_UP')
        MonkeyRunner.sleep(3)
        self.device.device.touch(1249, 35, 'DOWN_AND_UP')
        MonkeyRunner.sleep(3)
        self.device.device.touch(1192, 136, 'DOWN_AND_UP')
        MonkeyRunner.sleep(3)
        ''' 

        repeatTimes = 3
        cpu_sum = 0
        for i in range(repeatTimes):
            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)
            cpu_sum = cpu_sum + cpu
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, gallery_package))
        MonkeyRunner.sleep(3)
        avg = round(cpu_sum / repeatTimes, 2)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)


    def test_build_in_Music(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_build_in_Music")
        print 'Test Case: test_build_in_Music '
        musicName = 'Dus_remix_192Kbps_44100Hz_Stereo.mp3'
        musicPath = resourcePath + musicName
        #component = 'com.android.music/.MediaPlaybackActivity'
        #package = 'com.android.music'
        component = 'com.google.android.music/com.google.android.music.AudioPreview'
        package = 'com.google.android.music'
        lines = os.popen("adb -s %s shell ls /sdcard/Music/ | grep '%s'" %(self.serialno,musicName)).readlines()
        if len(lines) == 0:
            os.system("adb -s %s push %s /sdcard/Music" %(self.serialno,musicPath))
        else:
            pass

        lines = os.popen('adb -s %s shell am start -n %s  -d file:///sdcard/Music/%s' %(self.serialno, component, musicName)).readlines()
        for i in range(len(lines)):
            if lines[i].find('Error') >= 0:
                raise Exception('Can not play music')

        repeatTimes = 3
        cpu_sum = 0
        for i in range(repeatTimes):
            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)
            cpu_sum = cpu_sum + cpu
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(3)
        avg = round(cpu_sum / repeatTimes, 2)
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
	    count = 0
            print time.ctime()
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


    def test_IES_McAfee_background(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_McAfee_background")
        print '\nTest Case: test_IES_McAfee_background'
        package = 'com.wsandroid.suite.intelempg'
              

        self.launch_McAfee()
        self.device.device.press('KEYCODE_HOME', 'DOWN_AND_UP')

        repeatTimes = 3
        cpu_sum = 0
        for i in range(repeatTimes):
            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)
            cpu_sum = cpu_sum + cpu
        avg = round(cpu_sum / repeatTimes, 2)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(5)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)

    def test_IES_McAfee_scan(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_McAfee_scan")
        print '\nTest Case: test_IES_McAfee_scan'
        package = 'com.wsandroid.suite.intelempg'

        repeatTimes = 3
        cpu_sum = 0
        for i in range(repeatTimes):

            self.launch_McAfee()
            MonkeyRunner.sleep(3)

            self.device.device.touch(648, 248, 'DOWN_AND_UP')
            MonkeyRunner.sleep(3)
            self.device.device.touch(648, 288, 'DOWN_AND_UP')
            MonkeyRunner.sleep(2)
            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)
            cpu_sum = cpu_sum + cpu
            os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
            MonkeyRunner.sleep(5)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        avg = round(cpu_sum / repeatTimes, 2)
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
        cpu_sum = 0
        for i in range(repeatTimes):
            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)
            cpu_sum = cpu_sum + cpu
        avg = round(cpu_sum / repeatTimes, 2)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(3)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)
        labWifi.turnOffWifi()


    def test_IES_Foxit(self):
        try:
              package = 'com.foxit.mobile.pdf.lite'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_Foxit")
              print '\nTest Case: test_IES_Foxit'
              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
              repeatTimes = 3
              cpu_sum = 0
              for i in range(repeatTimes):
                  cpu = self.calAverageVal()
                  string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
                  print string
                  self.testResult.writeTestResult(string)
                  cpu_sum = cpu_sum + cpu
              self.device.device.touch(1240, 153, 'DOWN_AND_UP')
              monkey_thread.stop()
              self.device.device.touch(1240, 154, 'DOWN_AND_UP')
              avg = round(cpu_sum / repeatTimes, 2)
              os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
              MonkeyRunner.sleep(3)
              string = time.ctime() + '\tAverage value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
        except BaseException,e:
          print 'there is an exception ', e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()


    def test_IES_TD(self):
      try:
              package = 'com.intel.cmpc.td.agent'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_TD")
              print '\nTest Case: test_IES_TD'

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
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_IES_LabCam(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_LabCam")
        print '\nTest Case: test_IES_LabCam'
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
        cpu_sum = 0
        for i in range(repeatTimes):
            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)
            cpu_sum = cpu_sum + cpu
        avg = round(cpu_sum / repeatTimes, 2)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(3)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)


    def test_IES_MediaCam(self):
        self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_MediaCam")
        print '\nTest Case: test_IES_MediaCam'
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
        cpu_sum = 0
        for i in range(repeatTimes):
            cpu = self.calAverageVal()
            string = time.ctime() + '\t#%s CPU consumption is: ' %str(i+1) + str(cpu)
            print string
            self.testResult.writeTestResult(string)
            cpu_sum = cpu_sum + cpu
        avg = round(cpu_sum / repeatTimes, 2)
        os.system("adb -s %s shell am force-stop %s" %(self.serialno, package))
        MonkeyRunner.sleep(3)
        string = time.ctime() + '\tAverage value = ' + str(avg)
        print string
        self.testResult.writeTestResult(string)


    def test_IES_CLM(self):
        try:
              package = 'mythware.classroom.client'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_CLM")
              print '\nTest Case: test_IES_CLM' 
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
          print 'there is an exception ', e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()


    def test_IES_Kno(self):
        try:
              package = 'com.kno.textbooks'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_Kno")
              print '\nTest Case: test_IES_Kno'

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
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()


    def test_IES_DataAnalysis(self):
      try:
              package = 'com.isbx.pasco.Spark'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_DataAnalysis")
              print '\nTest Case: test_IES_DataAnalysis'

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
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()


    def test_IES_Artrage(self):
      try:
              package = 'com.ambientdesign.artrage'
	      lines = 0
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_Artrage")
              print '\nTest Case: test_IES_Artrage'

              monkey_thread = RunMonkey(package, self.serialno)
              monkey_thread.start()
	      MonkeyRunner.sleep(10)
	      isAlive=monkey_thread.isAlive()
	      if isAlive == False:
              		raise Exception("Can not launch package")
			
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
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_IES_VLC(self):
      try:
              package = 'org.videolan.vlc'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_VLC")
              print '\nTest Case: test_IES_VLC'

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
              string = time.ctime() + '\tVLC value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_IES_Pixlr(self):
      try:
              package = 'com.pixlr.oem.intel'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_Pixlr")
              print '\nTest Case: test_IES_Pixlr'

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
              string = time.ctime() + '\tPixlr value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_IES_SketchBook(self):
      try:
              package = 'com.adsk.sketchbook.oem.intel'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_SketchBook")
              print '\nTest Case: test_IES_SketchBook'

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
              string = time.ctime() + '\tSketchBook value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_IES_AdobeReader(self):
      try:
              package = 'com.adobe.reader'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_AdobeReader")
              print '\nTest Case: test_IES_AdobeReader'

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

    def test_IES_IER(self):
      try:
              package = 'com.intel.ipls.ierbundle'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_IER")
              print '\nTest Case: test_IES_IER'

	      self.launch_IER()
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
			
    def test_IES_WPS(self):
      try:
              package = 'cn.wps.moffice_eng'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_WPS")
              print '\nTest Case: test_IES_WPS'

	      self.launch_WPS()
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
              string = time.ctime() + '\tIER value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_IES_NetSupportstudent(self):
      try:
              package = 'com.netsupportsoftware.school.student.oem.intel'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_NetSupportstudent")
              print '\nTest Case: test_IES_NetSupportstudent'

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
              string = time.ctime() + '\tNetSupport student value = ' + str(avg)
              print string
              self.testResult.writeTestResult(string)
      except BaseException,e:
          print e
          line = os.popen("adb -s %s shell ps | awk '/com\.android\.commands\.monkey/ {system(\"adb -s %s shell kill \" $2)}'" %(self.serialno, self.serialno)).readlines()

    def test_IES_NetSupporttutor(self):
      try:
              package = 'com.netsupportsoftware.school.tutor.oem.intel'
              self.testResult.writeTestResult("Test Case: CPU Occupation\nTest Method: test_IES_NetSupporttutor")
              print '\nTest Case: test_IES_NetSupporttutor'

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

