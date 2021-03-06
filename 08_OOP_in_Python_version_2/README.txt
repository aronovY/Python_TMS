1) Опишите класс данных, назвав его Student.
В нем не должно быть описано вами ни одного перегружаемого метода (начинающихся на "__")
за исключением __post_init__(пригодится для последнего пункта, гуглим), но должна быть реализована следующая логика:
        a) Класс принимает на инициализацию объекта name (str),
            average_mark (float), age (int) и subjects (лист строк).
            Для листа строк используем такой тип: typing.List[str] (в начале файла нужен import typing)
        b) Возраст по умолчанию должен быть равен 18, а список предметов - пустым листом.
        c) Сравнение и сортировка студентов должны идти только по их среднему баллу.
            Для тех, у кого средний балл одинаков, порядок определяется их положением в листе для сортировки.
        d) В строковом представлении студента должна быть информация о его имени и средней оценке,
            но не должно быть информации о его возрасте и предметах.
        e) При инициализации в объект студента также должна записываться первая буква его имени
        (или None, если имя - пустая строка) в self.first_letter.
        В подходящем методе (__init__ переопределять нельзя) в объект добавляется только это.




2) Напишите метакласс, который исправляет классы, в которых “забыли” расставить декораторы 🙃
        a) Убирает из класса все атрибуты, начинающиеся на одно нижнее подчеркивание (только одно;
            два и более не трогаем).
        b) Добавляет декоратор property на все функции, которые принимают только self,
            а также в таких функциях убирают “get_” в начале названия (если присутствует).
        c) Добавляет декоратор classmethod на все функции, где первый параметр в ней назван “cls”.
        d) Добавляет декоратор staticmethod на все функции, которые не принимают ни self, ни cls.
        e) Добавляет к названию класса приставку “Decorated” (просто в начале строки с названием).

        Вспомогательные методы:
            1) Как узнать список параметров функции?
                """
                >>> def my_func(self, a ,b): pass
                ...
                >>> import inspect
                >>> list(inspect.signature(my_func).parameters.keys())
                ['self', 'a', 'b']
                """

	        2) Как добавить декоратор к объекту функции?
	                Вспоминаем, что декоратор - обычная функция,
	                принимающая какую-то другую функцию (объект),
	                и возвращающая ее обернутую версию, так что
	                """decorated_function = decorator(old_function)"""