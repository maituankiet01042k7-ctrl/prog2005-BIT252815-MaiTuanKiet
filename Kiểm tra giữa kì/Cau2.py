def bai2():
    print("Các số lẻ từ 17 đến 111 (theo thứ tự giảm dần):")
    for i in range(111, 15, -2):
        print(i, end=" ")
    print("\n")

    print("Các số nguyên tố trong khoảng từ 17 đến 111:")
    for i in range(17, 112):
        if is_prime(i):
            print(i, end=" ")
    print("\n")
