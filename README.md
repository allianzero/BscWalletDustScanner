# BscWalletDustScanner

Flag a token balance as dust when it is below a threshold.

## Features

- Small, dependency-free Python tool (standard library only).
- Pure function in `main.py` that is easy to import and reuse.
- Runnable example: `python main.py`.
- Unit test in `test_main.py`.

## Installation

Requires Python 3.10 or newer. No third-party dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Example:

```python
from main import calculate

result = calculate(0.0001, 0.001)  # -> True
print(result)
```

## Safety

This tool performs local calculations only. It never sends funds, never
stores a seed phrase or private key, and never makes network requests.
Validators in this collection check format only; never paste a real
seed phrase or private key into any tool you do not fully trust.

## License

MIT — see `LICENSE`.
