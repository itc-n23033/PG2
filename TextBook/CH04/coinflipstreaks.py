import random

def generate_coin_flips(length):
    """Generate a random sequence of coin flips of given length."""
    return [random.choice(['裏', '表']) for _ in range(length)]

def has_six_in_a_row(sequence):
    """Check if there are six consecutive '裏' or '表' in the sequence."""
    for i in range(len(sequence) - 5):
        if sequence[i:i+6] == ['裏'] * 6 or sequence[i:i+6] == ['表'] * 6:
            return True
    return False

number_of_streaks = 0
num_experiments = 10000

for experiment_number in range(num_experiments):
    # 100個の裏表のリストを作る
    coin_flips = generate_coin_flips(100)
    
    # 6連続の裏または表を見つける
    if has_six_in_a_row(coin_flips):
        number_of_streaks += 1

# 結果を表示
print(f'同じ6連続出現する確率: {number_of_streaks / num_experiments * 100:.2f}%')

