SYMBOL_CONVERSION = [(",", "comma"), (".", "period"), (";", "semicolon"), ("/", "forward slash"), ("-", "minus sign"), ("[", "left bracket"), ("'", "quote"), ("=", "equals sign"), ("]", "right bracket"), ("\\", "backslash")]

class Note:
    def __init__(self, symbol, keyRow):
        self.symbol = symbol
        self.symbolName = symbol
        self.keyRow = keyRow

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
    
    # Returns the row of the symbol
    def getKeyRow(self):
        return self.keyRow