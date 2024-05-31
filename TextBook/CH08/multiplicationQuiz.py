import random
import time

import pyinputplus as pyip

number_of_questions = 5
correct_answers = 0
for question_number in range(number_of_questions):

    num1 = random.randint(11, 99)
    num2 = random.randint(11, 99)
    prompt = f'#{question_number}: {num1} + {num2} = '

    try:
      
        pyip.inputStr(
            prompt,
            allowRegexes=[f'^{num1 + num2}$'],
            blockRegexes=[('.*', '残念!')],
            timeout=10,
            limit=3
        )
    except pyip.TimeoutException:
        print('時間切れです!')
    except pyip.RetryLimitException:
        print('所定の回数を超えました!')
    else:
        print('正解!')
        correct_answers += 1
    time.sleep(1)