from selenium import webdriver
from Sel_Python.setting import actiUrl,chromePath
import time

def writeData(data):
    fileObj = open("pythonSel.txt","w")
    fileObj.write(data)
    fileObj.close()

def webElementText():
    driver = webdriver.Chrome(executable_path=chromePath)
    driver.maximize_window()
    driver.get(url=r"C:\Users\WORK\PycharmProjects\PythonSelenium\Sel_Python\Assignments\index.html")
    time.sleep(4)
    pattern = "ul#subjects>li"
    webEleRef = driver.find_elements_by_css_selector(pattern)
    print("web element ref",webEleRef)
    print(type(webEleRef), len(webEleRef))
    listData =  []
    #listData.append(webEleRef[0].text)
    dictData = {}
    for i in range(len(webEleRef)):
        listData.append(webEleRef[i].text)
        dictData.setdefault(webEleRef[i].tag_name+str(i),listData[i])
    print("data in list",listData)
    print("dict data", dictData)
    driver.close()

webElementText()