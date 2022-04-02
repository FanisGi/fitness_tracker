from typing import List, Dict, Tuple, Type, Optional, Union

class Asset:
    def __init__(self, name:str) -> None:
        self.name = name

    def calc_fin_res(
        self, buy_price: float, sell_price: float, amout: float, balance: float
    ) -> Tuple[float, float]:
        """Рассчитать прибыль по формуле: 
        result = (sell_price - buy_price) * amount"""
        result = (sell_price - buy_price) * amount
        result_pct = result * 100.0 / balance
        return result, result_pct


class USDQouted (Asset):
    def __init__(self, name:str) -> None:
        super().__init__(name)
        self.usd_qoute: Optional[float] = None

    def set_usd_quote(self, usd_qoute: float) -> None:
        if not isinstance(usd_qoute, float):
            raise TypeError ('текст сообщения при аварии')
        self.usd_qoute = usd_qoute

    def calc_fin_res(
        self, buy_price: float, sell_price: float, amout: float, balance: float
    ) -> Tuple[float, float]:
        """Рассчитать прибыль по формуле: 
        result = (sell_price - buy_price) * amount * usd_qoute"""
        if not self.usd_qoute:
            raise ValueError ('текст при аварии')
        result, _ = super().calc_fin_res(buy_price, sell_price, amout, balance)
        result = result * self.usd_qoute # добавили в начале self т к в он теперь является отрибутом экземпляра
        result_pct = result * 100.0 / balance
        return result, result_pct



if __name__ == '__main__':
    buy_price = 150.0
    sell_price = 250.0
    amount = 10
    balance = 100000.0 # в рублях

    sber = Asset( 'SBER' ) # кругые скобки запустит работу конструктора класса
    result = sber.calc_fin_res(buy_price, sell_price, amount, balance)
    print(result)

