# class StockPrice:
#
#     def __init__(self):
#         self.t_price={}
#         self.maximum_t = 0
#         self.minimum_t = 0
#         self.current_t = 0
#
#     def update(self, timestamp: int, price: int) -> None:
#         if timestamp in self.t_price:
#             self.t_price[timestamp] = price
#             self.maximum_t = self.minimum_t = timestamp
#             for k, v in self.t_price.items():
#                 if v < self.t_price[self.minimum_t]:
#                     self.minimum_t = k
#                 if v > self.t_price[self.maximum_t]:
#                     self.maximum_t = k
#         else:
#             self.t_price[timestamp] = price
#             if self.maximum_t == 0:
#                 self.maximum_t = self.minimum_t = timestamp
#             if price > self.t_price[self.maximum_t]:
#                 self.maximum_t = timestamp
#             if price < self.t_price[self.minimum_t]:
#                 self.minimum_t = timestamp
#         if timestamp > self.current_t:
#             self.current_t = timestamp
#         # print(self.t_price,self.maximum_t)
#
#     def current(self) -> int:
#         return self.t_price[self.current_t]
#
#     def maximum(self) -> int:
#         return self.t_price[self.maximum_t]
#
#     def minimum(self) -> int:
#         return self.t_price[self.minimum_t]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

# class Node:
#     def __init__(self, timestamp, price, next, prior):
#         self.timestampe = timestamp
#         self.price = price
#         self.next = next
#         self.prior = prior
#
# class StockPrice:
#
#     def __init__(self):
#         self.time=set()
#         self.head=Node(0,0,None,None)
#         self.rail=Node(0, float("inf") ,None,None)
#         self.head.next=self.rail
#         self.rail.prior=self.head
#         self.current_t_p=[0,0]
#
#     def update(self, timestamp, price) -> None:
#         if timestamp>=self.current_t_p[0]:
#             self.current_t_p=[timestamp,price]
#         if timestamp not in self.time:
#             self.time.add(timestamp)
#             s = Node(timestamp, price, None, None)
#         else:
#             s=self.head
#             while s.timestampe != timestamp:
#                 s=s.next
#             s.prior.next=s.next
#             s.next.prior=s.prior
#             s.price=price
#         p = self.head
#         while p.next.price < price:
#             p = p.next
#         s.next=p.next
#         s.prior=p
#         p.next.prior = s
#         p.next = s
#
#     def current(self) -> int:
#         return self.current_t_p[1]
#
#     def maximum(self) -> int:
#         return self.rail.prior.price
#
#     def minimum(self) -> int:
#         return self.head.next.price


class Node:
    def __init__(self, data, next, prior):
        self.data = data
        self.next = next
        self.prior = prior


class SortList:
    def __init__(self):
        self.head = Node(0, None, None)
        self.tail = Node(float("inf"), None, None)
        self.head.next = self.tail
        self.tail.prior = self.head
        self.size = 0

    def add(self, x):
        p = self.head
        while x > p.next.data:
            p = p.next
        s = Node(x, p.next, p)
        p.next.prior = s
        p.next = s
        self.size += 1

    def discard(self, x):
        p = self.head.next
        while x != p.data and p != self.tail:
            p = p.next
        if p == self.tail:
            print("x is not in list")
            return
        p.next.prior = p.prior
        p.prior.next = p.next
        del p
        self.size -= 1

    def __getitem__(self, item):
        if item >= self.size or -item - 1 >= self.size:
            print("index out of range")
            return
        if item >= 0:
            p = self.head
            count = 0
            while count < item:
                p = p.next
                count += 1
            return p.next.data
        else:
            p = self.tail
            count = 0
            while count > item:
                p = p.prior
                count -= 1
            return p.data

    def __str__(self):
        data_list = []
        p = self.head.next
        while p != self.tail:
            data_list.append(p.data)
            p = p.next
        return " ".join(map(str, data_list))


class StockPrice:

    def __init__(self):
        self.price = SortList()
        self.time_price = {}
        self.current_time_price = [0, 0]

    def update(self, timestamp, price) -> None:
        if timestamp in self.time_price:
            self.price.discard(self.time_price[timestamp])
        self.price.add(price)
        self.time_price[timestamp] = price
        if timestamp >= self.current_time_price[0]:
            self.current_time_price = [timestamp, price]

    def current(self) -> int:
        return self.current_time_price[1]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]


stockPrice = StockPrice()
stockPrice.update(1, 10)
# print(stockPrice.price)
stockPrice.update(2, 5)
# print(stockPrice.price)
stockPrice.update(1, 3)
print(stockPrice.maximum())
print(stockPrice.price)
print(stockPrice.minimum())
print(stockPrice.current())
print(stockPrice.maximum())
