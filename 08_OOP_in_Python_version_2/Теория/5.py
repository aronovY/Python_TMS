from dataclasses import dataclass, field


def my_func(name: str, age: int, marks: list) -> float:
    pass


@dataclass
class Country:
    name: str
    population: int
    area: float
    coastline: float = 0

    def beach_per_person(self):
        """Метры береговой линии на человека"""
        return (self.coastline * 1000) / self.population


country = Country('Belarus', 10 ** 7, 123456)
print(country.name, country.population, country.area, country.coastline)
