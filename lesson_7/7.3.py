class Cell:
    def __init__(self, numb):
        self.numb = numb

    def __add__(self, other):
        return Cell(self.numb + other.numb)

    def __str__(self):
        return str(self.numb)

    def __sub__(self, other):
        if (self.numb - other.numb) > 0:
            return Cell(self.numb - other.numb)
        else:
            return Cell('разность отрицательна')

    def __mul__(self, other):
        return Cell(self.numb * other.numb)

    def __truediv__(self, other):
        return Cell(self.numb // other.numb)


    def make_order(self, cell_number):
        full_rows = self.numb // cell_number
        last_row = self.numb % cell_number
        lines = ''
        for i in range(full_rows - 1):
            lines += f'{"*" * cell_number} \n'
        lines += f'{last_row * "*"}'
        return lines

cell1 = Cell(15)
cell2 = Cell(12)


# print(cell1 + cell2)
print(cell1.make_order(4))
