import numpy as np

def predict_num(number, min_num=1, max_num=100):
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        min_num (int): Минимум диапазона загадонного числа. Defaults to 1.
        max_num (int): Максимум диапазона загадонного числа. Defaults to 100.

    Returns:
        int: Число попыток
    """

    count = 0
    predict_number = int(max_num / 2)

    while True:
        count += 1
        if number == 100:
            predict_number = number
            break # конец игры, выход из цикла

        elif min_num <= number < predict_number:
            max_num = predict_number
            predict_number = int(max_num / 2)

        elif predict_number < number <= max_num:
            min_num = predict_number
            predict_number = int((max_num + min_num) / 2)

        else:
            break # конец игры, выход из цикла

        if count == 1000: #условие выхода из бесконечного цикла
          print('Что-то не так! Бесконечный цикл')
          print('min_num', min_num, 'max_num', max_num, 'number', number)
          break #выход из цикла

    #вывод для проверки (при необходимости раскоментить)
    #print('number', number, 'predict_number', predict_number, 'count', count)

    return(count)

def score_game(predict_num) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        predict_num ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(42) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict_num(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(predict_num)