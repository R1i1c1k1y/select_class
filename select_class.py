from selenium import webdriver
import time
import datetime

from selenium.webdriver.common.by import By
url='https://qhfzkzxt.tsinghuax.com/airschool/sys/to/login'
options=webdriver.EdgeOptions()

options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
edge=webdriver.Edge(options=options)
edge.get(url)
time.sleep(1)
edge.switch_to.frame("uc-iframe")
un=edge.find_element(By.XPATH,'//*[@id="user"]')
pd=edge.find_element(By.XPATH,'//*[@id="pwd1"]')
un.send_keys('')#用户名
pd.send_keys('')#密码
bt=edge.find_element(By.XPATH,'//*[@id="form_container"]/form/a')
bt.click()
time.sleep(1)
bt=edge.find_element(By.XPATH,'//*[@id="student_my"]')
bt.click()
time.sleep(1)
bt=edge.find_element(By.XPATH,'//*[@id="student-course-schedule"]//td[@rowspan="2"]')
bt.click()
time.sleep(1)
bt=edge.find_element(By.XPATH,'//a[@pagenum=""]')#课程所在页面按钮的xpath路径
bt.click()
while True:
    now=datetime.datetime.now()
    now=now.strftime("%Y-%m-%d %H:%M:%S")
    date_now,time_now=now.split(' ')
    if date_now=='2022-10-07':
        if time_now[0:2]=='09':
            bt=edge.find_element(By.XPATH,'')#选择课程按钮的xpath路径
            bt.click()
            break