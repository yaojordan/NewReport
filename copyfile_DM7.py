import time
import os
import datetime
import calendar
import sys
import shutil

if sys.argv[1] == "DM7" :
    FILE_PATH = "\\\\mtkteams\\sites\\DT\\DP2\\DM7\\DT_sharing\\Team Report\\Weekly Report\\"

    F_report = "_ASIP_Toolchain_Report.pptx"
    F_AI = "_ASIP_Toolchain_Report_AI.pptx"
    F_Modem = "_ASIP_Toolchain_Report_Modem.pptx"
    F_Open_Platform = "_ASIP_Toolchain_Report_Open_Platform.pptx"
    F_OP = "_ASIP_Toolchain_Report_Operation.pptx"

else :
    print "please set parameter DM7"
    exit(1)


cur_date = datetime.date.today()#.strftime("%Y%m%d")
cur_y = cur_date.strftime("%y")
cur_w = cur_date.isocalendar()
cur_w = cur_w[1]

after_7_date = datetime.date.today()+datetime.timedelta(days = 7)
y = after_7_date.strftime("%y")
w = after_7_date.isocalendar()
w = w[1]


def getfilelist():

    newFolder = copyFolder()

    file_list = []
    
    for dirPath, dirNames, fileNames in os.walk(newFolder):
        
        for f in fileNames:
            file_list.append(f)

    return file_list, newFolder


def copyFolder():
    #This should be executed before next week so that it can recognise current date.

    cur_folder = FILE_PATH+"W"+cur_y+str(cur_w).zfill(2)+"\\"
    new_folder = FILE_PATH+"W"+y+str(w).zfill(2)+"\\"

    print(cur_folder)
    print(new_folder)
    shutil.copytree(cur_folder, new_folder)

    return new_folder

def main():
  

    file_list, newFolder = getfilelist()

    for filename in file_list:
    
        if filename.endswith('Report.pptx'):
            os.rename(newFolder+filename, newFolder+after_7_date.strftime("%Y%m%d")+"_W"+y+str(w).zfill(2)+F_report)
        elif filename.endswith('AI.pptx'):
            os.rename(newFolder+filename, newFolder+after_7_date.strftime("%Y%m%d")+"_W"+y+str(w).zfill(2)+F_AI)
        elif filename.endswith('Modem.pptx'):
            os.rename(newFolder+filename, newFolder+after_7_date.strftime("%Y%m%d")+"_W"+y+str(w).zfill(2)+F_Modem)
        elif filename.endswith('Open_Platform.pptx'):
            os.rename(newFolder+filename, newFolder+after_7_date.strftime("%Y%m%d")+"_W"+y+str(w).zfill(2)+F_OP)
        elif filename.endswith('Operation.pptx'):
            os.rename(newFolder+filename, newFolder+after_7_date.strftime("%Y%m%d")+"_W"+y+str(w).zfill(2)+F_Open_Platform)

main()
