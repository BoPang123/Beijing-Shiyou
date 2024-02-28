import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def fetch_exchange_rate(date, currency_code):
    # 创建 Chrome WebDriver
    driver = webdriver.Chrome()

    # 加载页面
    url = "https://www.boc.cn/sourcedb/whpj/index.html"
    driver.get(url)

    # 输入起始日期
    start_date_input = driver.find_element(By.NAME, "erectDate")
    start_date_input.clear()
    start_date_input.send_keys(date)

    # 输入结束日期
    end_date_input = driver.find_element(By.NAME, "nothing")
    end_date_input.clear()
    end_date_input.send_keys(date)

    # 选择货币选项
    currency_select = Select(driver.find_element(By.NAME, "pjname"))
    currency_select.select_by_visible_text(currency_code)

    # 点击查询按钮
    # 获取所有具有相同类名的按钮
    buttons = driver.find_elements(By.CLASS_NAME, "search_btn")

    # 选择第一个按钮并点击
    buttons[1].click()


    # 等待页面加载
    time.sleep(5)

    # 获取现汇卖出价

    # 定位到包含数据的<table>
    table = driver.find_element(By.XPATH, "//div[@class='BOC_main publish']//table")

    # 获取第一个<tr>中的第三个记录
    exchange_rate = table.find_element(By.XPATH, "//tr[2]/td[4]").text
    # 关闭 WebDriver
    driver.quit()

    return exchange_rate

def currency_to_chinese_name(currency_code):
    currency_names = {
               "USD": "美元",
        "GBP": "英镑",
        "HKD": "港币",
        "CHF": "瑞士法郎",
        "SGD": "新加坡元",
        "SEK": "瑞典克朗",
        "DKK": "丹麦克朗",
        "NOK": "挪威克朗",
        "JPY": "日元",
        "CAD": "加拿大元",
        "AUD": "澳大利亚元",
        "EUR": "欧元",
        "MOP": "澳门元",
        "PHP": "菲律宾比索",
        "THB": "泰国铢",
        "NZD": "新西兰元",
        "KRW": "韩元",
        "RUB": "卢布",
        "MYR": "林吉特",
        "TWD": "新台币",
        "ESP": "西班牙比塞塔",
        "ITL": "意大利里拉",
        "NLG": "荷兰盾",
        "BEF": "比利时法郎",
        "FIM": "芬兰马克",
        "IDR": "印尼卢比",
        "BRL": "巴西里亚尔",
        "AED": "阿联酋迪拉姆",
        "INR": "印度卢比",
        "ZAR": "南非兰特",
        "SAR": "沙特里亚尔",
        "TRY": "土耳其里拉",

    }
    return currency_names.get(currency_code)


def main():
    try:
        # 从终端输入日期和货币代号
        # date = input()
        # currency_code = input()
        # date="20240228"
        # currency_code="USD"
        if len(sys.argv) != 3:
            print("Usage: python3 yourcode.py <date> <currency_code>")
            sys.exit(1)

        date = sys.argv[1]
        currency_code = sys.argv[2]
        currency_code=currency_to_chinese_name(currency_code)
        exchange_rate = fetch_exchange_rate(date, currency_code)
        # print(f"日期：{date}，货币代号：{currency_code}，现汇卖出价：{exchange_rate}")
        print(exchange_rate)
        # 将结果写入文件
        with open("result.txt", "w") as f:
            f.write(exchange_rate)
            # f.write(f"日期：{date}，货币代号：{currency_code}，现汇卖出价：{exchange_rate}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
