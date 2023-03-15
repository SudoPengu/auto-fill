import pyautogui
import time


# User Information
user_id = input("Employee ID: ")
f_name = input("First Name: ")
m_name = input("Middle Name: ")
l_name = input("Last Name: ")
school = input("School: ")
course = input("Course/K12 Type(N/A for None): ")
major = input("Major/Strand Type(N/A for None): ")

# Essentials
number = "09123456789"
user_passord = "12345678"
year = "0000"
user_email = user_id+"@roc.com.ph"

# Date
date = "03082023"


print("Hover to Form First Name")

time.sleep(5)

# Create Python Auto Typer Function

# Personal Information
pyautogui.write(f_name)
pyautogui.press("tab")
pyautogui.write(m_name)
pyautogui.press("tab")
pyautogui.write(l_name)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write(date)
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")

# Contact Information
pyautogui.write(number)
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write(user_email)
pyautogui.press("tab")

# Address Information
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("Philippines")
pyautogui.press("tab")
pyautogui.write("Philippines")
pyautogui.press("tab")


# Emergency Contact

# Father
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write(date)
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write(number)
pyautogui.press("tab")

# Mother
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write(date)
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write(number)
pyautogui.press("tab")

# Guardian
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write(date)
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write(number)
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")


# Employee Information

pyautogui.write(user_id)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")

# Current School Information
pyautogui.write(school)
pyautogui.press("tab")
pyautogui.write(course)
pyautogui.press("tab")
pyautogui.write(major)
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("500")
pyautogui.press("tab")

# Coordinator

pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write(number)
pyautogui.press("tab")

# Education History

# College
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("0000")
pyautogui.press("tab")
pyautogui.write("0000")
pyautogui.press("tab")

# Senior High School

pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("0000")
pyautogui.press("tab")
pyautogui.write("0000")
pyautogui.press("tab")

# Junior High School

pyautogui.write("N/A")
pyautogui.press("tab")
pyautogui.write("0000")
pyautogui.press("tab")
pyautogui.write("0000")
pyautogui.press("tab")
pyautogui.press("enter")

# User Credentioals

pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("tab")
pyautogui.write("12345678")
