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
#from common.function import *
from common.config import *
#
reload(sys)
sys.setdefaultencoding('utf8')

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class StudentTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Baytrail_CR'
        desired_caps['appPackage'] = 'com.netsupportsoftware.school.student.oem.intel'
        desired_caps['appActivity'] = '.IntelCheckActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def teststudent(self):
	print "netsupport student testing" 
	sleep(3)
        Room = self.driver.find_element_by_id('com.netsupportsoftware.school.student.oem.intel:id/roomEditTextValue')
        Name = self.driver.find_element_by_id('com.netsupportsoftware.school.student.oem.intel:id/roomNameValue')

        Room.send_keys("ies")
        Name.send_keys("LiRuipeng")

        self.driver.press_keycode(5)

class TutorTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.netsupportsoftware.school.tutor.oem.intel'
        desired_caps['appActivity'] = 'com.netsupportsoftware.school.tutor.activity.IntelSplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def testtutor(self):
	print "netsupport tutor testing" 
	sleep(3)
        Views = self.driver.find_elements_by_class_name("android.widget.ImageView")
	Views[2].click()
        
	textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("test_training")

        self.assertEqual('test_training', textfields[0].text)

	sleep(2)
        Start_Room = self.driver.find_element_by_name("Start Room")
	Start_Room.click()
	sleep(2)
	
	Lesson_Detail = self.driver.find_elements_by_class_name("android.widget.EditText")
        Lesson_Detail[0].send_keys("Alan")
	sleep(2)
        
        #self.assertEqual('test_traing', Lesson_Detail[2].text)
        #self.assertEqual('Read less,know more!', Lesson_Detail[3].text)
        Enter_Room = self.driver.find_elements_by_class_name("android.widget.ImageView")
	Enter_Room[1].click()
	
	sleep(3)
        self.driver.press_keycode(5)

class LabCamTests(unittest.TestCase):
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

    def testlabcam(self):
	print "labcam testing" 
	sleep(6)
        LabCam_button = self.driver.find_elements_by_class_name("android.widget.Button")
	LabCam_button[2].click()
        
        recording = self.driver.find_elements_by_class_name("android.widget.Button")
	recording[0].click()
	sleep(5)
	recording[1].click()
        sleep(5)
	recording[3].click()
        sleep(20)
	recording[3].click()
        
	sleep(10)
        self.driver.press_keycode(3)

class RARTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.rarlab.rar'
        desired_caps['appActivity'] = '.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def testrar(self):
	print "rar testing" 
	sleep(3)
        RAR_option = self.driver.find_elements_by_class_name("android.widget.ImageButton")
	RAR_option[0].click()
       	
	sleep(2) 
	test_archived = self.driver.find_elements_by_class_name("android.widget.TextView")
	test_archived[0].click()

	sleep(2)
	check_ok = self.driver.find_element_by_name("OK")
	check_ok.click()
        
	sleep(5)
        self.driver.press_keycode(3)

class MythwareTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'mythware.classroom.client'
        desired_caps['appActivity'] = 'mythware.ux.student.form.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)
	try:
		Accept = self.driver.find_element_by_id("android:id/button1")
		Accept.click()
	except:
		pass
		

    def tearDown(self):
        self.driver.quit()

    def edittextclear(self,text):
	self.driver.keyevent(123)
	for i in range(0,len(text)):
		self.driver.keyevent(67)

    def testmythware(self):
	print "mythware testing" 
	sleep(5)
        Btn_SetName = self.driver.find_element_by_id("mythware.classroom.client:id/btnEdit")
	Btn_SetName.click()
 	
	Login = self.driver.find_element_by_id("mythware.classroom.client:id/editLoginName")
	Org_name=Login.get_attribute('text')
	self.edittextclear(Org_name)
	Login.send_keys("Alen")

	Btn_OK = self.driver.find_element_by_id("android:id/button1")
	Btn_OK.click()      	
	Student = self.driver.find_element_by_id("mythware.classroom.client:id/textStudentName")
	self.assertEqual('Alen', Student.text)
        
	sleep(5)
        self.driver.press_keycode(3)

class ESFileExplorerTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.estrongs.android.pop'
        desired_caps['appActivity'] = '.view.FileExplorerActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def testesfileexplorer(self):
	print "esfileexplorer testing" 
	sleep(5)
        Btn_Bottom = self.driver.find_elements_by_id("com.estrongs.android.pop:id/button_menu_bottom")
	Btn_Bottom[2].click()
 	
	Type_opt = self.driver.find_elements_by_class_name("android.widget.TextView")
	Type_opt[1].click()

	File_Name = self.driver.find_elements_by_class_name("android.widget.EditText")
	File_Name[0].send_keys("test_file")
	sleep(5)

	Btn_OK = self.driver.find_element_by_id("com.estrongs.android.pop:id/button_common_dialog_22")
	Btn_OK.click()

	sleep(2)
        #Btn_Bottom = self.driver.find_elements_by_id("com.estrongs.android.pop:id/button_menu_bottom")
	#Btn_Bottom[2].click()
        
	#Search_Bar = self.driver.find_element_by_id("com.estrongs.android.pop:id/edittext_search_bar")
	#Search_Bar.click()

	New_File = self.driver.find_elements_by_class_name("android.widget.ImageView")
	Point = TouchAction(self.driver)
	print len(New_File)
	key = len(New_File) - 3
	Point.long_press(New_File[key]).wait(10).perform()

        Btn_Bottom = self.driver.find_elements_by_id("com.estrongs.android.pop:id/button_menu_bottom")
	Btn_Bottom[4].click()
	sleep(3)
	Btn_OK = self.driver.find_element_by_id("com.estrongs.android.pop:id/button_common_dialog_22")
	Btn_OK.click()
	sleep(3)

        self.driver.press_keycode(3)

class KnoTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.kno.textbooks'
        desired_caps['appActivity'] = 'md5c6fc437aecb30701f36d1ffb4d673fe3.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)
				#NOTE: may not encounter the "Cancel" button when launching
	try:
		Cancel = self.driver.find_element_by_id("android:id/button2")
		Cancel.click()
		print "yes"
	except:
		pass
		print "no"

		

    def tearDown(self):
        self.driver.quit()

    def testkno(self):
#	try:
#        	Btn_Cancel = self.driver.find_element_by_id("android:id/button2")
#		Btn_Cancel.click()
#	except NoSuchElementException:
#		pass
	print "kno testing" 
	sleep(5)	
        Btn_AddCourse = self.driver.find_elements_by_class_name("android.widget.TextView")
	Btn_AddCourse[6].click()
	
	Course_Name = self.driver.find_element_by_id("com.kno.textbooks:id/courseName")
	Course_Name.send_keys("Rally")
        Btn_OK = self.driver.find_element_by_id("android:id/button1")
	Btn_OK.click()
	
	New_Course = self.driver.find_elements_by_class_name("android.widget.TextView")
	self.assertEqual('Rally', New_Course[6].text)
	
	Added_Course = self.driver.find_element_by_id("com.kno.textbooks:id/courseImage")
	Added_Course.click()
	Delete_option = self.driver.find_elements_by_class_name("android.widget.TextView")
	Delete_option[1].click()

	Btn_Delete = self.driver.find_element_by_id("android:id/button1")
	Btn_Delete.click()
	sleep(3)

        self.driver.press_keycode(3)

class VLCTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'org.videolan.vlc'
        desired_caps['appActivity'] = '.gui.MainActivity '

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def testvlc(self):
	print "vlc testing" 
	sleep(3)
        Video = self.driver.find_elements_by_class_name("android.widget.TextView")
	Video[1].click()
	
	sleep(30)
        self.driver.press_keycode(3)

class McAfeeTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.wsandroid.suite.intelempg'
        desired_caps['appActivity'] = 'com.mcafee.app.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

	try:
		Accept = self.driver.find_element_by_id("com.wsandroid.suite.intelempg:id/ws_eula_positive_btn")
		Accept.click()
		sleep(60)
	except:
		pass
	try:
		Get_started = self.driver.find_element_by_id("com.wsandroid.suite.intelempg:id/button3")
		Get_started.click()
		sleep(5)
	except:
		pass
	TextView = self.driver.find_elements_by_class_name("android.widget.TextView")
	print len(TextView)


    def tearDown(self):
        self.driver.quit()

    def testmcafee(self):
	print "mcafee testing" 
	sleep(5)

        Scan_Option = self.driver.find_elements_by_class_name("android.widget.TextView")
	Scan_Option[6].click()

	sleep(3)
	Scan_Now = self.driver.find_elements_by_id("com.wsandroid.suite.intelempg:id/title")
	Scan_Now[4].click()

	sleep(30)
	try:
		Btn_close = self.driver.find_element_by_id("com.wsandroid.suite.intelempg:id/id_btn_close")
		Btn_close.click()
	except:
		sleep(30)
		Btn_close = self.driver.find_element_by_id("com.wsandroid.suite.intelempg:id/id_btn_close")
		Btn_close.click()
		
	sleep(3)
        self.driver.press_keycode(3)

class SparkvueTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.isbx.pasco.Spark'
        desired_caps['appActivity'] = 'com.isbx.sparksandboxui.LaunchActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def testsparkvue(self):
	print "sparkvue testing" 
	sleep(5)
        Page = self.driver.find_element_by_class_name("android.webkit.WebView")
	sleep(3)
	self.driver.switch_to.context("WEBVIEW_com.isbx.pasco.Spark")
	print self.driver.contexts
	sleep(5)
	Sensor = self.driver.find_element_by_xpath("//*[@id='sensor-list-0']/ul/li")
	touch_actions = TouchActions(self.driver)
	touch_actions.tap(Sensor).perform()

	Show_btn = self.driver.find_element_by_xpath("//*[@id='home']/div[3]/a[2]")
	Show_btn.click()
	sleep(5)
	btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[3]/div[1]/div/a[1]")
	btn.click()
	home_btn = self.driver.find_element_by_xpath("//*[@id='workbook']/div[1]/div[1]/a[1]")
	home_btn.click()
	sleep(3)
	No_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/a[3]")
	No_btn.click()
	sleep(3)
	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

class TDTests(unittest.TestCase):
    def Connect_Wifi(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.wifi.WifiSettings'
    
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    
        sleep(5)
        Btn_Setting = self.driver.find_elements_by_class_name("android.widget.ImageButton")
        Btn_Setting[0].click()
        Add_Network = self.driver.find_elements_by_id("android:id/title")
        Add_Network[0].click()

	Security = self.driver.find_element_by_id("com.android.settings:id/security")
	Security.click()
	Security_option = self.driver.find_elements_by_class_name("android.widget.CheckedTextView")
	Security_option[2].click()
        T_SSID = self.driver.find_element_by_id("com.android.settings:id/ssid")
        #T_SSID.send_keys("shz23f-wajoint-ap99-IES")
        T_SSID.send_keys(essid)
       	Password_In = self.driver.find_element_by_id("com.android.settings:id/password")
        Password_In.send_keys(password)
        #Password_In.send_keys("ies+12345")
        Btn_Save = self.driver.find_element_by_id("android:id/button1")
        Btn_Save.click()
        #Wifi_List = self.driver.find_elements_by_id("android:id/title")
        #Wifi_List[0].click()
	#try:
        #	Password_In = self.driver.find_element_by_id("com.android.settings:id/password")
        #	Password_In.send_keys("ies+12345")
        #	Btn_Connect = self.driver.find_element_by_id("android:id/button1")
        #	Btn_Connect.click()
	#except :
	#	Btn_Done = self.driver.find_element_by_id("android:id/button2")
	#	Btn_Done.click()
    
        self.driver.quit()

    def setUp(self):
	self.Connect_Wifi()
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.intel.cmpc.td.agent'
        desired_caps['appActivity'] = 'com.intel.cmpc.td.ui.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def edittextclear(self,text):
	self.driver.keyevent(123)
	for i in range(0,len(text)):
		self.driver.keyevent(67)

    def testtd(self):
	print "td testing" 
	sleep(5)
        Setting_Option = self.driver.find_element_by_id("com.intel.cmpc.td.agent:id/settingTab")
	Setting_Option.click()

        Btn_Edit = self.driver.find_element_by_id("com.intel.cmpc.td.agent:id/editButton")
	Btn_Edit.click()
	Server_Address = self.driver.find_element_by_id("com.intel.cmpc.td.agent:id/serverAddress")
        Server_Address.click()
	IP=Server_Address.get_attribute('text')
	self.edittextclear(IP)
	Server_Address.send_keys("192.168.1.119")
        self.driver.press_keycode(4)
	Btn_Save = self.driver.find_element_by_id("com.intel.cmpc.td.agent:id/saveButton")
	Btn_Save.click()
	Btn_Test = self.driver.find_element_by_id("com.intel.cmpc.td.agent:id/testButton")
	Btn_Test.click()
	
	Student = self.driver.find_element_by_id("com.intel.cmpc.td.agent:id/resultText")
	self.assertEqual('Connection is successful.', Student.text)
	
	sleep(3)
        self.driver.press_keycode(3)

class PixlrTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.pixlr.oem.intel'
        desired_caps['appActivity'] = 'com.pixlr.express.StartupActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

	try:
		Accept_btn = self.driver.find_element_by_id("android:id/button1")
		Accept_btn.click()
	except:
		pass

    def tearDown(self):
        self.driver.quit()

    def testpixlr(self):
	print "pixlr testing" 
	sleep(5)

        Pothos_option = self.driver.find_element_by_id("com.pixlr.express:id/choose")
	Pothos_option.click()
	
        Potho = self.driver.find_elements_by_class_name("android.widget.ImageView")
	Potho[10].click()
        Effect = self.driver.find_elements_by_class_name("android.widget.TextView")
	Effect[3].click()
        Effect = self.driver.find_elements_by_id("com.pixlr.express:id/pack_name_label")
	Effect[1].click()
        Apply = self.driver.find_element_by_id("com.pixlr.express:id/apply")
	Apply.click()
        Save = self.driver.find_element_by_id("com.pixlr.express:id/save")
	Save.click()
        Current = self.driver.find_elements_by_id("com.pixlr.express:id/normal_view")
	Current[1].click()
        Close = self.driver.find_element_by_id("com.pixlr.express:id/close")
	Close.click()
	
	sleep(3)
        self.driver.press_keycode(3)

class FluidMathTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.fluiditysoftware.fluidmathforintel'
        desired_caps['appActivity'] = '.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)

	try:
		Accept_btn = self.driver.find_element_by_id("android:id/button1")
		Accept_btn.click()
	except:
		pass

    def tearDown(self):
        self.driver.quit()

    def testfluidmath(self):
	print "fluidmath testing" 
	sleep(5)
	self.driver.tap([(1225,100),])
	
	x = self.driver.get_window_size()['width']
	y = self.driver.get_window_size()['height']
	print x, y
	start_x = int(x*0.3)
	start_y = int(y*0.3)
	
	mid_x = int(x*0.5)
	mid_y = int(y*0.7)

	end_x = int(x*0.5)
	end_y = int(y*0.3)
	print start_x,start_y,mid_x,mid_y,end_x,end_y
	sleep(3)
	Point = TouchAction(self.driver)
	#Point.press(x=start_x,y=start_y).move_to(x=mid_x,y=mid_y).move_to(x=end_x,y=end_y).release().perform()
	Point.press(x=start_x,y=start_y).move_to(x=mid_x,y=mid_y).release().perform()
	sleep(3)	
	Point.press(x=start_x,y=start_y).move_to(x=end_x,y=end_y).release().perform()

	sleep(3)
	print self.driver.contexts	
	self.driver.switch_to.context("WEBVIEW_com.fluiditysoftware.fluidmathforintel")
	sleep(3)
	source = self.driver.page_source
	sleep(3)
	bar = self.driver.find_element_by_xpath("//*[@id='sidebar_handle']")
	touch_actions = TouchActions(self.driver)
	#touch_actions.tap(bar).perform()
	#sleep(3)
	#touch_actions.tap(bar).perform()
	bar.click()
	sleep(3)
	clear_button = self.driver.find_element_by_xpath("//*[@id='clearbutton']")
	clear_button.click()
#	isinstance(self.driver.page_source,"gbk")
	#source.decode("gb2312")
	#source.encode("ascii")	
#	print (self.driver.page_source.encode('ascii').decode('utf-8'))

	self.driver.switch_to.context("NATIVE_APP")
        self.driver.press_keycode(3)

class SketchBookTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Bytrail_CR'
        desired_caps['appPackage'] = 'com.adsk.sketchbook.oem.intel'
        desired_caps['appActivity'] = 'com.adsk.sketchbook.SketchBook'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	self.driver.implicitly_wait(8)
	
	try:
		self.driver.find_element_by_name('I accept').click()	
	except:
		pass

	try:
		self.driver.switch_to_alert().accept()
	except:
		pass
	sleep(5)
	try:
		x = int(700)
		y = int(130)
		self.driver.tap([(x,y),])
	except:
		pass

    def tearDown(self):
        self.driver.quit()

    def testsketchbook(self):
	print "sketchbook testing" 
	sleep(5)
	#Accept_button = self.driver.find_element_by_id("android:id/button1")
	#Accept_button.click()
	#sleep (5)
        Btn_Penpoint = self.driver.find_elements_by_class_name("android.widget.ImageView")
	print Btn_Penpoint
	Btn_Penpoint[12].click()
	
	x = self.driver.get_window_size()['width']
	y = self.driver.get_window_size()['height']
	print x, y
        start_x = int(x*0.3)
        start_y = int(y*0.3)

        mid_x = int(x*0.5)
        mid_y = int(y*0.7)

        end_x = int(x*0.5)
        end_y = int(y*0.3)
        print start_x,start_y,mid_x,mid_y,end_x,end_y
        sleep(3)
        Point = TouchAction(self.driver)
        #Point.press(x=start_x,y=start_y).move_to(x=mid_x,y=mid_y).move_to(x=end_x,y=end_y).release().perform()
        Point.press(x=start_x,y=start_y).move_to(x=mid_x,y=mid_y).release().perform()
        sleep(3)
        Point.press(x=start_x,y=start_y).move_to(x=end_x,y=end_y).release().perform()

	
	Option = self.driver.find_element_by_id("com.adsk.sketchbook.oem.intel:id/top_bar_main_menu")
	Option.click()
	New_Sketch = self.driver.find_elements_by_class_name("android.widget.ImageView")
	New_Sketch[0].click()

	sleep(2)
	Default = self.driver.find_elements_by_class_name("android.widget.TextView")
	Default[1].click()
	sleep(2)
	Clean_btn = self.driver.find_elements_by_class_name("android.widget.TextView")
	Clean_btn[2].click()
	
	sleep(3)
        self.driver.press_keycode(3)

