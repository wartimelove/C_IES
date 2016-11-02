import os
import unittest
from monkey_stress import MonkeyStress

def stressSuite(device=None, outputDir=None, debugFlag=True, serialno=None, testResult=None):
    suite = unittest.TestSuite()
    '''
    #suite.addTest(BluetoothStress('test_stress_bluetooth_on_off_50times',device,serialno,testResult))
    suite.addTest(CameraStress('test_stress_camera_front_record_720p_30mins_GH',device,serialno,testResult))
    suite.addTest(CameraStress('test_stress_camera_rear_take_picture_200times',device,serialno,testResult))
    #suite.addTest(CameraStress('test_stress_camera_rear_record_1080p_15mins',device,serialno,testResult))
    #suite.addTest(CameraStress('test_stress_camera_rear_record_720p_30mins',device,serialno,testResult))
    '''
#For test script development
    if debugFlag == True:
        product = device.getProduct()
        path = os.path.dirname(__file__)
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
            if case.split(':')[0] == 'Camera Stress':
                suite.addTest(CameraStress(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'Audio Stress':
                suite.addTest(AudioStress(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'Bluetooth Stress':
                suite.addTest(BluetoothStress(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'GFX Stress':
                suite.addTest(GFXStress(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'Wifi Stress':
                suite.addTest(WifiStress(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'ACPI Stress':
                suite.addTest(AcpiStress(case.split(':')[1], device, serialno, testResult))
            elif case.split(':')[0] == 'Monkey Stress':
                suite.addTest(MonkeyStress(case.split(':')[1], device, serialno, testResult))
     
    print 'Stress cases: ',suite.countTestCases()

    return suite
