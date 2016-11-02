#!/usr/bin/python

import os

from IESTestCase import IESTestCase
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

class artrage(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.ambientdesign.artrage/.MainActivity',
			artrage.__name__)


	def setUp(self):
		os.system('adb -s %s shell am start -n %s' % (self.serialno, self.className))
		MonkeyRunner.sleep(30)
		pass

class aviary(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.aviary.android.feather/.SplashScreenActivity',
			aviary.__name__)

	def _isAlive(self):
		procName = self.className.split('/')[0]
		lines = sorted(os.popen('adb -s %s shell procrank | grep %s | awk \'{print $6}\'' 
						% (self.serialno, procName)).readlines())

		print lines
		if len(lines) != 3:
			return False

		if procName + '\r\n' == lines[0] and procName + ':aviarycds\r\n' == lines[1] \
			 and procName + ':standalone\r\n' == lines[2] :
			return True

		return False

class esfileexplorer(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.estrongs.android.pop/.view.FileExplorerActivity',
			esfileexplorer.__name__)

	def _isAlive(self):
		procName = self.className.split('/')[0]
		lines = os.popen('adb -s %s shell procrank | grep %s | grep -v / | awk \'{print $6}\'' % (self.serialno, procName)).readlines()

		print lines
		if len(lines) != 1 :
			return False

		if procName + '\r\n' == lines[0] :
			return True

		return False

class foxitpdf(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.foxit.mobile.pdf.lite/com.foxit.filemanager.FM_MainActivity',
			foxitpdf.__name__)


class kno(IESTestCase):
	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.kno.textbooks/kno.textbooks.coursemanager.CourseListActivity',
			kno.__name__)

class labcam(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.labcam/.LabCamActivity',
			labcam.__name__)

class mcafee(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.wsandroid.suite.intelempg/com.mcafee.app.MainActivity',
			mcafee.__name__)

class mediacam(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.mediacam/.MediaCamActivity',
			mediacam.__name__)


class rar(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.rarlab.rar/.MainActivity', 
			rar.__name__)


class sparkvue(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.isbx.pasco.Spark/com.isbx.sparksandboxui.LaunchActivity', 
			sparkvue.__name__)


class pixlr(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.pixlr.oem.intel/com.pixlr.express.StartupActivity', 
			pixlr.__name__)

class sketchbook(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.adsk.sketchbook.oem.intel/com.adsk.sketchbook.SketchBook', 
			sketchbook.__name__)

class adobereader(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.adobe.reader/.AdobeReader', 
			adobereader.__name__)

class ierbundle(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.intel.ipls.ierbundle/.SplashScreen_Activity', 
			ierbundle.__name__)

class wps(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'cn.wps.moffice_eng/cn.wps.moffice.main.local.home.PadHomeActivity', 
			wps.__name__)

class vlc(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'org.videolan.vlc/.gui.MainActivity', 
			vlc.__name__)

class airwatch(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'cn.wps.moffice_eng/cn.wps.moffice.main.local.home.PadHomeActivity', 
			airwatch.__name__)

class netsupportstudent(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.netsupportsoftware.school.student.oem.intel/.IntelCheckActivity', 
			netsupportstudent.__name__)

class netsupporttutor(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.netsupportsoftware.school.tutor.oem.intel/com.netsupportsoftware.school.tutor.activity.IntelLicenseCheckActivity', 
			netsupporttutor.__name__)

class fluidmath(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.fluiditysoftware.fluidmath/.MainActivity', 
			fluidmath.__name__)

class td(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'com.intel.cmpc.td.agent/com.intel.cmpc.td.ui.MainActivity', 
			td.__name__)

class clm(IESTestCase):

	def __init__(self, methodName='runTest', device=None, serialno=None, testResult=None, resourcePath=None):
		IESTestCase.__init__(self, methodName, device, serialno, testResult, 
			'mythware.classroom.client/mythware.ux.student.form.MainActivity', 
			clm.__name__)
