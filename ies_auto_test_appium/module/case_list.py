import os,sys
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
from module.bat import *
from module.sparkvue import *
from module.labcam import *
from module.fluidmath import *
from module.kno import *
from module.rar import *
from module.es import *
from module.mcafee import *
from module.netsupport import *
from module.vlc import *
from module.pixlr import *
from module.sketchbook import *

reload(sys)
sys.setdefaultencoding('utf8')

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#case1 = unittest.TestLoader().loadTestsFromTestCase(SketchBookTests)
#case2 = unittest.TestLoader().loadTestsFromTestCase(TDTests)
#case3 = unittest.TestLoader().loadTestsFromTestCase(KnoTests)
#case4 = unittest.TestLoader().loadTestsFromTestCase(VLCTests)
#case5 = unittest.TestLoader().loadTestsFromTestCase(LabCamTests)
#case6 = unittest.TestLoader().loadTestsFromTestCase(RARTests)
#case7 = unittest.TestLoader().loadTestsFromTestCase(MythwareTests)
#case8 = unittest.TestLoader().loadTestsFromTestCase(McAfeeTests)
#case9 = unittest.TestLoader().loadTestsFromTestCase(PixlrTests)
#case10 = unittest.TestLoader().loadTestsFromTestCase(ESFileExplorerTests)
#case11 = unittest.TestLoader().loadTestsFromTestCase(StudentTests)
#case12 = unittest.TestLoader().loadTestsFromTestCase(FluidMathTests)
#case13 = unittest.TestLoader().loadTestsFromTestCase(SparkvueTests)
#case14 = unittest.TestLoader().loadTestsFromTestCase(FrontTimeLapseTests)
#case15 = unittest.TestLoader().loadTestsFromTestCase(FrontKinematicsTests)
#case16 = unittest.TestLoader().loadTestsFromTestCase(FrontMicroscopeTests)
#case17 = unittest.TestLoader().loadTestsFromTestCase(FrontUniversalLoggerTests)
#case18 = unittest.TestLoader().loadTestsFromTestCase(FrontPathfinderTests)
#case19 = unittest.TestLoader().loadTestsFromTestCase(RearTimeLapseTests)
#case20 = unittest.TestLoader().loadTestsFromTestCase(RearKinematicsTests)
#case21 = unittest.TestLoader().loadTestsFromTestCase(RearMicroscopeTests)
#case22 = unittest.TestLoader().loadTestsFromTestCase(RearUniversalLoggerTests)
#case23 = unittest.TestLoader().loadTestsFromTestCase(RearPathfinderTests)
#case24 = unittest.TestLoader().loadTestsFromTestCase(SuspendTimeLapseTests)
#case25 = unittest.TestLoader().loadTestsFromTestCase(SuspendKinematicsTests)
#case26 = unittest.TestLoader().loadTestsFromTestCase(SuspendMicroscopeTests)
#case27 = unittest.TestLoader().loadTestsFromTestCase(SuspendUniversalLoggerTests)
#case28 = unittest.TestLoader().loadTestsFromTestCase(SuspendPathfinderTests)
#case29 = unittest.TestLoader().loadTestsFromTestCase(ForcestopTimeLapseTests)
#case30 = unittest.TestLoader().loadTestsFromTestCase(ForcestopKinematicsTests)
##case31 = unittest.TestLoader().loadTestsFromTestCase(ForcestopSparkvueTests('test_forcestop_sparkvue'))
##case32 = unittest.TestLoader().loadTestsFromTestCase(NormallaunchSparkvueTests)
##case33 = unittest.TestLoader().loadTestsFromTestCase(FrontCameraSparkvueTests)
##case34 = unittest.TestLoader().loadTestsFromTestCase(RearCameraSparkvueTests)
##case35 = unittest.TestLoader().loadTestsFromTestCase(LightSparkvueTests)
##case36 = unittest.TestLoader().loadTestsFromTestCase(SoundSparkvueTests)
##case37 = unittest.TestLoader().loadTestsFromTestCase(SuspendSparkvueMainUITests)
##case38 = unittest.TestLoader().loadTestsFromTestCase(SuspendSparkvueDataTests)
#case39 = unittest.TestLoader().loadTestsFromTestCase(SwitchLanguageFluidMathTests)
#case40 = unittest.TestLoader().loadTestsFromTestCase(SuspendFluidMathTests)
#case41 = unittest.TestLoader().loadTestsFromTestCase(LoginFluidMathTests)
#case42 = unittest.TestLoader().loadTestsFromTestCase(TapFluidMathTests)
#case43 = unittest.TestLoader().loadTestsFromTestCase(EquationFluidMathTests)

bat = unittest.TestSuite()
#bat.addTest(SketchBookTests('testsketchbook'))
#bat.addTest(TDTests('testtd'))
#bat.addTest(KnoTests('testkno'))
#bat.addTest(VLCTests('testvlc'))
#bat.addTest(LabCamTests('testlabcam'))
#bat.addTest(RARTests('testrar'))
#bat.addTest(MythwareTests('testmythware'))
#bat.addTest(McAfeeTests('testmcafee'))
bat.addTest(ESFileExplorerTests('testesfileexplorer'))
#bat.addTest(StudentTests('teststudent'))
#bat.addTest(FluidMathTests('testfluidmath'))
#bat.addTest(SparkvueTests('testsparkvue'))

labcam = unittest.TestSuite()
labcam.addTest(LabcamFunctionTests('testtimelapsefront'))
labcam.addTest(LabcamFunctionTests('testkinematicsfront'))
labcam.addTest(LabcamFunctionTests('testmicroscopefront'))
labcam.addTest(LabcamFunctionTests('testuniversalloggerfront'))
labcam.addTest(LabcamFunctionTests('testpathfinderfront'))
labcam.addTest(LabcamFunctionTests('testtimelapserear'))
labcam.addTest(LabcamFunctionTests('testkinematicsrear'))
labcam.addTest(LabcamFunctionTests('testmicroscoperear'))
labcam.addTest(LabcamFunctionTests('testuniversalloggerrear'))
labcam.addTest(LabcamFunctionTests('testpathfinderrear'))
#labcam.addTest(LabcamFunctionTests('testtimelapsesuspend'))
#labcam.addTest(LabcamFunctionTests('testkinematicssuspend'))
#labcam.addTest(LabcamFunctionTests('testmicroscopesuspend'))
#labcam.addTest(LabcamFunctionTests('testuniversalloggersuspend'))
#labcam.addTest(LabcamFunctionTests('testpathfindersuspend'))
labcam.addTest(LabcamFunctionTests('testtimelapseforcestop'))
labcam.addTest(LabcamFunctionTests('testkinematicsforcestop'))

sparkvue = unittest.TestSuite()
sparkvue.addTest(SparkvueFunctionTests('testforcestop'))
sparkvue.addTest(SparkvueFunctionTests('testlaunch'))
sparkvue.addTest(SparkvueFunctionTests('testfrontcamera'))
sparkvue.addTest(SparkvueFunctionTests('testrearcamera'))
sparkvue.addTest(SparkvueFunctionTests('testlight'))
sparkvue.addTest(SparkvueFunctionTests('testsound'))
#sparkvue.addTest(SparkvueFunctionTests('testsuspendmainui'))
#sparkvue.addTest(SparkvueFunctionTests('testsuspenddata'))

fluidmath = unittest.TestSuite()
fluidmath.addTest(FluidmathFunctionTests('testswitchlanguage'))
#fluidmath.addTest(FluidmathFunctionTests('testsuspend'))
fluidmath.addTest(FluidmathFunctionTests('testlogin'))
#fluidmath.addTest(FluidmathFunctionTests('testtap'))
#fluidmath.addTest(FluidmathFunctionTests('testequation'))


kno = unittest.TestSuite()
kno.addTest(KnoFunctionTests('testSignIn'))
kno.addTest(KnoFunctionTests('testViewNexPagePreviousPage'))
kno.addTest(KnoFunctionTests('testHighlightText'))
kno.addTest(KnoFunctionTests('testAddNote'))
kno.addTest(KnoFunctionTests('testEnterIntoTheKNOStore'))
kno.addTest(KnoFunctionTests('testCheckCoversInMainUI'))
kno.addTest(KnoFunctionTests('testInsertPictureOrVideoNotesFromES'))
kno.addTest(KnoFunctionTests('testKnoWillCrashWhenSelectTextAndSearch'))
#kno.addTest(KnoFunctionTests('testReadBookAndEnterSuspend'))
#kno.addTest(KnoFunctionTests('testMainUIAndEnterSuspend'))
kno.addTest(KnoFunctionTests('testReadBookAndForceStop'))

mcafee = unittest.TestSuite()
mcafee.addTest(McafeeFunctionTests('testAutoLaunch'))
mcafee.addTest(McafeeFunctionTests('testManualScanDevice'))
mcafee.addTest(McafeeFunctionTests('testManualScanDeviceAndTapBackButton'))
mcafee.addTest(McafeeFunctionTests('testManualUpdateMcAfee'))
mcafee.addTest(McafeeFunctionTests('testAutoUpdateMcAfee'))
mcafee.addTest(McafeeFunctionTests('testManualScanDeviceAndTapHomeButton'))
#mcafee.addTest(McafeeFunctionTests('testManualUpdateMcafeeAndEnterSuspend'))
#mcafee.addTest(McafeeFunctionTests('testManualScanDeviceAndEnterSuspend'))
mcafee.addTest(McafeeFunctionTests('testManualScanDeviceAndForceStop'))

es = unittest.TestSuite()
es.addTest(ESFunctionTests('testReadDocument'))
es.addTest(ESFunctionTests('testCopyCutFunction'))
es.addTest(ESFunctionTests('testShowHideFile'))
es.addTest(ESFunctionTests('testLocalFilesShow'))
es.addTest(ESFunctionTests('testAddShortcutIcontoHomeScreen'))
#es.addTest(ESFunctionTests('testMainUIAndEnterSuspend'))
es.addTest(ESFunctionTests('testMainUIAndForceStop'))
es.addTest(ESFunctionTests('testBackupApp'))

vlc = unittest.TestSuite()
vlc.addTest(VLCFunctionTests('testPlayAudioIntheBackground'))
vlc.addTest(VLCFunctionTests('testAdjustVideoVolume'))
vlc.addTest(VLCFunctionTests('testAdjustVideoBrightness'))
vlc.addTest(VLCFunctionTests('testAudioPlayPauseResumeSeek'))
vlc.addTest(VLCFunctionTests('testVideoPlayPauseResumeSeek'))
vlc.addTest(VLCFunctionTests('testPlayMediaFileIntheRemovableDevice'))
vlc.addTest(VLCFunctionTests('testPreviousNextSongFastForwardFastBackward'))
#vlc.addTest(VLCFunctionTests('testPlayAudioAndEnterSuspend'))
#vlc.addTest(VLCFunctionTests('testPlayVideoAndEnterSuspend'))
vlc.addTest(VLCFunctionTests('testPlayAudioAndForceStop'))
vlc.addTest(VLCFunctionTests('testPlayAsAudio'))

rar = unittest.TestSuite()
rar.addTest(RARFunctionTests('testExtracttheArchive'))
rar.addTest(RARFunctionTests('testZipFormat'))
rar.addTest(RARFunctionTests('testRarFormat'))
rar.addTest(RARFunctionTests('testRar4xFormat'))
#rar.addTest(RARFunctionTests('testArchiveFileAndEnterSuspend'))
rar.addTest(RARFunctionTests('testArchiveFilesAndForceStop'))

netsupport = unittest.TestSuite()
netsupport.addTest(NetsupportFunctionTests('testChatWithTutor'))
netsupport.addTest(NetsupportFunctionTests('testDisconnectFromTutor'))
netsupport.addTest(NetsupportFunctionTests('testSurveyMode'))
netsupport.addTest(NetsupportFunctionTests('testLockAndUnlock'))
netsupport.addTest(NetsupportFunctionTests('testStudentDisableWifiWhenConnectToTutor'))
netsupport.addTest(NetsupportFunctionTests('testStudentDisableWifiWhenSurvey'))
netsupport.addTest(NetsupportFunctionTests('testFileTransfer'))
netsupport.addTest(NetsupportFunctionTests('testStudentDisableWifiWhenFileTransfer'))
#netsupport.addTest(NetsupportFunctionTests('testEnterSuspendWhileSurvey'))
netsupport.addTest(NetsupportFunctionTests('testFileTransferAndForceClose'))

sketchbook = unittest.TestSuite()
sketchbook.addTest(SketchBookFunctionTests('testImportImage'))
sketchbook.addTest(SketchBookFunctionTests('testNewSketch'))
sketchbook.addTest(SketchBookFunctionTests('testDrawAndSave'))
sketchbook.addTest(SketchBookFunctionTests('testNewFromCamera'))
sketchbook.addTest(SketchBookFunctionTests('testAddAndHideTheLayer'))
#sketchbook.addTest(SketchBookFunctionTests('testEditModeAndEnterSuspend'))
#sketchbook.addTest(SketchBookFunctionTests('testMainUIAndSuspend'))
sketchbook.addTest(SketchBookFunctionTests('testEditModeAndForceStop'))


pixlr = unittest.TestSuite()
pixlr.addTest(PixlrFunctionTests('testCollage'))
pixlr.addTest(PixlrFunctionTests('testAddText'))
pixlr.addTest(PixlrFunctionTests('testAddBorders'))
pixlr.addTest(PixlrFunctionTests('testPhotoAdjustment'))
pixlr.addTest(PixlrFunctionTests('testTakeAndViewAPhoto'))
#pixlr.addTest(PixlrFunctionTests('testEditModeAndEnterSuspend'))
#pixlr.addTest(PixlrFunctionTests('testMainUIAndEnterSuspend'))
pixlr.addTest(PixlrFunctionTests('testEditModeAndForceStop'))

#labcam = unittest.TestSuite()
#labcam.addTest(SparkvueFunctionTests('test_forcestop_sparkvue'))
#
#bat = unittest.TestSuite([case1,case3,case4,case5,case6,case7,case8,case9,case10,case11,case13])
##func = unittest.TestSuite([case14,case15,case16,case17, case18,\
##    			case19,case20,case21,case22,case23,\
##    			case24,case25,case26,case27,case28,case29,case30,\
##    			case31,case32,case33,case34,case35,case36,case37,case38,\
##    			case39,case40,case41,case42])   
##labcam = unittest.TestSuite([case14])
##labcam = unittest.TestSuite([case14,case15,case16,case17, case18,\
##    			case19,case20,case21,case22,case23,\
##    			case24,case25,case26,case27,case28,case29,case30])   
##sparkvue = unittest.TestSuite([case31,case32,case33,case34,case35,case36,case37,case38])
##sparkvue = unittest.TestSuite([case14,sparkvue])
#fluidmath = unittest.TestSuite([case39,case40,case41])
#test = unittest.TestSuite([case12,case39,case40,case41])
#
#
