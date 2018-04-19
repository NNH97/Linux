class khoa:
	makhoa = ''
	tenkhao = ''
	
	def __init__(self,makhoa,tenkhoa):
		self.makhoa = makhoa
		self.tenkhoa = tenkhoa

	def getmakhoa(self):
		return self.makhoa
	def gettenkhoa(self):
		return self.tenkhoa
	def setmakhoa(self, makhoa):
		self.makhoa = makhoa
	def settenkhoa(self, tenkhoa):
		self.tenkhoa = tenkhoa
	def Xuat(self):
		print "\nMa Khoa :",self.makhoa,"Ten Khoa :",self.tenkhoa
