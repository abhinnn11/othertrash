import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME
caps["goog:loggingPrefs"] = {"performance": "ALL"}

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--autoplay-policy=no-user-gesture-required")

driver = webdriver.Chrome(options=options, desired_capabilities=caps)

print("Opening page...")
driver.get("nnn")  # page loads cookies first
time.sleep(5)

# CHANGE THIS URL WHEN YOU RUN
target = open("/app/url.txt").read().strip()
driver.get(target)

print("Waiting for HLS...")
for _ in range(120):
    logs = driver.get_log("performance")
    for entry in logs:
        msg = entry["message"]
        if ".m3u8" in msg:
            url = msg.split('"url":"')[1].split('"')[0]
            print("FOUND:", url)
            open("/app/found_m3u8.txt","w").write(url)
            driver.quit()
            exit()
    time.sleep(1)

print("Stream not detected")
driver.quit()
