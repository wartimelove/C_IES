#!/usr/bin/python

import os
import unittest 
import traceback

from time import sleep
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

#NOTE: if not, show 'A new session could not be created' error
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class VLCFunctionTests(unittest.TestCase):

	TIME_PLAY	= 10
	TIME_SLEEP	= 5

	FILE_VIDEO		= 'Red Riding Hood - Trailer 2 (HD 1080p)'

	NAME_DIRETORIES		= 'Directories'
	NAME_SDCARD		= 'sdcard1'
	NAME_SDCARD_MUSIC	= 'Sleep Away.mp3'
	NAME_VIDEO		= 'Video'
	NAME_AUDIO		= 'Audio'
	NAME_SONGS		= 'SONGS'
	NAME_PLAY_ALL		= 'Play all'
	NAME_SETTINGS		= 'Settings'
	NAME_PLAY_AS_AUDIO	= 'Play as audio'

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'Baytrail_CR'
		desired_caps['appPackage'] = 'org.videolan.vlc'
		desired_caps['appActivity'] = '.gui.MainActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(15)

		try:
			print 'check the button Settings in the page during setUp'
			self.driver.find_element_by_name(VLCFunctionTests.NAME_SETTINGS)

			print 'choose the option Video in the page during setUp'
			self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO).click()

		except NoSuchElementException:
			pass
		

	def tearDown(self):
		self.driver.quit()
		pass

	def testPlayAudioIntheBackground(self):
		try:
			try:
				el = self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO)
			except NoSuchElementException:
				#NOTE: switch to the audio page
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO).click()

			self.driver.find_element_by_name('Mr. Scruff').click()
			self.driver.find_element_by_name('Ninja Tuna').click()


			#NOTE: wait to play the audio
			sleep(VLCFunctionTests.TIME_PLAY)

			#NOTE: check the play button 
			self.driver.find_element_by_id('org.videolan.vlc:id/header_play_pause')

			#NOTE: press the home key
			self.driver.press_keycode(3)


		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testAdjustVideoVolume(self):
		try:
			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO)
			except NoSuchElementException:
				#NOTE: switch to the audio page
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO).click()

			self.driver.find_element_by_name(VLCFunctionTests.FILE_VIDEO).click()
			sleep(VLCFunctionTests.TIME_SLEEP * 2)

			x = self.driver.get_window_size()['width'] // 4
			y = self.driver.get_window_size()['height'] // 4

			v = self.driver.find_element_by_id('org.videolan.vlc:id/subtitles_surface')
			print 'click the Button OK to destroy the dialog'
			self.driver.tap([(x * 2 + 20, v.location['y'])])
			sleep(VLCFunctionTests.TIME_SLEEP)

			self.driver.swipe(3*x, y, 3*x, 3*y, 0)

			#NOTE: wait for the hardware
			sleep(VLCFunctionTests.TIME_SLEEP)

			v0 = int(self._getVolume())

			self.driver.swipe(3*x, 3*y, 3*x, 2*y, 0)

			#NOTE: wait for the hardware
			sleep(VLCFunctionTests.TIME_SLEEP)

			v1 = int(self._getVolume())

			self.assertGreater(v1, v0)


		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testAdjustVideoBrightness(self):
		try:
			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO)
			except NoSuchElementException:
				#NOTE: switch to the audio page
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO).click()

			self.driver.find_element_by_name(VLCFunctionTests.FILE_VIDEO).click()
			sleep(VLCFunctionTests.TIME_SLEEP * 2)

			x = self.driver.get_window_size()['width'] // 4 
                        y = self.driver.get_window_size()['height'] // 4                                                             

			v = self.driver.find_element_by_id('org.videolan.vlc:id/subtitles_surface')
			print 'click the Button OK to destroy the dialog'
			self.driver.tap([(x * 2 + 20, v.location['y'])])
			sleep(VLCFunctionTests.TIME_SLEEP)

                        self.driver.swipe(x, y, x, 3*y, 0)

                        #NOTE: wait for the hardware              
                        sleep(VLCFunctionTests.TIME_SLEEP)

                        b0 = int(self._getBrightness())
 
                        self.driver.swipe(x, 3*y, x, 2*y, 0)

                        #NOTE: wait for the hardware              
                        sleep(VLCFunctionTests.TIME_SLEEP)             
                        
                        b1 = int(self._getBrightness())               
                                                                  
                        self.assertGreater(b1, b0)            

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testAudioPlayPauseResumeSeek(self):
		try:
			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO)
			except NoSuchElementException:
				#NOTE: switch to the audio page
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO).click()

			print 'play the audio'
			self.driver.find_element_by_name('Mr. Scruff').click()
			self.driver.find_element_by_name('Ninja Tuna').click()
			sleep(VLCFunctionTests.TIME_PLAY)

			try:
				self.driver.find_element_by_id('org.videolan.vlc:id/okgotit_button').click()
				sleep(VLCFunctionTests.TIME_SLEEP)
			except:
				pass

			print 'pause the audio'
			self.driver.find_element_by_id('org.videolan.vlc:id/header_play_pause').click()
			t0 = self.driver.find_element_by_id('org.videolan.vlc:id/header_time').text
			print 'time', t0
			sleep(VLCFunctionTests.TIME_SLEEP)

			print 'resume the audio'
			self.driver.find_element_by_id('org.videolan.vlc:id/header_play_pause').click()
			sleep(VLCFunctionTests.TIME_PLAY)
			t1 = self.driver.find_element_by_id('org.videolan.vlc:id/header_time').text
			print 'time', t1
			self.assertNotEqual(t0, t1)

			print 'seek the audio'
			self.driver.find_element_by_id('org.videolan.vlc:id/header').click()
			sleep(VLCFunctionTests.TIME_SLEEP)

			print 'click the middle of the screen'
			w = self.driver.get_window_size()['width'];
			h = self.driver.get_window_size()['height'];
			self.driver.tap([(w // 2, h // 2),])
			sleep(VLCFunctionTests.TIME_SLEEP)

			bar = self.driver.find_element_by_id('org.videolan.vlc:id/timeline') 
			self.driver.tap([(bar.location['x'] + bar.size['width'] // 2, bar.location['y'] + bar.size['height']//2),])
			sleep(VLCFunctionTests.TIME_PLAY)

			self.driver.find_element_by_id('org.videolan.vlc:id/play_pause').click()

			t2 = self.driver.find_element_by_id('org.videolan.vlc:id/time').text
			print 'time', t2
			self.assertNotEqual(t1, t2)

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testVideoPlayPauseResumeSeek(self):
		try:
			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO)
			except NoSuchElementException:
				#NOTE: switch to the video page
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO).click()
				
			self.driver.find_element_by_name(VLCFunctionTests.FILE_VIDEO).click()

			#NOTE: for the tips
			self.driver.tap([(100, 100),])

			self.driver.find_element_by_id('org.videolan.vlc:id/player_overlay_play').click()

			t0 = self.driver.find_element_by_id('org.videolan.vlc:id/player_overlay_time').text
			bar = self.driver.find_element_by_id('org.videolan.vlc:id/player_overlay_seekbar')
			#NOTE: seek the video
			self.driver.tap([(bar.size['width'] // 2, bar.location['y'] + bar.size['height'] // 2),])
			t1 = self.driver.find_element_by_id('org.videolan.vlc:id/player_overlay_time').text

			self.assertNotEqual(t0, t1)

			self.driver.find_element_by_id('org.videolan.vlc:id/player_overlay_play').click()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testPlayMediaFileIntheRemovableDevice(self):
		try:
			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_DIRETORIES)
			except NoSuchElementException:
				#NOTE: switch to the directory page
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_DIRETORIES).click()

			self.driver.find_element_by_name(VLCFunctionTests.NAME_SDCARD).click()
			self.driver.find_element_by_name(VLCFunctionTests.NAME_SDCARD_MUSIC).click()
			self.driver.find_element_by_id('org.videolan.vlc:id/artist')

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testPreviousNextSongFastForwardFastBackward(self):
		try:
			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO)
			except NoSuchElementException:
				#NOTE: switch to the directory page
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO).click()

			print 'click the item \'', VLCFunctionTests.NAME_SONGS, '\''
			self.driver.find_element_by_name(VLCFunctionTests.NAME_SONGS).click()

			print 'click the item more'
			self.driver.find_element_by_id('org.videolan.vlc:id/item_more').click()

			print 'click the button \'', VLCFunctionTests.NAME_PLAY_ALL, '\''
			self.driver.find_element_by_name(VLCFunctionTests.NAME_PLAY_ALL).click()
			self.driver.find_element_by_id('org.videolan.vlc:id/artist').click()

			t0 = self.driver.find_element_by_id('org.videolan.vlc:id/artist').text
			print 'artist', t0

			print 'destroy the dialog \'dismiss\''
			w = self.driver.get_window_size()['width']
			h = self.driver.get_window_size()['height']
			self.driver.tap([(w // 2, h // 2),])
			sleep(VLCFunctionTests.TIME_SLEEP)

			print 'click the next button'
			self.driver.find_element_by_id('org.videolan.vlc:id/next').click()
			sleep(VLCFunctionTests.TIME_PLAY)
			t1 = self.driver.find_element_by_id('org.videolan.vlc:id/artist').text
			print 'artist', t1
			
			self.assertNotEqual(t1, t0)

			self.driver.find_element_by_id('org.videolan.vlc:id/previous').click()
			sleep(VLCFunctionTests.TIME_SLEEP)
			t1 = self.driver.find_element_by_id('org.videolan.vlc:id/artist').text

			self.assertEqual(t1, t0)

			print 'play the song fast forward'
			t0 = self.driver.find_element_by_id('org.videolan.vlc:id/time').text
			print 'time', t0

			elNext = self.driver.find_element_by_id('org.videolan.vlc:id/next')
			wNext = elNext.size['width']
			hNext = elNext.size['height']
			self.driver.tap([(elNext.location['x'] + wNext // 2, elNext.location['y'] + hNext // 2),], 3000)
	
			t1 = self.driver.find_element_by_id('org.videolan.vlc:id/time').text
			print 'time', t1
			self.assertNotEqual(t0, t1)

			print 'click the next button'
			elNext.click()
			sleep(VLCFunctionTests.TIME_SLEEP)

			self.driver.tap([(elNext.location['x'] + wNext // 2, elNext.location['y'] + hNext // 2),], 3000)
			sleep(VLCFunctionTests.TIME_SLEEP)
			t0 = self.driver.find_element_by_id('org.videolan.vlc:id/time').text
			print 'time', t0

			print 'play the song fast backward'
			elPre = self.driver.find_element_by_id('org.videolan.vlc:id/previous')
			wPre = elPre.size['width']
			hPre = elPre.size['height']
			self.driver.tap([(elPre.location['x'] + wPre // 2, elPre.location['y'] + hPre // 2),], 3000)

			t1 = self.driver.find_element_by_id('org.videolan.vlc:id/time').text
			print 'time', t1
			self.assertNotEqual(t0, t1)

		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testPlayAudioAndEnterSuspend(self):
		try:
			try:
				el = self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO)
			except NoSuchElementException:
				#NOTE: switch to the audio page
				print 'switch to the page Audio'
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO).click()

			self.driver.find_element_by_name('Mr. Scruff').click()
			self.driver.find_element_by_name('Ninja Tuna').click()


			#NOTE: wait to play the audio
			sleep(VLCFunctionTests.TIME_PLAY)

			#NOTE: check the play button 
			self.driver.find_element_by_id('org.videolan.vlc:id/header_play_pause')

			self._suspendAndResume()

			self.driver.find_element_by_name('Mr. Scruff')


		except NoSuchElementException:
			self.fail(traceback.format_exc())


	def testPlayVideoAndEnterSuspend(self):
		try:

			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO)
			except NoSuchElementException:
				#NOTE: switch to the audio page
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO).click()

			print 'play the video'
			self.driver.find_element_by_name(VLCFunctionTests.FILE_VIDEO).click()

			print 'sleep 10 seconds'
			sleep(10)

			self._suspendAndResume()

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testPlayAudioAndForceStop(self):
		try:
			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO)
			except NoSuchElementException:
				#NOTE: switch to the audio page
				print 'switch to the page Audio'
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO).click()

			self.driver.find_element_by_name('Mr. Scruff').click()
			self.driver.find_element_by_name('Ninja Tuna').click()


			#NOTE: wait to play the audio
			sleep(VLCFunctionTests.TIME_PLAY)

			#NOTE: check the play button 
			self.driver.find_element_by_id('org.videolan.vlc:id/header_play_pause')

			print 'kill the self\'s proc'
			os.system('pid=`adb shell ps | grep  org.videolan.vlc | awk \'{print $2}\'` && adb shell kill $pid')
			sleep(VLCFunctionTests.TIME_SLEEP)
			self.driver.find_element_by_id('com.android.launcher:id/search_button_container')

			print 'start the self\'s proc'
			os.system('adb shell am start org.videolan.vlc/.gui.MainActivity')
			sleep(VLCFunctionTests.TIME_SLEEP)

			self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
			self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO)


		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def testPlayAsAudio(self):
		try:
			try:
				self.driver.find_element_by_name(VLCFunctionTests.NAME_VIDEO)

			except NoSuchElementException:
				print 'switch to the page Video'
				self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
				self.driver.find_element_by_name(VLCFunctionTests.NAME_AUDIO).click()

			self.driver.find_element_by_name(VLCFunctionTests.FILE_VIDEO)

			print 'click the more item'
			self.driver.find_element_by_id('org.videolan.vlc:id/item_more').click()

			print 'click the item "', VLCFunctionTests.NAME_PLAY_AS_AUDIO, '"'
			self.driver.find_element_by_name(VLCFunctionTests.NAME_PLAY_AS_AUDIO).click()
			self.driver.tap([(self.driver.get_window_size()['width']//2, self.driver.get_window_size()['height']//2),])

			el = self.driver.find_element_by_id('org.videolan.vlc:id/header_time')
			time1 = el.text
			sleep(VLCFunctionTests.TIME_PLAY)
			time2 = el.text
			print time1, time2
			self.assertNotEqual(time1, time2)

		except NoSuchElementException:
			self.fail(traceback.format_exc())

	def _suspendAndResume(self):
		print 'suspend with the command \"adb shell \'echo mem >/sys/power/state\'\" '
		os.system('adb shell \'echo mem >/sys/power/state\'')

		print 'wait 10 seconds to suspend'
		sleep(10)

		print 'resume with the command \"adb shell \'echo on >/sys/power/state\'\" '
		os.system('adb shell \'echo on >/sys/power/state\'')

		print 'wait 10 seconds to resume'
		sleep(VLCFunctionTests.TIME_PLAY)


	def _getBrightness(self):
		line = os.popen('adb shell dumpsys display | grep mScreenBrightness=').readlines()[0]
		return line.split('=')[1]


	def _getVolume(self):
		return os.popen('adb shell dumpsys audio | grep speaker | awk \'{print $7}\' | cut -d , -f 1').readlines()[2]


