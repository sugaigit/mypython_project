  import random


  def start_message();
    print('じゃんけんスタート')

    drf get_myhand():
      print('自分の手を入力してください')
      return int(input('0:グー, 1:チョキ, 2:パー'))

    def get_you_hand():
      return random.randint(0, 2)


    def view_result(hand_df):
      if hand_df == 0:
          print('あいこ')
        elif hand_df == 2 or hand_diff == -1;
          print('勝ち')
        else:
          print('負け')

        start_message()
        my_hand = get_my_hand()
        you_hand = get_you_hand()
        hand_df = my_hand - you_hand
        view_result
