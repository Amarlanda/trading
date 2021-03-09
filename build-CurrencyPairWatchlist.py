combinations = []

def combine(terms, accum):
    last = (len(terms) == 1)                       #find last term
    n = len(terms[0])
    bla = ""
                
    for i in range(n):
        if accum != terms[0][i] : # currency pairs do not match
          
            #ruleForCurrencyPairs(accum, terms[0][i])
            item = StockExchange + accum + terms[0][i]      #first

            if last:
                print(item)                       #last
                combinations.append(item)
            else:                            #body
                combine(terms[1:], item)

def ruleForCurrencyPairs():
    if accum == "USD" :
        StockExchange = "FX:"
    elif accum == "GBP":               #or  ( item = GBP) : #fix this 
        StockExchange = "OANDA:"
    elif accum == "JYP" :
        StockExchange = "KRAKEN:"
    return StockExchange

def label():
    if accum == "USD" :
        label = "FX:"
    elif (accum == "GBP"):
        label = "OANDA:"
    elif accum == "JYP" :
        label = "KRAKEN:"
    return label

a = [['GBP', 'USD', 'JYP'],['USD','GBP','AUD','CAD','CHF','JPY','NZD','BTC','ETH','XRP','EOS','XBT']]
combine(a, '')
print(combinations)