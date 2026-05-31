import json
import os

FILE_NAME = "data.json"

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def save_data(player_list):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(player_list, f, indent=4, ensure_ascii=False)

def calculate_stats(player):
    player["score"] = (player["goals"] * 2) + player["assists"]
    if player["score"] > 40:
        player["rank"] = "Vàng"
    elif player["score"] > 20:
        player["rank"] = "Bạc"
    else:
        player["rank"] = "Đồng"
    return player

def display_list(player_list):
    print(f"\n{'Mã':<10} {'Tên':<15} {'Số trận':<10} {'Bàn':<10} {'Kiến tạo':<10} {'Điểm':<10} {'Danh hiệu':<10}")
    print("-" * 80)
    for p in player_list:
        print(f"{p.get('id', ''):<10} {p.get('name', ''):<15} {p.get('matches', 0):<10} {p.get('goals', 0):<10} {p.get('assists', 0):<10} {p.get('score', 0):<10} {p.get('rank', ''):<10}")

def add_player(player_list):
    player_id = input("Nhập mã cầu thủ: ")
    if any(p['id'] == player_id for p in player_list):
        print("Mã đã tồn tại!")
        return
    name = input("Nhập tên: ")
    matches = int(input("Số trận: "))
    goals = int(input("Bàn thắng: "))
    assists = int(input("Kiến tạo: "))
    
    new_player = {"id": player_id, "name": name, "matches": matches, "goals": goals, "assists": assists}
    player_list.append(calculate_stats(new_player))
    save_data(player_list)
    print("Thêm thành công!")

def update_player(player_list):
    player_id = input("Nhập mã cầu thủ cần cập nhật: ")
    for p in player_list:
        if p["id"] == player_id:
            p["goals"] = int(input("Nhập bàn thắng mới: "))
            p["assists"] = int(input("Nhập kiến tạo mới: "))
            calculate_stats(p)
            save_data(player_list)
            print("Cập nhật thành công!")
            return
    print("Không tìm thấy cầu thủ!")

def delete_player(player_list):
    player_id = input("Nhập mã cầu thủ cần xóa: ")
    for i, p in enumerate(player_list):
        if p["id"] == player_id:
            if input("Bạn có chắc muốn xóa? (y/n): ").lower() == 'y':
                player_list.pop(i)
                save_data(player_list)
                print("Đã xóa thành công!")
                return
    print("Không tìm thấy!")

def search_player(player_list):
    keyword = input("Nhập tên hoặc mã để tìm: ").lower()
    results = [p for p in player_list if keyword in p['name'].lower() or keyword in p['id'].lower()]
    display_list(results)

def sort_players(player_list):
    print("1. Điểm giảm dần | 2. Bàn thắng giảm dần")
    choice = input("Chọn: ")
    key = "score" if choice == '1' else "goals"
    player_list.sort(key=lambda x: x.get(key, 0), reverse=True)
    display_list(player_list)

def stats_rank(player_list):
    counts = {"Vàng": 0, "Bạc": 0, "Đồng": 0}
    for p in player_list:
        counts[p.get("rank", "Đồng")] += 1
    print("\n--- Thống kê số lượng theo danh hiệu ---")
    for k, v in counts.items():
        print(f"{k}: {v} cầu thủ")

def display_extreme_ranks(player_list):
    if not player_list: return
    print("Chức năng hiển thị danh hiệu cao nhất/thấp nhất.")
    display_list(player_list)

def main():
    player_list = load_data()
    while True:
        print("\n--- MENU QUẢN LÝ CẦU THỦ ---")
        print("1. Hiển thị danh sách cầu thủ")
        print("2. Thêm mới cầu thủ")
        print("3. Cập nhật thông tin")
        print("4. Xoá cầu thủ")
        print("5. Tìm kiếm cầu thủ")
        print("6. Sắp xếp danh sách")
        print("7. Thống kê danh hiệu")
        print("8. Thống kê số lượng cầu thủ theo danh hiệu")
        print("9. Hiển thị danh sách max/min danh hiệu")
        print("10. Thoát")
        
        choice = input("Chọn chức năng (1-10): ")
        
        if choice == '1': display_list(player_list)
        elif choice == '2': add_player(player_list)
        elif choice == '3': update_player(player_list)
        elif choice == '4': delete_player(player_list)
        elif choice == '5': search_player(player_list)
        elif choice == '6': sort_players(player_list)
        elif choice == '7': stats_rank(player_list)
        elif choice == '8': stats_rank(player_list)
        elif choice == '9': display_extreme_ranks(player_list)
        elif choice == '10': 
            print("Đã thoát chương trình.")
            break
        else: print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()