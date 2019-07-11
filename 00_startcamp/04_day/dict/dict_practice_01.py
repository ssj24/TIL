"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
scores = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
total_score=0
for subject_score in scores.values():
    total_score += subject_score
avg_score = total_score/len(scores)
print(avg_score)





# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
# total_score=0
# for key in scores.keys():#value가 딕셔너리라서 또 for문을 돌리는 것
#     for value in scores[key].values():
#         total_score += value
# avg_score=total_score/len(scores)
# print(avg_score)
total_score=0
count=0
for person_score in scores.values():
    for individual_score in person_score.values():
        total_score += individual_score
        count += 1#for문이 몇 번 도는지를 카운트!!!
avg_score=total_score/count
print(avg_score)


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
for name, temp in city.items():#이렇게 하면 서울의 온도가 [-6, -10, 5]의 리스트로 나옴
    avg_temp = sum(temp)/len(temp)#sum은 리스트나 딕셔너리의 합을..
    print(f'{name} : {avg_temp:.1f}')#:.1f는 소수점 한자리까지 표현하겠다는 뜻

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
#처음for문으로 첫번째 key값인 서울의 온도 중 최고와 최저가 기록되고
# 두번째로 대전이 오면 기록된 최고와 최저온도와 비교해서 기록
# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
count = 0
for name, temp in city.items():
    #단 한번만 실행되는 비교조건이 필요
    if count == 0:
        hot_temp = max(temp)
        cold_temp = min(temp)
        hot_city = name
        cold_city = name
    else:
        #최저 온도가 cold_temp보다 낮으면, cold_temp에 값을 새로 넣고,
        if min(temp) < cold_temp:
            cold_temp = min(temp)
            cold_city = name
        #최고 온도가 hot_temp보다 높으면, hot_temp에 값을 새로 넣는다.
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
    count += 1#큰 if문의 true식은 한 번만 돌고
print(f'최고로 더웠던 지역은 {hot_city}로 {hot_temp}도였고, 최고로 추웠던 지역은 {cold_city}로 {cold_temp}도였다.')




# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
#이 문제는 서울 온도 리스트에 2가 있나요?라는 뜻
# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in city['서울']:
    print('네')
else:
    print('아니오, 없어요')


