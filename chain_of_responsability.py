import random
import time
from abc import ABC, abstractmethod

MONEY_CUTS = ['200', '100', '50', '20', '10']


class Chain(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, amount_of_money):
        pass


class AbstractChain(Chain):
    _next_chain = None
    _money_to_retire = []

    @staticmethod
    def reset_money_to_retire():
        AbstractChain._money_to_retire = []

    def set_next(self, chain):
        self._next_chain = chain
        return chain

    @abstractmethod
    def handle(self, amount_of_money, money_to_retire={}):
        if self._next_chain:
            return self._next_chain.handle(amount_of_money, money_to_retire)
        else:
            return money_to_retire


class TwoHundredChain(AbstractChain):
    def handle(self, amount_of_money, money_to_retire={}):
        if amount_of_money % 200 != amount_of_money:
            two_hundred_bill = (amount_of_money - amount_of_money % 200) / 200
            money_to_retire['200'] = {'quantity': two_hundred_bill, 'type': '200'}
            return super().handle(amount_of_money % 200, money_to_retire)
        else:
            return super().handle(amount_of_money, money_to_retire)


class OneHundredChain(AbstractChain):
    def handle(self, amount_of_money, money_to_retire={}):
        if amount_of_money % 100 != amount_of_money:
            two_hundred_bill = (amount_of_money - amount_of_money % 100) / 100
            money_to_retire['100'] = {'quantity': two_hundred_bill, 'type': '100'}
            return super().handle(amount_of_money % 100, money_to_retire)
        else:
            return super().handle(amount_of_money, money_to_retire)


class FiftyChain(AbstractChain):
    def handle(self, amount_of_money, money_to_retire={}):
        if amount_of_money % 50 != amount_of_money:
            two_hundred_bill = (amount_of_money - amount_of_money % 50) / 50
            money_to_retire['50'] = {'quantity': two_hundred_bill, 'type': '50'}
            return super().handle(amount_of_money % 50, money_to_retire)
        else:
            return super().handle(amount_of_money, money_to_retire)


class TwentyChain(AbstractChain):
    def handle(self, amount_of_money, money_to_retire={}):
        if amount_of_money % 20 != amount_of_money:
            two_hundred_bill = (amount_of_money - amount_of_money % 20) / 20
            money_to_retire['20'] = {'quantity': two_hundred_bill, 'type': '20'}
            return super().handle(amount_of_money % 20, money_to_retire)
        else:
            return super().handle(amount_of_money, money_to_retire)


class TenChain(AbstractChain):
    def handle(self, amount_of_money, money_to_retire={}):
        if amount_of_money % 10 != amount_of_money:
            two_hundred_bill = (amount_of_money - amount_of_money % 10) / 10
            money_to_retire['10'] = {'quantity': two_hundred_bill, 'type': '10'}
            return super().handle(amount_of_money % 10, money_to_retire)
        else:
            return super().handle(amount_of_money, money_to_retire)


class HasResidualChain(AbstractChain):
    def handle(self, amount_of_money, money_to_retire={}):
        if amount_of_money > 0:
            print('No se pudo retirar el dinero por que no entrego monedas de: {}'.format(amount_of_money))
            return {}
        else:
            return money_to_retire


class Atm:
    def __init__(self):
        self._some_random_name_here = {'200': {}, '100': {}, '50': {}, '20': {}, '10': {}}

    def fill_with_money(self, money):
        money_by_type = self._some_random_name_here[money['type']]
        quantity_of_money_by_type = money_by_type.get('quantity', 0)
        money_by_type['quantity'] = quantity_of_money_by_type + money['quantity']

    def has_money(self):
        total_quantity_of_money = 0
        for money_cut in MONEY_CUTS:
            quantity_of_money = self._some_random_name_here[money_cut].get('quantity', 0)
            total_quantity_of_money += quantity_of_money
        return True if total_quantity_of_money > 0 else False

    def retire_money(self, amount_of_money):
        has_residual = HasResidualChain()
        two_hundred_chain = TwoHundredChain()
        one_hundred_chain = OneHundredChain()
        fifty_chain = FiftyChain()
        twenty_chain = TwentyChain()
        ten_chain = TenChain()
        two_hundred_chain.set_next(one_hundred_chain)
        one_hundred_chain.set_next(fifty_chain)
        fifty_chain.set_next(twenty_chain)
        twenty_chain.set_next(ten_chain)
        ten_chain.set_next(has_residual)
        money_to_retire = two_hundred_chain.handle(amount_of_money)
        self._update_amount_of_bill(money_to_retire)
        return money_to_retire

    def _update_amount_of_bill(self, money_to_retire):
        self._some_random_name_here['200']['quantity'] -= money_to_retire.get('200', {}).get('quantity', 0)
        self._some_random_name_here['100']['quantity'] -= money_to_retire.get('100', {}).get('quantity', 0)
        self._some_random_name_here['50']['quantity'] -= money_to_retire.get('50', {}).get('quantity', 0)
        self._some_random_name_here['20']['quantity'] -= money_to_retire.get('20', {}).get('quantity', 0)
        self._some_random_name_here['10']['quantity'] -= money_to_retire.get('10', {}).get('quantity', 0)


if __name__ == '__main__':
    atm = Atm()
    atm.fill_with_money({'type': '200', 'quantity': random.randint(1, 3)})
    atm.fill_with_money({'type': '100', 'quantity': random.randint(1, 5)})
    atm.fill_with_money({'type': '50', 'quantity': random.randint(1, 8)})
    atm.fill_with_money({'type': '20', 'quantity': random.randint(1, 3)})
    atm.fill_with_money({'type': '10', 'quantity': random.randint(1, 8)})
    atm.retire_money(360)

    # while atm.has_money():
    #     independent_adult_impulse_buying = random.randint(1, 1000)
    #     print('independent_adult_impulse_buying: {}'.format(independent_adult_impulse_buying))
    #     retired_money = atm.retire_money(independent_adult_impulse_buying)
    #     if retired_money:
    #         print("retired_money: {}".format(retired_money))
    #     time.sleep(3)
