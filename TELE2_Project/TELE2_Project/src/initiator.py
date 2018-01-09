from browser_setup import DriverSetup
from database_connect import Database
from market_cap import MarketCapitalizationPage


class MarketCapitalization:

    def __init__(self):
        self.set_env_variables()

    def set_env_variables(self):
        with open("environment_variables.txt","r+") as file:
            self.platform=file.readline().splitlines()[0].split("=")[1]
            self.browser = file.readline().splitlines()[0].split("=")[1]
            self.url=file.readline().splitlines()[0].split("=")[1]
            self.implicit_wait_time=file.readline().splitlines()[0].split("=")[1]
            self.expicit_wait_time = file.readline().splitlines()[0].split("=")[1]
            self.db_name = file.readline().splitlines()[0].split("=")[1]

if __name__=="__main__":
    mcap=MarketCapitalization()
    driver_setup=DriverSetup(mcap.platform,mcap.browser,mcap.url,mcap.implicit_wait_time)
    db=Database(mcap.db_name)
    db.create_table("Gainers")
    db.create_table("Losers")
    market_cap_page=MarketCapitalizationPage(driver_setup.get_driver(),db)
    market_cap_page.navigate_to_trends_table()
    market_cap_page.get_table_data()
    market_cap_page.update_stock_price()
    print("************Gainers Table*****************")
    db.view_data("Gainers")
    print("************Losers Table*****************")
    db.view_data("Losers")


