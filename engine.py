import random
import time

coins = [
    "SIREN/USDT",
    "PIPPIN/USDT",
    "PEPE/USDT",
    "BONK/USDT",
    "FLOKI/USDT",
    "WIF/USDT",
    "AURA/USDT"
]

def pump_dna_score():
    return random.randint(50, 100)

def scan_market():
    results = []

    for coin in coins:
        score = pump_dna_score()
        results.append((coin, score))

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:3]

def run_engine():
    top3 = scan_market()

    print("\n🔥 TOP 3 PUMP CANDIDATES (4H CYCLE)\n")

    for i, (coin, score) in enumerate(top3, 1):
        print(f"{i}. {coin} → Pump Score: {score}")

if __name__ == "__main__":
    run_engine()
