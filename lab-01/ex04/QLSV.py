from QuanLySinhVien import QuanLySinhVien   

qlsv = QuanLySinhVien()
while True:
    print("\n CHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU*****************************")
    print("1. them sinh vien                  ***")
    print("2. cap nhat thong tin sinh vien    ***")
    print("3. xoa sinh vien boi ID            ***")
    print("4. tim kiem SV theo ten               ***")
    print("5. sap xep sinh vien theo diem trung binh                ***")    
    print("6. sap xep sinh vien theo chuyen nganh     ***")
    print("7. hien thi danh sach sinh vien.              ***")
    print("8. thoat chuong trinh.                  ***")
    print("*************************************")
    key = int(input("Nhap lua chon cua ban: "))
    if key == 1:
        print("\n them sinh vien")
        qlsv.nhapSinhVien()        
        print("\n them sinh vien thanh cong!")     
    elif key == 2:
        if qlsv.soluongSinhVien() > 0:
            print("\nNhap ID: ")
            id = int(input())
            qlsv.updateSinhVien(id)
            print("\n cap nhat thong tin sinh vien!")
        else:
            print("\n danh sach sinh vien rong!")
    elif key == 3:
        if qlsv.soluongSinhVien() > 0:
            print("\n xoa sinh vien boi ID")
            print("\nNhap ID: ")
            id = int(input())
            if qlsv.deleteByID(id):
                print("\nsinh vien co ID = ", id, " da bi xoa!")
            else:
                print("\nsinh vien co ID = ", id, " khong ton tai!")
        else:
            print("\n danh sach sinh vien rong!")
    elif key == 4:
        if qlsv.soluongSinhVien() > 0:
            print("\n tim kiem sinh vien theo ten")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\n danh sach sinh vien rong!")
    elif key == 5:
        if qlsv.soluongSinhVien() > 0:
            print("\n sap xep sinh vien theo diem trung binh")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n danh sach sinh vien rong!")
    elif key == 6:
        if qlsv.soluongSinhVien() > 0:
            print("\n sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n danh sach sinh vien rong!")
    elif key == 7:
        if qlsv.soluongSinhVien() > 0:
            print("\n hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n danh sach sinh vien rong!")
    elif key == 8:
        print("\n thoat chuong trinh")
        break
    else:
        print("\n khong co chuc nang nay!")
        print("\n hay chon chuc nang trong menu")