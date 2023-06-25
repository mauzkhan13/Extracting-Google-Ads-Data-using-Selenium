from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
import random
import pandas as pd
import os
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, TimeoutException,ElementNotInteractableException,MoveTargetOutOfBoundsException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

user_agent = ''

# Create Chrome options object
options = Options()
options.add_argument(f'user-agent={user_agent}')

# Add arguments to Chrome options
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--disable-infobars')
options.add_argument('--mute-audio')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-notifications')
options.add_argument('--disable-translate')
options.add_argument('--disable-logging')
options.add_argument('--disable-default-apps')
options.add_argument('--disable-background-timer-throttling')
options.add_argument('--disable-backgrounding-occluded-windows')
options.add_argument('--disable-breakpad')
options.add_argument('--disable-component-extensions-with-background-pages')
options.add_argument('--disable-features=TranslateUI')
options.add_argument('--disable-hang-monitor')
options.add_argument('--disable-ipc-flooding-protection')
options.add_argument('--disable-prompt-on-repost')
options.add_argument('--disable-renderer-backgrounding')
options.add_argument('--disable-sync')
options.add_argument('--disable-web-resources')
options.add_argument('--enable-automation')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--log-level=3')
options.add_argument('--test-type=webdriver')
options.add_argument('--user-data-dir=/tmp/user-data')
options.add_argument('--v=99')
options.add_argument('--incognito')
options.add_argument('--headless')

# Add experimental options
options.add_experimental_option('prefs', {
    'profile.managed_default_content_settings.images': 1,
    'profile.managed_default_content_settings.stylesheets': 2,
    'profile.managed_default_content_settings.plugins': 2,
    'profile.managed_default_content_settings.popups': 2,
    'profile.managed_default_content_settings.geolocation': 2,
    'profile.managed_default_content_settings.notifications': 2,
    'profile.managed_default_content_settings.automatic_downloads': 1,
    'profile.managed_default_content_settings.fullscreen': 2,
    'profile.managed_default_content_settings.mouselock': 2,
    'profile.managed_default_content_settings.pointerLock': 2,
    'profile.managed_default_content_settings.webusb': 2,
    'profile.managed_default_content_settings.webxr': 2,
    'profile.default_content_setting_values.media_stream_mic': 2,
    'profile.default_content_setting_values.media_stream_camera': 2,
})
# Start Chrome with the custom user-agent string
driver = webdriver.Chrome(options=options)

url = 'https://adstransparency.google.com/advertiser/AR04273916802288844801?region=anywhere'
driver.get(url)
driver.maximize_window()


description_video = []
heading_video = []
ads_links = []


for ads_link in ads_links:
    driver.get(ads_link)
    try:
        if len(driver.find_elements(By.TAG_NAME, 'iframe')) > 0:
            driver.switch_to.frame(0)
        else:
            print('No iframes found on the page')
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
        print('iframe is Not found.')

    time.sleep(2)

    try:
        heads = driver.find_elements(By.XPATH, '//div[@class="headline transparent"]')
        for h in heads[1:]:
            heading_video.append(h.text.strip('\u2069').replace('\u2066', ' '))
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
        heads = ""

    try:
        desc = driver.find_elements(By.XPATH, '//div[@class="description transparent  square-only"]')
        for d in desc[1:]:
            description_video.append(d.text.strip('\u2069').replace('\u2066', ' '))
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
        desc = ""
        
    time.sleep(random.uniform(1, 1.2))


df = pd.DataFrame(zip(description_video,heading_video), columns=['description_video', 'heading_video'])
file_path = os.path.join("C:/Users/Mauz Khan", "Google ads.xlsx")
df.to_excel(file_path, index=False)


description_image = []

for ad_link in ads_links:
    driver.get(ad_link)
    try:
        if len(driver.find_elements(By.TAG_NAME, 'iframe')) > 0:
            driver.switch_to.frame(0)
        else:
            print('No iframes found on the page')
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
        print('iframe is Not found.')

    time.sleep(3)
    try:
        desc1 = driver.find_elements(By.XPATH, '//span[@id="headline"] | //div[@style="display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;"]')
        for d in desc1:
            description_image.append(d.text.strip('\u2069').replace('\u2066', ' '))
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            desc1 = ""
    time.sleep(random.uniform(1, 1.2))

df = pd.DataFrame(zip(description_image), columns=['description_image'])
file_path = os.path.join("C:/Users/Mauz Khan", "Google ads.xlsx")
df.to_excel(file_path, index=False) 


description = []
heading = []

# for index, ad_link in enumerate(ads_links):
#     print(f"Opening link {index + 1}: {ad_link}")
#     driver.get(ad_link)
for ad_link in ads_links:
    driver.get(ad_link)
    try:
        if len(driver.find_elements(By.TAG_NAME, 'iframe')) > 0:
            driver.switch_to.frame(0)
        else:
            print('No iframes found on the page')
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
        print('iframe is Not found.')

        
    try:
        time.sleep(2)
        heads = driver.find_elements(By.XPATH, '//div[starts-with(@role, "link")]/span')
        for h in heads:
            heading.append(h.text.strip('\u2069').replace('\u2066', ' '))
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
        heads = ""
       
    try:
        desc = driver.find_element(By.XPATH, '//div[starts-with(@class, "MUxGbd yDYNvb")]/div | //div[starts-with(@class, "description transparent  square-only")] | //span[starts-with(@id, "headline")]')
        description.append(desc.text.strip('\u2069').replace('\u2066', ' '))
    except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
        desc = ""
        
    time.sleep(1)

df = pd.DataFrame(zip(heading, description), columns=['heading', 'description'])
file_path = os.path.join("C:/Users/Mauz Khan", "Google ads.xlsx")
df.to_excel(file_path, index=False) 