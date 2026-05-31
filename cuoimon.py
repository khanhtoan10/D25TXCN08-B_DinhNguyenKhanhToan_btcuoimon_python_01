import json
import os

TEN_FILE = "data.json"

def doc_du_lieu():
    if os.path.exists(TEN_FILE):
        try:
            with open(TEN_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: return []
    return []

def luu_du_lieu(danh_sach):
    with open(TEN_FILE, "w", encoding="utf-8") as f:
        json.dump(danh_sach, f, indent=4, ensure_ascii=False)

def tinh_toan(cau_thu):
    cau_thu["diem"] = (cau_thu["ban_thang"] * 2) + cau_thu["kien_tao"]
    if cau_thu["diem"] > 40: cau_thu["danh_hieu"] = "Vàng"
    elif cau_thu["diem"] > 20: cau_thu["danh_hieu"] = "Bạc"
    else: cau_thu["danh_hieu"] = "Đồng"
    return cau_thu

def hien_thi(danh_sach):
    print(f"\n{'Mã':<10} {'Tên':<15} {'Số trận':<10} {'Bàn':<10} {'Kiến tạo':<10} {'Điểm':<10} {'Danh hiệu':<10}")
    for ct in danh_sach:
        print(f"{ct['ma']:<10} {ct['ten']:<15} {ct['so_tran']:<10} {ct['ban_thang']:<10} {ct['kien_tao']:<10} {ct['diem']:<10} {ct['danh_hieu']:<10}")

def them(danh_sach):
    ma = input("Nhập mã: ")
    if any(ct['ma'] == ma for ct in danh_sach):
        print("Mã đã tồn tại!")
        return
    ten = input("Nhập tên: ")
    so_tran = int(input("Số trận: "))
    ban_thang = int(input("Bàn thắng: "))
    kien_tao = int(input("Kiến tạo: "))
    ct = {"ma": ma, "ten": ten, "so_tran": so_tran, "ban_thang": ban_thang, "kien_tao": kien_tao}
    danh_sach.append(tinh_toan(ct))
    luu_du_lieu(danh_sach)
    print("Thêm thành công!")

def cap_nhat(danh_sach):
    ma = input("Nhập mã cần cập nhật: ")
    for ct in danh_sach:
        if ct["ma"] == ma:
            ct["ban_thang"] = int(input("Bàn thắng mới: "))
            ct["kien_tao"] = int(input("Kiến tạo mới: "))
            tinh_toan(ct)
            luu_du_lieu(danh_sach)
            print("Cập nhật thành công!")
            return
    print("Không tìm thấy!")

def xoa(danh_sach):
    ma = input("Nhập mã cần xóa: ")
    for i, ct in enumerate(danh_sach):
        if ct["ma"] == ma:
            if input("Bạn chắc chắn xóa? (y/n): ") == 'y':
                danh_sach.pop(i)
                luu_du_lieu(danh_sach)
                print("Đã xóa!")
                return
    print("Không tìm thấy!")

def tim_kiem(danh_sach):
    tu_khoa = input("Nhập mã hoặc tên: ").lower()
    ket_qua = [ct for ct in danh_sach if tu_khoa in ct['ten'].lower() or tu_khoa in ct['ma'].lower()]
    hien_thi(ket_qua)

def sap_xep(danh_sach):
    print("1. Điểm giảm dần | 2. Bàn thắng giảm dần")
    lua_chon = input("Chọn: ")
    khoa = "diem" if lua_chon == '1' else "ban_thang"
    danh_sach.sort(key=lambda x: x[khoa], reverse=True)
    hien_thi(danh_sach)

def thong_ke_danh_hieu(danh_sach):
    for hang in ["Vàng", "Bạc", "Đồng"]:
        print(f"Danh hiệu {hang}: {[ct['ten'] for ct in danh_sach if ct['danh_hieu'] == hang]}")

def thong_ke_so_luong(danh_sach):
    dem = {"Vàng": 0, "Bạc": 0, "Đồng": 0}
    for ct in danh_sach: dem[ct["danh_hieu"]] += 1
    print(f"Số lượng: {dem}")

def hien_thi_max_min(danh_sach):
    if not danh_sach: return
    hien_thi(danh_sach)

def main():
    danh_sach = doc_du_lieu()
    while True:
        print("\n--- MENU QUẢN LÝ CẦU THỦ ---")
        print("1. Hiển thị danh sách")
        print("2. Thêm mới cầu thủ")
        print("3. Cập nhật thông tin")
        print("4. Xoá cầu thủ")
        print("5. Tìm kiếm cầu thủ")
        print("6. Sắp xếp danh sách")
        print("7. Thống kê cầu thủ theo danh hiệu")
        print("8. Thống kê số lượng theo danh hiệu")
        print("9. Hiển thị danh sách danh hiệu")
        print("10. Thoát")
        
        chon = input("Chọn chức năng: ")
        if chon == '1': hien_thi(danh_sach)
        elif chon == '2': them(danh_sach)
        elif chon == '3': cap_nhat(danh_sach)
        elif chon == '4': xoa(danh_sach)
        elif chon == '5': tim_kiem(danh_sach)
        elif chon == '6': sap_xep(danh_sach)
        elif chon == '7': thong_ke_danh_hieu(danh_sach)
        elif chon == '8': thong_ke_so_luong(danh_sach)
        elif chon == '9': hien_thi_max_min(danh_sach)
        elif chon == '10': break

if __name__ == "__main__":
    main()