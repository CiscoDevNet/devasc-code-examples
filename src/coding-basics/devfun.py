# Fill in this file with the code from the course introduction

from enum import Enum
class emoji(Enum):
  seenoevil = '\U0001F648'
  hearnoevil = '\U0001F649'
  speaknoevil = '\U0001F64A'

for monkey in emoji:
  print(monkey.name, monkey.value)
