class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration()
        value = self.data[self.index]
        self.index = self.index + 1
        return value
itr = MyIterator("spam")
for char in itr:
    print(char,end=" ")
print()

class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration()
        self.index = self.index - 1
        return self.data[self.index]
itr = Reverse("spam")
for char in itr:
    print(char,end=" ")
print()

