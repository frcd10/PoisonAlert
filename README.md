# PoisonAlert

Detects Solana address poisoning attacks by comparing addresses you want to send to against your transaction history.

## How it works
1. First address with a given prefix/suffix in your history = original
2. If you try to send to an address with same prefix/suffix but different middle = **ALERT**

## Usage
1. Set `sending_to` in `poison_alert.py` to the address you want to send to
2. Run: `python3 poison_alert.py`

## Sample
```
sending_to = "2LJTKDYmtF8U1L6s49AfFakeFakeFakeFakeFakeQRf1VF"
```
Output:
```
⚠️  POISON ADDRESS ALERT! ⚠️
Sending to: 2LJTKDYmtF8U1L6s49AfFakeFakeFakeFakeFakeQRf1VF
Looks like: 2LJTKDYmtF8U1L6s49AfRZALVz7LGLBWwvJ1w3QRf1VF
First 5: 2LJTK | Last 5: Rf1VF
Middle is DIFFERENT - DO NOT SEND!
```
