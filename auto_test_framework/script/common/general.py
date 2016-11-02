import time
import os
import sys
import string
import re
import HTML
import ConfigParser
import subprocess,commands
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

class DevicesList():
    def getFirstDeviceNo(self):
        """get current devices and return first dev"""
        dev = os.popen("adb devices | grep 'device' |awk '{print $1}'").readlines()
        if len(dev) < 2:
            print 'have no device'
            os._exit(1)
        return dev[1]


class SIMonkeyDevice():

    file_path = os.path.dirname(__file__)
    global resourcePath
    resourcePath = file_path + '/../../resource_files/common/'

    def __init__(self,serialno=None):
        self.serialno = serialno


    def connectMonkeyDevice(self):
        self.device = MonkeyRunner.waitForConnection(6, self.serialno)
        print '===================connect device====================   ',self.device
        MonkeyRunner.sleep(2)

        for k in range(10):
             x = len(self.monkey_thread(k))
             if x:
                print "already conenection success"
                break
             else:
                print "failtrue enter reconenct++++++"
                MonkeyRunner.sleep(2)
                self.device = MonkeyRunner.waitForConnection(6, self.serialno)
                MonkeyRunner.sleep(3)
        return self.device
    
    def wakeup(self):
        self.device.wake()
        MonkeyRunner.sleep(2)

    def unlockScreen(self):
	# update the point for the Android 5.0
	self.device.drag((640, 430), (640, 120))
        MonkeyRunner.sleep(2)
        self.device.press('KEYCODE_HOME', 'DOWN_AND_UP')
        MonkeyRunner.sleep(2)

    def rootDevice(self):
        '''
        if os.system("adb -s %s root" %self.serialno) != 0:
            print "Can't root device"
        else:    
            print "Root device successfully"
            self.connectMonkeyDevice()
            MonkeyRunner.sleep(2)
        '''
        print 'root device'
        line = os.popen('adb -s %s root' %self.serialno).readlines()
#        print len(line),'   ',line
#        if len(line) == 1 and line[0].find('restarting adbd as root') > -1:
        if len(line) == 0:
            print "Root device successfully"
            MonkeyRunner.sleep(6)
            self.connectMonkeyDevice()
            MonkeyRunner.sleep(2)
        elif len(line) == 1 and line[0].find('adbd is already running as root') > -1:
            print 'adbd is already running as root'
#            MonkeyRunner.sleep(6)
#            self.connectMonkeyDevice()
#            MonkeyRunner.sleep(2)
        else:
            print "Can't root device"
        MonkeyRunner.sleep(2)
    
    def monkey_thread(self,num):
        pidList1 = os.popen("adb -s %s shell ps | grep 'com.android.commands.monkey' | awk '{print $2}'" %self.serialno).readlines()
        print "Monkey thread address = %d pid = %s" %(num,pidList1)
        return pidList1


    def reboot(self):
        print "Reboot device..."
        os.system("adb -s %s reboot" %self.serialno)
        MonkeyRunner.sleep(60)
        i = 0
        while True:
            i += 1
            line = os.popen('adb devices | grep %s' %self.serialno).readlines()
            if len(line)<1:
                if i > 10:
                    raise Exception('device not found, had killed server five times.')
                    os.exit(1)
                print self.serialno,' device not found!!!!!!!!!!!!!!!!!!!!!!!!!'
                os.system('adb kill-server')
                print 'kill server' 
            else:
                print 'there is the device :', self.serialno
                break

    def getProduct(self):
        product = self.serialno[0:2]
        if product == 'EF':
            return 'flaghill'
        elif product == 'EG':
            return 'grandhill'
        elif product == 'Ba':
            return 'baytrail'
	elif product == 'EB':
	    return 'baytrail'
	elif product == 'CH':
	    return 'mounthill'
	elif product == 'ST':
	    return 'mounthill'
        else:
            return 'unknow'

    def prepareForTest(self):
        print "Go to Settings->Display, set sleep timeout as 30 minutes"
        lines = os.popen("adb -s %s shell am start -n com.android.settings/.DisplaySettings" %self.serialno).readlines()
        for i in range(len(lines)):
            if lines[i].find('Error') >=0:
                raise Exception("Can't open Display settings page!")
        MonkeyRunner.sleep(2)
        # Tap "Sleep"
        # and Select "30 minutes"
        MonkeyRunner.sleep(2)
	con_product = self.getProduct()
	if con_product == 'baytrail':
        	self.device.touch(880, 312, 'DOWN_AND_UP')
        	MonkeyRunner.sleep(2)
        	self.device.touch(640, 520, 'DOWN_AND_UP')
	elif con_product == 'grandhill':
        	self.device.touch(880, 248, 'DOWN_AND_UP')
        	MonkeyRunner.sleep(2)
        	self.device.touch(625, 548, 'DOWN_AND_UP')
	elif con_product == 'flaghill':
        	self.device.touch(880, 312, 'DOWN_AND_UP')
        	MonkeyRunner.sleep(2)
        	self.device.touch(625, 580, 'DOWN_AND_UP')
	elif con_product == 'mounthill':
        	self.device.touch(880, 312, 'DOWN_AND_UP')
        	MonkeyRunner.sleep(2)
        	self.device.touch(640, 520, 'DOWN_AND_UP')
	else:
		return 'unknow platform'
        MonkeyRunner.sleep(2)
	os.system('adb -s %s shell am force-stop "com.android.settings"' % self.serialno)


        print "Go to Settings->Security, disable 'Verify apps' option"
        lines = os.popen('adb -s %s shell am start -n com.android.settings/.SecuritySettings' %self.serialno).readlines()
        for i in range(len(lines)):
            if lines[i].find('Error') >=0:
                raise Exception("Can't open Security settings page!")
        MonkeyRunner.sleep(3)
        #refImage = MonkeyRunner.loadImageFromFile(resourcePath + 'verify_apps_on.png')
        #screenshot = self.device.takeSnapshot()
        #subImage = screenshot.getSubImage((1190,684,32,32))
        #if subImage.sameAs(refImage, 0.95):
        #    self.device.touch(650, 150, 'DOWN_AND_UP')
        #    MonkeyRunner.sleep(2)
        self.device.touch(650, 150, 'DOWN_AND_UP')
        MonkeyRunner.sleep(2)
        self.device.touch(650, 120, 'DOWN_AND_UP')
        MonkeyRunner.sleep(2)

        os.system('adb -s %s shell am force-stop "com.android.settings"' %self.serialno)


        #camera = Camera(self, self.serialno)
        #cameraComponent = camera.component
        #cameraPackage = camera.package
        #print cameraComponent
        #print cameraPackage
        #line = os.popen('adb -s %s shell am start -n %s' %(self.serialno, cameraComponent)).readlines()
        #for i in range(len(line)):
        #    if line[i].find('Error') >= 0:
        #        raise Exception("Can't open camera")
        #MonkeyRunner.sleep(5)
        #print '-----first time launch camera, choose the record location option----'
        #self.device.touch(500,470,'DOWN_AND_UP')
        #MonkeyRunner.sleep(3)
        #os.system('adb -s %s shell am force-stop %s' %(self.serialno, cameraPackage))
        

        #galleryComponent = camera.package +  '/com.android.gallery3d.app.Gallery'
        #galleryPackage = camera.package
        #galleryComponent = 'com.android.gallery3d/.app.GalleryActivity'
        #galleryPackage = 'com.android.gallery3d'

        #line = os.popen('adb -s %s shell am start -n %s' %(self.serialno, galleryComponent)).readlines()
        #for i in range(len(line)):
        #    if line[i].find('Error') >= 0:
        #        raise Exception("Can't open gallery")
        #MonkeyRunner.sleep(5)
        #print '-----first time launch gallery, choose the sign in option----'
        #self.device.touch(1044,689,'DOWN_AND_UP')
        #MonkeyRunner.sleep(3)
        #os.system('adb -s %s shell am force-stop %s' %(self.serialno, galleryPackage))

        #config_file_path = resourcePath + '../../script/common/config.txt'
        #os.system('adb -s %s push %s "/data/local/tmp/"' %(self.serialno, config_file_path))



class DeviceInfo():
    """get device information"""
    def __init__(self, serialno=None):
        self.serialno = serialno
        
    def getSerialno(self):
        serialno = os.popen("adb -s %s shell getprop ro.serialno" %self.serialno).readline()
        return serialno

    def getProductName(self):
        productName = os.popen("adb -s %s shell getprop ro.product.name" %self.serialno).readline()
        return productName

    def getModelName(self):
        modelName = os.popen("adb -s %s shell getprop ro.product.model" %self.serialno).readline()
        return modelName

    def getBrandName(self):
        brandName = os.popen("adb -s %s shell getprop ro.product.brand" %self.serialno).readline()
        return brandName

    def getManufacturerName(self):
        manufacturerName = os.popen("adb -s %s shell getprop ro.product.manufacturer" %self.serialno).readline()
        return manufacturerName
    
    def getOSVersion(self):
        osVersion = os.popen("adb -s %s shell getprop ro.build.version.release" %self.serialno).readline()
        return osVersion

    def getFingerprint(self):
        fingerprint = os.popen("adb -s %s shell getprop ro.build.fingerprint" %self.serialno).readline()
        return fingerprint

    def getInstalledSize(self):
        lines = os.popen("adb -s %s shell df | grep -e '/system' -e '/cache' -e '/data' | awk '{print $3}'" %self.serialno).readlines()
        size = 0
        for i in range(len(lines)):
            if lines[i].strip()[-1] == 'G':
                size += int(float(lines[i].strip()[:-1])*1024)
            else:
                size += int(float(lines[i].strip()[:-1]))
        return size

class TestResult():
    """Test result ordered by time"""
    
    def __init__(self, outputDir=None, serialno=None):
        self.serialno = serialno
        self.testResultDir = outputDir + serialno + os.sep + "test_results/"
        if os.path.exists(self.testResultDir):
            pass
        else:
            os.makedirs(self.testResultDir)
            
    def initTestResult(self):
        """Create test result file"""
        self.startTime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.curTestResultPath = self.testResultDir + self.startTime
        self.deviceInfo = DeviceInfo(self.serialno)
        self.installedSize = self.deviceInfo.getInstalledSize()
        fileName = "TestResult.txt"
	self.debug_path = self.curTestResultPath + os.sep + 'debug'
	self.media_path = self.curTestResultPath + os.sep + 'media'
        os.makedirs(self.curTestResultPath + os.sep + 'debug')
        os.makedirs(self.curTestResultPath + os.sep + 'media')
        self.fileFullPath = self.curTestResultPath + os.sep + fileName
        try:
            self.fp = open(self.fileFullPath, 'w')
        except IOError, e:
            print e
            os._exit(1)
        return self.fp, self.curTestResultPath, self.debug_path, self.media_path
        
    def writeTestResult(self, result):
        """Append test result"""
        try:
            self.fp.write(result + '\n')
            self.fp.flush()
        except IOError, e:
            print e
            os._exit(1)

    def openTestResult(self, mode):
        """open test result file by a certain mode(r,w,a)"""
        try:
            self.fp = open(self.fileFullPath, mode)
        except IOError, e:
            print e
            os._exit(1)
        finally:
            return self.fp

    def closeTestResult(self):
        """Close test result file """
        try:
            self.fp.close()
        except IOError, e:
            print e
            os._exit(1)

    def getTestResultPath(self):
        return self.curTestResultPath

    def getTestDebugPath(self):
        return self.curTestResultPath + os.sep + 'debug'

    def getTestFilePath(self):
        return self.curTestResultPath + os.sep + 'media'

    def generateHTMLTestReport(self):
        self.endTime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        report_name = 'TestReport.html'
        report_path = self.curTestResultPath + os.sep + report_name
        REPORT_TEMPLATE = \
        """
        <HTML>
        <head>
            <Title>$title</Title>
            <style type="text/css">
                #logtext {font-size:10; font-family:"comic sans ms" arial;}
            </style>
        </head>
        <body>
        <h1 align="center">$report_name</h1>
        <ul>
        <li><h3>Test Summary</h3></li>
        </ul>
        <!-- Show Device Information -->
        $test_summary
        <ul>
        <li><h3>Test Pie Chart</h3></li>

        <table border="0" cellPadding="0" cellSpacing="10" height="260px" width="100%">
            <tr>
                <td style="WIDTH: 50%">
                    <iframe frameBorder="0"  scrolling="no" src="/cgi-bin/pie_chart.cgi?pass=%NUM_PASS%&fail=%NUM_FAIL%&na=%NUM_NA%" style="Z-INDEX: 1; VISIBILITY: inherit; WIDTH: 100%; HEIGHT: 100%">
                    </iframe>
                </td>
            </tr>
        </table>

        <li><h3>Test Result</h3></li>
        <!-- Show Performance Test Result Table -->
        $performance_test_result
        <!-- Show System Benchmark Result -->
        $benchmark_result
        <!-- Show Stress Test Result Table -->
        $stress_test_result
        <!-- Show OS Behavior Test Result Table -->
        $osBehavior_test_result
        <!-- Show Built in Apps Test Result Table -->
        $builtinApps_test_result
        <!-- Show Image BAT Test Result Table -->
        $imageBAT_test_result
		<!-- Show IES Test Result Table -->
		$ies_test_result
        </ul>
        </ul>
        <ul>
        <li><h3>Test Log</h3></li>
        <li><a href="../../platform-log" target="_blank">Case Running Log</a></li>
        <li><a href="./media/" target="_blank">Media Pictures</a></li>
        <li><a href="./debug/" target="_blank">Debug Pictures</a></li>
        <li><a href="../../test_results.tar.gz" target="_blank">test_results</a></li>
        </ul>
        </body>
        </HTML>
        """
        
                                          
        #create test result table
        performance_table = HTML.Table(attribs={'bgcolor' : '#F0FFF0'})
        stress_table = HTML.Table(attribs={'bgcolor' : '#F0FFF0'})
        osBehavior_table = HTML.Table(attribs={'bgcolor' : '#F0FFF0'})
        builtinApps_table = HTML.Table(attribs={'bgcolor' : '#F0FFF0'})
        imageBAT_table = HTML.Table(attribs={'bgcolor' : '#F0FFF0'})
        ies_table = HTML.Table(attribs={'bgcolor' : '#F0FFF0'})


        case_name = None
        table_row = []
        pass_num = 0
        fail_num = 0
        NA_num = 0
        hasPerformance = False
        hasStress = False
        hasOSBehavior = False
        hasBuiltInApps = False
        hasImageBAT = False
        hasBenchmark = False
        hasIES = False
        config = ConfigParser.ConfigParser()
        iteration_conf = ConfigParser.ConfigParser()
        config.read(os.path.dirname(__file__) + "/../performance/performance_target.conf")
        iteration_conf.read(os.path.dirname(__file__) + "/../stress/stress_iteration.conf")
        lines = self.fp.readlines()
        #match pattern
        case_pattern = re.compile(r'Test Case:.(?P<case>[\w\s]+)')
        method_pattern = re.compile(r'Test Method:.(?P<method>[\w\s.]+)')
        val_pattern = re.compile(r'[\w\W\s]+(?P<value>\b\d+\.\d+[a-zA-Z]*\Z)')
        seperater_pattern = re.compile(r'=+')
        i = 0
        while i < len(lines):
            #stress test result table
            if lines[i].lower().find('stress') >= 0:
                if hasStress == False:
                    hasStress = True
                    stress_table.rows.append(HTML.TableRow(["Stress Test"],col_span=['5'], bgcolor='#2F4F4F',header=True, col_align=['left'],attribs={'style':'color:white'}))
                    stress_table.rows.append(HTML.TableRow(["Test", "Iteration", "Result", "cpu_usage[%]", "memory_usage[%]"], bgcolor='#AFEEEE',header=True, col_align=['left']*5))
                match = case_pattern.match(lines[i].strip())
                if case_name != match.group('case'):
                    case_name = match.group('case')
                    table_row.append(case_name)
                    stress_table.rows.append(HTML.TableRow(table_row,col_span=['7'],bgcolor='#E0FFFF', header=True, col_align=['left'], attribs={'style':'font-style:oblique'}))
                    table_row = []
                match = method_pattern.match(lines[i+1].strip())
		cpu_avg = match.group('method') + ".cpu.avg"
		memory_avg = match.group('method') + ".mem.avg"
		status,memory_usage=commands.getstatusoutput("cat %s" %memory_avg)
		status,cpu_usage=commands.getstatusoutput("cat %s" %cpu_avg)
                table_row.append(match.group('method'))
                table_row.append(iteration_conf.get(case_name,table_row[0]))
                if lines[i+2].strip() == 'Pass':
                    table_row.append('Passed')
                    table_row[-1] = HTML.TableCell('Passed',bgcolor='#66CC33')
                    pass_num += 1
                    i += 4
                elif lines[i+2].strip() == 'Fail':
                    table_row.append('Failed')
                    table_row[-1] = HTML.TableCell('Failed',bgcolor='red')
                    fail_num += 1
                    i += 4
                else:
                    table_row.append('NA')
                    table_row[-1] = HTML.TableCell('NA',bgcolor='#FFFF33')
                    NA_num += 1
                    i += 3
		table_row.append(cpu_usage)
		table_row.append(memory_usage)
                stress_table.rows.append(HTML.TableRow(table_row))
                print table_row
                table_row = []
            #imageBAT test result table
            elif lines[i].find('ImageBAT') >= 0:
                if hasImageBAT == False:
                    hasImageBAT = True
                    imageBAT_table.rows.append(HTML.TableRow(["Image BAT Test"],col_span=['2'], bgcolor='#2F4F4F',header=True, col_align=['left'],attribs={'style':'color:white'}))
                    imageBAT_table.rows.append(HTML.TableRow(["Test", "Result"], bgcolor='#AFEEEE',header=True, col_align=['left']*2))
                match = case_pattern.match(lines[i].strip())
                if case_name != match.group('case'):
                    case_name = match.group('case')
                    table_row.append(case_name[:-9])
                    imageBAT_table.rows.append(HTML.TableRow(table_row,col_span=['7'],bgcolor='#E0FFFF', header=True, col_align=['left'], attribs={'style':'font-style:oblique'}))
                    table_row = []
                match = method_pattern.match(lines[i+1].strip())
                table_row.append(match.group('method'))
                if lines[i+2].strip() == 'Pass':
                    table_row.append('Passed')
                    table_row[-1] = HTML.TableCell('Passed',bgcolor='#66CC33')
                    pass_num += 1
                    i += 4
                elif lines[i+2].strip() == 'Fail':
                    table_row.append('Failed')
                    table_row[-1] = HTML.TableCell('Failed',bgcolor='red')
                    fail_num += 1
                    i += 4
                else:
                    table_row.append('NA')
                    table_row[-1] = HTML.TableCell('NA',bgcolor='#FFFF33')
                    NA_num += 1
                    i += 3
                imageBAT_table.rows.append(HTML.TableRow(table_row))
                print table_row
                table_row = [] 
            #OS behavior test result table
            elif lines[i].find('OS_Behavior') >= 0:
                if hasOSBehavior == False:
                    hasOSBehavior = True
                    osBehavior_table.rows.append(HTML.TableRow(["OS Behavior Test"],col_span=['2'], bgcolor='#2F4F4F',header=True, col_align=['left'],attribs={'style':'color:white'}))
                    osBehavior_table.rows.append(HTML.TableRow(["Test", "Result"], bgcolor='#AFEEEE',header=True, col_align=['left']*2))
                match = case_pattern.match(lines[i].strip())
                if case_name != match.group('case'):
                    case_name = match.group('case')
                    table_row.append(case_name[:-9])
                    osBehavior_table.rows.append(HTML.TableRow(table_row,col_span=['7'],bgcolor='#E0FFFF', header=True, col_align=['left'], attribs={'style':'font-style:oblique'}))
                    table_row = []
                match = method_pattern.match(lines[i+1].strip())
                table_row.append(match.group('method'))
                if lines[i+2].strip() == 'Pass':
                    table_row.append('Passed')
                    table_row[-1] = HTML.TableCell('Passed',bgcolor='#66CC33')
                    pass_num += 1
                    i += 4
                elif lines[i+2].strip() == 'Fail':
                    table_row.append('Failed')
                    table_row[-1] = HTML.TableCell('Failed',bgcolor='red')
                    fail_num += 1
                    i += 4
                else:
                    table_row.append('NA')
                    table_row[-1] = HTML.TableCell('NA',bgcolor='#FFFF33')
                    NA_num += 1
                    i += 3
                osBehavior_table.rows.append(HTML.TableRow(table_row))
                print table_row
                table_row = [] 
            #Built In Apps test result table
            elif lines[i].find('BuiltinApps') >= 0:
                if hasBuiltInApps == False:
                    hasBuiltInApps = True
                    builtinApps_table.rows.append(HTML.TableRow(["Built-in Apps Test"],col_span=['2'], bgcolor='#2F4F4F',header=True, col_align=['left'],attribs={'style':'color:white'}))
                    builtinApps_table.rows.append(HTML.TableRow(["Test", "Result"], bgcolor='#AFEEEE',header=True, col_align=['left']*2))
                match = case_pattern.match(lines[i].strip())
                if case_name != match.group('case'):
                    case_name = match.group('case')
                    table_row.append(case_name[:-12])
                    builtinApps_table.rows.append(HTML.TableRow(table_row,col_span=['7'],bgcolor='#E0FFFF', header=True, col_align=['left'], attribs={'style':'font-style:oblique'}))
                    table_row = []
                match = method_pattern.match(lines[i+1].strip())
                table_row.append(match.group('method'))
                if lines[i+2].strip() == 'Pass':
                    table_row.append('Passed')
                    table_row[-1] = HTML.TableCell('Passed',bgcolor='#66CC33')
                    pass_num += 1
                    i += 4
                elif lines[i+2].strip() == 'Fail':
                    table_row.append('Failed')
                    table_row[-1] = HTML.TableCell('Failed',bgcolor='red')
                    fail_num += 1
                    i += 4
                else:
                    table_row.append('NA')
                    table_row[-1] = HTML.TableCell('NA',bgcolor='#FFFF33')
                    NA_num += 1
                    i += 3
                builtinApps_table.rows.append(HTML.TableRow(table_row))
                print table_row
                table_row = [] 
            #ies test result table
            elif lines[i].find('ies') >= 0 :
                assert len(lines[i].split(': ')) == 2

                if not hasIES:
                    hasIES = True
                    ies_table.rows.append(HTML.TableRow(["IES Test"],col_span=['7'], bgcolor='#2F4F4F',header=True, 
                                          col_align=['left'],attribs={'style':'color:white'}))
                    ies_table.rows.append(HTML.TableRow(["Test", "Result"], bgcolor='#AFEEEE',header=True, col_align=['left']*2))

                ies_table_row = []
                ies_table_row.append(lines[i].split(': ')[1] + ': ' + lines[i+1].split('\n')[0])
                ies_table_row.append(lines[i+2].split('\n')[0])
                ies_table_row[-1] = HTML.TableCell(lines[i+2].split('\n')[0], bgcolor='#66CC33')
                pass_num += 1

                #if lines[i+2].split('\n')[0] == '[PASS]':
                #    ies_table_row.append(lines[i+2].split('\n')[0])
                #    ies_table_row[-1] = HTML.TableCell('Passed', bgcolor='#66CC33')
                #    pass_num += 1

                #if lines[i+2].split('\n')[0] == '[FAIL]':
                #    ies_table_row.append(lines[i+2].split('\n')[0])
                #    ies_table_row[-1] = HTML.TableCell('Failed', bgcolor='red')
                #    pass_num += 1

                ies_table.rows.append(HTML.TableRow(ies_table_row))
                print lines[i].split(': ')[1].split('\n')[0], ':',lines[i+1].split('\n')[0], ':\t', lines[i+2].split('\n')[0]

                # three for every three lines of the case in the TestResult.txt 
                i += 3

            #performance test result table
            else:
                if hasPerformance == False:
                    hasPerformance = True
                    performance_table.rows.append(HTML.TableRow(["Performance Test"],col_span=['7'], bgcolor='#2F4F4F',header=True, col_align=['left'],attribs={'style':'color:white'}))
                    performance_table.rows.append(HTML.TableRow(["Test", "Value1", "Value2", "Value3", "Average", "Target", "Result"], \
		                           bgcolor='#AFEEEE',header=True, col_align=['left']*7)) 
                match = case_pattern.match(lines[i].strip())
                if case_name != match.group('case'):
                    case_name = match.group('case')
                    table_row.append(case_name)
                    performance_table.rows.append(HTML.TableRow(table_row,col_span=['7'],bgcolor='#E0FFFF', header=True, col_align=['left'], attribs={'style':'font-style:oblique'}))
                    table_row = []
                match = method_pattern.match(lines[i+1].strip())
                table_row.append(match.group('method'))
                i+=2
                j=0
                while not seperater_pattern.match(lines[i+j].strip()):
                    match = val_pattern.match(lines[i+j].strip())
                    table_row.append(match.group('value'))
                    j+=1   
                for k in range(4-j):
                    table_row.append("")
                print table_row
                table_row.append(config.get(case_name,table_row[0]))
                if config.get('criteria',table_row[0]) == 'greater':
                    if table_row[4] == "":
                        table_row.append('NA')
                        table_row[-1] = HTML.TableCell('Not Completed',bgcolor='#FFFF33')
                        NA_num += 1
                    elif string.atof(table_row[4]) > config.getfloat(case_name,table_row[0]):
                        table_row.append('Passed')
                        table_row[-1] = HTML.TableCell('Passed',bgcolor='#66CC33')
                        pass_num += 1
                    else:
                        table_row.append('Failed')
                        table_row[-1] = HTML.TableCell('Failed',bgcolor='red')
                        fail_num += 1
                elif config.get('criteria',table_row[0]) == 'less':
                    if table_row[4] == "":
                        table_row.append('NA')
                        table_row[-1] = HTML.TableCell('Not Completed',bgcolor='#FFFF33')
                        NA_num += 1
                    elif string.atof(table_row[4]) < config.getfloat(case_name,table_row[0]):
                        table_row.append('Passed')
                        table_row[-1] = HTML.TableCell('Passed',bgcolor='#66CC33')
                        pass_num += 1
                    else:
                        table_row.append('Failed')
                        table_row[-1] = HTML.TableCell('Failed',bgcolor='red')
                        fail_num += 1
                else:
                        table_row.append('NA')
                        NA_num += 1

                performance_table.rows.append(HTML.TableRow(table_row))
                table_row = []
                i += j+1

        #system benchmark table
        benchmark_table = HTML.Table(attribs={'bgcolor' : '#F0FFF0'})
        benchmark_table.rows.append(HTML.TableRow(["System Benchmark Test"],col_span=['2'], bgcolor='#2F4F4F',header=True, col_align=['left'],attribs={'style':'color:white'}))
        benchmark_table.rows.append(HTML.TableRow(["Test","Link"], bgcolor='#AFEEEE',header=True, col_align=['left']*2))
        table_row.append('test_Benchmark_Quadrant')
        table_row[0] = HTML.TableCell('test_Benchmark_Quadrant',attribs={'rowspan':'3'})
        for i in range(1,4):
            name = 'test_Benchmark_Quadrant_%s.png' %str(i)
            path = self.curTestResultPath + os.sep + name
            if os.path.exists(path):
                table_row.append('<a href=%s target="_blank">Screenshot #%s</a>' %(name,str(i)))
            else:
                table_row.append('NA')
            benchmark_table.rows.append(HTML.TableRow(table_row))
            table_row=[]
        table_row.append('test_Benchmark_AnTuTu')
        table_row[0] = HTML.TableCell('test_Benchmark_AnTuTu',attribs={'rowspan':'3'})
        for i in range(1,4):
            name = 'test_Benchmark_AnTuTu_%s.png' %str(i)
            path = self.curTestResultPath + os.sep + name
            if os.path.exists(path):
                table_row.append('<a href=%s target="_blank">Screenshot #%s</a>' %(name,str(i)))
            else:
                table_row.append('NA')
            benchmark_table.rows.append(HTML.TableRow(table_row))
            table_row=[]

        #test summary table
        summary = []
        summary.append({'Start Time' : self.startTime})
        summary.append({'End Time' : self.endTime})
        summary.append({'Description' : self.deviceInfo.getFingerprint().strip()})
        summary.append({'Model Name' : self.deviceInfo.getModelName().strip()})
        summary.append({'Manufacturer' : self.deviceInfo.getManufacturerName().strip()})
        summary.append({'Serial Number' : self.deviceInfo.getSerialno().strip()})
        summary.append({'OS Version' :  self.deviceInfo.getOSVersion().strip()})
        summary.append({'Installed Size' : str(self.installedSize) + 'MB'})
        summary.append({'Passed' : str(pass_num)})
        summary.append({'Failed' : str(fail_num)})
        summary.append({'NA' : str(NA_num)})

        summary_table = HTML.Table(attribs={'bgcolor' : '#F0FFF0'})
        summary_table.rows.append(HTML.TableRow(["Test Summary"], col_span=['2'],bgcolor='#AFEEEE',header=True))
        for item in summary:
            summary_row = list(item.items()[0])
            summary_table.rows.append(HTML.TableRow(summary_row, col_styles=['font-weight:bold', None]))

        #fill in template
        page = string.Template(REPORT_TEMPLATE).substitute(
                                            title="Test Report for %s-%s" %(self.deviceInfo.getModelName().strip(),self.serialno),
                                            report_name="Test Report for %s-%s" %(self.deviceInfo.getModelName().strip(),self.serialno),
                                            test_summary=str(summary_table) + '<p>\n',
                                            performance_test_result=str(performance_table) + '<p>\n',
                                            stress_test_result=str(stress_table) + '<p>\n',
                                            osBehavior_test_result=str(osBehavior_table) + '<p>\n',
                                            builtinApps_test_result=str(builtinApps_table) + '<p>\n',
                                            benchmark_result=str(benchmark_table) + '<p>\n',
                                            imageBAT_test_result=str(imageBAT_table) + '<p>\n',                                        
                                            ies_test_result=str(ies_table) + '<p>\n')                                         
        page = page.replace("%NUM_PASS%", str(pass_num)).replace("%NUM_FAIL%", str(fail_num)).replace("%NUM_NA%", str(NA_num));
        f = open(report_path, "w")
        f.write(page)
        f.close()
	os.system('mv *.log ' +  self.debug_path)
	os.system('mv *.mem ' +  self.debug_path)
	os.system('mv *.avg ' +  self.debug_path)

 
class Log():
    def __init__(self, serialno=None, testResult=None, \
		appName=None, device=None):
        self.serialno =serialno
	self.testResult = testResult
	self.appName = appName
	self.device = device

    def clearLog(self):
        os.system("adb -s %s logcat -c" %self.serialno)

    def captureLog(self, testcase=None, testResultPath=None, lines=None):
        fileName = "Logcat_" + testcase + ".log"
        fullPath = testResultPath + os.sep + fileName
        if os.system("adb -s %s logcat -v time -d > %s" %(self.serialno, fullPath)) != 0:
            print "Error when capturing TestCase:%s log" %testcase
            os._exit(1)
        else:
            print "Detailed log in %s" %fullPath
	monkeylog = testcase + ".log"
	fullmonkeyPath = testResultPath + os.sep + monkeylog
	for line in lines:
		os.system("echo '%s' >> %s" %(line, fullmonkeyPath))

		
    
    def captureJavaScreenOutput(self, outputStr=None, testcase=None, debugFolderPath=None):
        fileName = "JavaOutput_" + testcase + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".log"
        fullPath = debugFolderPath + os.sep + fileName
        fp = open(fullPath, 'w')
        for i in range(len(outputStr)):
            try:
                fp.write(outputStr[i])
                fp.flush()
            except IOError, e:
                print e
                os._exit(1)
        try:
            fp.close()
        except IOError, e:
            print e
            os._exit(1)

    def _getAndSaveActResult(self, filename):
		logPath = self.testResult.curTestResultPath + os.sep + self.appName
		if not os.path.exists(logPath):
			os.mkdir(logPath)

		pathfilename = logPath + os.sep + filename + '.png'
		result = self.device.device.takeSnapshot()
		result = result.getSubImage((0,0,1280,750))
		result.writeToFile(pathfilename,'png')
		return result
   
    def get_cpu_usage(self, filename):
		logPath = self.testResult.curTestResultPath + os.sep + self.appName
		if not os.path.exists(logPath):
			os.mkdir(logPath)

		cpuLogName = filename + '.cpu'
		cpu = 0
	        cnt = 0
        	appmonLogName = "appmon_" + self.serialno + ".log"
        	os.system("adb -s %s shell /data/appmon -c 1 -p 1 > %s" %(self.serialno,appmonLogName))
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
        	cpu_avg = round(cpu/cnt,2)
		avg_tmp = cpuLogName + ".avg"
		os.system("echo %s > %s " % (cpu_avg, avg_tmp))
        	return cpu_avg


    def get_mem_usage(self, filename):
        	memory = 0
        	cnt = 0
        	memoryLogName = filename + ".mem"
        	count = 0
        	avg_sum = 0
        	for count in range(1):
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
        	mem_avg = round(avg_orig,2)
		avg_tmp = memoryLogName + ".avg"
		os.system("echo %s > %s " % (mem_avg, avg_tmp))
        	return mem_avg

