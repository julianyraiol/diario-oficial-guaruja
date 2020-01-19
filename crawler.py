import time
import requests
import logging
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
delay = 6

class GuarujaCrawler(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.guaruja.sp.gov.br/edicoes-diario-oficial/")
        logging.basicConfig(level = logging.INFO)

    def download_and_save_file(self, filelink, filename):

        if (not os.path.exists(filename)):
            try:
                requestlink = requests.get(filelink)
                with open(filename, "wb") as f:
                    f.write(requestlink.content)
                logging.info("Arquivo baixado: " + filename)
            except:
                logging.warning("Falha ao fazer download dos arquivos")
        else:
            logging.warning("Arquivo já existente")

    def get_files_by_day(self):
        calendar = self.driver.find_elements_by_class_name("mec-color-hover")
        
        print("Descendo pro calendário")
        self.driver.execute_script("window.scrollTo(0, 400)")

        for days in calendar:
            filelink = days.get_attribute("href")
            filename = days.get_attribute('text').replace("/", "-") + ".pdf"
            self.download_and_save_file(filelink, filename)
    
    def set_filter_by_month_year(self):
        elementyear = self.driver.find_element_by_id("mec_sf_year_22564")
        elementmonth = self.driver.find_element_by_id("mec_sf_month_22564")

        selectyear = Select(elementyear)
        years = [x.get_attribute("value") for x in selectyear.options]

        selectmonth = Select(elementmonth)

        for year in years:
            selectyear.select_by_visible_text(year)
            time.sleep(delay)
        
            for month in months:
                print("=================================")
                print("Mês que tá sendo baixado:", month)
                print("=================================")
                
                selectmonth.select_by_visible_text(month)
                time.sleep(delay)
                
                self.get_files_by_day()          
                self.driver.execute_script("window.scrollTo(0, 0)")
                
      
if __name__ == "__main__":
    crawler = GuarujaCrawler()
    crawler.set_filter_by_month_year()
    crawler.driver.close()

