from bittrex.bittrex import Bittrex
import threading

class TradeClass():
    """"Клас метода трейдинга "Двигаем стоплосс" """
    def __init__(self, key, secret, market, command, amount, coinname, step, stoploss):
        self.key = key
        self.secret = secret
        self.market = market
        self.command = command
        self.amount = amount
        self.coinname = coinname
        self.step = step
        self.stoploss = stoploss

    def Test(self, key, secret, market, coinname):
        # threading.Timer(10, Test, args=(key, secret, market, coinname)).start()
        TestTrading = Bittrex(key, secret)
        t = TestTrading.get_ticker(market)
        # balance = TestTrading.get_balance(coinname)
        bid = t['result']['Bid']
        print("| Bid          | {: .8f} ".format(bid))
        return bid

    def Compare(self, BID, step, stoploss):
        FirstCycle = True
        threading.Timer(5, Compare, args=(BID, step, stoploss)).start()
        print("working")
        CurrVal = BID
        # фигачим во временную переменную
        CurrVal1 = BID
        # если текуищее значение отличается от предыдущего
        if CurrVal1 != CurrVal:
            print("Value has changed! It was {: .8f}".format(CurrVal))
            print("Now it is {: .8f}".format(CurrVal1))
            if CurrVal1 >= CurrVal + step:
                print("MOVING STOP LOSS")
                CurrVal = CurrVal1
            elif CurrVal <= CurrVal - stoploss:
                print("SELL ORDER")

    def TradingAlorythm(self, command, market, amount, coinname, step, stoploss, key, secret):
        if command == "y":
            print("buying {0} of {1} coins".format(amount, coinname))
            # раскомментировать для созадния ордера на покупку
            # TestTrading.buy_limit(market, amount, coinprice)

            #Compare(Test(key, secret, market, coinname), step, stoploss)