SYMBOL_CONVERSION = [(",", "comma"), (".", "period"), (";", "semicolon"), ("/", "forward slash"), ("-", "minus sign"), ("[", "left bracket"), ("'", "quote"), ("=", "equals sign"), ("]", "right bracket"), ("\\", "backslash")]

class Note:
    def __init__(self, symbol):
        self.symbol = symbol
        self.symbolName = symbol

        # If symbol contains symbol name, convert to symbol
        for i in SYMBOL_CONVERSION:
            if self.symbol == i[0]:
                self.symbolName = i[1]

    # Returns the symbol
    def getSymbol(self):
        return self.symbol
    
    # Returns the name of the symbol
    def getSymbolName(self):
        return self.symbolName