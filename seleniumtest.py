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


# 控制浏览器窗口大小
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


# 控制浏览器后退、前进
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


# #其他常用方法
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# # 获得输入框的尺寸
# size = driver.find_element_by_id('kw').size
# print(size)
#
# # 返回百度页面底部备案信息
# text = driver.find_element_by_id("cp").text
# print(text)
#
# # 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
# attribute = driver.find_element_by_id("kw").get_attribute('type')
# print(attribute)
#
# # 返回元素的结果是否可见， 返回结果为 True 或 False
# result = driver.find_element_by_id("kw").is_displayed()
# print(result)
#
# driver.quit()


# 鼠标悬停操作
"""

在 WebDriver 中， 将这些关于鼠标操作的方法封装在 ActionChains 类提供。

ActionChains 类提供了鼠标操作的常用方法：

perform()： 执行所有 ActionChains 中存储的行为；

context_click()： 右击；

double_click()： 双击；

drag_and_drop()： 拖动；

move_to_element()： 鼠标悬停。

导入提供鼠标操作的 ActionChains 类。

ActionChains(driver)
调用 ActionChains()类， 将浏览器驱动 driver 作为参数传入。

move_to_element(above)
context_click()方法用于模拟鼠标右键操作， 在调用时需要指定元素定位。

perform()
执行所有 ActionChains 中存储的行为， 可以理解成是对整个操作的提交动作。
"""

# from selenium import webdriver
# # 引入 ActionChains 类
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.cn")
#
# # 定位到要悬停的元素
# above = driver.find_element_by_link_text("设置")
# # 对定位到的元素执行鼠标悬停操作
# ActionChains(driver).move_to_element(above).perform()


"""
需要说明的是， 下面的脚本没有什么实际意义， 仅向我们展示模拟键盘各种按键与组合键的用法。

from selenium.webdriver.common.keys import Keys
在使用键盘按键方法前需要先导入 keys 类。



以下为常用的键盘操作：

send_keys(Keys.BACK_SPACE)  删除键（BackSpace）

send_keys(Keys.SPACE)       空格键(Space)

send_keys(Keys.TAB)         制表键(Tab)

send_keys(Keys.ESCAPE)      回退键（Esc）

send_keys(Keys.ENTER)       回车键（Enter）

send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）

send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）

send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）

send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）

send_keys(Keys.F1)          键盘 F1

……

send_keys(Keys.F12)         键盘 F12
"""
# from selenium import webdriver
# # 引入 Keys 模块
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# # 输入框输入内容
# driver.find_element_by_id("kw").send_keys("seleniumm")
# sleep(2)
# # 删除多输入的一个 m
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# sleep(2)
#
#
# # 输入空格键+“教程”
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# driver.find_element_by_id("kw").send_keys("教程")
# sleep(2)
#
# # ctrl+a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
# sleep(2)
#
# # ctrl+x 剪切输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
# sleep(2)
#
# # ctrl+v 粘贴内容到输入框
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
# sleep(2)
#
# # 通过回车键来代替单击操作
# driver.find_element_by_id("su").send_keys(Keys.ENTER)
# sleep(2)
#
# driver.quit()


"""
不管是在做功能测试还是自动化测试，最后一步需要拿实际结果与预期进行比较。这个比较的称之为断言。

我们通常可以通过获取title 、URL和text等信息进行断言。text方法在前面已经讲过，它用于获取标签对之间的文本信息。 下面同样以百度为例，介绍如何获取这些信息。



"""
# from selenium import webdriver
# from time import sleep
#
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# print('Before search================')
#
# # 打印当前页面title
# title = driver.title
# print(title)
#
# # 打印当前页面URL
# now_url = driver.current_url
# print(now_url)
#
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# sleep(1)
#
# print('After search================')
#
# # 再次打印当前页面title
# title = driver.title
# print(title)
#
# # 打印当前页面URL
# now_url = driver.current_url
# print(now_url)
#
# # 获取结果数目
# result_num = driver.find_element_by_class_name('nums').text
# print(result_num)
#
# driver.quit()


# 显式等待和隐式等待
"""
显式等待
显式等待使WebdDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# element = WebDriverWait(driver, 5, 0.5).until(
#                       EC.presence_of_element_located((By.ID, "kw"))
#                       )
# element.send_keys('selenium')
# driver.quit()
"""
WebDriverWait类是由WebDirver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。具体格式如下：

WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver ：浏览器驱动。

timeout ：最长超时时间，默认以秒为单位。

poll_frequency ：检测的间隔（步长）时间，默认为0.5S。

ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。

WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。

until(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为True。

until_not(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为False。

在本例中，通过as关键字将expected_conditions 重命名为EC，并调用presence_of_element_located()方法判断元素是否存在。
"""

"""
隐式等待
WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0。它的用法相对来说要简单得多。
"""
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from time import ctime
#
# driver = webdriver.Chrome()
#
# # 设置隐式等待为10秒
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
#
# try:
#     print(ctime())
#     driver.find_element_by_id("kw22").send_keys('selenium')
# except NoSuchElementException as e:
#     print(e)
# finally:
#     print(ctime())
#     driver.quit()


"""
implicitly_wait()
默认参数的单位为秒，本例中设置等待时长为10秒。首先这10秒并非一个固定的等待时间，它并不影响脚本的执行速度。
其次，它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；
如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。假设在第6秒定位到了元素则继续执行，
若直到超出设置时长（10秒）还没有定位到元素，则抛出异常。
"""


"""
定位一组元素,定位一组元素的方法与定位单个元素的方法类似，唯一的区别是在单词element后面多了一个s表示复数
find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_link_text()
find_elements_by_partial_link_text()
find_elements_by_xpath()
find_elements_by_css_selector()
"""
#
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# sleep(1)
#
# # 定位一组元素
# texts = driver.find_elements_by_xpath('//div/h3/a')
#
# # 循环遍历出每一条搜索结果的标题
# for t in texts:
#     print(t.text)
#
# driver.quit()


"""
在Web应用中经常会遇到frame/iframe表单嵌套页面的应用，WebDriver只能在一个页面上对元素识别与定位，
对于frame/iframe表单内嵌页面上的元素无法直接定位。这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面中

<html>
  <body>
    ...
    <iframe id="x-URS-iframe" ...>
      <html>
         <body>
           ...
           <input name="email" >

126邮箱登录框的结构大概是这样子的，想要操作登录框必须要先切换到iframe表单

from selenium import webdriver
driver = webdriver.Firefox()
driver.switch_to.frame(0)  # 1.用frame的index来定位，定位第一个frame （index 下标从0开始）
"""
"""
# xpath 绝对路径 定位难，不要用
# driver.find_element_by_xpath('/div[1]/div[1]/div[1]/form/div/div[0]/div[1]/input').clear()


# xpath 相对路径 定位好
<html>
<div>
<input class='btn',name="button1">
</div>
<div>
    <span>
         <input   class='btn',name="button2">
    </span>
</div>
</html>

# driver = webdriver.Firefox()
# driver.get("http://www.chesudi.com")
# element = driver.find_element_by_xpath(.//input[@class="btn"])
# """
# from selenium import webdriver
# from time import sleep
#
#
# driver = webdriver.Chrome()
# driver.get("http://www.126.com")
# sleep(3)
# driver.find_element_by_id("switchAccountLogin").click() # 找到密码登录按钮按下
# sleep(3)
# # i=driver.find_element_by_id("x-URS-iframe") 由于定位的id是随机，故不可用，直接定位frame(0)即第一个frame
# driver.switch_to.frame(0)
# sleep(3)
# driver.find_element_by_name("email").clear()
# driver.find_element_by_name("email").send_keys("username")
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("password")
# driver.find_element_by_id("dologin").click()
# driver.switch_to.default_content() # 在进入多级表单的情况下，可以通过switch_to.default_content()跳回最外层的页面
# sleep(3)
# driver.quit()


