class Departament:
    def __init__(self, name, budget, employees={}):
        self.name = name
        self.budget = float(budget)
        self.employees = employees

    class BudgetError(ValueError):
        pass

    def get_budget_plan(self):
        try:
            if self.budget - sum(self.employees.values()) < 0:
                raise self.BudgetError('Budget Error :(', self, float(round(self.budget - sum(self.employees.values()), 2)) )
        except ValueError as be:
            print(be)
            return float(round(self.budget - sum(self.employees.values()), 2))
        else:
            return float(round(self.budget - sum(self.employees.values()), 2))

    def get_average_salary(self):
        return float(round(sum(self.employees.values()) / len(self.employees.keys()), 2))

    def merge_departament(self, *args):
        name_new = self.name
        budget_new = self.budget
        employees_new = self.employees.copy()
        for item in args:
            name_new += ' - ' + item.name
            budget_new += item.budget
            employees_new.update(item.employees)
        Departament(name_new, budget_new, employees_new).get_budget_plan()
        return Departament(name_new, budget_new, employees_new)

    def __str__(self):
        return f'Name: {self.name} (Workers:({len(self.employees.keys())})' \
               f' - average salaries: {self.get_average_salary()}, ' \
               f'budget: {round(self.budget, 2)})'

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        return self.get_budget_plan() > other.get_budget_plan()

    def __eq__(self, other):
        return self.get_budget_plan() == other.get_budget_plan()

    def __or__(self, other):
        if self > other:
            print('Win departament ->', self)
        elif self == other:
            print('Win departament ->', self)
        else:
            print('Win departament ->', other)


if __name__ == '__main__':
    dep = Departament('WOK', 2000, {'Vasya': 220., 'Anna': 249.1})
    dep_2 = Departament('McDonalds', 2000, {'John': 20.34, 'Julia': 509.12})
    dep_3 = Departament('Leto', 2000, {'Bill': 220., 'Kate': 249.1})
    dep_4 = Departament('Green', 1000, {'Jeff': 220.34, 'Matt': 509.12})
    dep_5 = Departament.merge_departament(dep_4, dep_2, dep, dep_3)
    print(dep_5)
    dep_2 | dep_4
