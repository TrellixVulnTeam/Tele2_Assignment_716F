from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import sys

class CommanMethods:
    def __init__(self,driver):
        self.driver=driver


    def get_element_text(self,locator):
        return self.wait_for_element(locator).text


    def wait_for_element(self,locator):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,locator)))
            return element
        except:
            sys.exit("Element not Found:"+ str(locator))

    def is_element_present(self,locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    def check_element_not_visible(self,locator):
        try:
            self.driver.find_element_by_xpath(locator)
            return False
        except:
            return True



    def get_element_list(self,locator):
        if(self.is_element_present(locator)):
            return self.driver.find_elements_by_xpath(locator)
        else:
            sys.exit("Element not Found:" + str(locator))

    def get_element_text_list(self,locator):
        list=[]
        for elem in self.get_element_list(locator):
            list.append(elem.text)

        return list

    def click_element(self,locator):
        self.wait_for_element(locator).click()

    def jsClick(self,locator):
        self.driver.execute_script("arguments[0].click();", self.wait_for_element(locator))

    def jsClick_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def click_to_open_in_new_window(self,link):
        ActionChains(self.driver).key_down(Keys.SHIFT).click(link).key_up(Keys.SHIFT).perform()

    def resolve_stale_element(self,element):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of(element))