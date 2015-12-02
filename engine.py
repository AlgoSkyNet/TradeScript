import datetime

def makeOrder(asks, bids, N=1):
	pass


bin_size_in_minutes=5
bins=3*1000

def make_bins(data, bins_number, bins_size):
	bin_borders=[]
	bins=[[] for i in range(0,bins_number)]
	
	for i in range(1,bins_number+1):
		bin_borders.append(datetime.datetime.now()-datetime.timedelta(minutes=bins_size)*i)
	
	i=0

	for data_point_time in data.keys():
		print "\n"+str(data_point_time)
		if data_point_time > bin_borders[i] :
			bins[i].append(data[data_point_time])
		else:
			i+=1
			bins[i].append(data[data_point_time])
			
	new_bins=[]
	for one_bin in bins:
		len_bin=len(one_bin)
		if len_bin==0:
			one_bin=-1
		else:
			one_bin=sum(one_bin)/len_bin
			
		new_bins.append(float(one_bin))
			
	for i in range(0,bins_number):
		for i in range(0,bins_number-1):
			if new_bins[i]==-1:
				new_bins[i]=new_bins[i+1]
			
	return new_bins

import data_from_btce
data=data_from_btce.getHistory(minutes=bin_size_in_minutes*bins, operation="b")
prices=make_bins(data,bins,bin_size_in_minutes)

print prices

import when_to_trade
orders=[]
for i in range(0,998):
	print i
	j=1000-i-1
	print prices[j-2],prices[j-1],prices[j]
	order=when_to_trade.tradeFunc(prices[j-2],prices[j-1],prices[j])
	print order.operation, order.price
	print ""
	orders.append(order)


import trade_to_file
for order in orders:
	trade_to_file.trade(order)







