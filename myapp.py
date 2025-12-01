
import math

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# --- Kiểm tra tam giác ---
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("a, b, c là 3 cạnh của một tam giác.")

    # --- Tam giác đều ---
    if a == b == c:
        print("→ Đây là tam giác ĐỀU.")

    # --- Tam giác cân ---
    elif a == b or a == c or b == c:
        # kiểm tra vuông luôn
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
            print("→ Đây là tam giác VUÔNG CÂN.")
        else:
            print("→ Đây là tam giác CÂN.")

    # --- Tam giác vuông ---
    elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
        print("→ Đây là tam giác VUÔNG.")

    else:
        # --- Tam giác nhọn / tù ---
        # sắp xếp tăng dần
        x, y, z = sorted([a, b, c])

        if x*x + y*y > z*z:
            print("→ Đây là tam giác NHỌN.")
        else:
            print("→ Đây là tam giác TÙ.")

else:
    print("a, b, c KHÔNG phải là 3 cạnh của tam giác!")


a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("a, b, c là độ dài 3 cạnh của một tam giác.")
else:
    print("a, b, c KHÔNG phải là độ dài 3 cạnh của một tam giác.")
