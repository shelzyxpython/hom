# WS 08.10.23

# def my_decorator(func):
#     def wrapper():
#         print('before decorator')
#         func()
#         print('after decorator')
#     return wrapper
#
# @my_decorator
# def hello():
#     print('hello')
#
#
# hello()


# class Vector:
#     '''kjhgfd'''
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x):
#             self.x = x
#
#         if self.validate(y):
#             self.y = y
#         print(Vector.norm2(self.x, self.y))
#         print(self.norm2(self.x, self.y))
#
#     def get_coord(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x, y):
#         return x ** 2 + y ** 2
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD < arg < cls.MAX_COORD
#
#
# v = Vector(1, 5)
# print(v.norm2(1, 8))
# print(v.__dict__)
# print(Vector.norm2)

# from math import pi
#
#
# class Cylinder:
#
#     @staticmethod
#     def make_area(d, h):
#         circle = pi * d ** 2 / 4
#         site = pi * d * h
#         return circle * 2 + site
#
#     def __init__(self, diam, high):
#         self.diam = diam
#         self.high = high
#         self.area = self.make_area(self.diam, self.high)
#
#     def __str__(self):
#         return f'Diam = {self.diam}, hight = {self.high}, area = {self.area}'
#
# c = Cylinder(2, 4)
# print(c)
# print(c.__dict__)


# class MyClass:
#     TOTAL_COUNTS = 0
#
#     def __init__(self):
#         MyClass.TOTAL_COUNTS = MyClass.TOTAL_COUNTS + 1
#
#     @classmethod
#     def total_counts(cls):
#         print('total counts = ', cls.TOTAL_COUNTS)
#
#
# class ChildClass(MyClass):
#     TOTAL_COUNTS = 0
#
#     def __init__(self):
#         ChildClass.TOTAL_COUNTS += 1
#
# m = MyClass()
# m1 = MyClass()
# MyClass.total_counts()
# cs = ChildClass()
# cs.total_counts()


# class Point:
#     MIN_COORD = 0
#     MAX_COORD = 100
#     z = 123
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if self.MIN_COORD < x < self.MAX_COORD:
#             self.x = x
#         if self.MIN_COORD < y < self.MAX_COORD:
#             self.y = y
#
#     @classmethod
#     def set_bound(self, left):
#         self.MIN_COORD = left
#
#     def __getattribute__(self, item):
#         if item == '_Point__x':
#             raise ValueError('цап-царап')
#         return object.__getattribute__(self, item)
#
#     def __str__(self):
#         return f'x = {self.x}, y = {self.y}'
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise ValueError
#         object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         print('getattr' + item)
#
#     def __del__(self):
#         print('no object')
#
#
# p = Point(1, 6)
# # p.MAX_COORD = 7000
# # p.set_bound(-100)
# # p1 = Point(2, 7)
# # print(p._Point__x)
# p.j = 15
# # # p.set_coord(2, -5)
# # p.set_coord(-2, 500)
# # p1.set_coord(-10, 15)
# # # print(p)
# # print(Point.__dict__)
# print(p.__dict__)
# # print(p1.__dict__)


# MOODLE


# class Snow:
#
#     def __init__(self, num):
#         self.num = num
#
#     def make_snow(self, el):
#         for i in range((self.num // el)):
#             print('*' * el)
#         print('*' * (self.num % el))
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         res = other if isinstance(other, int) else other.num
#         return Snow(self.num + res)
#
#     def __sub__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         res = other if isinstance(other, int) else other.num
#         return Snow(self.num - res)
#
#     def __mul__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         return Snow(self.num * other)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         return Snow(self.num // other)
#
#     def __truediv__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         return Snow(self.num // other)
#
#
# s = Snow(1000)
# s1 = Snow(10)
# s2 = s / 10
# s2.make_snow(200)
# # print(s + s1)
# # s.make_snow(50)

# class SnowFlake:
#     def __init__(self, s):
#         self.s = s
#         self.m = [['-' for _ in range(s)] for _ in range(s)]
#         self.m[s // 2][s // 2] = '*'
#
#     def thaw(self, line):
#         for _ in range(line):
#             self.s -= 2
#             for i in range(self.s):
#                 self.m[i][i] = '-'
#                 self.m[self.s - 1 - i][i] = '-'
#                 self.m[i][self.s - 1 - i] = '-'
#                 self.m[self.s - 1 - i][self.s - 1 - i] = '-'
#
#     def freeze(self, n):
#         side = self.s + 2 * n
#         matrix = [['-' for _ in range(side)] for _ in range(side)]
#         for i in range(self.s):
#             for j in range(self.s):
#                 matrix[i + n][j + n] = self.m[i][j]
#         self.s = side
#         self.m = matrix
#
#     def thicken(self):
#         new_side = self.s + 2
#         new_matrix = [['-' for _ in range(new_side)] for _ in range(new_side)]
#         for i in range(self.s):
#             for j in range(self.s):
#                 new_matrix[i + 1][j + 1] = self.m[i][j]
#         self.s = new_side
#         self.m = new_matrix
#
#     def show(self):
#         for k in self.m:
#             print(' '.join(k))
#
#
# flake = SnowFlake(8)
# flake.show()


# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.loc = [(x, y)]
#
#     def move(self, commands):
#         for command in commands:
#             if command == 'W' and self.y < 100:
#                 self.y += 1
#             elif command == 'S' and self.y > 0:
#                 self.y -= 1
#             elif command == 'D' and self.x < 100:
#                 self.x += 1
#             elif command == 'A' and self.x > 0:
#                 self.x -= 1
#             self.loc.append((self.x, self.y))
#         return self.x, self.y
#
#     def get_loc(self):
#         return self.loc
#
#
# robot = Robot(20, 300)
# print(robot.move('W'))
# print(robot.move('S'))
# print(robot.move('D'))
# print(robot.move('A'))


# class Talking:
#     def __init__(self, name):
#         self.name = name
#         self.yes_count = 0
#         self.no_count = 0
#         self.answer = True
#
#     def ans(self):
#         if self.answer:
#             self.answer = False
#             self.yes_count += 1
#             return "moore-moore"
#         else:
#             self.answer = True
#             self.no_count += 1
#             return "meow-meow"
#
#     def number_yes(self):
#         return self.yes_count
#
#     def number_no(self):
#         return self.no_count
#
#
# tk = Talking('Pussy')
# tk1 = Talking('Barsik')
# print(tk.ans())
# print(tk1.ans())
# print(tk1.ans())
# print(tk1.ans())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
# print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no" {tk1.number_no()} times')
