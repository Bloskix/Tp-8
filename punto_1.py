class TorreDeControl:

    def __init__(self):
        self.to_land = []
        self.to_take_off = []

    def recognition(self,airplain, status):
        if status == 1:
            self.to_land.append(airplain)
        elif status == 2:
            self.to_take_off.append(airplain)

    def action(self):
        if self.to_land == []:
            try:
                return self.to_land.pop(0)
            except IndexError:
                raise ValueError("La cola esta vacía")
        else:
            try:
                return self.to_take_off.pop(0)
            except IndexError:
                raise ValueError("La cola esta vacía")

    def __str__(self):
        return len(self.to_land) and len(self.to_take_off)

