class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = round(0.5 * self.a * self.b, 1)

    def is_right(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            print(self.area)
        else:
            print("Not right")


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

triangle = RightTriangle(input_c, input_a, input_b)
triangle.is_right()
