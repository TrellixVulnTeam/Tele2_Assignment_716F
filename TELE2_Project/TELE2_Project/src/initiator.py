from browser_setup import DriverSetup
from database_connect import Database
from market_cap import MarketCapitalizationPage
import datetime
from common_methods import CommanMethods
import os, logging



class MarketCapitalization:

    def __init__(self):
        logging.basicConfig(filename='mrk_cap_logfile.log', level=logging.DEBUG,
                                     format='%s(asctime)s:%(levelname)s:%(message)s')
        self.set_env_variables()
        self.reports_path = os.path.abspath('') + "\\reports\\"
        self.report_path=os.makedirs(self.reports_path+"\\report_"+self.geneate_time_stamp()+"\\")

    def set_env_variables(self):
        with open("environment_variables.txt","r+") as file:
            self.platform=file.readline().splitlines()[0].split("=")[1]
            self.browser = file.readline().splitlines()[0].split("=")[1]
            self.url=file.readline().splitlines()[0].split("=")[1]
            self.implicit_wait_time=file.readline().splitlines()[0].split("=")[1]
            self.expicit_wait_time = file.readline().splitlines()[0].split("=")[1]
            self.db_name = file.readline().splitlines()[0].split("=")[1]
            self.xml_filename = file.readline().splitlines()[0].split("=")[1]
            logging.info("All Environment Variables are Set")

    def geneate_time_stamp(self):
        return datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

if __name__=="__main__":
    mcap=MarketCapitalization()
    driver_setup=DriverSetup(mcap.platform,mcap.browser,mcap.url,mcap.implicit_wait_time)
    db=Database(mcap.db_name)
    db.delete_all_data("Gainers")
    db.delete_all_data("Losers")
    db.create_table("Gainers")
    db.create_table("Losers")
    driver=driver_setup.get_driver()
    common_methods=CommanMethods(driver)
    market_cap_page=MarketCapitalizationPage(driver,db,common_methods)
    market_cap_page.navigate_to_trends_table()
    market_cap_page.get_table_data()
    market_cap_page.update_stock_price()
    gainers_details=db.view_data("Gainers")
    losers_details=db.view_data("Losers")
    print("************Gainers Table*****************")
    print(gainers_details)
    print("************Losers Table*****************")
    print(losers_details)
    #print(mcap.report_path+"MarketCapitalization.xml")
    common_methods.generate_XML_file("MarketCapitalization.xml",gainers_details,losers_details)
    driver.close()

