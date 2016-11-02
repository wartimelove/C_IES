#!/usr/bin/python

import unittest
import os
from ies_class import kno, sparkvue, rar, labcam, aviary, esfileexplorer, mediacam, mcafee, artrage, foxitpdf, pixlr, sketchbook, adobereader, ierbundle, wps, vlc, netsupportstudent, netsupporttutor, fluidmath, td, clm

def ies_apps_suite(device=None, outputDir=None, debugFlag=True, serialno=None, testResult=None):
	suite = unittest.TestSuite()
	test_cases = []

	if debugFlag == True:
		product = device.getProduct()
		path = os.path.dirname(__file__)
		print product, path

		if product == 'grandhill':
			f = open(path + os.sep + 'case_grandhill.txt')
		if product == 'flaghill':
			f = open(path + os.sep + 'case_flaghill.txt')
		if product == 'baytrail':
			f = open(path + os.sep + 'case_baytrail.txt')
		if product == 'mounthill':
			f = open(path + os.sep + 'case_mounthill.txt')

		test_cases = f.readlines()
		f.close()

	for i in range(len(test_cases)):
		case = test_cases[i].strip()

		if case != '' and case[0] != '#' and case.split(':')[0] == 'kno':
			suite.addTest(kno(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'sparkvue':
			suite.addTest(sparkvue(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'rar':
			suite.addTest(rar(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'labcam':
			suite.addTest(labcam(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'aviary':
			suite.addTest(aviary(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'esfileexplorer':
			suite.addTest(esfileexplorer(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'mediacam':
			suite.addTest(mediacam(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'mcafee':
			suite.addTest(mcafee(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'artrage':
			suite.addTest(artrage(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'pixlr':
			suite.addTest(pixlr(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'sketchbook':
			suite.addTest(sketchbook(case.split(':')[1], device, serialno, testResult))
		
		if case != '' and case[0] != '#' and case.split(':')[0] == 'ierbundle':
			suite.addTest(ierbundle(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'adobereader':
			suite.addTest(adobereader(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'netsupportstudent':
			suite.addTest(netsupportstudent(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'netsupporttutor':
			suite.addTest(netsupporttutor(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'foxitpdf':
			suite.addTest(foxitpdf(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'wps':
			suite.addTest(wps(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'fluidmath':
			suite.addTest(fluidmath(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'vlc':
			suite.addTest(vlc(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'td':
			suite.addTest(td(case.split(':')[1], device, serialno, testResult))

		if case != '' and case[0] != '#' and case.split(':')[0] == 'clm':
			suite.addTest(clm(case.split(':')[1], device, serialno, testResult))

	print 'ies_apps_suite cases:', suite.countTestCases()
	return suite

if __name__ == 'main':
	unittest.main()
