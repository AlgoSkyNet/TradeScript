import btceapi
import datetime 

pair = "ltc_eur"

def getHistory(minutes=5, operation="b"):
	if operation!="b" and operation!="a":
		raise ValueError("Operation should be either 'a' for asks, or 'b' for bids")
		
	since_time=datetime.datetime.now() - datetime.timedelta(minutes=minutes)
	trades=btceapi.getTradeHistory(pair=pair, count=minutes*10) #Have no idea how many items we need
	trades.sort(key=lambda x: x.date, reverse=False)
	
	prices_bids=dict()
	prices_asks=dict()

	extra_items=0

	for t in trades:
		if t.date<since_time:
			#print t.date
			extra_items+=1
			continue
			
		if t.trade_type=="bid":
			prices_bids[t.date]=t.price
			
		if t.trade_type=="ask":
			prices_asks[t.date]=t.price

	print "downloaded %d extra records" % extra_items 

	print 'asks:'
	print len(prices_asks)
	print prices_asks
		
	print ''
		
	print 'bids:'
	print len(prices_bids)
	print prices_bids
	
	returnDict=prices_bids if operation=="b" else prices_asks
	
	return returnDict
	
#print getHistory(minutes=20)
