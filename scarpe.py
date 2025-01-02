import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

#SBR_WEBDRIVER = 'https://brd-customer-hl_c0f053f9-zone-scraping_browser1:hcoiejf7ri7m@brd.superproxy.io:9515'

def scarpeWebsite(website):
    print('Launching Web Page')

    print("Connecting to Scraping Browser...")
    '''sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html'''

    chromePath = 'chromedriver.exe-PATH'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chromePath), options=options)

    try:
        driver.get(website)
        print('Page Loaded....')

        pageCode = driver.page_source
        time.sleep(10)
        return pageCode

    finally:
        driver.quit()


def extractBodyContent(htmlContent):
    soup = BeautifulSoup(htmlContent, 'html.parser')

    bodyContent = soup.body
    if bodyContent:
        return str(bodyContent)
    
    return ''

def cleanBodyContent(bodyContent):
    soup = BeautifulSoup(bodyContent, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    cleanedContent = soup.get_text(separator='\n')
    cleanedContent = '\n'.join(
        line.strip() for line in cleanedContent.splitlines() if line.strip()
    )

    return cleanedContent

def splitContent(domContent, maxLength = 6000):
    return [
        domContent[i:i + maxLength] for i in range(0, len(domContent), maxLength)
    ]