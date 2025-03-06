text01 = "문자열"
print(text01)
text02 = '문자열'
print(text02)
text03 = "jihee's"
print(text03)
text04 = '"jihee" is'
print(text04)
text05 = '''첫번째 줄
두번째 줄'''
print(text05)

# 따옴표 세개는 줄바꿈 가능

'''
여러줄 주석 대용: 첫번째 줄
두번째 줄
세번째 줄
'''
text06 = '첫줄 \n두번째'
print(text06)

print(text01 + text03)
# print(text04 + 3)
# str이랑 숫자는 더하기 안됨 

print(text04 * 2)

print(len(text01))

a = "life is too short, You need Python"
print(a[0])
print(a[33])
print(a[-1])

print(a[19:22])

data1 = "I eat %d apples. %s"
print(data1 % (3,'ggg'))
num01 = 1
txt01 = "I eat {:,.2f} apples {}"
print(txt01.format(300000, text03))

name = '홍길동'
age = 24
text02 = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(text02)

txt03 = f'나의 이름은 {name:^20}입니다. 나이는 {age:.2f}입니다.'
print(txt03)