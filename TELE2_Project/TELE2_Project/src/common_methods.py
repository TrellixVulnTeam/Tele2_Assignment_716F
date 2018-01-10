from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os.path
import logging


import sys

class CommanMethods:
    def __init__(self,driver):
        self.driver=driver
        logging.basicConfig(filename='mrk_cap_logfile.log', level=logging.DEBUG,
                            format='%s(asctime)s:%(levelname)s:%(message)s')


    def get_element_text(self,locator):
        logging.debug("Element Found:"+locator)
        return self.wait_for_element(locator).text


    def wait_for_element(self,locator):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,locator)))
            logging.debug("Element Found:" + locator)
            return element
        except:
            logging.debug("Element Not Found:" + locator)
            sys.exit("Element not Found:"+ str(locator))

    def is_element_present(self,locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            logging.debug("Element Found:" + locator)
            return True
        except:
            logging.debug("Element Not Found:" + locator)
            return False

    def check_element_not_visible(self,locator):
        try:
            self.driver.find_element_by_xpath(locator)
            logging.debug("Element Found:" + locator)
            return False
        except:
            logging.debug("Element Not Found:" + locator)
            return True



    def get_element_list(self,locator):
        if(self.is_element_present(locator)):
            logging.debug("Element List Found:" + locator)
            return self.driver.find_elements_by_xpath(locator)
        else:
            logging.debug("Element Not Found:" + locator)
            sys.exit("Element not Found:" + str(locator))

    def get_element_text_list(self,locator):
        list=[]
        for elem in self.get_element_list(locator):
            list.append(elem.text)

        return list

    def click_element(self,locator):
        try:
            self.wait_for_element(locator).click()
            logging.debug("Clicked Element Successfully:" + locator)
        except:
            logging.debug("Issue in click Element Successfully:" + locator)


    def jsClick(self,locator):
        self.driver.execute_script("arguments[0].click();", self.wait_for_element(locator))

    def jsClick_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def click_to_open_in_new_window(self,link):
        ActionChains(self.driver).key_down(Keys.SHIFT).click(link).key_up(Keys.SHIFT).perform()

    def resolve_stale_element(self,element):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of(element))

    def generate_XML_file(self,file_path,gainers_data,losers_data):
        try:
            if (os.path.exists(file_path)):
                file = open(file_path, "a+")
            else:
                file = open(file_path, "w+")

            file.write('<?xml version="1.0" ?>\n')
            file.write('<Market_Capitalization_Data>\n')

            for record1, record2 in zip(gainers_data, losers_data):
                file.write('<Gainers>\n')
                file.write('<name>' + record1[0] + '</name>\n')
                file.write('<change>' + record1[1] + '</change>\n')
                file.write('<mkt_Cap>' + record1[2] + '</mkt_Cap>\n')
                file.write('<stock_price>' + str(record1[3]) + '</stock_price>\n')
                file.write('</Gainers>\n')

                file.write('<Losers>\n')
                file.write('<name>' + record2[0] + '</name>\n')
                file.write('<change>' + record2[1] + '</change>\n')
                file.write('<mkt_Cap>' + record2[2] + '</mkt_Cap>\n')
                file.write('<stock_price>' + str(record1[3]) + '</stock_price>\n')
                file.write('</Losers>\n')
            file.write('</Market_Capitalization_Data>\n')
            file.close()
            logging.debug("XML File Generated Successfully")
        except:
            logging.debug("Issue in XML File Generation")



