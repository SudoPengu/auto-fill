from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select


import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
actions = ActionChains(browser)


# Essentials
time.sleep(3)
browser.get("https://hris.roc.com.ph/")
username = input("Input Username:")
user_pass = input("Input Password:")

actions = actions.send_keys(Keys.TAB)

print("Logging in... Please wait...")
login_user = browser.find_element(by=By.NAME, value="work-email")
login_user.send_keys(username)
login_pass = browser.find_element(by=By.NAME, value="password")
login_pass.send_keys(user_pass)

submit_button = browser.find_element(
    by=By.NAME, value="submit-login")
submit_button.click()

time.sleep(3)
employee_id = input("Input Employee ID:")
browser.get(
    "https://hris.roc.com.ph/talents/attendance.php?employeeID="+employee_id)

time.sleep(3)

# Attendance
add_attendance = browser.find_element(by=By.ID, value="add-shift-button")
add_attendance.click()

arr_months = []
arr_days = []

month = input("Input Month Number (Eg. 06, 12): ")
arr_months.append(month)
num_days = input("How many days: ")
for i in range(int(num_days)):
    day = input("Input Day Number (Eg. 15, 30, 31): ")
    arr_days.append(day)


for i in range(int(num_days)):
    print("Month: " + month)
    print("Day: " + arr_days[i])

    # Add Time In
    time_in = browser.find_element(by=By.NAME, value="time-in-submitted")
    time_in.send_keys(month, arr_days[i], "2022")
    time_in.send_keys(Keys.TAB)
    time_in.send_keys("07:46AM")

    # Add Status
    status = Select(browser.find_element(by=By.ID, value="time-in-status"))
    status.select_by_visible_text('On Time')

    # Late Deduction
    late_deduction = browser.find_element(
        by=By.NAME, value="time-in-late-deduction")
    late_deduction.send_keys("00:00")

    # Upload Picture
    upload_picture = browser.find_element(
        by=By.XPATH, value="//input[@type='file']")
    upload_picture.send_keys("C:\\Users\\Administrator\\Pictures\\DP.jpg")

    # Submit
    submit_button = browser.find_element(
        by=By.NAME, value="add-attendance-btn")
    submit_button.click()

    # Repeat
    add_attendance2 = browser.find_element(by=By.ID, value="add-shift-button")
    add_attendance2.click()

    time.sleep(1)
