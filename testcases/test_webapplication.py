from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

appium_server_url = "http://127.0.0.1:4723"

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.android.chrome",
    "appActivity": "com.google.android.apps.chrome.Main",
    "chromedriverExecutable": "/Users/user/Driver/chromedriver",
    "noReset": True
}

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)

time.sleep(5)  # Give Chrome some time to launch

# Switch to webview context
print("Available contexts:", driver.contexts)  # For debugging
for context in driver.contexts:
    if "WEBVIEW" in context or "CHROMIUM" in context:
        driver.switch_to.context(context)
        break

# Now you're in webview context and can load a URL
driver.get("https://www.google.com")
print("Launching google search screen")
print("Page title:", driver.title)
time.sleep(3)
driver.quit()
