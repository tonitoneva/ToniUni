def get_symbols (first, second):
    collected_symbols = []
    for symbol in range(ord(first)+1, ord(second)):
        collected_symbols.append(chr(symbol))
    return collected_symbols
first_symbol = input()
second_symbol = input()
result = get_symbols(first_symbol, second_symbol)
print(" ".join(result))
