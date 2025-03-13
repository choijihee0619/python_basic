# f = open('새파일.txt','a') #쓰기모드는 자동으로 새파일 생성 #w는 덮어쓰기임
# result = f.write('문서에 저장되는 내용입니다.\n')
# print(result)
# print(len('문서에 저장되는 내용입니다.'))
# f.close()

f = open('새파일.txt')
# for line in f.readlines():
#     print(line)

# print(f.readline())
# while True:
#     line = f.readline() #리드라인을 사용하면 이미 한줄 읽음
#     print(line)
#     if not line:
#         break

print(f.read())

f.close()