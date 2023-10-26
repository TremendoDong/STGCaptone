# TremendoDong_u3249826_ST1Assignment2_Week11_1

class MobilePhone:
    def __init__(self, manufacturer, model, retail_price):
        self.__manufact = manufacturer
        self.__model = model
        self.__retail_price = retail_price

    def set_manufact(self, manufacturer):
        self.__manufact = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, price):
        self.__retail_price = price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
