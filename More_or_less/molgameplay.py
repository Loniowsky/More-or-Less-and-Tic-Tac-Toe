import random
from More_or_less.validators.input_validator import input_validation


class MoLGameplay:


    def __init__(self, connection):
        self.connection = connection
        self.guess_number = 0

    def set_random_guess_number(self):
        self.guess_number = random.randint(-100,100)

    def get_answer(self):
        rcv = self.connection.send_data("Input number: ", True)
        if input_validation(rcv):
            return int(rcv)
        else:
            return self.get_answer()

    def answer(self, answer):
        if answer < self.guess_number:
            self.connection.send_data("More", False)
            return False
        elif answer > self.guess_number:
            self.connection.send_data("Less", False)
            return False
        else:
            return True

    def start(self):
        self.set_random_guess_number()
        print(self.guess_number)
        while True:
            if self.answer(self.get_answer()):
                break
        print("END")
