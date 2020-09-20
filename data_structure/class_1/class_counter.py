class MyCounter:
    count: int = 0

    def __init__(self):
        MyCounter.count += 1


for _ in range(10):
    c1 = MyCounter()


print(MyCounter.count)