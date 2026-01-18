def get_nearest_shop(shop_points: list[tuple]) -> tuple:

    return min(shop_points, key=lambda point: (point[0] ** 2 + point[1] ** 2) ** 0.5)


if __name__ == '__main__':
    points = [
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    nearest_shop = get_nearest_shop(points)
    print(f"Ближайший магазин находится в координатах: {nearest_shop}")