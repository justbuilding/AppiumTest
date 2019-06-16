# from appium import webdriver
#
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.2'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = '.Calculator'

# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# #测试淘宝
# from appium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# desired_caps = {}
# desired_caps['platformName'] = "Android"         # 声明是ios还是Android系统
# desired_caps['platformVersion'] = '4.4.2'        # Android内核版本号，可以在夜神模拟器设置中查看
# desired_caps['deviceName'] = '127.0.0.1:62001'   # 连接的设备名称
# desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'    # apk的包名
# desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'  # apk的launcherActivity
# # desired_caps['appWaitActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)          # 建立 session
#
# time.sleep(5)
# print('+++++++')
# # 通过xpyth定位：find_element_by_xpath(“//android.widget.TextView[10]”) xpath下标从1开始，使用完整的classname
# # 通过text name：find_element_by_name（name对应uiautomator扫描后text的内容）
# # 通过id：find_element_by_id（id对应resource-id)
# # 通过classname定位：find_element_by_class_name(class_name对应class)
# # 通过accessibility id：find_element_by_accessibility_id(accessibility_id对应content-desc)
# # 定位到某个文本框，并输入内容：
# # driver.find_element_by_id(“xxxxx”) .send_keys(“123456”)
# # 滑动屏幕：
# # 获取屏幕尺寸 width=self.driver.get_window_size()[‘width’] height=self.driver.get_window_size()[‘height’]
# # 滑动屏幕 driver.swipe(width*9/10, height*1/2, width*1/10, height*1/2, 1000)
#
# # driver.find_element_by_id("************").click()         # 点击元素
# #
# # driver.find_element_by_xpath("************").click()      # 点击元素
# #
# # driver.find_element_by_xpath("************").send_keys(u'123456')   # 发送键值
# driver.quit()      # 退出 session

# import os
# import time
# import unittest
# from selenium import webdriver
#
#
#
# # 设置路径信息
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
#
#
# class LoginAndroidTests(unittest.TestCase):
#     def setUp(self):
#         # 初始化测试平台
#         desired_caps = {}
#         desired_caps['device'] = 'android'
#         desired_caps['platformName'] = 'Android'  # 测试平台
#         desired_caps['browserName'] = ''
#         desired_caps['version'] = '5.1.1500190521'  # 系统版本
#         desired_caps['deviceName'] = '127.0.0.1:62001'  # 模拟器名称
#         desired_caps['app-package'] = 'com.duowan.mobile'  # 要测试的app
#         desired_caps['app-activity'] = 'com.yy.mobile.plugin.homepage.ui.home.HomeActivity'  # 当前活动应用
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
#
# def tearDown(self):
#     self.driver.quit()
#
#
# def test_login(self):
#     time.sleep(30)
#     # 点击“注册登录”按钮
#     button = self.driver.find_element_by_id("com.subject.zhongchou:id/register_button")
#     button.click()
#     time.sleep(10)
#     # 登录
#     name = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_phone')
#     name.click()
#     name.send_keys('183XXXXX905')  # 输入用户名
#     psd = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_password')
#     psd.click()
#     psd.send_keys('XXXXXXX')  # 输入密码
#     blogin = self.driver.find_element_by_id('com.subject.zhongchou:id/go_numberlogin')  # 单击登录按钮
#     blogin.click()
#     time.sleep(10)
#     # 此处检测是否登录成功
#
#
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
#     unittest.TextTestRunner(verbosity=2).run(suite)


# 显式等待和隐式等待
# coding=utf-8
# from selenium import webdriver
# # 导入 WebDriverWait包
# from selenium.webdriver.support.ui import WebDriverWait
# # 导入 time 包
# from sleep import  sleep
#
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# # WebDriverWait()显式等待方法的使用
# element=WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("kw"))
# element.send_keys("selenium")
# # 添加隐式等待
# driver.implicitly_wait(30)
# # implicitly_wait()比 sleep() 更智能，后者只能选择一个固定时间的等待，前者可在一个时间范围内智能的等待
# driver.find_element_by_id("su").click()
# # 添加固定休眠时间，sleep()方法以秒为单位，假如休眠时间小时 1 秒，可以用小数表示。
# sleep(5)
# driver.quit()
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 向左滑动
def swipe_left():
    screen = get_size()
    x1 = int(screen[0]*0.9)
    y1 = int(screen[1]*0.5)
    x2 = int(screen[0]*0.1)
    driver.swipe(x1, y1, x2, y1, 1000)


def swipe_up():
    screen = get_size()
    x1 = int(screen[0] * 0.5)
    y1 = int(screen[1] * 0.95)
    y2 = int(screen[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)


def swipe_down():
    screen = get_size()
    x1 = int(screen[0] * 0.5)
    y1 = int(screen[1] * 0.35)
    y2 = int(screen[1] * 0.85)
    driver.swipe(x1, y1, x1, y2, 1000)


def swipe_right():
    screen = get_size()
    y1 = int(screen[1] * 0.5)
    x1 = int(screen[0] * 0.25)
    x2 = int(screen[0] * 0.95)
    driver.swipe(x1, y1, x2, y1, 1000)


desired_caps = {
    # 设备系统
    'platformName': 'Android',
    # 设备名称
    'deviceName': '127.0.0.1:62001',
    # 安卓版本
    'platformVersion': '5.1.1',
    # apk包名
    # 'appPackage': 'com.taobao.taobao',
    'appPackage': 'com.duowan.mobile',
    # apk的launcherActivity
    # 'appActivity': 'com.taobao.tao.welcome.Welcome',
    'appActivity': 'com.yy.mobile.plugin.homepage.ui.home.HomeActivity',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
    'resetKeyboard': True  # 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来
}
# 启动app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

live_video = WebDriverWait(driver, 10).until(lambda driver1: driver.find_element_by_xpath("//android.widget.TextView[@text = '直播']"))
live_video.click()
sleep(5)
# 点击个人中心
personal_center = WebDriverWait(driver, 10).until(lambda driver1: driver.find_element_by_xpath("//android.widget.TextView[@text = '个人中心']"))
personal_center.click()
sleep(5)

# 点击用户登录
user_login = WebDriverWait(driver, 100).until(lambda driver1: driver.find_element_by_id("com.yy.mobile.plugin.personalcenter:id/rl_user_info_no_login"))
user_login.click()
sleep(3)
# # user_login = driver.find_element_by_xpath("//android.widget.TextView[@text = '登录YY']")
# # user_login.click()
# # sleep(3)
# user_login = driver.find_element_by_xpath("//android.widget.TextView[0]")
# user_login.click()
# sleep(3)

# 输入账号
account = WebDriverWait(driver, 10).until(lambda driver1: driver.find_element_by_id("com.yy.mobile.plugin.main:id/EdtAccount"))
account.send_keys("13415145594")
sleep(3)

# 输入密码
password = WebDriverWait(driver, 10).until(lambda driver1: driver.find_element_by_id("com.yy.mobile.plugin.main:id/EdtPassword"))
password.send_keys("jyxy161060009")
sleep(3)

# 点击登录按钮
login_button = WebDriverWait(driver, 10).until(lambda driver1: driver.find_element_by_id("com.yy.mobile.plugin.main:id/btn_login"))
login_button.click()
sleep(10)

# 跳过关注主播
# skip = driver.find_element_by_id("com.yy.mobile.plugin.main:id/recommend_follow_pass")
# skip.click()
# sleep(2)
skip = WebDriverWait(driver, 10).until(lambda driver1: driver.find_element_by_xpath("//android.widget.TextView[@text = '跳过']"))
skip.click()
sleep(3)

# 点击直播
live_video = WebDriverWait(driver, 10).until(lambda driver1: driver.find_element_by_xpath("//android.widget.TextView[@text = '直播']"))
live_video.click()
sleep(2)

# 向左滑动2次
for i in range(2):
    swipe_left()
    sleep(0.5)
sleep(2)

# 向右滑动2次
for i in range(2):
    swipe_right()
    sleep(0.5)
sleep(2)

# 向上滑动2次
for i in range(2):
    swipe_up()
    sleep(0.5)
sleep(2)



