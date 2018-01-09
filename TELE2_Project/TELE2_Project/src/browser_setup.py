from selenium import webdriver
import os


class DriverSetup:

    utils_directory_path=os.path.abspath('')+"\\utils\\"
    def __init__(self,platform,browser,url,implicit_wait):
        self.platform=platform
        self.browser=browser
        self.url=url
        self.implicit_wait=implicit_wait



    def get_browser(self):
        if self.browser=="firefox":
            if self.platform=="windows":
                self.driver=webdriver.Firefox(self.utils_directory_path+"geckodriver.exe")
            else:
                self.driver = webdriver.Firefox(self.utils_directory_path + "geckodriver")

            return self.driver
        if self.browser == "chrome":
            if self.platform == "windows":
                self.driver = webdriver.Chrome(self.utils_directory_path + "chromedriver.exe")
            else:
                self.driver = webdriver.Chrome(self.utils_directory_path + "chromedriver")

            return self.driver

        if self.browser == "headless":
            if self.platform == "windows":
                self.driver = webdriver.PhantomJS(self.utils_directory_path + "phantomjs.exe")
            else:
                self.driver = webdriver.PhantomJS(self.utils_directory_path + "phantomjs")

            return self.driver

    def get_driver(self):
        driver=self.get_browser()
        driver.get(self.url)
        driver.implicitly_wait(self.implicit_wait)
        driver.maximize_window()
        return driver