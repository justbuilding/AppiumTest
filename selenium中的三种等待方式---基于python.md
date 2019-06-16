## selenium中的三种等待方式---基于python



###### 我们在实际使用selenium或者appium时，等待下个等待定位的元素出现，特别是web端加载的过程，都需要用到等待，而等待方式的设置是保证脚本稳定有效运行的一个非常重要的手段，在selenium中（appium通用）常用的等待分为**显式等待WebDriverWait()**、**隐式等待implicitly_wait()**、**强制等待sleep()**三种

- sleep()： 强制等待，设置固定休眠时间。 python 的 time 包提供了休眠方法 sleep() ， 导入 time 包后就可以使用 sleep()，进行脚本的执行过程进行线程**休眠**。
- implicitly_wait()：隐式等待，也叫智能等待，是 webdirver 提供的一个超时等待。隐的等待一个元素被发现，或一个命令完成。如果超出了设置时间的则抛出异常。隐式等待可以理解成在规定的时间范围内，浏览器在不停的刷新页面，直到找到相关元素或者时间结束。**线程不休眠，隐式等待是针对全部元素设置的等待时间，一旦设置，这个隐式等待会在WebDriver对象实例的整个生命周期起作用。当于设置全局的等待，在定位元素时，对所有元素设置超时时间。（隐式等待就是针对页面的，是等页面加载，而不是元素加载，显式等待是针对元素的。）**
- WebDriverWait()：显式等待，同样也是 webdirver 提供的方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。默认检测频率为0.5s，默认抛出异常为：NoSuchElementException，线程**不休眠**，**显式等待是针对某个元素来设置的等待时间**。一般比较前面两方法快



```
#coding=utf-8
from selenium import webdriver
# 导入 WebDriverWait包
from selenium.webdriver.support.ui import WebDriverWait
# 导入 time 包
from sleep import  sleep


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# WebDriverWait()显式等待方法的使用
element=WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("kw"))   
element.send_keys("selenium")
# 添加隐式等待
driver.implicitly_wait(30)               
# implicitly_wait()比 sleep() 更智能，后者只能选择一个固定时间的等待，前者可在一个时间范围内智能的等待
driver.find_element_by_id("su").click()
# 添加固定休眠时间，sleep()方法以秒为单位，假如休眠时间小时 1 秒，可以用小数表示。
sleep(5)                     
driver.quit()
```

