# info: 조용찬 202004484 컴퓨터전자시스템전공
print("이름: 조용찬")
print("학번: 202004484")
print("학과: 컴퓨터전자시스템전공")

# quiz
from random import shuffle

nameList = ['조용찬', '조용필', '조용호']
shuffle(nameList)

ans = nameList.index('조용찬')
print('\n다음 중 저의 이름에 해당하는 번호를 고르시오.')
for i in range(len(nameList)):
  print(i + 1, '. ', nameList[i], sep = '')

if int(input()) - 1 == ans:
  print('정답입니다.')
else:
  print('오답입니다.')
