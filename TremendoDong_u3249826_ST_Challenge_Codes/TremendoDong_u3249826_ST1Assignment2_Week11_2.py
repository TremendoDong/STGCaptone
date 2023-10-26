# TremendoDong_u3249826_ST1Assignment2_Week11_2

from TremendoDong_u3249826_ST1Assignment2_Week11_1 import MobilePhone


def main():

    phone = MobilePhone("Acme Electronics", "M1000", 199.99)

    print("Here is the data that you entered:")
    print("Manufacturer:", phone.get_manufact())
    print("Model Number:", phone.get_model())
    print("Retail Price: ${:.2f}".format(phone.get_retail_price()))


if __name__ == "__main__":
    main()
