from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Appium server URL
appium_server_url = "http://127.0.0.1:4723"

# Desired capabilities
desired_caps = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.android.chrome",
    "appActivity": "com.google.android.apps.chrome.Main",
    "chromedriverExecutable": "/Users/user/Driver/chromedriver2",
    "noReset": True,
    "skipDeviceInitialization": True
}


# Load capabilities using UiAutomator2Options
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

# Start Appium session
driver = webdriver.Remote(appium_server_url, options=capabilities_options)

time.sleep(5)  # Let Chrome launch

# Print and switch to CHROMIUM or WEBVIEW context
print("Available contexts:", driver.contexts)
for context in driver.contexts:
    if "WEBVIEW" in context or "CHROMIUM" in context:
        print(f"Switching to context: {context}")
        driver.switch_to.context(context)
        break
else:
    print("Could not find WEBVIEW/CHROMIUM context.")
    driver.quit()
    exit()

# Open Wikipedia and wait for it to load
driver.get("https://www.wikipedia.org/")
time.sleep(8)

# Select language from dropdown
dropdown = driver.find_element(By.CSS_SELECTOR, "#searchLanguage")
select = Select(dropdown)
select.select_by_value("hi")  # Select Hindi

# Get and print all language options
options = dropdown.find_elements(By.TAG_NAME, 'option')
print(f"Number of language options: {len(options)}")
for option in options:
    print("Text is:", option.text, "Lang is:", option.get_attribute('lang'))

# Print page title
print("Page title:", driver.title)

# Close the session
time.sleep(3)
driver.quit()

