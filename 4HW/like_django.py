class Desk:
    def __init__(self, name, general_dict):
        self.name = name
        self.general_dict = general_dict

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if instance is None:  # если вдруг мы захотели изменить атрибут класса, я не дам
            return self
        example = None
        flag = None
        # проверка на корректность введенных данных
        if self.name == 'student':
            flag = 0
            if type(value) is not str:
                raise TypeError
        if self.name == 'subject':
            flag = 1
            if type(value) is not str:
                raise TypeError
        if self.name == 'mark':
            flag = 2
            if (type(value) is not int) or (value > 5) or (value < 2):
                raise ValueError
        # конец проверки
        instance.__dict__[self.name] = value  # добавляем в словарь экземпляра наш атрибут
        for i in globals().items():
            if i[1] == instance:
                example = i[0]
        if example not in self.general_dict:  # создаем лист главном словаре, если в первый раз используем экземпляр
            self.general_dict[example] = [None for i in range(3)]
        self.general_dict[example][flag] = value

    def __del__(self):
        pass


class Students:
    """
    в классе за метод Update отвечает дескриптор, то есть если изменить атрибут экземпляра класса,
    то он и изменится в таблице, только для изменения не нужно вызывать функцию save
    """
    general_dict = dict()  # в этом словаре ключ-название экземпляра класса, а в значении лист,
    # где первый элемент имя студента, второй- предмет, третий оценка за него

    student = Desk('student', general_dict)
    subject = Desk('subject', general_dict)
    mark = Desk('mark', general_dict)

    def __init__(self, student, subject, mark):
        self.student = student
        self.subject = subject
        self.mark = mark

    @staticmethod
    def create(instance, student=None, subject=None, mark=None):
        # проверка на корректность введенных данных
        if (student is not None) and (type(student) is not str):
            raise TypeError
        if (subject is not None) and (not isinstance(subject, str)):
            raise TypeError
        if ((mark is not None) and (not isinstance(mark, int))) or (mark > 5) or (mark < 2):
            raise TypeError
        # конец проверки
        Students.general_dict.update({instance: [student, subject, mark]})

    @staticmethod
    def all():
        print('name str\t\tStudent\t subject\t  mark')
        for i in Students.general_dict.items():
            print(f'{i[0]}\t\t\t\t{i[1][0]}\t\t{i[1][1]}\t\t{i[1][2]}')

    @staticmethod
    def get(student=None, subject=None, mark=None):
        similarity = list()
        items = list(Students.general_dict.items())
        for i in items:
            temp = 0
            if (student is not None) and (student == i[1][0]):
                temp += 1
            if (subject is not None) and (subject == i[1][1]):
                temp += 1
            if (mark is not None) and (mark == i[1][2]):
                temp += 1
            similarity.append(temp)
        minimal = max(similarity)
        answer_list = list()
        for i in range(len(similarity)):
            if similarity[i] == minimal:
                answer_list.append(items[i])
        return answer_list


a = Students('a','math',4)
b = Students('b','math',3)

a.student = 'a0'
b.student = 'b0'
Students.create('k', 'C0', 'math', 2)
Students.create('f', '20', 'math', 3)
print(Students.get(mark=2))
Students.all()
