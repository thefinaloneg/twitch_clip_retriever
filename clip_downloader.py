from selenium import webdriver
from selenium.webdriver.common.by import By
import glob
import os
import time
import clips


def download_clips(downloads_folder_path):
    driver = webdriver.Safari()
    driver.get("https://clipsey.com/")  # load the page
    ele_1 = driver.find_element(By.CLASS_NAME, "clip-url-input")
    ele_1.clear()
    ele_1.send_keys("https://clips.twitch.tv/GrotesqueAmericanBarracudaStoneLightning-RIv51p7GZxMe8djl")
    driver.find_element(By.CLASS_NAME, "get-download-link-button").click()
    assert "No results found." not in driver.page_source
    link = driver.find_element(By.LINK_TEXT, "Download")
    time.sleep(1)  # wait for the link to be ready
    link.click()
    driver.close()
    list_of_files = glob.glob(downloads_folder_path + '/*')
    latest_file = max(list_of_files, key=os.path.getctime)


download_clips('/Users/final/Downloads')
