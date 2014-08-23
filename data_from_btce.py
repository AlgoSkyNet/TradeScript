import btceapi

pair = "ltc_eur"

trades=btceapi.getTradeHistory(pair=pair, count=5000)
trades.sort(key=lambda x: x.date, reverse=False)
prices_bids=[]
prices_asks=[]
for t in trades:
	print t.date
	if t.trade_type=="bid":
		prices_bids.append(t.price)
		
	if t.trade_type=="ask":
		prices_asks.append(t.price)
	
print prices_asks
print ''
print prices_bids
