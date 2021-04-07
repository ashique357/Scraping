from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def scraping():
    DRIVER_PATH = r"C:\Users\ashiq\Downloads\chromedriver_win32\chromedriver.exe"
    site='https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F'

    try:
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        try:
            driver.get(site)
            html=driver.page_source

            df = pd.read_html(html)
            print(df[0])
            df[0].to_csv('Scraping.csv')

        except:
            print("Web Site Not Found")

    except:
        print("Web Driver Not Found")


scraping()