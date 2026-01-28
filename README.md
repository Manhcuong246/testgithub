## Quy trình GitHub mẫu cho nhóm 6 dev + 1 reviewer

Ví dụ này mô phỏng **như thật** cách một nhóm làm việc với Git/GitHub trên một project nhỏ bằng Python.

- **Repo**: `sample-calculator`
- **Lead/Reviewer**: Anh T
- **Dev**: A, B, C, D, E, F

Trong thư mục này có mã nguồn ví dụ trong thư mục `src/`.

---

## 1. Góc nhìn Lead/Reviewer – Khởi tạo & cấu hình repo

### 1.1. Tạo repo trên GitHub

Trên GitHub (trang web):

1. Nhấn **New repository** → đặt tên `sample-calculator`.
2. Chọn:
   - **Public** (hoặc Private nếu cần).
   - Tick **Add a README file** (hoặc không cũng được).
3. Nhấn **Create repository**.

### 1.2. Clone về máy local (Lead làm bước này)

```bash
git clone https://github.com/<your-username>/sample-calculator.git
cd sample-calculator
```

Giả sử Lead tạo cấu trúc ban đầu:

- Tạo thư mục `src/`
- Tạo file `src/calculator.py` (đã có trong ví dụ này)
- Commit & push:

```bash
git add .
git commit -m "Init project structure with calculator module"
git push origin main
```

### 1.3. Thêm thành viên & bảo vệ nhánh `main`

Trên GitHub:

- Vào `Settings` → `Collaborators`:
  - Thêm 6 dev: A, B, C, D, E, F.

- Vào `Settings` → `Branches` → `Add branch protection rule`:
  - Branch name pattern: `main`
  - Tick:
    - **Require a pull request before merging**
    - **Require approvals** (1 approval)
    - **Do not allow bypassing the above settings**
  - Lưu lại.

Từ giờ: **Không ai được push trực tiếp vào `main`**, mọi thay đổi phải qua Pull Request.

---

## 2. Mã nguồn ví dụ và phân chia task

Trong `src/calculator.py` ban đầu (Lead viết khung, dev sẽ bổ sung chi tiết):

- Hàm tính tổng `add(a, b)`
- Hàm nhân `multiply(a, b)`
- TODO cho dev: thêm hàm `subtract`, `divide`, viết tests, thêm CLI.

Giả sử Lead tạo các task:

- Dev A: Thêm hàm `subtract(a, b)`
- Dev B: Thêm hàm `divide(a, b)` (có xử lý chia cho 0)
- Dev C: Viết file `tests/test_calculator.py`
- Dev D: Tạo CLI đơn giản `main.py` đọc input và in kết quả
- Dev E, F: Task khác (ví dụ logging, format output, v.v.)

---

## 3. Góc nhìn Developer – Quy trình đầy đủ với ví dụ cụ thể

### 3.1. Chuẩn bị ban đầu (mỗi dev làm **1 lần**)

Dev A (tương tự cho các dev khác):

```bash
git clone https://github.com/<your-username>/sample-calculator.git
cd sample-calculator
```

Thiết lập Python environment (tùy chọn nhưng nên làm):

```bash
python -m venv venv
.\venv\Scripts\activate   # Windows PowerShell
pip install -r requirements.txt  # nếu có
```

### 3.2. Dev A làm task: thêm hàm `subtract(a, b)`

1. **Lấy code mới nhất từ `main`**:

```bash
git checkout main
git pull origin main
```

2. **Tạo nhánh tính năng**:

```bash
git checkout -b feature/add-subtract-function
```

3. **Sửa code trong `src/calculator.py`**

Ví dụ Dev A thêm hàm `subtract` (xem file thực tế trong `src/calculator.py`):

```python
def subtract(a: float, b: float) -> float:
    """
    Trừ hai số a - b.
    Ví dụ:
    >>> subtract(5, 2)
    3
    """
    return a - b
```

4. **Chạy thử (tạm thời)**:

```bash
python src/calculator.py
```

5. **Commit thay đổi**:

```bash
git status              # kiểm tra file thay đổi
git add src/calculator.py
git commit -m "Add subtract function to calculator"
```

6. **Push nhánh lên GitHub**:

```bash
git push -u origin feature/add-subtract-function
```

7. **Tạo Pull Request (PR)**:

Trên GitHub:
- Thấy banner “Compare & pull request” → nhấn.
- Chọn:
  - Base: `main`
  - Compare: `feature/add-subtract-function`
- Nhập:
  - Title: `[Feature] Add subtract function`
  - Description: mô tả ngắn.
- Gửi PR và assign Lead (Anh T) làm reviewer.

---

## 4. Góc nhìn Reviewer – Review & yêu cầu sửa

Lead (Anh T) vào Pull Request:

1. Tab **Files changed**:
   - Xem phần code của `subtract`.
2. Nếu muốn chỉnh cách viết docstring, có thể comment:
   - Ví dụ: “Bổ sung ví dụ cho số âm” hoặc “Thống nhất dùng tiếng Anh trong docstring”.
3. Lead chọn:
   - Nếu cần sửa: **Request changes**
   - Nếu ổn: **Approve**

### 4.1. Trường hợp yêu cầu sửa

Giả sử Lead comment:  
“Hãy thêm validate kiểu dữ liệu: nếu không phải số thì raise `TypeError`.”

Dev A quay lại nhánh của mình trên local:

```bash
git checkout feature/add-subtract-function
```

- Sửa code theo góp ý (ví dụ bổ sung type checking hoặc test).

Sau đó:

```bash
git add src/calculator.py
git commit -m "Improve subtract: add type checking"
git push
```

GitHub tự cập nhật thêm commit vào PR.  
Lead review lại:

- Nếu OK → **Approve** → **Merge pull request** (nên dùng “Squash and merge” cho gọn commit).

Sau khi merge:

- Dev A có thể xóa nhánh:

```bash
git checkout main
git pull origin main
git branch -d feature/add-subtract-function
```

---

## 5. Ví dụ đồng thời: Dev B làm hàm `divide(a, b)` và xử lý conflict

### 5.1. Dev B tạo nhánh tính năng

```bash
git checkout main
git pull origin main
git checkout -b feature/add-divide-function
```

Dev B thêm function `divide(a, b)` vào `src/calculator.py` (xem file thực tế) và commit:

```bash
git add src/calculator.py
git commit -m "Add divide function with zero division handling"
git push -u origin feature/add-divide-function
```

Tạo PR: `[Feature] Add divide function`.

### 5.2. Trường hợp `main` đã thay đổi trước khi merge PR của B

Giả sử PR của Dev A đã merge, làm cho `main` mới hơn.  
Dev B nên cập nhật nhánh của mình trước khi merge:

```bash
git checkout feature/add-divide-function
git pull origin main        # hoặc: git fetch origin && git merge origin/main
```

- Nếu có **merge conflict** trong `src/calculator.py`, Git sẽ báo:
  - Mở file, sửa vùng conflict (giữ cả `subtract` và `divide`).
  - Sau khi sửa xong:

```bash
git add src/calculator.py
git commit -m "Resolve merge conflict in calculator"
git push
```

PR được cập nhật, Lead review và merge bình thường.

---

## 6. Góc nhìn tổng thể – 6 dev + 1 reviewer

Tóm tắt vai trò:

- **Lead/Reviewer**
  - Thiết kế cấu trúc project.
  - Tạo repo, phân quyền, bật branch protection cho `main`.
  - Tạo issue/task, gán cho dev.
  - Review PR, comment, approve, merge.

- **Developer**
  - Luôn:
    - Pull `main` mới → tạo nhánh `feature/...`.
    - Code, test local.
    - Commit nhỏ, rõ message.
    - Push nhánh → tạo PR.
    - Sửa theo feedback review, push lại.
  - Không bao giờ push trực tiếp lên `main`.

Khi bạn mở file `src/calculator.py` trong ví dụ này, hãy tưởng tượng:

- Các hàm khác nhau được thêm bởi các dev khác nhau, mỗi người thông qua 1 nhánh + PR.
- Mỗi lần thêm hàm mới là 1 vòng lặp: **Task → Branch → Code → Commit → PR → Review → Merge**.

---

## 7. Bạn nên làm gì tiếp theo để “thực hành như thật”

1. Tạo một repo trên GitHub giống cấu trúc này (`src/calculator.py`).
2. Mời 1–2 bạn khác làm chung:
   - Bạn đóng vai Lead.
   - Mỗi bạn đóng vai Dev làm 1 hàm khác nhau.
3. Thử cố tình tạo conflict trong `calculator.py` rồi cùng nhau giải.

Nếu cần, bạn có thể yêu cầu thêm:
- Ví dụ cho **2–3 Pull Request thật chi tiết** (bao gồm diff và comment gợi ý).
- Hướng dẫn **giải conflict cụ thể** dựa trên nội dung `calculator.py`.


