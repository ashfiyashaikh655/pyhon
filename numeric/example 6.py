buying_price=int(input('buying_price:'))
selling_price=int(input('selling_price:'))
if selling_price>buying_price:
    profit=selling_price-buying_price
    print('profit=',profit)
else:
    loss=selling_price-buying_price
    print('loss=',abs(loss))
