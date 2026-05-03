class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self._salary = 0
        self.set_salary(salary)
        self.__department = ""
        self.set_department(department)

    def get_salary(self):
        return f"ваша зарплата: {self._salary}"
    
    def get_department(self):
        return f"ваш відділ: {self.__department}"
    
    def set_salary(self, value):
        if value < self._salary:
            print(f"Помилка: Не можна зменшити зарплату з {self._salary} до {value}!")
        else:
            self._salary = value
            print(f"Зарплату успішно оновлено до {self._salary}")
    
    def set_department(self, new_dep):
        if isinstance(new_dep, str) and len(new_dep) > 0:
            self.__department = new_dep
        else:
            print("Помилка: Назва відділу має бути рядком.")