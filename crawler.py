from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.guaruja.sp.gov.br/edicoes-diario-oficial/")

element = driver.find_element_by_id("mec_sf_year_22564")
select = Select(element)

years = [x.get_attribute("value") for x in element.find_elements_by_tag_name("option")]

select.select_by_value("2016")

driver.close()
