import re
import time
import requests
from bs4 import BeautifulSoup

#معالج
url = "https://www.masrawy.com/gold"
headers = {"User-Agent": "Mozilla/5.0"}

# حفظ اخر نتيجة 10 دقائق حتى لا نطلب الموقع مع كل رسالة
cache = {"time": 0, "text": ""}
karats = ["24", "21", "18", "14", "10"]


def get_price(page_text):
    # البحث عن كل عيار ثم اخذ رقمين بعده (البيع ثم الشراء)
    prices = {}
    pattern = r"عيار\s*(\d+)\D{0,20}?(\d[\d,]*\.?\d*)\D{0,20}?(\d[\d,]*\.?\d*)"
    for k, sell, buy in re.findall(pattern, page_text):
        if k in karats and k not in prices:
            prices[k] = (sell, buy)
    return prices


def get_gold():
    # اذا مرت اقل من 10 دقائق نرجع النتيجة المحفوظة
    if cache["text"] != "" and time.time() - cache["time"] < 600:
        return cache["text"]

    try:
        page = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(page.content, "lxml")
        page_text = soup.get_text(" ", strip=True)
        prices = get_price(page_text)
    except Exception:
        return "تعذر جلب اسعار الذهب حاليا"

    if len(prices) == 0:
        return "تعذر قراءة اسعار الذهب من الموقع"

    text = "اسعار الذهب في مصر (جنيه مصري)\n"
    for k in karats:
        if k in prices:
            text = text + "عيار " + k + " : بيع " + prices[k][0] + " | شراء " + prices[k][1] + "\n"
    text = text + "المصدر: masrawy.com"

    cache["time"] = time.time()
    cache["text"] = text
    return text


if __name__ == "__main__":
    print(get_gold())
