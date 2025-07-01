#Вариант 31
#2)Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год
#выпуска". От этого класса унаследуйте класс "Автомобиль" и добавьте в него
#свойство "тип кузова".

class Transport:
    def __init__(self, brand="", model="", year=0):
        self._brand = brand  
        self._model = model  
        self._year = year 
    
    def get_info(self):
        return {
            "brand": self._brand,
            "model": self._model,
            "year": self._year
        }

class Car(Transport):
    def __init__(self, brand="", model="", year=0, body_type=""):
        super().__init__(brand, model, year)
        self._body_type = body_type  

