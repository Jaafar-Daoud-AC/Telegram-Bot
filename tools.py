import math

#معالج
# الرموز المسموحة في الحاسبة فقط (بدون ** حتى لا تتعطل المعالجة باعداد ضخمة)
allowed = "0123456789+-*/(). %"


def calc(text):
    text = text.strip()
    if text == "":
        return "اكتب العملية بعد الامر مثل: /calc 5*(2+3)"
    if len(text) > 100 or "**" in text:
        return "العملية غير مقبولة"
    for c in text:
        if c not in allowed:
            return "يسمح فقط بالارقام والرموز + - * / % ( )"

    try:
        result = eval(text, {"__builtins__": {}}, {})
    except ZeroDivisionError:
        return "لا يمكن القسمة على صفر"
    except Exception:
        return "العملية غير صحيحة"

    if isinstance(result, float):
        result = round(result, 10)
        if result.is_integer():
            result = int(result)
    return text + " = " + str(result)


def to_db(text):
    # تحويل النسبة الى ديسيبل للقدرة وللجهد
    try:
        ratio = float(text.strip())
    except Exception:
        return "اكتب النسبة بعد الامر مثل: /db 100"
    if ratio <= 0:
        return "النسبة يجب ان تكون اكبر من صفر"

    power = round(10 * math.log10(ratio), 4)
    voltage = round(20 * math.log10(ratio), 4)
    return ("نسبة " + text.strip() + "\n"
            "قدرة: 10 log10(P2/P1) = " + str(power) + " dB\n"
            "جهد: 20 log10(V2/V1) = " + str(voltage) + " dB")
