#python2.7
#2018-1-26 vend_dt076
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
	
	browser.get("http://mtkteams.mediatek.inc/sites/DT/DP2/DM7/DT_sharing/_layouts/15/listedit.aspx?List=%7B7B9BA546-5432-42F5-AC41-ECA6F60EAADA%7D")
	
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