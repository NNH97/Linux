class SinhVien:
	MSSV = ''
	hoten = ''
	mkhoa = ''
	def __init__ (self, MSSV, hoten, mkhoa):
		self.MSSV = MSSV
		self.hoten = hoten
		self.mkhoa = mkhoa
	def getMSSV(self):
	        return self.MSSV 
	def setMSSV(self, MSSV):
		self.MSSV = MSSV
	def getHoTen(self):
	        return self.hoten
	def setHoTen(self, hoten):
		self.hoten = hoten
	def getNhom(self):
	        return self.mkhoa
	def setmkhoa(self, mkhoa):
		self.mkhoa = mkhoa
	def Xuat(self):
		print "\n MSSV : ",self.MSSV,"Ho Ten : ",self.hoten,"Ma Khoa : ",self.mkhoa
