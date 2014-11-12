import json
import datetime

def getHistory(operation="b"):
	if operation!="b" and operation!="a":
		raise ValueError("Operation should be either 'a' for asks, or 'b' for bids")
	
	trades=json.load(file("trades"))
	trades.sort(key=lambda x: x['date'], reverse=False)

	prices_bids=dict()
	prices_asks=dict()

	for t in trades:
		if t['trade_type']=="bid":
			prices_bids[t['date']]=t['price']
			
		if t['trade_type']=="ask":
			prices_asks[t['date']]=t['price']

	from collections import Counter

	print 'asks:'
	print len(prices_asks)
	print prices_asks
		
	print ''
		
	print 'bids:'
	print len(prices_bids)
	print prices_bids
	
	returnDict=prices_bids if operation=="b" else prices_asks
	
	return returnDict

getHistory()
