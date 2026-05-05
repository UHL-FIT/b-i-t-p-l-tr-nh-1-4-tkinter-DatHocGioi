import tkinter as tk

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x250")

# root.columnconfigure(1,weight=1)
root.columnconfigure(1,weight=1)
# Khi đổi cột muốn ưu tiên (co giãn) sang cột 0 thì cột chứa các ô nhập liệu sẽ không được
# co giãn theo kích thước của cửa sổ nữa mà thay vào đó cột chứa các nhãn sẽ được co giãn
# theo kích thước của cửa sổ

# trong thực tế ta thường chỉ cho cột chứa ô nhập liệu co giãn vì các ô nhãn thường là các
# từ ngắn, cố định, nếu cho cột chứa nhãn co giãn khi người dùng mở rộng cửa sổ khoảng cách
# giữa nhãn và ô nhập liệu sẽ bị kéo giãn khiến việc đọc trở nên khó hơn và nên ưu tiên cho
# dữ liệu biến động do dữ liệu người dùng nhập vào có độ dài không xác định, nếu người dùng
# mở rộng cửa sổ mà ô nhập liệu quá bé sẽ khiến người dùng có cảm giác khó chịu do không nhìn
# được những nội dung mà mình nhập vào


# 1. Tạo các thành phần (nhưng chưa hiện lên)
nhan_ma_sv = tk.Label(root, text="Mã sinh viên:")
input_ma_sv = tk.Entry(root)

nhan_ho_ten = tk.Label(root, text="Họ và tên:")
input_ho_ten = tk.Entry(root)

# Hàng 0
nhan_ma_sv.grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Hàng 1
nhan_ho_ten.grid(row=1, column=0, padx=10, pady=10, sticky="w")
input_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

root.mainloop()
