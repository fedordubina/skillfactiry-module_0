import numpy as np


def score_game(game_core):
  '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
  count_ls = []
  np.random.seed(1) # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
  random_array = np.random.randint(1,101, size=(1000))
  for number in random_array:
    count_ls.append(game_core(number))
  score = int(np.mean(count_ls))
  print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
  return(score) 
    

def game_core_v3(number):
  count = 1
  predict = temp = 100//2
  while number != predict:
    if temp>1:
      temp //= 2
    count+=1
    if number > predict: 
      predict += temp
    elif number < predict: 
      predict -= temp
  return(count)
score_game(game_core_v3)