def main():
    
    print("start")
    
   
    points2 = [
        (17, 4), (32, 19), (6, 39), (0, 33), (20, 34),
        (38, 8), (21, 18), (32, 35), (4, 16), (20, 11)
    ]

   
    def get_line(x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        while True:
            yield (x1, y1)
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    
    unique_points = set()
    for i in range(len(points2) - 1):
        for p in get_line(*points2[i], *points2[i+1]):
            unique_points.add(p)

    print(len(unique_points))  


if __name__ == "__main__":
    main()
