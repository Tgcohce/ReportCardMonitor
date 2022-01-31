from  selenium import webdriver
import time
from datetime import date

# @ author Tolga G Cohce | b1gturk

# Python - Selenium Script
# to login crawl and scrape data 
# and store the data in a txt file

def getDriver_option():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")

  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options) 
  driver.get("https://moodle.mta.ca/login/index.php")
  return driver

def main():
  driver = getDriver_option()

# Entering Username
  username = input("Enter moodle username: ")
  driver.find_element(by="id",value="username").send_keys(username)
  time.sleep(3)

# Entering password
  shadow = input("Enter moodle password: ")
  driver.find_element(by="id",value="password").send_keys(shadow)
  time.sleep(2)

# Logs in
  driver.find_element(by="id", value="loginbtn").click()

# Opens menu
  print(f"Current url: {driver.current_url}")
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/div[3]/nav/div/button").click()

# Clicks on my class
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/div[3]/div[2]/nav/ul/li[6]/a/div/div/span[2]").click()

# open menu again
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/div[3]/nav/div/button").click()

# open grades
  time.sleep(3)
  driver.find_element(by="xpath", value="/html/body/div[3]/div[2]/nav[1]/ul/li[4]/a/div/div/span[2]").click()
  time.sleep(3)

# Switch to general overivew of classes
  generalOv = driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div/section/div/div[2]/ul/li[1]/a")
  generalOv.click()

  bizmark = driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div/section/div/div[3]/table/tbody/tr[1]/td[2]").text
  progmark = driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div/section/div/div[3]/table/tbody/tr[2]/td[2]").text
  histmark = driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div/section/div/div[3]/table/tbody/tr[3]/td[2]").text
  mathmark = driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div/section/div/div[3]/table/tbody/tr[4]/td[2]").text
  philmark = driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div/section/div/div[3]/table/tbody/tr[5]/td[2]").text

  print("COMM1011 --&& Business Class Grade: " +  bizmark)
  print("PROG1731 --&& Programming Class Grade: " + progmark)
  print("HIST1661 --&& History Class Grade: " + histmark)
  print("MATH1151 --&& Math Class Grade: " + mathmark)
  print("PHIL1601 --&& Philosophy Class Grade: " + philmark)

  gradeCard = (
  f"Todays Date: {date.today()} \n \
  COMM1011 --&& Business Class Grade:  {bizmark} \n \
  PROG1731 --&& Programming Class Grade: {progmark} \n \
  HIST1661 --&& History Class Grade: {histmark} \n \
  MATH1151 --&& Math Class Grade: {mathmark} \n \
  PHIL1601 --&& Philosophy Class Grade: {philmark}")

  with open('gradeCard.txt', 'w') as f:
    f.write(gradeCard)



main()