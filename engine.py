import datetime

def makeOrder(asks, bids, N=1):
	pass


bin_size_in_minutes=15
bins=3

def make_bins(data, bins_number, bins_size):
	bin_borders=[]
	bins=[[] for i in range(0,bins_number)]
	
	for i in range(1,bins_number+1):
		bin_borders.append(datetime.datetime.now()-datetime.timedelta(minutes=bins_size)*i)
		
	print "\n"+str(bin_borders)
	
	i=0
	print bins
	for data_point_time in data.keys():
		print "\n"+str(data_point_time)
		if data_point_time > bin_borders[i] :
			bins[i].append(data[data_point_time])
		else:
			i+=1
			bins[i].append(data[data_point_time])
			
	print bins
	new_bins=[]
	for one_bin in bins:
		len_bin=len(one_bin)
		if len_bin==0:
			one_bin=-1
		else:
			one_bin=sum(one_bin)/len_bin
			
		new_bins.append(one_bin)
			
	for i in range(0,bins_number):
		for i in range(0,bins_number-1):
			if new_bins[i]==-1:
				new_bins[i]=new_bins[i+1]
			
	return new_bins

import data_from_btce
#data=data_from_btce.getHistory(minutes=bin_size_in_minutes*bins, operation="a")
#make_bins(data,bins,bin_size_in_minutes)





