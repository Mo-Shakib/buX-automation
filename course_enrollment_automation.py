from selenium import webdriver
import os, time

# adding the chromedriver folder location to PATH variable
os.environ['PATH'] += r"E:/GitHub/buX-automation"

# User info:
bux_email = input('Enter your email address for buX: ')
bux_password = input('Password: ')
courses = list(input('Enter courses code you want to enroll (separated by comma):').split(','))

driver = webdriver.Chrome()

def buX_login(email, password):
    driver.get('https://bux.bracu.ac.bd/login')
    emailForm = driver.find_element_by_xpath('//*[@id="login-email"]')
    emailForm.send_keys(email)
    passwordForm = driver.find_element_by_xpath('//*[@id="login-password"]')
    passwordForm.send_keys(password)
    loginButton = driver.find_element_by_xpath('//*[@id="login"]/button')
    loginButton.click()
    time.sleep(10)
    print('[] - Login Successfull ')

def enroll_course(course_code):
    driver.get(f'https://bux.bracu.ac.bd/courses/course-v1:buX+{course_code.upper()}+2021_Fall/about')
    enroll_Course = driver.find_element_by_xpath('//*[@id="content"]/section/header[2]/div/div[2]/h1/div/a')
    enroll_Course.click()
    time.sleep(10)
    
    
buX_login(bux_email,bux_password)
for i in courses:
    enroll_course(i.strip())
    
driver.quit()