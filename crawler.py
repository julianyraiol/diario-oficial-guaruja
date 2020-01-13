import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

delay = 2

driver = webdriver.Firefox()
driver.get("http://www.guaruja.sp.gov.br/edicoes-diario-oficial/")

elementyears = driver.find_element_by_id("mec_sf_year_22564")
elementmonth = driver.find_element_by_id("mec_sf_month_22564")
 
months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
days = driver.find_elements_by_class_name("mec-calendar-day")
years = [x.get_attribute("value") for x in elementyears.find_elements_by_tag_name("option")]

select = Select(elementyears)
select1 = Select(elementmonth)

for year in years:
    select.select_by_value(year)

    for month in months:
        time.sleep(delay)
        select1.select_by_visible_text(month)
    time.sleep(delay)

driver.close()


