from iexfinance import Share
import cryptocompare

def get_current_price(abbrv, crypt):
	if crypt != 0:	#yahoo
		share = Share(abbrv)
		return share.get_price()
	else:
		# print ("PRICE OF " + abbrv + "is: $" + str(cryptocompare.get_price(abbrv, curr='USD')[abbrv]['USD']))
		return cryptocompare.get_price(abbrv, curr='USD')[abbrv]['USD']