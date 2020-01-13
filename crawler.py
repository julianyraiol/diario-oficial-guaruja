import time
import requests
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys

delay = 2
logging.basicConfig(level = logging.INFO)

driver = webdriver.Firefox()
driver.get("http://www.guaruja.sp.gov.br/edicoes-diario-oficial/")

elementyears = driver.find_element_by_id("mec_sf_year_22564")
elementmonth = driver.find_element_by_id("mec_sf_month_22564")
 
months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
days = driver.find_elements_by_class_name("mec-calendar-day")
years = [x.get_attribute("value") for x in elementyears.find_elements_by_tag_name("option")]

select = Select(elementyears)
select1 = Select(elementmonth)

driver.execute_script("window.scrollBy(0, 400)")
time.sleep(delay)
calendar = driver.find_elements_by_class_name("mec-color-hover") 

for days in calendar:
    try:    
        filelink = days.get_attribute("href")
        request_file = requests.get(filelink)
        namefile = days.get_attribute('text').replace("/", "-") + ".pdf"
        with open(namefile, "wb") as filepdf:
            filepdf.write(request_file.content)
        logging.info("Arquivo baixado")
    except: 
        logging.warning("Falha ao fazer download dos arquivos")
        
'''
for year in years:
    select.select_by_value(year)
    for month in months:
        select1.select_by_visible_text(month)
        time.sleep(delay)
        #add codigo aqui
    driver.execute_script("window.scrollBy(0, 0)")
    time.sleep(delay)
'''
driver.close()


