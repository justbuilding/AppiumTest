# from appium import webdriver
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.2'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = '.Calculator'
#
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

import os
import time
import unittest
from selenium import webdriver



# 设置路径信息
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        # 初始化测试平台
        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'Android'  # 测试平台
        desired_caps['browserName'] = ''
        desired_caps['version'] = '5.1.1500190521'  # 系统版本
        desired_caps['deviceName'] = '127.0.0.1:62001'  # 模拟器名称
        desired_caps['app-package'] = 'com.duowan.mobile'  # 要测试的app
        desired_caps['app-activity'] = 'com.yy.mobile.plugin.homepage.ui.home.HomeActivity'  # 当前活动应用
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def tearDown(self):
    self.driver.quit()


def test_login(self):
    time.sleep(30)
    # 点击“注册登录”按钮
    button = self.driver.find_element_by_id("com.subject.zhongchou:id/register_button")
    button.click()
    time.sleep(10)
    # 登录
    name = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_phone')
    name.click()
    name.send_keys('183XXXXX905')  # 输入用户名
    psd = self.driver.find_element_by_id('com.subject.zhongchou:id/loginnumber_password')
    psd.click()
    psd.send_keys('XXXXXXX')  # 输入密码
    blogin = self.driver.find_element_by_id('com.subject.zhongchou:id/go_numberlogin')  # 单击登录按钮
    blogin.click()
    time.sleep(10)
    # 此处检测是否登录成功


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
