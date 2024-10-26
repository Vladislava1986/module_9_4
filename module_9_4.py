from random import choice
#1
first = 'Мама мыла раму'
second = 'Рамена мало было'
res = list(map(lambda x,y: x==y, first, second))
print(res)

#2
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open (file_name, mode='w', encoding='UTF-8') as file:
            for line in data_set:
                file.write(str(line))
                file.write('\n')
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 1, 2, 3, 1.25)

#3
class MysticBall:
    def __init__(self, *word):
        self.words = word
    def __call__(self):
        word = choice(self.words)
        return word

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'да-да', 'ага')
print(first_ball())
print(first_ball())
print(first_ball())
