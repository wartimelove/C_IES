import unittest
from ies_cpu_occupation import IES_CPU_occupation
from ies_app_launch_time import IES_App_launch_time
from ies_memory_utilization import IES_Memory_utilization
#from graphics import Graphics
#from system import System
#from camera_performance import CameraPerformance
from time_others import Time_others
import os

def performanceSuite(device=None, outputDir=None, debugFlag=True, serialno=None, testResult=None):
    suite = unittest.TestSuite()
            
    ''' 
    suite.addTest(CPU_occupation('test_IES_MediaCam', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_LabCam', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_MediaCam', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_Kno', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_Artrage', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_Foxit', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_TD', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_CLM', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_Aviary', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_ES_File_Explorer', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_RAR', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_SPARKvue', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_VLC', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_McAfee', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_Pixlr', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_SketchBook', device, serialno, testResult))
    suite.addTest(App_launch_time('test_LT_AdobeReader', device, serialno, testResult))
    '''
#For test script development
    if debugFlag == True:
        product = device.getProduct()
        path = os.path.dirname(__file__)
        print path, product
        if product  == 'grandhill':
            f = open(path + os.sep + 'case_grandhill.txt')
        elif product == 'flaghill':
            f = open(path + os.sep + 'case_flaghill.txt')
        elif product == 'baytrail':
            f = open(path + os.sep + 'case_baytrail.txt')
        elif product == 'mounthill':
            f = open(path + os.sep + 'case_mounthill.txt')
#For test suite execution
    else:
        f = open(outputDir + serialno + os.sep + 'platform-configure')
    
    test_cases = f.readlines()
    f.close()
    for i in range(len(test_cases)):

        case  = test_cases[i].strip()

        if case != '' and case[0] != '#':
            if case.split(':')[0] == 'Camera Performance':
                suite.addTest(CameraPerformance(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'CPU Occupation':
                suite.addTest(IES_CPU_occupation(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'Memory Utilization':
                suite.addTest(IES_Memory_utilization(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'Graphics':
                suite.addTest(Graphics(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'System':
                suite.addTest(System(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'App Launch Time':
                suite.addTest(IES_App_launch_time(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'Others':
                suite.addTest(Time_others(case.split(':')[1], device, serialno, testResult))
    print 'Performance cases: ',suite.countTestCases()
    return suite

if __name__ == '__main__':
     unittest.main()
