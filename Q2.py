def get_line(x1, y1, x2, y2):
    """برگشتن نقاط روی خط بین (x1,y1) و (x2,y2) با الگوریتم بسلاین"""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        yield (x1, y1)   # مستقیم نقطه رو برگردون
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy


def count_unique_cells(points):
    """محاسبه تعداد خانه‌های یکتا در مسیر بین لیست نقاط"""
    unique_points = set()
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        for p in get_line(x1, y1, x2, y2):
            unique_points.add(p)
    return len(unique_points)


def main():
    # ورودی نمونه
    points = [
        (13, 14), (6, 13), (18, 7), (4, 11), (3, 14)
    ]

    print(count_unique_cells(points))  # خروجی نهایی


if __name__ == "__main__":
    main()
