import json
from pathlib import Path

sending_to = "2LJTKDYmtF8U1L6s49AfFakeFakeFakeFakeFakeQRf1VF"
TX_FILE = Path("sample_transactions.json")

def load_senders(path):
    if not path.exists():
        return []
    return [tx["from"] for tx in json.loads(path.read_text()) if "from" in tx]

def check_poison(address, senders):
    if not senders:
        print("No history.")
        return
    
    originals = {}
    for s in senders:
        if len(s) >= 10:
            key = (s[:5], s[-5:])
            if key not in originals:
                originals[key] = s
    
    if len(address) >= 10:
        key = (address[:5], address[-5:])
        if key in originals and address != originals[key]:
            print("=" * 60)
            print("⚠️  POISON ADDRESS ALERT! ⚠️")
            print("=" * 60)
            print(f"Sending to: {address}")
            print(f"Looks like: {originals[key]}")
            print(f"First 5: {address[:5]} | Last 5: {address[-5:]}")
            print("Middle is DIFFERENT - DO NOT SEND!")
            print("=" * 60)
            return
    
    print(f"✓ OK: {address}")

if sending_to:
    check_poison(sending_to, load_senders(TX_FILE))
