from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'title')
worksheet.write('B1', 'des')
worksheet.write('C1', 'img')


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    options=options, executable_path="path/to/executable")
driver.get(
    'file:///home/hes/Downloads/%D8%AC%D8%AF%D9%88%D9%84%20%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA%20%D8%A8%D8%AF%D9%88%D9%86%20%D8%B9%D9%86%D9%88%D8%A7%D9%86/%D8%A7%D9%84%D9%88%D8%B1%D9%82%D8%A91.html')
x = driver.find_elements(By.TAG_NAME, 'a')
c = []
for e in x:
    c.append(e.get_attribute('href'))
    time.sleep(2)
    print("!")

time.sleep(3)
inter = 2
for y in c:
    driver.get(y)
    img = driver.find_element(By.CLASS_NAME, 'image_first_click')
    title = driver.find_element(By.CLASS_NAME, 'product-details__title')
    des = driver.find_element(By.CLASS_NAME, 'product-detials__desc')
    worksheet.write('A'+str(inter), title.text)
    worksheet.write('B'+str(inter), des.text)
    worksheet.write('C'+str(inter), img.get_attribute('src'))
    inter = inter+1
    print(inter)
    time.sleep(2)


workbook.close()

# for y in img:
#     print(y.get_attribute('src'))
#     print(title[0].text)
#     print(des[0].text)
