import requests

BASE_URL = "https://api.coinex.com/v1/market/ticker/all"

def get_market_data():
    """
    گرفتن دیتا واقعی از CoinEx
    """
    try:
        res = requests.get(BASE_URL, timeout=10)
        data = res.json()

        if data["code"] != 0:
            print("API Error")
            return {}

        return data["data"]["ticker"]

    except Exception as e:
        print("Request failed:", e)
        return {}

def calculate_score(coin_data):
    """
    ساخت Pump Score ساده از داده واقعی
    """
    try:
        # حجم 24h
        vol = float(coin_data.get("vol", 0))

        # تغییر قیمت
        change = float(coin_data.get("change", 0))

        # فرمول ساده امتیازدهی
        score = (vol / 100000) + (change * 10)

        return round(score, 2)

    except:
        return 0

def scan_market():
    data = get_market_data()

    results = []

    for symbol, info in data.items():

        # فقط USDT pairs
        if "USDT" not in symbol:
            continue

        score = calculate_score(info)

        results.append((symbol, score))

    # مرتب‌سازی بر اساس امتیاز
    results.sort(key=lambda x: x[1], reverse=True)

    return results[:3]

def run_engine():
    top3 = scan_market()

    print("\n🔥 TOP 3 REAL PUMP CANDIDATES\n")

    for i, (coin, score) in enumerate(top3, 1):
        print(f"{i}. {coin} → Score: {score}")

if __name__ == "__main__":
    run_engine()
