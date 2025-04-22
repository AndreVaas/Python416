class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def show_rect(self):
        print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")


class RectFon(Rect):
    def __init__(self, width, height, background):
        super().__init__(width, height)
        self.fon = background

    def show_rect(self):
        super().show_rect()
        print("Фон:", self.fon)


class RectBorder(Rect):
    def __init__(self, width, height, border_width, frame_type, color_frame):
        super().__init__(width, height)
        self.border_width = border_width
        self.frame_type = frame_type
        self.color_type = color_frame

    def show_rect(self):
        super().show_rect()
        print(f"Толщина линии: {self.border_width}\nТип линии: {self.frame_type}\nЦвет линии: {self.color_type}")


shape1 = RectFon(400, 200, "yellow")
shape1.show_rect()
print()
shape2 = RectBorder(600, 300, "1px", "solid", "blue")
shape2.show_rect()