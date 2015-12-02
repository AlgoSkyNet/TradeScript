euro=1000
btc=10
file_name="trades_log.txt"


class Order:
	def __init__(self, operation="none", amount=1, price=-1):
		self.operation=operation
		self.amount=amount
		self.price=price

#Buy euro=sell BTC. sell euro=byu BTC => what=euro is obsolete
def trade(order):
	global euro
	global btc
	
	if order.operation=="none":
		return
	
	if order.operation=="buy":
		order.amount=-1*order.amount
		
	deal_euro=order.price*order.amount
	euro+=deal_euro
	btc-=order.amount
	
	log=open(file_name, 'a+')
	log.write("%s %f BTC for %f euro. \t" % (order.operation, order.amount, order.price))
	log.write("%.3f euro, %.3f BTC\n" % (euro, btc))
	log.close()
	


order3=Order(operation="sell", price=200)
order4=Order(operation="none", price=100)


#trade(order3)
#trade(order4)

			
