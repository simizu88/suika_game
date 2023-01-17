import math
import random
BOARD_SIZE = 5  # ボードの初期サイズ

def calc_distance(pos1, pos2):
    # ２点間の距離を求める
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)

def generate_position(size):
    x = random.randrange(0, size)  # x座標
    y = random.randrange(0, size)  # y座標
    return (x, y)

def move_position(direction, player_pos):
    # direction にしたがって、posを移動する
    player_x, player_y = player_pos
    if direction == "n":
      player_y = player_y - 1
    elif direction == "s":
      player_y = player_y + 1
    elif direction == "w":
      player_x = player_x - 1
    elif direction == "e":
      player_x = player_x + 1

    return (player_x, player_y)



#suika_x = random.randrange(0, BOARD_SIZE)  # スイカのx座標
#suika_y = random.randrange(0, BOARD_SIZE)  # スイカのy座標

#player_x = random.randrange(0, BOARD_SIZE)  # プレイヤーのx座標
#player_y = random.randrange(0, BOARD_SIZE)  # プレイヤーのy座標

# スイカの位置のタプル
#suika_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))
suika_pos = generate_position(BOARD＿SIZE)
# プレイヤーの位置のタプル
#player_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE)) 
player_pos = generate_position(BOARD＿SIZE)

print("スイカの位置は", suika_pos)
print("プレイヤーの位置は", player_pos)

#while (suika_x != player_x) or (suika_y != player_y):
while (suika_pos != player_pos):
  distance = calc_distance(suika_pos, player_pos)
  print("スイカへの距離:", distance)

  c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
  player_pos = move_position(c, player_pos)
  print("プレイヤーの位置は", player_pos)


#  player_x, player_y = player_pos
#  if c == "n":
#    player_y = player_y - 1
#  elif c == "s":
#    player_y = player_y + 1
#  elif c == "w":
#    player_x = player_x - 1
#  elif c == "e":
#    player_x = player_x + 1
  
#  player_pos = (player_x, player_y)
#  print("プレイヤーの位置は", player_pos)

print("スイカを割りました！")
