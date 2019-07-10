#read() : 개행문자를 포함한 하나의 문자열
with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)

#readlines(): 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 만들어냄
with open('with_ssafy.txt','r') as f:
    lines = f.readlines()#어차피 리스트를 만들어내는 것이므로 변수에 저장
    for line in lines:
        # print(line.strip())#print 자체가 개행문자 포함되어 있으므로 라인이 가지고 있는 뒤의 요소를 없앰.
        print(dir(line))#dir()자주 사용
