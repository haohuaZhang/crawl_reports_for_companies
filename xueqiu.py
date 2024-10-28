from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import pandas as pd
import time
import requests


def get_column_data(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)
    
    # 获取第一列（除去前两行）的非空值
    column_data = df.iloc[2:, 0].dropna().to_numpy()
    
    return column_data


def get_xueqiu_data():
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

    try:
        # 访问雪球网首页
        driver.get("https://xueqiu.com/")
        
        # 等待页面加载
        time.sleep(5)

        # 获取 cookies
        cookies = driver.get_cookies()

        # 将 cookies 转换为字典
        cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
    finally:
        # 确保浏览器被关闭
        driver.quit()

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
        return data  # 返回获取的数据
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None
    
# 获取公司最新的年度报告和半年度报告链接
def get_symbols(companies):

    # 输入公司名，从https://xueqiu.com/k?q=获取公司的股票号，然后再去请求接口数据
    urls = build_announcement_urls(stock_id, reportTypes)
    report_urls = {}  # 初始化字典，避免在异常情况下未定义
    for url in urls:
        driver.get(url)

        try:
            # 等待页面加载完成
            WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.datelist'))
            )
            
            # 获取页面源码
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            # 查找符合条件的报告链接
            links = get_reports_urls(soup, years)

            # 检查链接是否为 BeautifulSoup 对象
            for link in links:
                if isinstance(link, str):
                    # 如果 link 是字符串，则解析为 <a> 标签
                    link = BeautifulSoup(link, 'html.parser').a
                text = link.text.strip()  # 获取 <a> 标签的文本
                href = 'https://vip.stock.finance.sina.com.cn/' + link['href']       # 获取 href 属性
                report_urls[text] = href  # 将文本作为 key，href 作为 value


        except Exception as e:
            print(f"获取报告链接时出现错误: {e}")
            # 返回一个空字典，而不是 None
            report_urls = {}

    return report_urls

# 调用函数并获取 Excel 文件的第一列数据
file_path = './template/营收-净利润-应收账款-经营活动产生的现金流量净额（万元）.xlsx'  # 替换为你的文件路径
column_data = get_column_data(file_path)
print("Excel 第一列数据：", column_data)

# 获取雪球网数据
# xueqiu_data = get_xueqiu_data()
# print("雪球网数据：", xueqiu_data)