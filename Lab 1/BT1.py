danhsach1 = [1. , 3.] 
danhsach2 = [5. , 7.] 
danhsach = danhsach1 + danhsach2 
print(danhsach)
danhsach_gapdoi = 2 * danhsach 
print(danhsach_gapdoi)
danhsach2 = danhsach * 2 
print(danhsach2)
danhsach3 = danhsach / 2
print(danhsach3)
#Ghép các danh sách bằng lệnh zip:
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1] 
diem_so = [10, 9, 8, 7] 
anh_xa = zip(thu_tu, mon_hoc, diem_so) 
print(list(anh_xa))
tap_hop = set(anh_xa)
print(tap_hop) 

lay_TT, lay_monhoc , lay_diem = zip(*anh_xa) 
print(lay_monhoc)

import itertools
tap_sinh = list(itertools.chain(range(4), range(5,10), range(15, 20)))
print(tap_sinh)
list(zip(range(4), range(7, 12), reversed(range(11) ) ) ) 
#Lệnh thực thi một tập tin python
#Bước 1: Tạo một tập tin thucthi1.py và đặt tại một thư mục (trong hình minh họa là đặt tại ‘d:/’) 

a = b = c = 0
mylist = []
exec(open('thucthi1.py').read())


