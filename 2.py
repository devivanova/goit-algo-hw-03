import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_snowflake(t, order - 1, size)
        t.left(60)
        koch_snowflake(t, order - 1, size)
        t.right(120)
        koch_snowflake(t, order - 1, size)
        t.left(60)
        koch_snowflake(t, order - 1, size)


def draw_snowflake(order):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    for _ in range(3):
        koch_snowflake(t, order, 200)
        t.right(120)

    turtle.done()


if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха (0-5): "))
        if level < 0 or level > 5:
            print("Будь ласка, введіть число від 0 до 5.")
        else:
            draw_snowflake(level)
    except ValueError:
        print("Будь ласка, введіть дійсне число.")
