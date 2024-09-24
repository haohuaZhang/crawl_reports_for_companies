from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import requests

# 配置 Firefox 浏览器选项
options = Options()
options.set_preference('permissions.default.image', 2)  # 禁用图片加速加载
options.add_argument('--headless')  # 后台运行
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 指定 geckodriver 的路径，使用 Service 来设置
service = Service('/usr/local/bin/geckodriver')

# 创建 WebDriver 实例
driver = webdriver.Firefox(service=service, options=options)

# 访问雪球网首页
driver.get("https://xueqiu.com/")

# 等待页面加载（可以根据需要调整时间或使用更智能的等待方式）
time.sleep(5)

# 获取 cookies
cookies = driver.get_cookies()

# 关闭浏览器
driver.quit()

# 将 cookies 转换为字典
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

# 设置请求的 URL
url = "https://stock.xueqiu.com/v5/stock/finance/cn/income.json?symbol=SH688049&type=all&is_detail=true&count=5&timestamp=1727159190458"

# 设置请求头，模仿浏览器的请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://xueqiu.com/',
    'Origin': 'https://xueqiu.com',
}

# 发送带 cookies 的请求
response = requests.get(url, headers=headers, cookies=cookies_dict)

# 检查响应状态
if response.status_code == 200:
    # 解析 JSON 数据
    data = response.json()
    print(data)
else:
    print(f"请求失败，状态码: {response.status_code}")
