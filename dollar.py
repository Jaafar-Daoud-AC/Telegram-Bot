import time
import requests

#معالج
url = "https://open.er-api.com/v6/latest/USD"
currencies = {"SYP": "الليرة السورية", "EGP": "الجنيه المصري", "TRY": "الليرة التركية", "EUR": "اليورو"}

# حفظ اخر نتيجة 10 دقائق
cache = {"time": 0, "text": ""}


def get_dollar():
    if cache["text"] != "" and time.time() - cache["time"] < 600:
        return cache["text"]

    try:
        data = requests.get(url, timeout=10).json()
        rates = data["rates"]
    except Exception:
        return "تعذر جلب سعر الدولار حاليا"

    text = "سعر 1 دولار امريكي:\n"
    for code in currencies:
        if code in rates:
            text = text + currencies[code] + " : " + str(round(rates[code], 2)) + "\n"
    text = text + "الاسعار رسمية من open.er-api.com وقد تختلف عن سعر السوق"

    cache["time"] = time.time()
    cache["text"] = text
    return text


if __name__ == "__main__":
    print(get_dollar())
