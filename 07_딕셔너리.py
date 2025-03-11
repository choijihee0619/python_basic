name_card = {'name':'홍길동',
             'tel':'010-0000-0000',
             'address':'부산', #,를 기준으로 줄바꿈가능, 중복키값 입력하면 덮어쓰기        
             'email':'hong@gmail.com'}#튜플을 키값으로 쓸수도있음
           
print(name_card)

name_card['etc'] = ['이사갈 수도 있음','1년안에'] #딕셔너리 추가

print(name_card)

print(name_card['address']) #key를 이용해서 value값

print(name_card['etc'][1]) #키 밸류가 리스트일 경우 인덱스로 접근가능

del name_card['address'] #밸류 삭제

print(name_card)

print(type(name_card)) #타입 dict

print(len(name_card))

print('address' not in name_card)

print(name_card.keys()) #key가 뭐 있는지 궁금하면
print(name_card.values()) #value값 도출
print(name_card.items()) #(key,value) 튜플로 도출

for k in name_card: #딕셔너리는 언급하지 않으면 key값이 우선
    print(k)
print('-'*30)
for k in name_card.values():
    print(k)
print('-'*30)
for k in name_card.items():
    print(k)
print('-'*30)
for k,v in name_card.items(): #k,v를 따로 변수 설정해서 프린트 하면 튜플 풀려서 출력
    print(k,v)
print('-'*30)

name_card.clear()
print(name_card) #비어있는 딕셔너리{} 출력, 비워주는 개념

# print(name_card['address']) 아래 get사용과 다른 값 -> 키에러
print(name_card.get('address')) # 없는 키를 입력해도 오류 안뜸 none

#다양한 함수나 메소드는 api 검색


s1 = set([1,2,3,3,2])
print(s1) #key값의 모임이라 중복값 덮어써버림

s2 = set('hello')
print(s2) #순서 없이 랜덤 배열 / 딕셔너리도 똑같음

