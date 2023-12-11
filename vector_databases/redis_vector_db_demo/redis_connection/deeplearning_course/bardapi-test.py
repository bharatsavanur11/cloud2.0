from bardapi import Bard
import os
os.environ['_BARD_API_KEY'] = 'AIzaSyDx2gqnfrfZW_GyYBdMxMcdZkGUQR-Gg2k'
input_text = 'What is google bard'

bard_output = Bard().get_answer(input_text)['content']
print(bard_output)



