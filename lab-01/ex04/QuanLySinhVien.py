from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soluongSinhVien() > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId

    def soluongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, id):
        sv = self.findByID(id)
        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(id))

    def sortID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if self.soluongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv._id == ID:
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSv = []
        if self.soluongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword.upper() in sv._name.upper():
                    listSv.append(sv)
        return listSv

    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocluc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocluc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"

    def showSinhVien(self, listsv):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        if len(listsv) > 0:
            for sv in listsv:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
 .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
        