import json
import datetime

def getHistory(period_mins=0.01):
	trades=json.load(file("trades"))
	trades.sort(key=lambda x: x['date'], reverse=False)

	#The first period
	period_end_date=trades[0]['date']+period_mins*60
	period_num=0

	prices_bids=[]
	prices_asks=[]
	prices_asks.append([])
	prices_bids.append([])

	mode_prices_bids=[]
	mode_prices_asks=[]

	for t in trades:
		if t['date']<period_end_date:
			if t['trade_type']=="bid":
				prices_bids[period_num].append(t['price'])
			
			if t['trade_type']=="ask":
				prices_asks[period_num].append(t['price'])
		else:		
			period_num=period_num+1
			period_end_date=period_end_date+period_mins*60
			prices_asks.append([])
			prices_bids.append([])


	from collections import Counter

	print 'asks:'
	print len(prices_asks)
	for a in prices_asks:
		mode=None
		data = Counter(a)
		mode=data.most_common(1)
		if len(mode)>0:
			mode=data.most_common(1)[0]
		mode_prices_asks.append(mode)
		
		print mode
		
	print ''
		
	print 'bids:'
	print len(prices_bids)
	for b in prices_bids:
		mode=None
		data = Counter(b)
		mode=data.most_common(1)
		if len(mode)>0:
			mode=data.most_common(1)[0]
		mode_prices_bids.append(mode)
		
		print mode
	returnDict=dict()
	
	return [mode_prices_asks, mode_prices_bids]

getHistory()
