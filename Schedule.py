from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import os.path
import getpass


def daySelector(int):

    DoW = "win0divDAY_OF_WEEK_DESCR$" + str(int)
    date = "win0divAF_SM_MYSCH_WRK_AF_SHIFT_ST_DT$" + str(int)
    Start = "win0divAF_SCHED_CUR_VW_START_TIME$" + str(int)
    End = "win0divAF_SCHED_CUR_VW_END_TIME$" + str(int)
    day = driver.find_element_by_id(DoW).text 
    Date = driver.find_element_by_id(date).text
    dayStart = driver.find_element_by_id(Start).text
    if dayStart == "   ":
       return
    dayEnd = driver.find_element_by_id(End).text
    dayString = "{} {}: {} - {}".format(day, Date, dayStart, dayEnd)
    days.append(dayString) 
    makeEvent(Date, dayStart, dayEnd)

def makeEvent(date, timeStart, timeEnd):
      time.sleep(3)
      sendC = "c"

      action = webdriver.common.action_chains.ActionChains(driver2)
      action1 = webdriver.common.action_chains.ActionChains(driver2)
      action2 = webdriver.common.action_chains.ActionChains(driver2)
      action3 = webdriver.common.action_chains.ActionChains(driver2)
      action4 = webdriver.common.action_chains.ActionChains(driver2)
      action5 = webdriver.common.action_chains.ActionChains(driver2)
      action6 = webdriver.common.action_chains.ActionChains(driver2)
      action7 = webdriver.common.action_chains.ActionChains(driver2)

      create = driver2.find_element_by_id("topcontainerwk")
      create.send_keys(sendC)
      action.perform()

      action1.send_keys('Hollister')
      action1.perform()
      time.sleep(1)

      action2.send_keys(Keys.TAB)
      action2.send_keys(date)
      action2.perform()
      time.sleep(1)

      action3.send_keys(Keys.TAB)
      action3.send_keys(timeStart)
      action3.perform()
      time.sleep(1)

      action4.send_keys(Keys.TAB)
      action4.send_keys(timeEnd)
      action2.send_keys('c')
      action4.perform()
      calander = driver2.find_element_by_class_name("ep-dp-calendar-sel")
      time.sleep(1)

      action5.move_to_element(calander).click()
      action5.send_keys(Keys.ARROW_DOWN)
      action5.send_keys(Keys.ENTER)
      action5.perform()
      time.sleep(1)

      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.send_keys(Keys.TAB)
      action6.perform()
      time.sleep(10)

      action7.send_keys(Keys.ENTER)
      action7.perform()
      time.sleep(10)

  
en = input("Employee Number: ")
pas = getpass.getpass("Password: ")
gm = input("Gmail email: ")
gmpas = getpass.getpass("Password: ")

vis = input("Do you want to watch? Y/N: ")
 
driver = webdriver.Chrome() if vis == 'y' else webdriver.PhantomJS(executable_path=r'C:\Python\phantomJS\bin\phantomjs.exe')
driver2 = webdriver.Chrome() if vis == 'y' else webdriver.PhantomJS(executable_path=r'C:\Python\phantomJS\bin\phantomjs.exe')

driver.get("https://my.anfcorp.com/psp/hrprd/EXTERNAL/?&cmd=login&languageCd=ENG")
driver2.get("https://calendar.google.com")
userID = driver.find_element_by_name("userid")
email = driver2.find_element_by_name("Email")
userID.send_keys(en)
email.send_keys(gm) 
email.send_keys(Keys.RETURN)
time.sleep(1)
pwd = driver.find_element_by_name("pwd")
pwd.send_keys(pas)
passwd = driver2.find_element_by_name("Passwd")
passwd.send_keys(gmpas)
passwd.send_keys(Keys.RETURN)
userID.send_keys(Keys.RETURN)
driver.get("https://my.anfcorp.com/psp/hrprd/EXTERNAL/HRMS/c/AF_SM_MENU.AF_SM_VIEWMYSCHED.GBL?PORTALPARAM_PTCNAV=AF_SM_VIEWMYSCHED_GBL&EOPP.SCNode=HRMS&EOPP.SCPortal=EXTERNAL&EOPP.SCName=AFHR_AF_HR_EXT_HMPG&EOPP.SCLabel=Personal Information&EOPP.SCPTcname=&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.AF_TIME_AND_ATTENDANCE.AF_SM_VIEWMYSCHED_GBL&IsFolder=false")
driver.implicitly_wait(5)
driver.switch_to.frame("TargetContent")
driver.find_element_by_name("AF_SM_MYSCH_WRK_NEXT_WK_BTN").click()
time.sleep(1) # wait for the page to load the next week
#driver2.find_element_by_class_name("goog-imageless-button-content").click()

if driver.find_elements(By.ID,'win0divAF_SM_MYSCH_WRK_AF_SCHEDULED_HRS'):
   sch_hours = driver.find_element_by_id("win0divAF_SM_MYSCH_WRK_AF_SCHEDULED_HRS").text

   if sch_hours:
      print("Scheduled Hours: " + sch_hours)
      days = []
        
      daySelector(0)
      day0b = True 

      if day0b:
         if driver.find_elements(By.ID,'win0divDAY_OF_WEEK_DESCR$1'):
            daySelector(1)
            day1b = True 
           
            if day1b:
               if driver.find_elements(By.ID,'win0divDAY_OF_WEEK_DESCR$2'):    
                  daySelector(2)
                  day2b = True 
                     
                  if day2b:
                     if driver.find_elements(By.ID,'win0divDAY_OF_WEEK_DESCR$3'):   
                        daySelector(3)
                        day3b = True 

                        if day3b:
                           if driver.find_elements(By.ID,'win0divDAY_OF_WEEK_DESCR$4'):   
                              daySelector(4)
                              day4b = True 
                       
                              if day4b:
                                 if driver.find_elements(By.ID,'win0divDAY_OF_WEEK_DESCR$5'):     
                                    daySelector(5)
                                    day5b = True  
                          
                                    if day5b:
                                       if driver.find_elements(By.ID,'win0divDAY_OF_WEEK_DESCR$6'):   
                                          daySelector(6)

      
      print("Days Working: ")
      print(*days, sep='\n')
      save_path = 'D:\Dropbox\Schedule'
      name_of_file = 'hours'
      completeName = os.path.join(save_path, name_of_file+".txt")                                       
      f = open(completeName, 'w+')
      f.write("You've been scheduled: " + sch_hours + " hours this week. \n\n")
      for item in days:
          f.write("%s\n" % item)
       

                 
else: 
   print("Next Weeks Schedule not yet released")
   save_path = 'D:\Cloud Storage\Dropbox\Schedule'
   name_of_file = 'hours'
   completeName = os.path.join(save_path, name_of_file+".txt")                                       
   f = open(completeName, 'w+')
   f.write("Next Weeks Schedule not yet released")
   
f.close()
driver.quit()
driver2.quit()





  

