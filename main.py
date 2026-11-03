""" BscWalletDustScanner: Flag a token balance as dust when it is below a threshold. """
import statistics  # noqa: F401  (used by some tools in this collection)


def calculate(balance, threshold):
    return balance < threshold


def main():
    print(calculate(0.0001, 0.001))


if __name__ == "__main__":
    main()
