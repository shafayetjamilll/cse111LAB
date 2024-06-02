class CellPackage:
    def __init__(self, price, data, talk_time, messages, cashback, validity):
        self.price = price
        self.data = int(data.split()[0]) * 1024
        self.talk_time = talk_time
        self.messages = messages
        self.cashback = int((int(cashback.replace("%", "")) * 0.01 * self.price))
        self.validity = validity

        if self.data:
            print(f"Data = {self.data} MB")
        if self.talk_time:
            print(f"Talktime = {self.talk_time} Minutes")
        if self.messages:
            print(f"SMS/MMS = {self.messages}")

        print(f"""Validity = {self.validity} Days
--> Price = {self.price} tk""")

        if self.cashback:
            print(f"Buy now to get {self.cashback} tk cashback.")


pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('===========Package 1=============')
# Subtask 2: Check each attribute and print

pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('===========Package 2=============')
# Subtask 3: Check each attribute and print

pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============Package 3============')
