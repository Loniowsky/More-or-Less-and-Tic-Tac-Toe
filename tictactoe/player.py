class Player:
    __name = ''

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def is_name_empty(self):
        if self.__name == "":
            return True
        return False
