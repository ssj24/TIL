from django import template


register = template.Library() # 기존 템플릿 라이브러리에 

@register.filter
def hashtag_link(word):
    # word는 article 객체가 들어갈 건데
    # article의 content들만 모두 가져와서 그 중 해시태그에만 링크를 붙인다
    content = word.content + ' ' # 공백으로 구분하기 때문
    hashtags = word.hashtags.all()
    for hashtag in hashtags:
        content = content.replace(hashtag.content+' ', f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}<a/> ')
        # html a태그를 씌운 hashtag.content로 바꿈
        # 주소는 하드코딩을 해야 한다.(f 스트링으로 변수를 넣어줘야 함.))
        #변경 전 내용도 공백을 포함하고
        #변경 후 내용도 공백을 포함한다.(f 스트링 마지막에 공백))
    return content
