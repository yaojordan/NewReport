#python2.7
#2018-1-26 
import sys
import time
from selenium import webdriver

#Use Chrome driver connect to TeamReport settings
chromeDriver = "C:\Python27\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(chromeDriver)


def versionSetting():
	
	requireCheckoutNo = browser.find_element_by_id("onetidFCheckoutEnabledNo")
	requireCheckoutYes = browser.find_element_by_id("onetidFCheckoutEnabledYes")
	ok = browser.find_element_by_id("onetidCreateList")
	cancel = browser.find_element_by_id("onetidClose")
	

	if sys.argv[1] == "ChangeSet":
		requireCheckoutNo.click()
	elif sys.argv[1] == "Done":
		requireCheckoutYes.click()
	else:
		print "Error argv, please check!"
		exit(1)
		
	ok.click()
	
	
def main():
	
	browser.get("YOUR_URL")
	
	time.sleep(3)
	versionSet = browser.find_element_by_id("ctl00_PlaceHolderMain_ctl09_RptControls_onetidListEdit1")
	versionSet.click()
	versionSetting()

try:	
	main()
	browser.quit()
except Exception as e:
	print e
	exit(1)
