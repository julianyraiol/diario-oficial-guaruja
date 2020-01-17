import time
import requests
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys

months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
delay = 3

class GuarujaDriver(object):
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        logging.basicConfig(level = logging.INFO)
    
    def get_element_by_id(self, element_id):
        return self.driver.find_element_by_id(element_id)
    
    def get_elements_by_class(self, element_class):
        return self.driver.find_elements_by_class_name(element_class)
    
    def get_options_by_id(self, element):
        element_id = Select(element)
        return [x.get_attribute("value") for x in element_id.options]

    def select_by_text(self, element, text):

        select = Select(element)
        select.select_by_visible_text(text)
        time.sleep(delay)

    def select_by_value(self, element, value):
        select = Select(element)
        select.select_by_value(value)

    def go_to_calendar(self):
        print("Descendo pro calendário")
        self.driver.execute_script("window.scrollTo(0, 400)")

class GuarujaCrawler(object):
    def __init__(self):
        self.driver = GuarujaDriver("http://www.guaruja.sp.gov.br/edicoes-diario-oficial/")

    def download_and_save_file(self, filelink, filename):
        try:
            requestlink = requests.get(filelink)
            with open(filename, "wb") as f:
                f.write(requestlink.content)
            logging.info("Arquivo baixado: " + filename)
        except:
            logging.warning("Falha ao fazer download dos arquivos")

    def get_files_by_day(self):
        calendar = self.driver.get_elements_by_class("mec-color-hover")
        self.driver.go_to_calendar()

        for days in calendar:
            filelink = days.get_attribute("href")
            filename = days.get_attribute('text').replace("/", "-") + ".pdf"
            self.download_and_save_file(filelink, filename)
    
    def set_filter_by_month_year(self):
        selectyear = self.driver.get_element_by_id("mec_sf_year_22564")
        selectmonth = self.driver.get_element_by_id("mec_sf_month_22564")

        years = self.driver.get_options_by_id(selectyear)

        for year in years:
            self.driver.select_by_text(selectyear, year)
        
            for month in months:
                print("=================================")
                print("Mês que tá sendo baixado:", month)
                print("=================================")
                self.driver.select_by_text(selectmonth, month)
                self.get_files_by_day()          
                self.driver.driver.execute_script("window.scrollTo(0, 0)")
      
if __name__ == "__main__":
    crawler = GuarujaCrawler()
    crawler.set_filter_by_month_year()
    crawler.driver.driver.close()
