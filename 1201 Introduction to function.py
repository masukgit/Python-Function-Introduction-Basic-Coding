iphone_dollar = 493
bdt_exchange = 123.58
iphone_bdt_price = iphone_dollar * bdt_exchange
print(iphone_bdt_price)

nokia_dollar = 293
bdt_exchange = 123.58
nokia_bdt_price = nokia_dollar * bdt_exchange
print(nokia_bdt_price)

walton_dollar = 93
bdt_exchange = 123.58
walton_bdt_price = walton_dollar * bdt_exchange
print(walton_bdt_price)


# DRY = don't repeat yourself

def mobile_price_bdt(usd_price, exchange_rate):
    bdt_price = usd_price * exchange_rate
    return bdt_price

nokia_price = mobile_price_bdt(225, 127.36)
print(nokia_price)

walton_price = mobile_price_bdt(235, 127.36)
print(walton_price)

def greeting():
    print('Hello Python')
greeting()

def greeting(name):
    # print('Hello', name)
    return f'Hello, {name}'
my_greeting = greeting('Sai Masuk')
print(my_greeting)

def voter_maturity(age):
    if age >= 18:
        return 'He is eligible to vote'
    else:
        return 'He is not eligible to vote'
print(voter_maturity(18))
print(voter_maturity(16))