import configparser
from selenium import webdriver
class StartFramework:
    driver = None
    url = ""
    browser = ""
    exepath = ""
    orpath = ""

    def readConfig(self):
        config = configparser.RawConfigParser()
        config.read(r'C:\Users\Lenovo\PycharmProjects\eMasterAutomation\AutomationScripts\config.properties')
        config.sections()
        StartFramework.browser = config.get('DEFAULT', 'browser')
        StartFramework.exepath = config.get('DEFAULT', 'browserbinarypath')
        StartFramework.url = config.get('DEFAULT', 'url')
        StartFramework.orpath = config.get('DEFAULT', 'orpath')
        print("Browser: "+StartFramework.browser)
        print("URL: "+ StartFramework.url)
        print("path: "+ StartFramework.exepath)

    def launchBrowser(self):

        if str(StartFramework.browser).upper() == "chrome".upper():
            StartFramework.driver = webdriver.Chrome(StartFramework.exepath)
            StartFramework.driver.maximize_window()
        elif str(StartFramework.browser).upper() == "firefox".upper():
            StartFramework.driver = webdriver.Firefox()
        elif str(StartFramework.browser).upper() == "internet explore".upper() or str(StartFramework.browser).upper() == "ie".upper():
            StartFramework.driver = webdriver.Ie()

        StartFramework.driver.get(str(self.url))

    def getDataFromObjectRepository(self,section, key):
        config = configparser.RawConfigParser()
        config.read(StartFramework.orpath)
        config.sections()
        return config.get(str(section), str(key))
    def getwebelements(self,locator, value):
        if str(locator).upper() == "id".upper():
            return StartFramework.driver.find_elements_by_id(str(value))
        elif str(locator).upper() == "name".upper():
            return StartFramework.driver.find_elements_by_name(str(value))
        elif str(locator).upper() == "xpath".upper():
            return StartFramework.driver.find_elements_by_xpath(str(value))
        elif str(locator).upper() == "linktext".upper():
            return StartFramework.driver.find_elements_by_link_text(str(value))
        elif str(locator).upper() == "partiallinktext".upper():
            return StartFramework.driver.find_elements_by_partial_link_text(str(value))
        elif str(locator).upper() == "tagname".upper():
            return StartFramework.driver.find_elements_by_tag_name(str(value))
        elif str(locator).upper() == "class".upper():
            return StartFramework.driver.find_elements_by_class_name(str(value))
        elif str(locator).upper() == "cssselector".upper():
            return StartFramework.driver.find_elements_by_class_css_selector(str(value))
        else:
            return None




obj = StartFramework()
obj.readConfig()
obj.launchBrowser()
print(StartFramework.orpath)
#print(
email = obj.getDataFromObjectRepository("Login Page","email")
import time
time.sleep(25)
obj.getwebelements(email.split("***")[0],email.split("***")[1])[0].send_keys("vivek")
