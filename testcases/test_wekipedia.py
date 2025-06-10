from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # corrected import

appium_server_url = "http://127.0.0.1:4723"

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.android.chrome",
    "appActivity": "com.google.android.apps.chrome.Main",
    "chromedriverExecutable": "/Users/user/Driver/chromedriver 2",
    "noReset": True
}

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)

time.sleep(5)  # Let Chrome launch

# Switch to WEBVIEW or CHROMIUM context
print("Available contexts:", driver.contexts)
for context in driver.contexts:
    if "WEBVIEW" in context or "CHROMIUM" in context:
        driver.switch_to.context(context)
        break

# Navigate to Wikipedia and interact
driver.get("https://www.wikipedia.org/")
time.sleep(3)  # Wait for page to load

dropdown = driver.find_element(By.CSS_SELECTOR, "#searchLanguage")
select = Select(dropdown)
select.select_by_value("lld")  # Select Hindi

# Get all <option> elements
options = dropdown.find_elements(By.TAG_NAME, 'option')  # Fix this line

print(f"Number of language options: {len(options)}")

for option in options:
    print("Text is:", option.text, "Lang is:", option.get_attribute('lang'))  # Fix attribute access

print("Page title:", driver.title)

time.sleep(3)
driver.quit()  # Good practice to end the session
