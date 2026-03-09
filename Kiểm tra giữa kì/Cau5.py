def main():
    while True:
        print("======== MENU ========")
        print("- Bài 1")
        print("- Bài 2")
        print("- Bài 3")
        print("- Bài 4")
        print("- Thoát")
        print("======================")

        choice = input("Chọn chương trình chạy: ").strip()

        if choice in ['1', 'Bài 1', 'bai 1']:
            bai1()
        elif choice in ['2', 'Bài 2', 'bai 2']:
            bai2()
        elif choice in ['3', 'Bài 3', 'bai 3']:
            bai3()
        elif choice in ['4', 'Bài 4', 'bai 4']:
            bai4()
        elif choice.lower() in ['thoát', 'thoat', '5']:
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!\n")


if __name__ == "__main__":
    main()
