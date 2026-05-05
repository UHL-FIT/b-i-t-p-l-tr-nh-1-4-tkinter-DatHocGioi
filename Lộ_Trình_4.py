import tkinter as tk
from datetime import datetime
from tkinter import messagebox

def xu_ly_du_lieu():
   # 1. Lấy dữ liệu từ ô nhập bằng phương thức .get()
    mssv = input_ma_sv.get()
    ho_ten = input_ho_ten.get()

    thoi_gian = datetime.now().strftime("%H:%M:%S")

    # Kiểm tra trống
    if ho_ten == "":
        messagebox.showwarning("Chú ý", "Bạn không được để trống họ tên!")
        return # Dừng hàm tại đây, không chạy tiếp bên dưới
    
    if mssv == "":
        messagebox.showwarning("Chú ý", "Bạn không được để trống mã sinh viên!")
        return # Dừng hàm tại đây, không chạy tiếp bên dưới
    
    # Kiểm tra MSSV phải là số
    if not mssv.isdigit():
        # Thông báo Popup lỗi
        messagebox.showerror("Lỗi dữ liệu", "Mã sinh viên phải là số!")
        # In ra terminal lỗi để dev biết
        print(f"[{thoi_gian}] Lỗi: MSSV '{mssv}' không hợp lệ.")
        return # Dừng hàm
    
    # 2. In ra Terminal để lập trình viên kiểm tra
    print(f"Dữ liệu nhận được: [{thoi_gian}] MSSV: {mssv} - Họ tên: {ho_ten}")
    
    # 3. Cập nhật trực tiếp lên giao diện (Label kết quả)
    if ho_ten != "":
        nhan_ket_qua.config(text=f"Chào sinh viên: {ho_ten} ({mssv})", fg="blue")
    else:
        nhan_ket_qua.config(text="Vui lòng không để trống thông tin!", fg="red")

    # --- Xóa trắng ô nhập liệu ---
    # .delete(0, tk.END) nghĩa là xóa từ vị trí đầu tiên (0) đến hết (END)
    input_ma_sv.delete(0, tk.END)
    input_ho_ten.delete(0, tk.END)


root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

# --- PHẦN GIAO DIỆN (Giữ nguyên từ Lộ trình 3) ---
tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_ma_sv = tk.Entry(root)
input_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
input_ho_ten = tk.Entry(root)
input_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- PHẦN MỚI: NÚT BẤM VÀ KẾT QUẢ ---

# Nút bấm có tham số 'command' kết nối tới hàm xử lý
nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu)
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

# Nhãn hiển thị kết quả ngay trên giao diện
nhan_ket_qua = tk.Label(root, text="Chưa có dữ liệu", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
