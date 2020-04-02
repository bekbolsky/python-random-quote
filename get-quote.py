import random


def primary():
    with open("quotes.txt") as f:
        quotes = f.read().splitlines()
        last = len(quotes) - 1
        rnd = random.randint(0, last)
        print(quotes[rnd])


if __name__ == "__main__":
    primary()
