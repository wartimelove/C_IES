#!/bin/bash

set +x
 
AdobeReader='com.adobe.reader'
Artrage='com.ambientdesign.artrage'
Aviary='com.aviary.android.feather'
CLM='mythware.classroom.client'
ESFileExplorer='com.estrongs.android.pop'
Foxit='com.foxit.mobile.pdf.lite'
IER='com.intel.ipls.ierbundle'
Kno='com.kno.textbooks'
LabCam='com.labcam'
McAfee='com.wsandroid.suite.intelempg'
MediaCam='com.mediacam'
Pixlr='com.pixlr.oem.intel'
RAR='com.rarlab.rar'
SketchBook='com.adsk.sketchbook.oem.intel'
SPARKvue='com.isbx.pasco.Spark'
TD='com.intel.cmpc.td.agent'
VLC='org.videolan.vlc'
WPS='cn.wps.moffice_eng'
NetSupportstudent='com.netsupportsoftware.school.student.oem.intel'
NetSupporttutor='com.netsupportsoftware.school.tutor.oem.intel'
FluidMath='com.fluiditysoftware.fluidmath'

bt_per_conf="performance/case_baytrail.txt"
bt_stress_conf="stress/case_baytrail.txt"
bt_version_conf="version/case_baytrail.txt"
fh_per_conf="performance/case_flaghill.txt"
fh_stress_conf="stress/case_flaghill.txt"
fh_version_conf="version/case_flaghill.txt"
gh_per_conf="performance/case_grandhill.txt"
gh_stress_conf="stress/case_grandhill.txt"
gh_version_conf="version/case_grandhill.txt"
mh_per_conf="performance/case_mounthill.txt"
mh_stress_conf="stress/case_mounthill.txt"
mh_version_conf="version/case_mounthill.txt"


check_module()
{
eval package=\$$1
echo  $package
adb shell pm list packages | grep $package
if [ $?  -eq 0 ];
then
	echo -e "\e[32m\e[1m$1 had been added!\e[0m"
	enable_case $1
else
	echo -e "\e[31m\e[1m$1 is  not install!\e[0m"
	disable_case $1
fi
}

disable_case()
{
	per_case_key=$1
	stress_case_key=$1
	version_case_key=$(echo $1 | tr [:upper:] [:lower:])
	sed -i "/$per_case_key/s/^/#/g" $bt_per_conf
	sed -i "/$stress_case_key/s/^/#/g" $bt_stress_conf
	sed -i "/$version_case_key/s/^/#/g" $bt_version_conf
	sed -i "/$per_case_key/s/^/#/g" $fh_per_conf
	sed -i "/$stress_case_key/s/^/#/g" $fh_stress_conf
	sed -i "/$version_case_key/s/^/#/g" $fh_version_conf
	sed -i "/$per_case_key/s/^/#/g" $gh_per_conf
	sed -i "/$stress_case_key/s/^/#/g" $gh_stress_conf
	sed -i "/$version_case_key/s/^/#/g" $gh_version_conf
	sed -i "/$per_case_key/s/^/#/g" $mh_per_conf
	sed -i "/$stress_case_key/s/^/#/g" $mh_stress_conf
	sed -i "/$version_case_key/s/^/#/g" $mh_version_conf
	echo "disable $per_case_key"
}

enable_case()
{
	per_case_key=$1
	stress_case_key=$1
	version_case_key=$(echo $1 | tr [:upper:] [:lower:])
	sed -i "/$per_case_key/s/#//g" $bt_per_conf
	sed -i "/$stress_case_key/s/#//g" $bt_stress_conf
	sed -i "/$version_case_key/s/#//g" $bt_version_conf
	sed -i "/$per_case_key/s/#//g" $fh_per_conf
	sed -i "/$stress_case_key/s/#//g" $fh_stress_conf
	sed -i "/$version_case_key/s/#//g" $fh_version_conf
	sed -i "/$per_case_key/s/#//g" $gh_per_conf
	sed -i "/$stress_case_key/s/#//g" $gh_stress_conf
	sed -i "/$version_case_key/s/#//g" $gh_version_conf
	sed -i "/$per_case_key/s/#//g" $mh_per_conf
	sed -i "/$stress_case_key/s/#//g" $mh_stress_conf
	sed -i "/$version_case_key/s/#//g" $mh_version_conf
	echo "enable $per_case_key"
	
}

check_module AdobeReader
check_module Artrage
check_module Aviary 
check_module CLM
check_module ESFileExplorer
check_module Foxit
check_module IER
check_module Kno
check_module LabCam
check_module McAfee 
check_module MediaCam
check_module Pixlr
check_module RAR
check_module SketchBook
check_module SPARKvue 
check_module TD
check_module VLC
check_module WPS
check_module NetSupportstudent
check_module NetSupporttutor
check_module FluidMath




