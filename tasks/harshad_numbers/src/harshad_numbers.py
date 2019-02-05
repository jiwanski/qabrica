class Harshad:

    @staticmethod
    def is_valid(number):
        sum_digits = sum([int(s) for s in str(number)])
        return bool(not number % sum_digits)

    @staticmethod
    def get_next(number):
        result = number + 1
        while Harshad.is_valid(result) is False:
            result += 1
        return result

    @staticmethod
    def get_series(count, start=0):
        result = []
        c = 0
        while c < count:
            nxt = Harshad.get_next(start)
            result.append(Harshad.get_next(start))
            c += 1
            start = nxt
        return result
