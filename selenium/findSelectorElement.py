HUB_REMOTE = 'http://10.217.59.39:4444/wd/hub'
from selenium import webdriver
import time

op = webdriver.ChromeOptions()
# op.add_argument('--headless')
# "--log-level" sets the minimum log level.
# Valid values are from 0 to 3: INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3.
# op.add_argument('--log-level=3')
op.add_argument('--ignore-certificate-errors')
op.add_argument('--ignore-ssl-errors=yes')
ds = {'platform': 'ANY',
      'browserName': "chrome",
      'version': '',
      'javascriptEnabled': True,
      }
browser = webdriver.Remote(HUB_REMOTE, desired_capabilities=ds, options=op)
browser.get('https://{}'.format('www.sina.com.cn'))
time.sleep(1)
# 第一种方式，直接使用 select 标签的，这种情况可以直接使用selenium API
# selector = browser.find_element_by_id("Selector")
# select = Select(selector)
# select.selectByIndex(1)
# select.selectByVisibleText("123")
# select.selectByValue("1232")

# 第二种方式，下拉菜单不是通过 select 实现的，可以通过 JS 进行操作
# menu = browser.find_element_by_class_name('SI_Top_Blog')
a = browser.find_element_by_xpath('//*[@id="SI_Top_Blog"]/div/ul/li[1]')
print(a)
# action = Actions(browser)
# action.clickAndHold(menu).build().perform()
# technicalQuestion = browser.find_element_by_xpath("")
# technicalQuestion.click()
