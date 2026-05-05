from struct import pack
import tkinter as tk

from numpy import pad

# 1 Khởi tạo cửa sổ gốc
root = tk.Tk()
root.title("Nguyễn Văn Đạt")
root.geometry("500x500")
# Khi thay đổi kích thước cửa sổ chính không có sự thay đổi về dòng chữ chào mừng
# dòng chữ luôn được canh giữa cửa sổ theo chiều ngang và luôn cách lề trên cửa sổ chính 50px

# 2 Tạo thành phần hiển thị (Label)
Loi_Chao = tk.Label(root, text = "Chào mừng sinh viên Đại học Hạ Long!")
Loi_Chao.pack(pady = 50) # Đưa nhãn vào cửa sổ và tạo khoảng cách lề

# 3. Duy trì cửa sổ (vòng lặp chính)
root.mainloop()
