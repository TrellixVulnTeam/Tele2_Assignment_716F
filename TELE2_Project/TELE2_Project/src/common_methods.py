from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

class CommanMethods:
    def __init__(self,driver):
        self.driver=driver


    def get_element_text(self,locator):
        pass


    def wait_for_element(self,locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator)))
            return element
        except:
            sys.exit("Element not Found:", locator)

    def is_element_present(self,locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator)))
            return True
        except:
            return False


    def get_element_list(self,locator):
        if(self.is_element_present(locator)):
            return self.driver.find_elements_by_xpath(locator)
        else:
            sys.exit("Element not Found:",locator)

    def get_element_text_list(self,locator):
        list=[]
        for elem in self.get_element_list(locator):
            list.append(elem.text)

        return list

    def click_element(self,locator):
        self.wait_for_element(locator).click()

    def jsClick(self,locator):
        self.driver.execute_script("arguments[0].click();", self.wait_for_element(locator))