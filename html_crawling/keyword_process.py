# -*- coding: utf-8 -*-
from konlpy.tag import Okt
okt=Okt()

import yake

#for korean
def konlpy(text):
    from konlpy.tag import Okt
    tokens = okt.phrases(text)
    okt = Okt()
    tokens = [ token for token in tokens if len(token) > 1 ] # 한 글자인 단어는 제외
    count_dict = [(token, text.count(token)) for token in tokens ]
    ranked_words = sorted(count_dict, key=lambda x:x[1], reverse=True)[:10]
    return [ keyword for keyword, freq in ranked_words ]


def keyword_extractor(tagger,lang,text):
    if tagger=='yake':
        return yake(text,lang)
    elif tagger=='okt':
        return konlpy(text)

def yake(text,lang):
    import yake
    kw_extractor = yake.KeywordExtractor()
    language = str(lang)
    print(language)
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 10
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    ls=[]
    for kw in keywords:
        ls.append(kw[0])

    return ls
# def keyword_extractor_en(tagger,text):
#

#
# text="""도로와 철도 레일 위를 모두 달릴 수 있는 '레일버스'가 개발돼 벽지 노선 등에 투입될 것으로 보인다.
# 코레일은 "현재 25인승 버스를 개조해 만든 레일버스의 안전성 검증과 기술 추가 개발이 끝나면 3대를 제작해 이르면 2019년 말 강원 정선 지역의 정선선 등에 투입할 계획"이라고 6일 밝혔다.
# 레일버스는 버스 차량이 철도 레일 위에서도 달릴 수 있도록 일종의 보조 바퀴 역할을 하는 '가이드 휠'을 단 차량이다. 25~35인승 버스를 개조해 만들 계획이며 선로 위에서 시속 80㎞ 속도로 달릴 수 있다. 코레일 담당자는 "필요할 경우 차량 3대를 연결 운행하면 75~105명까지 탈 수 있을 것"이라고 말했다. 레일버스는 도로에서도 달릴 수 있어 기차역에 도착한 뒤 관광지, 버스 정류장까지 도로 주행이 가능하다. 도로를 달릴 때는 유압으로 가이드 휠을 들어 올리고 주행하는 방식이다.
# 코레일은 올해 초부터 레일버스 시험 차량을 제작해 대전의 시험 선로에서 운행하고 있다. 레일버스 개발에는 총 20억원이 들어갈 것으로 보이며, 차량 1대 제작 가격은 3억원 수준이다. 코레일 측은 "영국에서는 버스를 열차로 완전히 개조해 운행한 사례가 있으며, 일본은 2020년까지 레일버스와 형태가 비슷한 DMV(Dual Mode Vehicle)를 2020년까지 상용화할 계획"이라고 밝혔다.
# 코레일은 "레일버스가 투입되면 벽지 노선 적자는 줄이면서도 운행 횟수는 늘려나갈 수 있다"고 밝혔다. 예를 들여 정선선에 레일버스를 투입하면 정선선에서 발생하는 연간 적자를 18억원에서 13억원 수준으로 5억원 줄이면서 열차 운행 횟수는 현재(관광 열차 편도 2회)의 6.5배 수준인 편도 13회까지 늘릴 수 있을 것으로 기대하고 있다. 레일버스를 투입하면 현재 운행 중인 새마을·무궁화호급 열차보다 운영비 등을 줄일 수 있기 때문이다. 코레일은 이용객이 적고 적자가 나는 다른 벽지 노선 등에도 레일버스를 투입할 수 있을 것으로 기대하고 있다."""
#
# print( keyword_extractor(okt, text))