import json

class JSONWorker:

    def __init__(self, data: list):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data

    def make_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.get_data(), fp, ensure_ascii=False, indent=4)
        return 'Запись прошла успешно'

    def reading_data_from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            python_data = json.load(file)
        return python_data

jsonworker = JSONWorker([
{'Тайто Кубо' : 'Блич', 'Гэгэ Акутами' : 'Магическая битва'},
{'Дэвид Финчер' : 'Бойцовский клуб','Даррен Аронофски' : 'Реквием по мечте'},
{'Олег Кузовков' : 'Маша и медведь', 'Александр Татарский' : 'Фиксики'}])

print(jsonworker.make_json('data/company.json'))
print(jsonworker.reading_data_from_json('data/company.json'))
