import shutil

from selenium import webdriver
from selenium.webdriver.common.by import By
import glob
import os
import time
import clips
import constants


def download_clips(downloads_folder_path):
    """Downloads clips from Twitch.tv.

    Keyword arguments:
    downloads_folder_path -- the folder to download clips to
    """
    driver = webdriver.Safari()
    driver.get("https://clipsey.com/")  # load the page
    ele_1 = driver.find_element(By.CLASS_NAME, "clip-url-input")
    ele_1.clear()
    ele_1.send_keys(clips.get_clips(constants.game_ids['League of Legends'])[0])
    driver.find_element(By.CLASS_NAME, "get-download-link-button").click()
    assert "No results found." not in driver.page_source
    time.sleep(1)  # wait for the link to be ready
    link = driver.find_element(By.LINK_TEXT, "Download")
    link.click()
    time.sleep(1)  # needs time to click on clip
    driver.close()
    list_of_files = glob.glob(downloads_folder_path + '/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    shutil.move(latest_file, '/Users/final/Desktop/twitch_clip_retriever/clip_folder')


download_clips('/Users/final/Downloads')
