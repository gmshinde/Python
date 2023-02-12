#from selenium import webdriver

#print("package loaded")
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
##driver = webdriver.Chrome(executable_path="chromedriver.exe")
# to maximize the browser window
##driver.maximize_window()
#get method to launch the URL
##driver.get("https://www.tutorialspoint.com/index.htm")
#to refresh the browser
##driver.refresh()
#to close the browser
##driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

print("package loaded")
print("Getting Service")
service_obj = Service("chromedriver.exe")
print("Getting Driver")
driver = webdriver.Chrome(service=service_obj)

# browser exposes an executable file
# Through Selenium test we will invoke the executable file which will then #invoke actual browser
# driver = webdriver.Chrome(executable_path="chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
# get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
# to refresh the browser
driver.refresh()
# to close the browser
driver.close()