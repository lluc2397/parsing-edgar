from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# Opciones de navegación
options = Options()
# options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
# options.add_argument("--headless")
options.binary_location = '/opt/brave.com/brave/brave'
driver_path = '/home/lucas/Downloads/chromedriver'

driver = webdriver.Chrome( executable_path = driver_path, options=options)

# Inicializamos el navegador
html_pet = driver.get('https://www.sec.gov/include/ticker.txt')
# company_name = driver.find_element_by_id("company")
# company_name.send_keys("Intel")



    
