from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select

import time
import os

# Browser and Keys
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
actions = ActionChains(browser)

# Remove Everything in Array


def pop_all(value):
    result, value[:] = value[:], []
    return result


# Loop for Running
running = True

# Main
while running:
    # Essentials
    browser.get("https://hris.roc.com.ph/")
    time.sleep(5)
    print("\n")
    print("="*20)
    print("Please Wait...")
    time.sleep(3)
    print("Login to HRIS...")
    print("="*20)
    username = input("Input Username:")
    user_pass = input("Input Password:")
    print("="*10)
    os.system('cmd /c "cls"')
    print("Logging in... Please wait...")
    time.sleep(5)
    os.system('cmd /c "cls"')

    login_user = browser.find_element(by=By.NAME, value="work-email")
    login_user.send_keys(username)
    login_pass = browser.find_element(by=By.NAME, value="password")
    login_pass.send_keys(user_pass)

    submit_button = browser.find_element(
        by=By.NAME, value="submit-login")
    submit_button.click()
    time.sleep(5)

    employee_id = input("Input Employee ID:")
    browser.get(
        "https://hris.roc.com.ph/talents/attendance.php?employeeID="+employee_id)

    time.sleep(3)

    # CLick Attendance
    add_attendance = browser.find_element(by=By.ID, value="add-shift-button")
    add_attendance.click()

    # Arrays of Months and Days
    arr_months = []
    arr_days = []

    # Input Months
    num_month = input("Input How Many Months: ")
    for i in range(int(num_month)):
        month = input("Input Month Number (Eg. 01, 02, 03): ")
        arr_months.append(month)

    # For Loop in Months
    for i in range(int(num_month)):
        # Input Days
        num_days = input("How many (DAY)s in month " + arr_months[i] + ":")

        # For Loop in Days
        for k in range(int(num_days)):
            day = input("Input Day Number (Eg. 15, 30, 31): ")
            arr_days.append(day)

        # For Loop in adding Attendance
        for j in range(int(num_days)):
            print("Month: " + arr_months[i] + "\t" + "Day: " + arr_days[j])

            # Add Time In
            time_in = browser.find_element(
                by=By.NAME, value="time-in-submitted")
            time_in.send_keys(arr_months[i], arr_days[j], "2022")
            time_in.send_keys(Keys.TAB)
            time_in.send_keys("07:46AM")

            # Add Status
            status = Select(browser.find_element(
                by=By.ID, value="time-in-status"))
            status.select_by_visible_text('On Time')

            # Late Deduction
            late_deduction = browser.find_element(
                by=By.NAME, value="time-in-late-deduction")
            late_deduction.send_keys("00:00")

            # Upload Picture
            upload_picture = browser.find_element(
                by=By.XPATH, value="//input[@type='file']")
            upload_picture.send_keys(
                "C:\\Users\\Administrator\\Pictures\\DP.jpg")

            # Submit
            submit_button = browser.find_element(
                by=By.NAME, value="add-attendance-btn")
            submit_button.click()

            # Repeat
            add_attendance2 = browser.find_element(
                by=By.ID, value="add-shift-button")
            add_attendance2.click()

            # Wait Time
            time.sleep(2)

        # Remove Days in Array
        pop_all(arr_days)
        print("Reset Days Array")

    # Exit or Change Employee ID
    asking = input("Do you want to exit? (Y/N): ")
    if asking == "Y":
        print("Exiting...")
        for i in range(5):
            print(5-i)
            time.sleep(1)
            running = False
    else:
        break
