import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



## Set the path to the chromedriver executable
chromedriver_path = "/user/bin/chromedriver"

# Create a Service object
service = Service(chromedriver_path)

# Create ChromeOptions object
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")  # Disable notifications

# Create the WebDriver using the service and options
browser = webdriver.Chrome(service=service, options=chrome_options)

# open facebook.com using get() method
browser.get('https://gotranscript.com/text-compare#diff')

# Enter text 1 
text1 = "this what consistency can do"
text1_element = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.NAME, 'text1'))
)
text1_element.send_keys(text1)
print("text1 entered")

# Enter text 2 
text2 = "WinMerge is a free and open-source tool for comparing files and folders. It includes a visual differencing and merging tool that can be used to compare CSV files. WinMerge highlights the differences between the files and allows you to merge changes if needed. "
text2_element = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.NAME, 'text2'))
)
text2_element.send_keys(text2)
print("text2 entered")


# Click on the compare button
compare_button = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID, 'recaptcha'))
)
compare_button.click()
print("successful")
time.sleep(10)

browser.save_screenshot('screenshot.png')
# Close the browser
browser.close()
