# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.youtube.com/")
time.sleep(5)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
time.sleep(5)
search_bar.send_keys("songs")
time.sleep(5)
# Submitting the search query
search_icon = driver.find_element("xpath", "//*[@id='search-icon-legacy']")
search_icon.click()
time.sleep(5)

video_icon = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-search-pyv-renderer/div/ytd-ad-slot-renderer/div/ytd-in-feed-ad-layout-renderer/div/ytd-promoted-video-renderer/div/ytd-thumbnail/a/yt-image/img")
video_icon.click()
time.sleep(5)

like_icon = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
like_icon.click()
time.sleep(5)

login_icon = driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
login_icon.click()
time.sleep(5)

time.sleep(5)
# Closing the webdriver
driver.close()
