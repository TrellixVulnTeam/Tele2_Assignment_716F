from selenium.webdriver.common.by import By
from common_methods import CommanMethods
import time


class MarketCapitalizationPage:
    firstFrame = (By.XPATH,"hist_frame")
    secondFrame = (By.CLASS_NAME,"invfr")
    price_tab = "//b[@class='t' and contains(text(),'Price')]"
    trends_table = "//div[@id='trend']//td[contains(text(),'Gainers')]/../.."
    trends_table_rows = "//div[@id='trend']//div[@style='display: block;']//td[contains(text(),'Gainers')]/../..//td[@class='name']/.."
    all_names_locator = "//div[@id='trend']//div[@style='display: block;']//td[contains(text(),'Gainers')]/../..//td[@class='name']/..//td[@class='name']"
    all_gainers_names = "//div[@id='trend']//div[@id='tm_price_0']//td[@class='change chg']/..//td[@class='name']//a"
    all_gainers_mktCap = "//div[@id='trend']//div[@id='tm_price_0']//td[@class='name']/..//td[@class='change chg']/..//td[@class='mktCap']"
    all_gainers_change = "//div[@id='trend']//div[@id='tm_price_0']//td[@class='name']/..//td[@class='change chg']/..//td[@class='mktCap']"
    all_losers_names =   "//div[@id='trend']//div[@id='tm_price_0']//td[@class='change chr']/..//td[@class='name']//a"
    all_losers_mktCap =  "//div[@id='trend']//div[@id='tm_price_0']//td[@class='change chr']/..//td[@class='mktCap']"
    all_losers_change = "//div[@id='trend']//div[@id='tm_price_0']//td[@class='change chr']"
    all_name_links = "//div[@id='trend']//div[@style='display: block;']//td[@class='name']//a"
    stock_price_locator = "//div[@id='price-panel']//span[@class='unchanged']"

    def __init__(self,driver,db):
        self.driver=driver
        self.db=db
        self.common = CommanMethods(self.driver)
    def __del__(self):
        self.driver.quit()

    def navigate_to_trends_table(self):
        self.common.jsClick(self.price_tab)
        if self.common.is_element_present(self.all_gainers_names)==False:
            self.common.jsClick(self.price_tab)


    def get_table_data(self):
        #self.switch_control_trends_table()
        for name, change, mktCap in zip(self.common.get_element_text_list(self.all_gainers_names),
                                        self.common.get_element_text_list(self.all_gainers_change),
                                        self.common.get_element_text_list(self.all_gainers_mktCap)):
            self.db.insert_data("Gainers", name, change, mktCap, None)

        for name, change, mktCap in zip(self.common.get_element_text_list(self.all_losers_names),
                                        self.common.get_element_text_list(self.all_losers_change),
                                        self.common.get_element_text_list(self.all_losers_mktCap)):
            self.db.insert_data("Losers", name, change, mktCap, None)

    def update_stock_price(self):

        for elem in self.common.get_element_list(self.all_gainers_names):
            name = elem.text
            stock_price = self.get_stock_price(elem)
            self.db.update_data("Gainers", name, stock_price)
        for elem in self.common.get_element_list(self.all_losers_names):
            name = elem.text
            stock_price = self.get_stock_price(elem)
            self.db.update_data("Losers", name, stock_price)

    def get_stock_price(self,comp_element):
        comp_element.click()
        time.sleep(3)
        handles = self.driver.window_handles
        self.driver.switch_to(handles[-1])
        stock_price = self.common.get_element_text(self.stock_price_locator)
        self.driver.close()
        self.driver.switch_to(handles[0])
        #self.switch_control_trends_table()
        return stock_price

    def switch_control_trends_table(self):
        self.driver.switch_to.frame(self.firstFrame)
        self.driver.switch_to.frame(self.secondFrame)
















