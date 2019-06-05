#
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
#
# print(driver.title)
#
# driver.quit()



#控制浏览器窗口大小
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# # 参数数字为像素点
# print("设置浏览器宽480、高800显示")
# driver.set_window_size(480, 800)
# driver.quit()



#控制浏览器后退、前进
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
#
# #访问百度首页
# first_url= 'http://www.baidu.com'
# print("now access %s" %(first_url))
# driver.get(first_url)
#
# #访问新闻页面
# second_url='http://news.baidu.com'
# print("now access %s" %(second_url))
# driver.get(second_url)
#
# #返回（后退）到百度首页
# print("back to  %s "%(first_url))
# driver.back()
#
# #前进到新闻页
# print("forward to  %s"%(second_url))
# driver.forward()
#
# driver.quit()



# #点击和输入
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# driver.find_element_by_id("kw").clear()#百度输入框的id为kw
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()#百度按钮的id为su
#
# driver.quit()



#其他常用方法
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

# 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见， 返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.quit()

