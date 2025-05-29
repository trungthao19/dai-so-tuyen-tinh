# danhsach1 = [1. , 3.] 
# danhsach2 = [5. , 7.] 
# danhsach = danhsach1 + danhsach2 
# print(danhsach)
# danhsach_gapdoi = 2 * danhsach 
# print(danhsach_gapdoi)
# danhsach2 = danhsach * 2 
# print(danhsach2)
# danhsach3 = danhsach / 2
# print(danhsach3)
# #Ghép các danh sách bằng lệnh zip:
# mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
# thu_tu = [2, 3, 4, 1] 
# diem_so = [10, 9, 8, 7] 
# anh_xa = zip(thu_tu, mon_hoc, diem_so) 
# print(list(anh_xa))
# tap_hop = set(anh_xa)
# print(tap_hop) 

# lay_TT, lay_monhoc , lay_diem = zip(*anh_xa) 
# print(lay_monhoc)

# import itertools
# tap_sinh = list(itertools.chain(range(4), range(5,10), range(15, 20)))
# print(tap_sinh)
# list(zip(range(4), range(7, 12), reversed(range(11) ) ) ) 
# #Lệnh thực thi một tập tin python
# #Bước 1: Tạo một tập tin thucthi1.py và đặt tại một thư mục (trong hình minh họa là đặt tại ‘d:/’) 

# a = b = c = 0
# mylist = []
# exec(open('thucthi1.py').read())

from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f)

a = Symbol('Noi')
b = Symbol('Chim')
c = 3*b + 7*a
print(c)
a = Symbol('Noi')
b = Symbol('Chim') 

c=a.name 
d=b.name 
print(c)
print(d)

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)

p = x*(x+2*x) 
print(p)

p = (x+2)*(y+3) 
print(p)

p = (x+2)*(y+3) + (x+2)*(x-3) 
print(p)

p = x*(-x+2*x-x)
print(p)

p = (x+2)*(y+3)
print(p)

from sympy import Symbol
x = Symbol('x') 
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)

giatri = bieuthuc.subs({x:3, y:2}) 
print(giatri)

giatri = bieuthuc.subs({x:3, y:2}) 
print(giatri)

giatri = bieuthuc.subs({x:y, y:3})
print(giatri)

giatri = bieuthuc.subs({y:x}).subs({x:3}) 
print(giatri)

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
bieuthuc
x**2 - x*y + y**2
bieuthuc_moi = bieuthuc.subs({x:1-y}) #  x được thay thế bằng (1-y)
print(bieuthuc_moi)

from sympy import simplify
dongian = simplify(bieuthuc_moi)
print(dongian)

from sympy import Symbol
from sympy import sin, cos
x = Symbol('x')
y = Symbol('y')
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print(bt_moi)

import numpy as np 
from numpy import *
vec1 = np.array([1., 3., 5.]) 
print(vec1 * 2)
print(vec1 * vec1)
print(vec1 /2 )
print(vec1 + vec1 )
vec2 = array([2., 4.]) 
# print(vec1 + vec2)  
vec3 = array([2., 4., 6.]) 
print(vec1 + vec3)  
print( vec1 / vec3)
print(vec1 * vec3 )
print(2* vec1 + 5* vec3)
print(vec3[2] )

vec4 = np.linspace(0, 20, 5) 
print(vec4)

vec5 = np.zeros(5) 
print(vec5)

vec6 = np.ones(5) 
print(vec6)

vec7 = np.empty(5) 
print(vec7)

vec8 = np.random.random(5)
print(vec8)

v = np.array([1., 3., 5.]) 
print(np.sum(v) )
print(v.shape )
print(v.transpose())

v1 = v[:2] 
print(v1)

v[0] = 5 
print(v)

print(v1)

v1[:2] = [1., 2., 3.] 
print(v1[:2])
v6 = v1[:2] = [1., 2] 
print(v6)

v3 = 2 * v[:2] + v1 * 3 
print(v3)

