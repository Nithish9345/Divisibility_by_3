class Divisibility3:
    def divide(self, array):
        s = 0
        for i in array:
            s += i

        return 1 if s % 3 == 0 else 0

object = Divisibility3()
array = list(map(int, input().split()))
print(object.divide(array))
