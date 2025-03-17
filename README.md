# Rakuten_bank_balance_check

## Overview

Get your Rakuten Bank balance easily with this Python package.

## Install from source
```sh
git clone https://github.com/Shibajob/Rakuten_bank_balance_check.git
cd Rakuten_bank_balance_check
pip install .
```

## Requirements
- Python 3.11.0
- selenium >= 4.5.0
- webdriver-manager >= 4.0.2

## How to use
```python
from Rakuten_bank_balance_check import Rakuten_bank_balance_check

account_id = "your_id"
account_pw = "your_password"

balance = Rakuten_bank_balance_check.Rakuten_bank_balance_check(account_id, account_pw)
print(f"Your balance: {balance}")
```

## LICENSE

This project is licensed under the MIT License.
