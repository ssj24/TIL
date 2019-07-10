import os
#1. 해당 파일들이 있는 위치로 이동 chdir = change directory
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\change_filenames')#파일 주소에 있는 \가 이스케이프 문자열이 아니라 그냥 파일위치를 알려주는 것이라는 것을 알리기 위해 윈도우에서만 주소 앞에 r넣기
#2. 현재 폴더 안의 모든 파일 이름을 수집
filenames = os.listdir('.')#listdir = list directory 이미 해당 파일들이 있는 위치로 이동했기 때문에 ()에 디렉토리 주소를 써야 하는데 현재 위치면 되므로 .
#3. 각각의 파일명을 돌면서 수정한다.
#for filename in filenames:
#    os.rename(filename, f'SAMSUNG_{filename}')#os.rename(이전파일명, 바꿀파일명)

#4. SAMSUNG을 SSAFY로 변환
for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG_', "SSAFY_"))#'happy'.replace('h', 'b')이런 식으로 일부만 바꿈 