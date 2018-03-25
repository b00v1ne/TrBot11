import TradingAlgorythm
import TradingAlgorythm_Threading
import TradeClass
from bittrex.bittrex import Bittrex

def ValueCheck(x):
    while not 0 < x < 99999999:
        x = float(input("Give a number > 0"))
        continue


def ThresholdCalc(initial, x, ):
    return float(initial - (x/100)*initial)


def CurrencyNameCheck(cur):
    while cur:
        marketsummary = TestTrading.get_ticker('{0}-{1}'.format(trade, cur))
        # Проверяем, валидна ли валюта
        if marketsummary['success']:
            print("OK, continue...")
            return marketsummary['result']['Last'], cur
        else:
            cur = input("Give a correct currency: ")
            continue


command = "N"
key = ''
secret = ''
TestTrading = Bittrex(key, secret)

#************CONSTANTS************
StartValue = 0
trade = 'BTC'
#*********************************
# Начинаем...
currency = input("I am a trading bot, gimme currency to traid with BTC: ")

# Прорверяем, существет ли такая валюта, и если да, то сколько она сейчас стоит и какое в итоге имя монеты
coinprice, coinname = CurrencyNameCheck(currency)
# Обьявляем торговую пару
market = '{0}-{1}'.format(trade, coinname)
print('The price for {0} is {1:.8f} {2}.'.format(coinname, coinprice, trade))

# Сколько монет купить?
amount = float(input("How many coins to buy?: "))
ValueCheck(amount)

# Ставим стоп лосс
StopLossPercents = float(input("Stop-loss value in percents: "))
ValueCheck(StopLossPercents)
StopLoss = ThresholdCalc(coinprice, StopLossPercents)

# При каком увеличении цены монеты, двигать стоп-лосс?
StepPercent = float(input("When should I move Stop-loss? percents: "))
ValueCheck(StepPercent)
Step = coinprice - ThresholdCalc(coinprice, StepPercent)

# Еще раз выведем общую информацию
print("Stop-loss is {0: .8f}, Step is {1: .8f}".format(StopLoss, Step))

# Стартуем?
command = input("Should I start? [Y]/[N]: ")

#Trade1 = TradeClass(key, secret, market, command, amount, coinname, Step, StopLoss)

TradingAlgorythm_Threading.TradingAlorythm(command, market, amount, coinname, Step, StopLoss, key, secret)
