"""
Mô-đun calculator đơn giản dùng làm ví dụ quy trình Git/GitHub.

Giả lập:
- Lead tạo file này với 2 hàm cơ bản: add, multiply.
- Dev A thêm hàm subtract thông qua 1 nhánh feature + Pull Request.
- Dev B thêm hàm divide thông qua 1 nhánh feature + Pull Request.

Trong thực tế, mỗi lần thêm hàm là một vòng:
Task -> Tạo branch -> Code -> Commit -> Push -> Pull Request -> Review -> Merge.
"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """
    Cộng hai số a và b.

    Ví dụ:
    >>> add(2, 3)
    5
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """
    Nhân hai số a và b.

    Ví dụ:
    >>> multiply(2, 3)
    6
    """
    return a * b


def subtract(a: float, b: float) -> float:
    """
    Trừ hai số a - b.

    Hàm này giả sử được thêm bởi Dev A trong nhánh
    'feature/add-subtract-function' và merge qua Pull Request.

    Ví dụ:
    >>> subtract(5, 2)
    3
    """
    return a - b


def divide(a: float, b: float) -> float:
    """
    Chia a cho b, có xử lý chia cho 0.

    Hàm này giả sử được thêm bởi Dev B trong nhánh
    'feature/add-divide-function' và merge qua Pull Request.

    Ví dụ:
    >>> divide(6, 3)
    2.0

    :raises ZeroDivisionError: nếu b == 0.
    :raises TypeError: nếu a hoặc b không phải là số (int/float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a và b phải là số (int hoặc float)")

    if b == 0:
        raise ZeroDivisionError("Không thể chia cho 0")

    return a / b


if __name__ == "__main__":
    # Đoạn này mô phỏng việc chạy nhanh để test bằng tay.
    print("Demo calculator:")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("2 * 3 =", multiply(2, 3))
    print("6 / 3 =", divide(6, 3))


