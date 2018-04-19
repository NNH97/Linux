from SinhVien import *
from khoa import *

l=[]
sv = SinhVien('001', 'Nguyen Ngoc Hoai', '57')
l.append(sv)
sv = SinhVien('002', 'Nguyen Quang Lam', '57')
l.append(sv)
sv = SinhVien('003', 'Tran Bao Hien', '57')
l.append(sv)
sv = SinhVien('004', 'Nguyen Van Nghia', '57')
l.append(sv)
sv = SinhVien('005', 'Vo Ba Nghia', '57')
l.append(sv)
sv = SinhVien('006', 'Ngo Quoc Huy', '57')
l.append(sv)
for i in l:
	i.Xuat()

k=[]
k1 = khoa('01','CNTT')
k.append(k1)
k1 = khoa('02','KToan')
k.append(k1)
k1 = khoa('03','CoKhi')
k.append(k1)
k1 = khoa('04','Nuoitrong')
k.append(k1)
for i in k:
	i.Xuat()

for i in k:
	if '01' == i.getmakhoa():
		i.Xuat()


