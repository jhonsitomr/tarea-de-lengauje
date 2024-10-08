class Vehicle:

    brand: str
    model: str
    year: str

    def __init__(self, b: str, m: str, y: str):

        self.brand = b
        self.model = m
        self.year = y

    def description(self) -> str:

        return f'Marca: {self.brand}. Modelo: {self.model}. Año: {self.year}.'

class Car(Vehicle):

    doors: int

    def __init__(self, b: str, m: str, y: str, d: int):

        super().__init__(b, m, y)

        self.doors = d

    def description(self) -> str:

        return f'Marca: {self.brand}. Modelo: {self.model}. Año: {self.year}. Puertas: {self.doors}'

class Bicycle(Vehicle):

    type: str

    def __init__(self, b: str, m: str, y: str, t: str):

        super().__init__(b, m, y)

        self.type = t

    def description(self) -> str:

        return f'Marca: {self.brand}. Modelo: {self.model}. Año: {self.year}. Tipo: {self.type}'
