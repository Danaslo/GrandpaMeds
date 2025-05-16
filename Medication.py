
class Medication:

    def __init__(self,name,dose):
        self.__name = name
        self.__dose = dose

    def get_name(self):
        return self.__name
    
    def get_dose(self):
        return self.__dose
    
    def to_string(self):
        return f"{self.__name} {self.__dose}"