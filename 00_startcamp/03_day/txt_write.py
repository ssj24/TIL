#1.변수에 만들고 싶은 파일을 open()해야 한다.
# f = open('만들 파일 명', '행동')
#open()할 행동 > r: 읽기 / w: 쓰기(덮어씌워짐) / a: 추가
f = open('ssafy.txt', 'w')
#1부터 10까지 작성하기
for i in range(10):
    f.write(f'This is line {i+1}.\n')#이스케이프 문자열 중 \n은 개행 #i+1한 것은 range는 마지막 문자 포함 안 하기 때문
f.close()#반드시 닫아줘야 합니다.

#with 구문 : context manager
# f와 비슷함 그런데 close안 해도 됨
# with open('만들 파일 명', '행동')
with open('with_ssafy.txt', 'w') as f:
        for i in range(10):
            f.write(f'This is line {i+1}.\n')

#writelines() list를 넣어주면 요소 하나당 한 줄씩 작성한다.
with open('ssafy.txt', 'w') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])#리스트를 넣어줘야 함
