import streamlit as st
import random
import json
import time
from datetime import datetime

# 한자 데이터 (확장된 버전)
HANJA_DATA = {
    "聿": ("붓", "율"),
    "曰": ("말하다", "왈"),
    "步": ("걷다", "보"),
    "立": ("서다", "립"),
    "力": ("힘", "력"),
    "宀": ("집", "면"),
    "耂": ("늙다", "로"),
    "法": ("법", "법"),
    "古": ("옛", "고"),
    "創": ("비롯할", "창"),
    "新": ("새로울", "신"),
    "甲": ("갑옷", "갑"),
    "守": ("지킬", "수"),
    "卵": ("알", "란"),
    "有": ("있을", "유"),
    "悟": ("깨달을", "오"),
    "淸": ("맑을", "청"),
    "潔": ("깨끗하다", "결"),
    "不": ("아닐", "불"),
    "言": ("말씀", "언"),
    "長": ("길", "장"),
    "短": ("짧을", "단"),
    "評": ("평할", "평"),
    "落": ("떨어질", "락"),
    "點": ("점", "점"),
    "鈍": ("둔할", "둔"),
    "筆": ("붓", "필"),
    "借": ("빌릴", "차"),
    "騎": ("탈", "기"),
    "還": ("돌아갈", "환"),
    "盜": ("도둑", "도"),
    "賊": ("도둑", "적"),
    "風": ("바람", "풍"),
    "聞": ("들을", "문"),
    "諷": ("풍자할", "풍"),
    "刺": ("찌를", "자"),
    "剽": ("겁박할", "표"),
    "竊": ("훔칠", "절"),
    "舍": ("버릴", "사"),
    "從": ("좇을", "종"),
    "蛙": ("개구리", "와"),
    "弘": ("넓을", "홍"),
    "益": ("이로울", "익"),
    "間": ("사이", "간"),
    "見": ("볼", "견"),
    "金": ("쇠", "김"),
    "如": ("같을", "여"),
    "石": ("돌", "석"),
    "八": ("여덟", "팔"),
    "商": ("장사", "상"),
    "泥": ("진흙", "이"),
    "田": ("밭", "전"),
    "狗": ("개", "구"),
    "碧": ("푸를", "벽"),
    "昌": ("창성할", "창"),
    "牛": ("소", "우"),
    "場": ("마당", "장"),
    "機": ("기틀", "기"),
    "智": ("지혜", "지"),
    "致": ("이룰", "치"),
    "貪": ("탐할", "탐"),
    "夫": ("지아비", "부"),
    "徇": ("쫓다", "순"),
    "財": ("재물", "재"),
    "固": ("굳을", "고"),
    "執": ("잡을", "집"),
    "通": ("통할", "통"),
    "杜": ("막을", "두"),
    "門": ("문", "문"),
    "出": ("나갈", "출"),
    "征": ("칠", "정"),
    "明": ("명나라", "명"),
    "假": ("빌릴", "가"),
    "道": ("길", "도"),
    "走": ("달릴", "주"),
    "肖": ("닮을", "초"),
    "爲": ("될", "위"),
    "王": ("임금", "왕"),
    "持": ("가질", "지"),
    "斧": ("도끼", "부"),
    "疏": ("소통할", "소"),
    "吏": ("벼슬아치", "리"),
    "興": ("흥할", "흥"),
    "亡": ("망할", "망"),
    "櫨": ("거먕옻나무", "노"),
    "櫃": ("궤", "궤"),
    "刻": ("새기다", "각"),
    "求": ("구할", "구"),
    "劍": ("칼", "검"),
    "株": ("그루터기", "주"),
    "待": ("기다릴", "대"),
    "兎": ("토끼", "토"),
    "膠": ("아교", "교"),
    "柱": ("기둥", "주"),
    "鼓": ("두드릴", "고"),
    "瑟": ("거문고", "슬"),
    "尾": ("꼬리", "미"),
    "生": ("날", "생"),
    "之": ("~의", "지"),
    "信": ("믿을", "신"),
    "食": ("먹을", "식"),
    "佩": ("찰", "패"),
    "鈴": ("방울", "령"),
    "誡": ("경계할", "계"),
    "松": ("소나무", "송"),
    "都": ("도읍", "도"),
    "員": ("인원", "원"),
    "沙": ("모래", "사"),
    "野": ("들", "야"),
    "鼠": ("쥐", "서"),
    "婚": ("혼인", "혼"),
    "妻": ("아내", "처"),
    "高": ("높을", "고"),
    "麗": ("고울", "려"),
    "公": ("공변될", "공"),
    "快": ("쾌할", "쾌"),
    "錦": ("비단", "금"),
    "兄": ("형", "형"),
    "友": ("우애", "우"),
    "弟": ("아우", "제"),
    "南": ("남녘", "남"),
    "入": ("들", "입"),
    "納": ("들일", "납"),
    "審": ("자세하다", "심"),
    "問": ("묻다", "문"),
    "編": ("책 끈", "편"),
    "發": ("피다", "발"),
    "忘": ("잊다", "망"),
    "息": ("쉬다", "식"),
    "功": ("공", "공"),
    "者": ("사람", "자"),
    "亦": ("또한", "역"),
    "能": ("할 수 있다", "능"),
    "學": ("배울", "학"),
    "勿": ("말라", "물"),
    "今": ("이제", "금"),
    "而": ("그리고", "이"),
    "年": ("해", "년"),
    "讀": ("읽다", "독"),
    "必": ("반드시", "필"),
    "氣": ("기운", "기"),
    "念": ("생각", "념"),
    "主": ("주로하다", "주"),
    "先": ("먼저", "선"),
    "桂": ("계수나무", "계"),
    "枝": ("가지", "지"),
    "外": ("바깥", "외"),
    "內": ("안", "내"),
    "剛": ("굳세다", "강"),
    "禮": ("예절", "례"),
    "義": ("옳다", "의"),
    "恥": ("부끄럽다", "치"),
    "招": ("부르다", "초"),
    "受": ("받다", "수"),
    "論": ("논할", "론"),
    "故": ("연고", "고"),
    "其": ("그", "기"),
    "海": ("바다", "해"),
    "擇": ("가리다", "택"),
    "流": ("흐르다", "류"),
    "深": ("깊다", "심"),
    "破": ("깨뜨리다", "파"),
    "心": ("마음", "심"),
    "同": ("같을", "동"),
    "體": ("몸", "체"),
    "異": ("다르다", "이"),
    "聲": ("소리", "성"),
    "渾": ("모두", "혼"),
    "然": ("그러하다", "연"),
    "團": ("모이다", "단"),
    "床": ("평상", "상"),
    "夢": ("꿈", "몽"),
    "咸": ("모두", "함"),
    "差": ("다를", "차"),
    "使": ("사신", "사"),
    "烏": ("까마귀", "오"),
    "飛": ("날", "비"),
    "梨": ("배", "이"),
    "瓜": ("오이", "과"),
    "履": ("신", "리"),
    "李": ("오얏", "이"),
    "冠": ("갓", "관"),
    "袖": ("소매", "수"),
    "手": ("손", "수"),
    "傍": ("옆", "방"),
    "觀": ("볼", "관"),
    "管": ("대롱", "관"),
    "鮑": ("절인 물고기", "포"),
    "交": ("사귈", "교"),
    "蘭": ("난초", "란"),
    "漆": ("옻", "칠"),
    "伯": ("맏", "백"),
    "牙": ("어금니", "아"),
    "絃": ("줄", "현"),
    "刎": ("목벨", "문"),
    "頸": ("목", "경"),
    "過": ("지날", "과"),
    "猶": ("같을", "유"),
    "及": ("미칠", "급"),
    "時": ("때", "시"),
    "桃": ("복숭아나무", "도"),
    "園": ("동산", "원"),
    "常": ("항상", "상"),
    "邯": ("땅이름", "한"),
    "鄲": ("조나라서울", "단"),
    "柯": ("가지", "가"),
    "胡": ("나비", "호"),
    "蝶": ("나비", "접"),
    "塞": ("변방", "새"),
    "翁": ("늙은이", "옹"),
    "用": ("쓸", "용"),
    "意": ("뜻", "의"),
    "周": ("두루", "주"),
    "到": ("이를", "도"),
    "孤": ("외로울", "고"),
    "奮": ("떨칠", "분"),
    "五": ("다섯", "오"),
    "多": ("많을", "다"),
    "苦": ("괴로울", "고"),
    "各": ("각각", "각"),
    "圖": ("꾀하다", "도"),
    "莫": ("없을", "막"),
    "逆": ("거스를", "역"),
    "實": ("열매, 실제", "실"),
    "相": ("서로", "상"),
    "符": ("부합할", "부"),
    "辭": ("말씀", "사"),
    "句": ("글귀", "구"),
    "前": ("앞", "전"),
    "代": ("시대", "대"),
    "未": ("아닐", "미"),
    "曾": ("일찍", "증"),
    "佳": ("아름다울", "가"),
    "約": ("약속, 맺을", "약"),
    "喜": ("기쁠", "희"),
    "再": ("두 번", "재"),
    "歸": ("돌아갈", "귀"),
    "姻": ("혼인", "인"),
    "數": ("세다", "수"),
    # 추가 한자들
    "人": ("사람", "인"),
    "無": ("없을", "무"),
    "三": ("셋", "삼"),
    "水": ("물", "수"),
    "山": ("뫼", "산"),
    "馬": ("말", "마"),
    "太": ("클", "태"),
    "鷄": ("닭", "계"),
    "骨": ("뼈", "골"),
    "下": ("아래", "하"),
    "勝": ("이길", "승"),
    "聰": ("총명할", "총"),
    "甲": ("갑옷", "갑"),
    "含": ("머금을", "함"),
    "從": ("따를", "종"),
    "蛙": ("개구리", "와"),
    "見": ("볼", "견"),
    "如": ("같을", "여"),
    "石": ("돌", "석"),
    "包": ("쌀", "포"),
    "大": ("클", "대"),
    "商": ("장사", "상"),
    "泥": ("진흙", "니"),
    "田": ("밭", "전"),
    "鬪": ("싸울", "투"),
    "狗": ("개", "구"),
    "碧": ("푸를", "벽"),
    "昌": ("창성할", "창"),
    "牛": ("소", "우"),
    "亂": ("어지러울", "란"),
    "場": ("마당", "장"),
    "杜": ("막을", "두"),
    "門": ("문", "문"),
    "不": ("아닐", "불"),
    "出": ("날", "출"),
    "征": ("칠", "정"),
    "明": ("밝을", "명"),
    "假": ("빌릴", "가"),
    "道": ("길", "도"),
    "走": ("달릴", "주"),
    "肖": ("닮을", "초"),
    "爲": ("될", "위"),
    "王": ("임금", "왕"),
    "持": ("가질", "지"),
    "斧": ("도끼", "부"),
    "上": ("위", "상"),
    "疏": ("성길", "소"),
    "淸": ("맑을", "청"),
    "白": ("흰", "백"),
    "吏": ("관리", "리"),
    "興": ("일으킬", "흥"),
    "亡": ("망할", "망"),
    "櫟": ("상수리나무", "역"),
    "木": ("나무", "목"),
    "槁": ("마를", "고"),
    "刻": ("새길", "각"),
    "舟": ("배", "주"),
    "求": ("구할", "구"),
    "劍": ("칼", "검"),
    "株": ("그루터기", "주"),
    "待": ("기다릴", "대"),
    "兎": ("토끼", "토"),
    "膠": ("아교", "교"),
    "柱": ("기둥", "주"),
    "鼓": ("북", "고"),
    "瑟": ("거문고", "슬"),
    "尾": ("꼬리", "미"),
    "生": ("날", "생"),
    "之": ("~의", "지"),
    "信": ("믿을", "신"),
    "不": ("아닐", "불"),
    "食": ("먹을", "식"),
    "言": ("말씀", "언"),
    "佩": ("찰", "패"),
    "鈴": ("방울", "령"),
    "自": ("스스로", "자"),
    "戒": ("경계할", "계"),
    "松": ("소나무", "송"),
    "都": ("도읍", "도"),
    "契": ("계약", "계"),
    "員": ("원", "원"),
    "月": ("달", "월"),
    "沙": ("모래", "사"),
    "夫": ("지아비", "부"),
    "人": ("사람", "인"),
    "野": ("들", "야"),
    "鼠": ("쥐", "서"),
    "婚": ("혼인", "혼"),
    "夫": ("지아비", "부"),
    "妻": ("아내", "처"),
    "詵": ("펼", "승"),
    "鏡": ("거울", "경"),
    "高": ("높을", "고"),
    "麗": ("고울", "려"),
    "公": ("공변될", "공"),
    "事": ("일", "사"),
    "三": ("셋", "삼"),
    "日": ("날", "일"),
    "愾": ("분개할", "개"),
    "山": ("뫼", "산"),
    "寃": ("원통할", "원"),
    "牛": ("소", "우"),
    "錦": ("비단", "금"),
    "繡": ("수놓을", "수"),
    "江": ("강", "강"),
    "山": ("뫼", "산"),
    "兄": ("형", "형"),
    "友": ("벗", "우"),
    "弟": ("아우", "제"),
    "恭": ("공손할", "공"),
    "南": ("남녘", "남"),
    "大": ("클", "대"),
    "門": ("문", "문"),
    "入": ("들", "입"),
    "納": ("들일", "납"),
    "博": ("넓을", "박"),
    "學": ("배울", "학"),
    "審": ("자세히", "심"),
    "問": ("묻다", "문"),
    "韋": ("가죽", "위"),
    "編": ("엮을", "편"),
    "三": ("셋", "삼"),
    "絶": ("끊을", "절"),
    "發": ("쏠", "발"),
    "憤": ("분할", "분"),
    "忘": ("잊을", "망"),
    "食": ("먹을", "식"),
    "自": ("스스로", "자"),
    "强": ("강할", "강"),
    "不": ("아닐", "불"),
    "息": ("쉴", "식"),
    "螢": ("반딧불", "형"),
    "雪": ("눈", "설"),
    "之": ("~의", "지"),
    "功": ("공", "공"),
    "手": ("손", "수"),
    "不": ("아닐", "불"),
    "釋": ("놓을", "석"),
    "卷": ("권", "권")
}

# 엑셀에서 가져온 사자성어 데이터 (겉뜻과 속뜻 구분)
IDIOM_DATA = {
    "法古創新": {
        "korean": "법고창신",
        "outer_meaning": "옛것을 본받아 새로운것을 창조한다",
        "inner_meaning": "옛것에 토대를 두되 그것을 변화시킨줄 알고 새것을 만들어 가되 근본을 잃지 말아야한다"
    },
    "三水甲山": {
        "korean": "삼수갑산",
        "outer_meaning": "함경도의 삼수와 갑산",
        "inner_meaning": "매우 힘들고 험난한 곳으로 가거나 어려운 지경에 이름"
    },
    "三馬太守": {
        "korean": "삼마태수",
        "outer_meaning": "세마리의 말만 타고 행차하는 수령",
        "inner_meaning": "여러 사람이 한 자리를 놓고 다툼"
    },
    "鷄卵有骨": {
        "korean": "계간유골",
        "outer_meaning": "달걀이 곯았다",
        "inner_meaning": "운수가 나쁜 사람은 모처럼 좋은 기회를 만나도 역시 일이 잘 안됨"
    },
    "不言長短": {
        "korean": "불언장단",
        "outer_meaning": "남의 장단점을 말하지 않는다",
        "inner_meaning": "황희정승과 농부의 대화에서 유래"
    },
    "下馬評": {
        "korean": "하마평",
        "outer_meaning": "말에서 내린 뒤의 평가",
        "inner_meaning": "관직의 인사이동이나 관직에 임명될 후보자에 대한 풍문"
    },
    "落點": {
        "korean": "낙점",
        "outer_meaning": "점을 찍다",
        "inner_meaning": "여러 후보가 있을대 그중 마땅한 대상을 고름"
    },
    "鈍筆勝聰": {
        "korean": "둔필승총",
        "outer_meaning": "무딘 붓이 총명함보다 낫다",
        "inner_meaning": "서툰 글이라도 기록하는것이 기억보다 낫다"
    },
    "借鷄騎還": {
        "korean": "차계기환",
        "outer_meaning": "닭을 빌려 타고 들어간다",
        "inner_meaning": "손님을 박대하는 것을 빗대어 이르는 말"
    },
    "勝甲盜賊": {
        "korean": "슬갑도적",
        "outer_meaning": "슬갑(방한구-무릎가리개)을 머리에 쓴 도적",
        "inner_meaning": "남의 글이나 저술을 베껴 마치 제가 지은 것처럼 하는 사람"
    },
    "含人從蛙": {
        "korean": "사인종와",
        "outer_meaning": "개구리를 삼킨 사람이 개구리를 따른다",
        "inner_meaning": "위금 상황에 기지를 발휘하여 대처함"
    },
    "弘益人間": {
        "korean": "홍익인간",
        "outer_meaning": "널리 인간을 이롭게 한다",
        "inner_meaning": "홍익인간 사상의 근본 이념"
    },
    "見金如石": {
        "korean": "견금여석",
        "outer_meaning": "황금을 돌같이 본다",
        "inner_meaning": "지나친 욕심을 절제함"
    },
    "八包大商": {
        "korean": "팔포대상",
        "outer_meaning": "여덟 자루의 짐을 가진 큰 상인",
        "inner_meaning": "생활에 걱정이 없는 사람"
    },
    "泥田鬪狗": {
        "korean": "이전투구",
        "outer_meaning": "진흙밭에서 개가 싸운다",
        "inner_meaning": "자기 이익을 위하여 불썽사납게 싸움"
    },
    "碧昌牛": {
        "korean": "벽창우",
        "outer_meaning": "푸른 창가의 소",
        "inner_meaning": "미련하고 고집이 센 사람"
    },
    "亂場": {
        "korean": "난장",
        "outer_meaning": "어지러운 마당",
        "inner_meaning": "여러 사람이 어지러이 뒤섞여 떠들어대거나 뒤엉켜 뒤죽박죽이 된 곳"
    },
    "杜門不出": {
        "korean": "두문불출",
        "outer_meaning": "문을 막고 나가지 않는다",
        "inner_meaning": "집에서 은거하면서 관직에 나가지 아니하거나 사회의 일을 하지 아니함"
    },
    "征明假道": {
        "korean": "정명가도",
        "outer_meaning": "명나라를 치기 위해 길을 빌린다",
        "inner_meaning": "어떤 일을 이루기 위해 말도 안되는 명분을 내세움"
    },
    "走肖爲王": {
        "korean": "주초위왕",
        "outer_meaning": "달려가서 닮은 자를 왕으로 세운다",
        "inner_meaning": "정적을 없애기 위해 갖은 술수를 씀"
    },
    "持斧上疏": {
        "korean": "지수상소",
        "outer_meaning": "도끼를 들고 상소를 올린다",
        "inner_meaning": "왕의 실정에 대해 목숨을 걸고 지적하는 신하의 기개"
    },
    "淸白吏": {
        "korean": "청백리",
        "outer_meaning": "깨끗하고 흰 관리",
        "inner_meaning": "청렴하고 결백한 관리"
    },
    "興淸亡淸": {
        "korean": "흥청망청",
        "outer_meaning": "흥청거리며 망청거린다",
        "inner_meaning": "돈이나 물건을 함부로 쓰며 마음껏 즐기는 모양"
    },
    "櫟木槁": {
        "korean": "노목계",
        "outer_meaning": "상수리나무가 마른다",
        "inner_meaning": "조금도 융통성이 없는 미련한 사람"
    },
    "刻舟求劍": {
        "korean": "각주구검",
        "outer_meaning": "배에 새겨서 칼을 구한다",
        "inner_meaning": "어리석고 미련하여 융통성이 없음"
    },
    "守株待兔": {
        "korean": "수주대토",
        "outer_meaning": "그루터기를 지키며 토끼를 기다린다",
        "inner_meaning": "요행으로 일이 성취되기를 바라거나 어떤 착각에 빠져 되지도 않을 일을 공연히 고집하는 어리석음"
    },
    "膠柱鼓瑟": {
        "korean": "교주고슬",
        "outer_meaning": "아교로 기둥을 붙여 거문고를 친다",
        "inner_meaning": "고지식하여 융통성이 전혀 없음"
    },
    "尾生之信": {
        "korean": "미생지신",
        "outer_meaning": "미생의 신의",
        "inner_meaning": "고지식하여 융통성이 전혀 없음"
    },
    "王不食言": {
        "korean": "왕불식언",
        "outer_meaning": "왕은 말을 먹지 않는다",
        "inner_meaning": "함부로 거짓말이나 빈말을 해선 안됨"
    },
    "佩鈴自戒": {
        "korean": "패령자계",
        "outer_meaning": "방울을 차고 스스로 경계한다",
        "inner_meaning": "나쁜 습관이나 단점을 고치기 위해 스스로 노력하는 자세"
    },
    "松都契員": {
        "korean": "송도계원",
        "outer_meaning": "송도의 계원",
        "inner_meaning": "하찮은 지위나 세력을 믿고 남을 멸시하고 오만하게 구는 사람"
    },
    "月沙夫人": {
        "korean": "월사부인",
        "outer_meaning": "달빛 모래의 부인",
        "inner_meaning": "남편의 지위가 높은데도 검소하여 타의 모범이 되는 부인"
    },
    "野鼠婚": {
        "korean": "야서혼",
        "outer_meaning": "들쥐의 혼인",
        "inner_meaning": "제 분수에 넘치는 허영심. 동류는 동류끼리 가장 잘 어울림"
    },
    "夫妻詵鏡": {
        "korean": "부처승경",
        "outer_meaning": "부부가 거울을 펼친다",
        "inner_meaning": "가상과 실상의 혼란에 빠진 존재의 어리석음"
    },
    "高麗公事三日": {
        "korean": "고려공사삼일",
        "outer_meaning": "고려의 공사는 삼일",
        "inner_meaning": "한번 시작한 일이 오래 계속되어 가지 못함"
    },
    "愾山寃牛": {
        "korean": "쾌산원우",
        "outer_meaning": "산에 분개하고 소를 원망한다",
        "inner_meaning": "충성을 바쳤으나 도리어 죽음을 맞이함"
    },
    "錦繡江山": {
        "korean": "금수강산",
        "outer_meaning": "비단으로 수놓은 강산",
        "inner_meaning": "우리나라의 산천을 비유적으로 이르는 말"
    },
    "兄友弟恭": {
        "korean": "형우제공",
        "outer_meaning": "형은 우애하고 아우는 공손하다",
        "inner_meaning": "형제간에 서로 우애 깊게 지냄"
    },
    "南大門入納": {
        "korean": "남대문입납",
        "outer_meaning": "남대문으로 들어가 납부한다",
        "inner_meaning": "줄거리나 골자를 알 수 없는 말을 비유적으로 이르는 말"
    },
    "博學審問": {
        "korean": "박학심문",
        "outer_meaning": "넓게 배우고 자세히 묻는다",
        "inner_meaning": "학문을 하는 올바른 자세"
    },
    "韋編三絶": {
        "korean": "위편삼절",
        "outer_meaning": "가죽끈이 세 번 끊어진다",
        "inner_meaning": "책을 열심히 읽음, 부지런히 배우다, 학문에 힘씀"
    },
    "發憤忘食": {
        "korean": "발분망식",
        "outer_meaning": "분발하여 식사를 잊는다",
        "inner_meaning": "끼니까지도 잊을 정도로 어떤일에 열중하여 노력함"
    },
    "自强不息": {
        "korean": "자강불식",
        "outer_meaning": "스스로 강해지기를 쉬지 않는다",
        "inner_meaning": "자신의 목표를 향해 끊임 없이 노력하는것"
    },
    "螢雪之功": {
        "korean": "형설지공",
        "outer_meaning": "반딧불과 눈의 공",
        "inner_meaning": "어려운 환경에서도 부지런하고 꾸준하게 공부하여 성공함"
    },
    "手不釋卷": {
        "korean": "수불석권",
        "outer_meaning": "손에서 책을 놓지 않는다",
        "inner_meaning": "항상 손에 책을 들고 글을 읽으면서 공부함"
    },
    "人生無常": {
        "korean": "인생무상",
        "outer_meaning": "사람의 인생이 무상하다",
        "inner_meaning": "사람의 일생이 덧없이 흘러감"
    },
    "桂林一枝": {
        "korean": "계림일지",
        "outer_meaning": "계수나무 숲의 한 가지",
        "inner_meaning": "사람됨이 비범하면서 겸손함"
    },
    "外柔內剛": {
        "korean": "외유내강",
        "outer_meaning": "겉은 부드럽고 속은 굳세다",
        "inner_meaning": "겉으로는 부드럽고 순하나 속은 곧고 꿋꿋함"
    },
    "禮義廉恥": {
        "korean": "예의염치",
        "outer_meaning": "예절과 의리와 청렴과 부끄러움",
        "inner_meaning": "예절, 의리, 청렴, 부끄러움을 아는 태도"
    },
    "一心同體": {
        "korean": "일심동체",
        "outer_meaning": "한 마음 같은 몸",
        "inner_meaning": "둘 이상의 사람이 굳게 뭉치는 일"
    },
    "異口同聲": {
        "korean": "이구동성",
        "outer_meaning": "다른 입으로 같은 소리",
        "inner_meaning": "여러 사람의 말이 한결같음"
    },
    "渾然一體": {
        "korean": "혼연일체",
        "outer_meaning": "모두 하나의 몸",
        "inner_meaning": "조금의 어긋남도 없이 한덩어리가 됨"
    },
    "大同團結": {
        "korean": "대동단결",
        "outer_meaning": "크게 같이 뭉친다",
        "inner_meaning": "여러 집단이나 사람이 어떤 목적을 이루려고 크게 한 덩어리로 뭉침"
    },
    "同床異夢": {
        "korean": "동상이몽",
        "outer_meaning": "같은 잠자리에서 다른 꿈",
        "inner_meaning": "겉으로는 같이 행동하면서도 속으로는 각각 딴생각을 하고 있음"
    },
    "咸興差使": {
        "korean": "함흥차사",
        "outer_meaning": "함흥으로 간 차사",
        "inner_meaning": "심부름을 간 사람이 소식이 아주 없거나 또는 회답이 좀처럼 오지 않음"
    },
    "烏飛梨落": {
        "korean": "오비이락",
        "outer_meaning": "까마귀가 날고 배가 떨어진다",
        "inner_meaning": "우연의 일치로 의심을 받음"
    },
    "袖手傍觀": {
        "korean": "수수방관",
        "outer_meaning": "소매에 손을 넣고 옆에서 본다",
        "inner_meaning": "팔짱을 끼고 보고만 있다"
    },
    "過猶不及": {
        "korean": "과유불급",
        "outer_meaning": "지나침은 미치지 못함과 같다",
        "inner_meaning": "정도를 지나침은 미치지 못함과 같다는 뜻"
    },
    "時時刻刻": {
        "korean": "시시각각",
        "outer_meaning": "때때로 각각",
        "inner_meaning": "시간이 흐름에 따라"
    },
    "桃園結義": {
        "korean": "도원결의",
        "outer_meaning": "복숭아 동산에서 의를 맺다",
        "inner_meaning": "의형제를 맺음. 서로 다른 사람들이 사욕을 버리고 목적을 향해 합심할 것을 결의함"
    },
    "管鮑之交": {
        "korean": "관포지교",
        "outer_meaning": "관중과 포숙의 사귐",
        "inner_meaning": "우정이 아주 돈독한 친구 관계"
    },
    "金蘭之交": {
        "korean": "금란지교",
        "outer_meaning": "황금과 난초의 사귐",
        "inner_meaning": "친구 사이의 매우 두터운 정"
    },
    "芝蘭之交": {
        "korean": "지란지교",
        "outer_meaning": "지초와 난초의 사귐",
        "inner_meaning": "벗 사이의 맑고도 고귀한 사귐"
    },
    "水魚之交": {
        "korean": "수어지교",
        "outer_meaning": "물과 물고기의 사귐",
        "inner_meaning": "매우 친밀하게 사귀어 떨어질 수 없는 사이"
    },
    "膠漆之交": {
        "korean": "교칠지교",
        "outer_meaning": "아교와 옻의 사귐",
        "inner_meaning": "아주 친밀하여 서로 떨어지지 않고 마음이 변하지 않는 두터운 우정"
    },
    "伯牙絶絃": {
        "korean": "백아절현",
        "outer_meaning": "백아가 거문고 줄을 끊다",
        "inner_meaning": "자기를 알아주는 절친한 벗의 죽음을 슬퍼함"
    },
    "刎頸之交": {
        "korean": "문경지교",
        "outer_meaning": "목을 베는 사귐",
        "inner_meaning": "생사를 같이할 만큼 매우 친한 사람"
    },
    "塞翁之馬": {
        "korean": "새옹지마",
        "outer_meaning": "변방 늙은이의 말",
        "inner_meaning": "인생의 길흉화복은 늘 바뀌어 변화가 많음"
    },
    "用意周到": {
        "korean": "용의주도",
        "outer_meaning": "뜻을 쓰기를 두루 이른다",
        "inner_meaning": "어떤일을 하려고 뜻을 세우고 마음을 가짐에 있어 준비가 두루 미쳐 빈틈이 없음"
    },
    "孤軍奮鬪": {
        "korean": "고군분투",
        "outer_meaning": "외로운 군사가 분발하여 싸운다",
        "inner_meaning": "따로 떨어져 도움을 받지 못하게된 군사가 많은 수의 적군과 용감하게 잘 싸운다"
    },
    "名實相符": {
        "korean": "명실상부",
        "outer_meaning": "이름과 실제가 서로 부합한다",
        "inner_meaning": "알려진 것과 실제 내용이 일치함"
    },
    "美辭麗句": {
        "korean": "미사여구",
        "outer_meaning": "아름다운 말과 고운 구절",
        "inner_meaning": "내용은 없으면서 아름다운 말로 듣기 좋게 꾸민 글귀"
    },
    "前代未聞": {
        "korean": "전대미문",
        "outer_meaning": "전 시대에 듣지 못했다",
        "inner_meaning": "이제껏 들어 본 적이 없다는 뜻"
    },
    "未曾有": {
        "korean": "미증유",
        "outer_meaning": "일찍이 있지 않았다",
        "inner_meaning": "전례가 없음"
    },
    "一場春夢": {
        "korean": "일장춘몽",
        "outer_meaning": "한바탕 봄꿈",
        "inner_meaning": "헛된 영화나 덧없는 일"
    },
    "邯鄲之夢": {
        "korean": "한단지몽",
        "outer_meaning": "한단의 꿈",
        "inner_meaning": "세상의 부귀영화가 허황된"
    },
    "南柯一夢": {
        "korean": "남가일몽",
        "outer_meaning": "남쪽 가지의 한 꿈",
        "inner_meaning": "인생이나 부귀영화의 덧없음"
    },
    "胡蝶之夢": {
        "korean": "호접지몽",
        "outer_meaning": "나비의 꿈",
        "inner_meaning": "몰아일체의 경지 또는 현실과 꿈의 구별이 안되어 허무함"
    },
    "三三五五": {
        "korean": "삼삼오오",
        "outer_meaning": "셋셋 다섯다섯",
        "inner_meaning": "서너 사람 또는 대여섯 사람이 떼를 지어다니거나 무슨 일을 함"
    },
    "多多益善": {
        "korean": "다다익선",
        "outer_meaning": "많으면 많을수록 더욱 좋다",
        "inner_meaning": "많으면 많을수록 좋음"
    },
    "同苦同樂": {
        "korean": "동고동락",
        "outer_meaning": "고생도 즐거움도 함께",
        "inner_meaning": "괴로움도 즐거움도 함께함"
    },
    "各自圖生": {
        "korean": "각자도생",
        "outer_meaning": "각자 살아갈 방법을 꾀한다",
        "inner_meaning": "제각기 살아 나갈 방법을 꾀함"
    },
    "莫逆之友": {
        "korean": "막역지우",
        "outer_meaning": "거스르지 않는 벗",
        "inner_meaning": "허물없이 아주 친한 친구"
    },
    "百年佳約": {
        "korean": "백년가약",
        "outer_meaning": "백년의 아름다운 약속",
        "inner_meaning": "남녀가 결혼하여 평생을 함께 지낼것을 다짐하는 아름다운 언약"
    },
    "喜喜樂樂": {
        "korean": "희희낙락",
        "outer_meaning": "기뻐하고 즐거워한다",
        "inner_meaning": "매우 기뻐하고 즐거워함"
    },
    "非一非再": {
        "korean": "비일비재",
        "outer_meaning": "한 번이 아니고 두 번이 아니다",
        "inner_meaning": "같은 현상이나 일이 한두 번이나 한 둘이 아니고 많음"
    },
    "事必歸正": {
        "korean": "사필귀정",
        "outer_meaning": "일은 반드시 바른 곳으로 돌아간다",
        "inner_meaning": "모든 일은 결국에는 반드시 바른 길로 돌아가게 되어 있음"
    }
}

# 한자 분석 함수
def analyze_hanja_chars(hanja_string):
    """사자성어의 각 한자를 분석하여 뜻과 음을 표시"""
    chars = list(hanja_string)
    analysis = []
    
    for char in chars:
        if char in HANJA_DATA:
            meaning, sound = HANJA_DATA[char]
            analysis.append(f"{meaning}({char})")
        else:
            analysis.append(f"({char})")
    
    return " ".join(analysis)

# 세션 상태 초기화
if 'wrong_answers' not in st.session_state:
    st.session_state.wrong_answers = []
if 'score' not in st.session_state:
    st.session_state.score = {"correct": 0, "total": 0}
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'speed_quiz_score' not in st.session_state:
    st.session_state.speed_quiz_score = 0
if 'speed_quiz_total' not in st.session_state:
    st.session_state.speed_quiz_total = 0
if 'speed_quiz_start_time' not in st.session_state:
    st.session_state.speed_quiz_start_time = None
if 'exam_questions' not in st.session_state:
    st.session_state.exam_questions = []
if 'exam_current_index' not in st.session_state:
    st.session_state.exam_current_index = 0
if 'exam_answers' not in st.session_state:
    st.session_state.exam_answers = {}
if 'exam_submitted' not in st.session_state:
    st.session_state.exam_submitted = False
if 'exam_results' not in st.session_state:
    st.session_state.exam_results = None
if 'review_list' not in st.session_state:
    st.session_state.review_list = []

def main():
    st.set_page_config(page_title="📚 한자 & 사자성어 학습", page_icon="📚", layout="wide")
    
    # 사이드바 - 메뉴 및 모든 선택 옵션
    with st.sidebar:
        st.header("📋 메뉴")
        mode = st.selectbox("학습 모드 선택", [
            "🏠 홈",
            "📚 암기 연습",
            "🧠 퀴즈 모드", 
            "⚡ 스피드 퀴즈",
            "📝 시험 모드",
            "📊 학습 통계",
            "💾 복습 노트",
            "🔍 사자성어 검색"
        ])
        
        st.markdown("---")
        
        # 암기 연습 모드 설정
        if mode == "📚 암기 연습":
            st.subheader("📚 암기 연습 설정")
            practice_type = st.selectbox("연습 유형 선택", [
                "한자 → 뜻 맞히기",
                "뜻 → 한자 맞히기", 
                "사자성어 → 겉뜻 맞히기",
                "사자성어 → 속뜻 맞히기",
                "겉뜻 → 사자성어 맞히기",
                "속뜻 → 사자성어 맞히기"
            ])
            
            if st.button("🎯 새 문제 시작", use_container_width=True):
                generate_memory_question(practice_type)
            
            if st.button("🔄 초기화", use_container_width=True):
                st.session_state.current_question = None
                st.session_state.show_answer = False
        
        # 퀴즈 모드 설정
        elif mode == "🧠 퀴즈 모드":
            st.subheader("🧠 퀴즈 설정")
            quiz_type = st.selectbox("퀴즈 유형 선택", [
                "한자 4지선다",
                "사자성어 4지선다 (겉뜻)", 
                "사자성어 4지선다 (속뜻)",
                "한자 O/X 퀴즈",
                "사자성어 O/X 퀴즈 (겉뜻)",
                "사자성어 O/X 퀴즈 (속뜻)",
                "혼합 랜덤 퀴즈"
            ])
            
            if st.button("🎯 퀴즈 시작", use_container_width=True):
                generate_quiz_question(quiz_type)
            
            if st.button("🔄 초기화", use_container_width=True):
                st.session_state.current_question = None
                st.session_state.show_answer = False

        # 스피드 퀴즈 설정
        elif mode == "⚡ 스피드 퀴즈":
            st.subheader("⚡ 스피드 퀴즈 설정")
            if st.button("🚀 스피드 퀴즈 시작", use_container_width=True):
                start_speed_quiz()
            
            if st.button("🔄 초기화", use_container_width=True):
                reset_speed_quiz()

        # 시험 모드 설정
        elif mode == "📝 시험 모드":
            st.subheader("📝 시험 설정")
            if st.button("📝 새 시험 시작", use_container_width=True):
                generate_exam()
            
            if st.button("🔄 초기화", use_container_width=True):
                reset_exam()
        
        # 사자성어 검색 설정
        elif mode == "🔍 사자성어 검색":
            st.subheader("🔍 검색 설정")
            search_term = st.text_input("사자성어 검색:")
            if search_term:
                st.session_state.search_term = search_term
            
            show_all = st.checkbox("전체 목록 보기")
            if show_all:
                st.session_state.show_all_idioms = True
        
        st.markdown("---")
        st.markdown("### 📈 현재 점수")
        if st.session_state.score["total"] > 0:
            accuracy = (st.session_state.score["correct"] / st.session_state.score["total"]) * 100
            st.metric("정답률", f"{accuracy:.1f}%")
            st.metric("총 문제", st.session_state.score["total"])
            st.metric("정답", st.session_state.score["correct"])
        else:
            st.info("아직 문제를 풀지 않았습니다.")
    
    # 메인 컨텐츠
    if mode == "🏠 홈":
        show_home()
    elif mode == "📚 암기 연습":
        show_memory_practice()
    elif mode == "🧠 퀴즈 모드":
        show_quiz_mode()
    elif mode == "⚡ 스피드 퀴즈":
        show_speed_quiz()
    elif mode == "📝 시험 모드":
        show_exam_mode()
    elif mode == "📊 학습 통계":
        show_statistics()
    elif mode == "💾 복습 노트":
        show_review_notes()
    elif mode == "🔍 사자성어 검색":
        show_idiom_search()

def show_home():
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📖 데이터 현황")
        st.info(f"한자: {len(HANJA_DATA)}개")
        st.info(f"사자성어: {len(IDIOM_DATA)}개")
        st.success(f"총 학습 항목: {len(HANJA_DATA) + len(IDIOM_DATA)}개")
    
    with col2:
        st.subheader("🎯 학습 모드")
        st.markdown("""
        **📚 암기 연습 모드**
        - 한자 → 뜻 맞히기
        - 뜻 → 한자 맞히기
        - 사자성어 → 뜻 맞히기
        
        **🧠 퀴즈 모드**
        - 4지선다 퀴즈
        - O/X 퀴즈
        
        **⚡ 스피드 퀴즈**
        - 빠른 속도의 연속 퀴즈
        
        **📝 시험 모드**
        - 사자성어 20문제 시험
        - 점수 및 분석 제공
        """)
    
    st.markdown("---")
    st.subheader("🚀 빠른 시작")
    
    col3, col4, col5, col6 = st.columns(4)
    with col3:
        if st.button("📚 한자 암기", use_container_width=True):
            st.session_state.quick_start = "hanja_memory"
    with col4:
        if st.button("📜 사자성어 암기", use_container_width=True):
            st.session_state.quick_start = "idiom_memory"
    with col5:
        if st.button("⚡ 스피드 퀴즈", use_container_width=True):
            start_speed_quiz()
    with col6:
        if st.button("📝 시험 보기", use_container_width=True):
            generate_exam()

def show_memory_practice():
    st.header("📚 암기 연습 모드")
    
    if st.session_state.current_question:
        show_memory_question()

def generate_memory_question(practice_type):
    if "한자" in practice_type:
        hanja, (meaning, reading) = random.choice(list(HANJA_DATA.items()))
        if practice_type == "한자 → 뜻 맞히기":
            st.session_state.current_question = {
                "type": "hanja_to_meaning",
                "question": hanja,
                "answer": f"{meaning} ({reading})",
                "hanja": hanja,
                "meaning": meaning,
                "reading": reading
            }
        else:  # 뜻 → 한자 맞히기
            st.session_state.current_question = {
                "type": "meaning_to_hanja",
                "question": f"{meaning} ({reading})",
                "answer": hanja,
                "hanja": hanja,
                "meaning": meaning,
                "reading": reading
            }
    else:  # 사자성어
        idiom, data = random.choice(list(IDIOM_DATA.items()))
        korean = data["korean"]
        outer_meaning = data["outer_meaning"]
        inner_meaning = data["inner_meaning"]
        
        if practice_type == "사자성어 → 겉뜻 맞히기":
            st.session_state.current_question = {
                "type": "idiom_to_outer",
                "question": f"{idiom}",
                "answer": outer_meaning,
                "idiom": idiom,
                "korean": korean,
                "outer_meaning": outer_meaning,
                "inner_meaning": inner_meaning
            }
        elif practice_type == "사자성어 → 속뜻 맞히기":
            st.session_state.current_question = {
                "type": "idiom_to_inner",
                "question": f"{idiom}",
                "answer": inner_meaning,
                "idiom": idiom,
                "korean": korean,
                "outer_meaning": outer_meaning,
                "inner_meaning": inner_meaning
            }
        elif practice_type == "겉뜻 → 사자성어 맞히기":
            st.session_state.current_question = {
                "type": "outer_to_idiom",
                "question": outer_meaning,
                "answer": f"{idiom}",
                "idiom": idiom,
                "korean": korean,
                "outer_meaning": outer_meaning,
                "inner_meaning": inner_meaning
            }
        else:  # 속뜻 → 사자성어 맞히기
            st.session_state.current_question = {
                "type": "inner_to_idiom",
                "question": inner_meaning,
                "answer": f"{idiom}",
                "idiom": idiom,
                "korean": korean,
                "outer_meaning": outer_meaning,
                "inner_meaning": inner_meaning
            }
    
    st.session_state.show_answer = False

def show_memory_question():
    question = st.session_state.current_question
    
    # 문제 표시 (더 큰 상자)
    st.markdown(f"""
    <div style='font-size: 32px; padding: 40px; background-color: #f0f2f6; 
                border-radius: 15px; text-align: center; margin: 20px 0; 
                border: 2px solid #e1e5e9; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
        {question['question']}
    </div>
    """, unsafe_allow_html=True)
    
    # 플래시 카드 형식 - 상단에 버튼 2개
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💡 정답 확인", use_container_width=True, type="primary"):
            st.session_state.show_answer = True
    
    with col2:
        if st.button("⏭️ 다음 문제", use_container_width=True):
            practice_type = get_practice_type_from_question(question)
            generate_memory_question(practice_type)
            st.rerun()
    
    # 정답 표시 (정답 확인 버튼을 눌렀을 때만)
    if st.session_state.show_answer:
        st.markdown("### ✅ 정답")
        st.success(f"정답: {question['answer']}")
        
        # 상세 정보 표시
        if "hanja" in question:
            st.markdown("### 📚 상세 정보")
            st.info(f"한자: {question['hanja']}")
            st.info(f"뜻: {question['meaning']}")
            st.info(f"음: {question['reading']}")
        elif "idiom" in question:
            st.markdown("### 📚 상세 정보")
            st.info(f"사자성어: {question['idiom']}")
            st.info(f"한글: {question['korean']}")
            
            # 한자 분석 추가
            hanja_analysis = analyze_hanja_chars(question['idiom'])
            st.info(f"한자 분석: {hanja_analysis}")
            
            st.info(f"겉뜻: {question['outer_meaning']}")
            st.info(f"속뜻: {question['inner_meaning']}")

def get_practice_type_from_question(question):
    if question["type"] == "hanja_to_meaning":
        return "한자 → 뜻 맞히기"
    elif question["type"] == "meaning_to_hanja":
        return "뜻 → 한자 맞히기"
    elif question["type"] == "idiom_to_outer":
        return "사자성어 → 겉뜻 맞히기"
    elif question["type"] == "idiom_to_inner":
        return "사자성어 → 속뜻 맞히기"
    elif question["type"] == "outer_to_idiom":
        return "겉뜻 → 사자성어 맞히기"
    else:
        return "속뜻 → 사자성어 맞히기"

def show_quiz_mode():
    st.header("🧠 퀴즈 모드")
    
    if st.session_state.current_question and st.session_state.current_question.get("quiz_type"):
        show_quiz_question()

def generate_quiz_question(quiz_type):
    if "4지선다" in quiz_type:
        generate_multiple_choice_question(quiz_type)
    elif "O/X" in quiz_type:
        generate_ox_question(quiz_type)
    else:  # 혼합 랜덤
        random_type = random.choice([
            "한자 4지선다", "사자성어 4지선다 (겉뜻)", "사자성어 4지선다 (속뜻)",
            "한자 O/X 퀴즈", "사자성어 O/X 퀴즈 (겉뜻)", "사자성어 O/X 퀴즈 (속뜻)"
        ])
        generate_quiz_question(random_type)

def generate_multiple_choice_question(quiz_type):
    if "한자" in quiz_type:
        # 한자 4지선다
        correct_hanja, (correct_meaning, correct_reading) = random.choice(list(HANJA_DATA.items()))
        
        # 오답 선택지 생성
        wrong_choices = random.sample([item for item in HANJA_DATA.items() if item[0] != correct_hanja], 3)
        
        choices = [f"{correct_meaning} ({correct_reading})"]
        for _, (meaning, reading) in wrong_choices:
            choices.append(f"{meaning} ({reading})")
        
        random.shuffle(choices)
        correct_answer = choices.index(f"{correct_meaning} ({correct_reading})")
        
        st.session_state.current_question = {
            "quiz_type": "multiple_choice",
            "type": "hanja",
            "question": f"다음 한자의 뜻은? {correct_hanja}",
            "choices": choices,
            "correct_answer": correct_answer,
            "explanation": f"한자 '{correct_hanja}'의 뜻은 '{correct_meaning}'이고 음은 '{correct_reading}'입니다."
        }
    else:
        # 사자성어 4지선다
        correct_idiom, data = random.choice(list(IDIOM_DATA.items()))
        correct_korean = data["korean"]
        
        if "겉뜻" in quiz_type:
            correct_meaning = data["outer_meaning"]
            # 다른 사자성어의 겉뜻들
            wrong_choices = random.sample([item[1]["outer_meaning"] for item in IDIOM_DATA.items() if item[0] != correct_idiom], 3)
            question_text = f"다음 사자성어의 겉뜻은? {correct_idiom}"
        else:  # 속뜻
            correct_meaning = data["inner_meaning"]
            # 다른 사자성어의 속뜻들
            wrong_choices = random.sample([item[1]["inner_meaning"] for item in IDIOM_DATA.items() if item[0] != correct_idiom], 3)
            question_text = f"다음 사자성어의 속뜻은? {correct_idiom}"
        
        choices = [correct_meaning] + wrong_choices
        random.shuffle(choices)
        correct_answer = choices.index(correct_meaning)
        
        # 한자 분석 추가
        hanja_analysis = analyze_hanja_chars(correct_idiom)
        
        st.session_state.current_question = {
            "quiz_type": "multiple_choice",
            "type": "idiom",
            "question": question_text,
            "choices": choices,
            "correct_answer": correct_answer,
            "explanation": f"사자성어 '{correct_idiom}({correct_korean})'의 한자 분석: {hanja_analysis}\n겉뜻: {data['outer_meaning']}\n속뜻: {data['inner_meaning']}"
        }
    
    st.session_state.show_answer = False

def generate_ox_question(quiz_type):
    if "한자" in quiz_type:
        # 한자 O/X 퀴즈
        hanja, (meaning, reading) = random.choice(list(HANJA_DATA.items()))
        
        # 50% 확률로 정답/오답 문제 생성
        is_correct = random.choice([True, False])
        
        if is_correct:
            question_text = f"한자 '{hanja}'의 뜻은 '{meaning}'이다."
            correct_answer = "O"
        else:
            # 다른 한자의 뜻을 가져옴
            wrong_meaning = random.choice([item[1][0] for item in HANJA_DATA.items() if item[0] != hanja])
            question_text = f"한자 '{hanja}'의 뜻은 '{wrong_meaning}'이다."
            correct_answer = "X"
        
        st.session_state.current_question = {
            "quiz_type": "ox",
            "type": "hanja",
            "question": question_text,
            "correct_answer": correct_answer,
            "explanation": f"한자 '{hanja}'의 올바른 뜻은 '{meaning}'({reading})입니다."
        }
    else:
        # 사자성어 O/X 퀴즈
        idiom, data = random.choice(list(IDIOM_DATA.items()))
        korean = data["korean"]
        
        # 50% 확률로 정답/오답 문제 생성
        is_correct = random.choice([True, False])
        
        if "겉뜻" in quiz_type:
            correct_meaning = data["outer_meaning"]
            if is_correct:
                question_text = f"사자성어 '{idiom}'의 겉뜻은 '{correct_meaning}'이다."
                correct_answer = "O"
            else:
                wrong_meaning = random.choice([item[1]["outer_meaning"] for item in IDIOM_DATA.items() if item[0] != idiom])
                question_text = f"사자성어 '{idiom}'의 겉뜻은 '{wrong_meaning}'이다."
                correct_answer = "X"
        else:  # 속뜻
            correct_meaning = data["inner_meaning"]
            if is_correct:
                question_text = f"사자성어 '{idiom}'의 속뜻은 '{correct_meaning}'이다."
                correct_answer = "O"
            else:
                wrong_meaning = random.choice([item[1]["inner_meaning"] for item in IDIOM_DATA.items() if item[0] != idiom])
                question_text = f"사자성어 '{idiom}'의 속뜻은 '{wrong_meaning}'이다."
                correct_answer = "X"
        
        # 한자 분석 추가
        hanja_analysis = analyze_hanja_chars(idiom)
        
        st.session_state.current_question = {
            "quiz_type": "ox",
            "type": "idiom",
            "question": question_text,
            "correct_answer": correct_answer,
            "explanation": f"사자성어 '{idiom}({korean})'의 한자 분석: {hanja_analysis}\n겉뜻: {data['outer_meaning']}\n속뜻: {data['inner_meaning']}"
        }
    
    st.session_state.show_answer = False

def show_quiz_question():
    question = st.session_state.current_question
    
    # 문제 표시 (더 큰 상자)
    st.markdown(f"""
    <div style='font-size: 24px; padding: 30px; background-color: #f0f2f6; 
                border-radius: 15px; margin: 20px 0; 
                border: 2px solid #e1e5e9; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
        {question['question']}
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.show_answer:
        if question["quiz_type"] == "multiple_choice":
            # 4지선다
            user_answer = st.radio("정답을 선택하세요:", 
                                 options=range(len(question["choices"])),
                                 format_func=lambda x: f"{chr(65+x)}. {question['choices'][x]}",
                                 key="quiz_answer")
            
            if st.button("정답 확인", use_container_width=True, type="primary"):
                check_quiz_answer(user_answer, question["correct_answer"])
                
        else:
            # O/X 퀴즈
            st.markdown("**선택하세요:**")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("⭕ A. O (맞다)", use_container_width=True, type="primary"):
                    check_quiz_answer("O", question["correct_answer"])
            with col2:
                if st.button("❌ B. X (틀리다)", use_container_width=True):
                    check_quiz_answer("X", question["correct_answer"])
    
    # 정답 표시
    if st.session_state.show_answer:
        if hasattr(st.session_state, 'quiz_result'):
            if st.session_state.quiz_result:
                st.success("🎉 정답입니다!")
            else:
                st.error("❌ 틀렸습니다!")
                # 틀린 문제를 복습 노트에 추가
                st.session_state.wrong_answers.append({
                    "question": question["question"],
                    "user_answer": st.session_state.user_quiz_answer,
                    "correct_answer": question["correct_answer"],
                    "explanation": question["explanation"],
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        
        st.info(f"설명: {question['explanation']}")
        
        if st.button("➡️ 다음 문제", use_container_width=True):
            # 같은 유형의 다음 문제 생성하고 자동으로 화면 새로고침
            if question["quiz_type"] == "multiple_choice":
                if question["type"] == "hanja":
                    generate_quiz_question("한자 4지선다")
                else:
                    # 현재 문제에서 겉뜻/속뜻 유형 파악
                    if "겉뜻" in question["question"]:
                        generate_quiz_question("사자성어 4지선다 (겉뜻)")
                    else:
                        generate_quiz_question("사자성어 4지선다 (속뜻)")
            else:
                if question["type"] == "hanja":
                    generate_quiz_question("한자 O/X 퀴즈")
                else:
                    # 현재 문제에서 겉뜻/속뜻 유형 파악
                    if "겉뜻" in question["question"]:
                        generate_quiz_question("사자성어 O/X 퀴즈 (겉뜻)")
                    else:
                        generate_quiz_question("사자성어 O/X 퀴즈 (속뜻)")
            
            # 화면 새로고침
            st.rerun()

def check_quiz_answer(user_answer, correct_answer):
    st.session_state.show_answer = True
    st.session_state.user_quiz_answer = user_answer
    
    # 점수 업데이트
    st.session_state.score["total"] += 1
    
    if user_answer == correct_answer:
        st.session_state.quiz_result = True
        st.session_state.score["correct"] += 1
    else:
        st.session_state.quiz_result = False

# 스피드 퀴즈 기능들
def start_speed_quiz():
    st.session_state.speed_quiz_score = 0
    st.session_state.speed_quiz_total = 0
    st.session_state.speed_quiz_start_time = time.time()
    generate_speed_quiz_question()

def reset_speed_quiz():
    st.session_state.speed_quiz_score = 0
    st.session_state.speed_quiz_total = 0
    st.session_state.speed_quiz_start_time = None
    st.session_state.current_question = None
    st.session_state.show_answer = False

def generate_speed_quiz_question():
    # 랜덤하게 한자 또는 사자성어 문제 생성
    question_type = random.choice(["hanja", "idiom_outer", "idiom_inner"])
    
    if question_type == "hanja":
        hanja, (meaning, reading) = random.choice(list(HANJA_DATA.items()))
        
        # 4지선다 생성
        wrong_choices = random.sample([item[1] for item in HANJA_DATA.items() if item[0] != hanja], 3)
        choices = [f"{meaning} ({reading})"]
        for m, r in wrong_choices:
            choices.append(f"{m} ({r})")
        
        random.shuffle(choices)
        correct_answer = choices.index(f"{meaning} ({reading})")
        
        st.session_state.current_question = {
            "quiz_type": "speed_multiple_choice",
            "type": "hanja",
            "question": f"{hanja}",
            "choices": choices,
            "correct_answer": correct_answer,
            "explanation": f"한자 '{hanja}'의 뜻은 '{meaning}'({reading})입니다."
        }
    
    elif question_type == "idiom_outer":
        idiom, data = random.choice(list(IDIOM_DATA.items()))
        
        # 5지선다 생성
        wrong_choices = random.sample([item[1]["outer_meaning"] for item in IDIOM_DATA.items() if item[0] != idiom], 4)
        choices = [data["outer_meaning"]] + wrong_choices
        random.shuffle(choices)
        correct_answer = choices.index(data["outer_meaning"])
        
        st.session_state.current_question = {
            "quiz_type": "speed_multiple_choice",
            "type": "idiom",
            "question": f"{idiom}",
            "choices": choices,
            "correct_answer": correct_answer,
            "explanation": f"사자성어 '{idiom}({data['korean']})'의 겉뜻: {data['outer_meaning']}, 속뜻: {data['inner_meaning']}"
        }
    
    else:  # idiom_inner
        idiom, data = random.choice(list(IDIOM_DATA.items()))
        
        # 5지선다 생성
        wrong_choices = random.sample([item[1]["inner_meaning"] for item in IDIOM_DATA.items() if item[0] != idiom], 4)
        choices = [data["inner_meaning"]] + wrong_choices
        random.shuffle(choices)
        correct_answer = choices.index(data["inner_meaning"])
        
        st.session_state.current_question = {
            "quiz_type": "speed_multiple_choice",
            "type": "idiom",
            "question": f"{idiom}",
            "choices": choices,
            "correct_answer": correct_answer,
            "explanation": f"사자성어 '{idiom}({data['korean']})'의 겉뜻: {data['outer_meaning']}, 속뜻: {data['inner_meaning']}"
        }
    
    st.session_state.show_answer = False

def show_speed_quiz():
    st.header("⚡ 스피드 퀴즈")
    
    if st.session_state.speed_quiz_start_time:
        # 경과 시간 표시
        elapsed_time = time.time() - st.session_state.speed_quiz_start_time
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("경과 시간", f"{elapsed_time:.1f}초")
        with col2:
            st.metric("점수", f"{st.session_state.speed_quiz_score}/{st.session_state.speed_quiz_total}")
        with col3:
            if st.session_state.speed_quiz_total > 0:
                accuracy = (st.session_state.speed_quiz_score / st.session_state.speed_quiz_total) * 100
                st.metric("정확도", f"{accuracy:.1f}%")
        
        if st.session_state.current_question:
            show_speed_quiz_question()
    else:
        st.info("오른쪽 사이드바에서 '🚀 스피드 퀴즈 시작' 버튼을 눌러주세요!")

def show_speed_quiz_question():
    question = st.session_state.current_question
    
    # 문제 표시 (더 큰 상자)
    st.markdown(f"""
    <div style='font-size: 36px; padding: 40px; background-color: #ff6b6b; color: white;
                border-radius: 15px; text-align: center; margin: 20px 0; 
                border: 3px solid #ff5252; box-shadow: 0 4px 8px rgba(0,0,0,0.2);'>
        {question['question']}
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.show_answer:
        # 선택지들
        st.markdown("**선택하세요:**")
        for i, choice in enumerate(question["choices"]):
            key_letter = chr(65+i)  # A, B, C, D, E
            if st.button(f"{key_letter}. {choice}", use_container_width=True, key=f"speed_{i}"):
                check_speed_quiz_answer(i, question["correct_answer"])
                st.rerun()
    
    # 정답 표시
    if st.session_state.show_answer:
        if hasattr(st.session_state, 'speed_quiz_result'):
            if st.session_state.speed_quiz_result:
                st.success("🎉 정답!")
            else:
                st.error("❌ 틀림!")
        
        st.info(f"설명: {question['explanation']}")
        
        # 자동으로 다음 문제로 (1초 후)
        time.sleep(1)
        generate_speed_quiz_question()
        st.rerun()

def check_speed_quiz_answer(user_answer, correct_answer):
    st.session_state.show_answer = True
    st.session_state.speed_quiz_total += 1
    
    if user_answer == correct_answer:
        st.session_state.speed_quiz_result = True
        st.session_state.speed_quiz_score += 1
    else:
        st.session_state.speed_quiz_result = False

# 시험 모드 기능들
def generate_exam():
    """20문제 시험 생성 (사자성어 속뜻 맞추기 10문제 + 속뜻으로 사자성어 맞추기 10문제)"""
    st.session_state.exam_questions = []
    st.session_state.exam_current_index = 0
    st.session_state.exam_answers = {}
    st.session_state.exam_submitted = False
    st.session_state.exam_results = None
    
    # 사자성어 20개 선택
    selected_idioms = random.sample(list(IDIOM_DATA.items()), 20)
    
    # 1-10번: 사자성어 → 속뜻 맞추기 (5지선다)
    for i in range(10):
        idiom, data = selected_idioms[i]
        
        # 5지선다 생성
        wrong_choices = random.sample([item[1]["inner_meaning"] for item in IDIOM_DATA.items() if item[0] != idiom], 4)
        choices = [data["inner_meaning"]] + wrong_choices
        random.shuffle(choices)
        correct_answer = choices.index(data["inner_meaning"])
        
        st.session_state.exam_questions.append({
            "question_num": i + 1,
            "type": "idiom_to_inner",
            "question": f"{idiom}",
            "choices": choices,
            "correct_answer": correct_answer,
            "idiom": idiom,
            "data": data
        })
    
    # 11-20번: 속뜻 → 사자성어 맞추기 (5지선다)
    for i in range(10, 20):
        idiom, data = selected_idioms[i]
        
        # 5지선다 생성
        wrong_choices = random.sample([item[0] for item in IDIOM_DATA.items() if item[0] != idiom], 4)
        choices = [idiom] + wrong_choices
        random.shuffle(choices)
        correct_answer = choices.index(idiom)
        
        st.session_state.exam_questions.append({
            "question_num": i + 1,
            "type": "inner_to_idiom",
            "question": data["inner_meaning"],
            "choices": choices,
            "correct_answer": correct_answer,
            "idiom": idiom,
            "data": data
        })

def reset_exam():
    st.session_state.exam_questions = []
    st.session_state.exam_current_index = 0
    st.session_state.exam_answers = {}
    st.session_state.exam_submitted = False
    st.session_state.exam_results = None

def show_exam_mode():
    st.header("📝 시험 모드")
    
    if not st.session_state.exam_questions:
        st.info("오른쪽 사이드바에서 '📝 새 시험 시작' 버튼을 눌러주세요!")
        return
    
    if st.session_state.exam_submitted:
        show_exam_results()
    else:
        show_exam_question()

def show_exam_question():
    # 진행률 표시
    progress = len(st.session_state.exam_answers) / len(st.session_state.exam_questions)
    st.progress(progress)
    st.write(f"진행률: {len(st.session_state.exam_answers)}/{len(st.session_state.exam_questions)} 문제")
    
    # 현재 문제 표시
    current_q = st.session_state.exam_questions[st.session_state.exam_current_index]
    
    st.markdown(f"### 문제 {current_q['question_num']}")
    
    # 문제 표시 (더 큰 상자)
    if current_q["type"] == "idiom_to_inner":
        question_text = f"다음 사자성어의 속뜻은?"
        question_main = current_q["question"]
    else:
        question_text = f"다음 속뜻에 해당하는 사자성어는?"
        question_main = current_q["question"]
    
    st.markdown(f"**{question_text}**")
    st.markdown(f"""
    <div style='font-size: 28px; padding: 30px; background-color: #e3f2fd; 
                border-radius: 15px; text-align: center; margin: 20px 0; 
                border: 2px solid #2196f3; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
        {question_main}
    </div>
    """, unsafe_allow_html=True)
    
    # 선택지
    answer_key = f"exam_q_{current_q['question_num']}"
    current_answer = st.session_state.exam_answers.get(current_q['question_num'], None)
    
    user_answer = st.radio(
        "정답을 선택하세요:",
        options=range(len(current_q["choices"])),
        format_func=lambda x: f"{chr(65+x)}. {current_q['choices'][x]}",
        key=answer_key,
        index=current_answer if current_answer is not None else 0
    )
    
    # 답 저장
    st.session_state.exam_answers[current_q['question_num']] = user_answer
    
    # 네비게이션 버튼
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.session_state.exam_current_index > 0:
            if st.button("⬅️ 이전 문제"):
                st.session_state.exam_current_index -= 1
                st.rerun()
    
    with col2:
        if len(st.session_state.exam_answers) == len(st.session_state.exam_questions):
            if st.button("✅ 시험 제출", type="primary"):
                submit_exam()
                st.rerun()
    
    with col3:
        if st.session_state.exam_current_index < len(st.session_state.exam_questions) - 1:
            if st.button("➡️ 다음 문제"):
                st.session_state.exam_current_index += 1
                st.rerun()

def submit_exam():
    """시험 제출 및 채점"""
    correct_count = 0
    results = []
    
    for question in st.session_state.exam_questions:
        question_num = question["question_num"]
        user_answer = st.session_state.exam_answers.get(question_num)
        correct_answer = question["correct_answer"]
        
        is_correct = user_answer == correct_answer
        if is_correct:
            correct_count += 1
        
        results.append({
            "question_num": question_num,
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct
        })
    
    st.session_state.exam_results = {
        "score": correct_count,
        "total": len(st.session_state.exam_questions),
        "percentage": (correct_count / len(st.session_state.exam_questions)) * 100,
        "results": results
    }
    
    st.session_state.exam_submitted = True

def show_exam_results():
    """시험 결과 표시"""
    results = st.session_state.exam_results
    
    st.header("📊 시험 결과")
    
    # 점수 표시
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("점수", f"{results['score']}/{results['total']}")
    with col2:
        st.metric("정답률", f"{results['percentage']:.1f}%")
    with col3:
        if results['percentage'] >= 80:
            grade = "A"
            color = "🟢"
        elif results['percentage'] >= 70:
            grade = "B"
            color = "🟡"
        elif results['percentage'] >= 60:
            grade = "C"
            color = "🟠"
        else:
            grade = "D"
            color = "🔴"
        st.metric("등급", f"{color} {grade}")
    
    # 성과 분석
    if results['percentage'] >= 90:
        st.success("🎉 매우 우수합니다! 완벽한 이해도를 보여주고 있습니다.")
    elif results['percentage'] >= 80:
        st.success("👍 우수합니다! 대부분의 내용을 잘 이해하고 있습니다.")
    elif results['percentage'] >= 70:
        st.warning("⚠️ 양호합니다. 조금 더 학습하면 더 좋은 결과를 얻을 수 있습니다.")
    elif results['percentage'] >= 60:
        st.warning("📚 더 열심히 공부해야 합니다.")
    else:
        st.error("❌ 기초부터 다시 학습하는 것을 권합니다.")
    
    # 틀린 문제들을 복습 목록에 추가
    wrong_questions = [r for r in results['results'] if not r['is_correct']]
    if wrong_questions:
        if st.button("📝 틀린 문제 복습 목록에 추가"):
            for wrong in wrong_questions:
                question = wrong['question']
                user_choice = question['choices'][wrong['user_answer']] if wrong['user_answer'] is not None else "선택 안함"
                correct_choice = question['choices'][wrong['correct_answer']]
                
                # 한자 분석 추가
                hanja_analysis = analyze_hanja_chars(question['idiom'])
                
                review_item = {
                    "question": question['question'],
                    "user_answer": user_choice,
                    "correct_answer": correct_choice,
                    "explanation": f"사자성어: {question['idiom']} ({question['data']['korean']})\n한자 분석: {hanja_analysis}\n겉뜻: {question['data']['outer_meaning']}\n속뜻: {question['data']['inner_meaning']}",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "type": "exam"
                }
                
                # 중복 확인 후 추가
                if review_item not in st.session_state.review_list:
                    st.session_state.review_list.append(review_item)
            
            st.success(f"{len(wrong_questions)}개의 틀린 문제가 복습 목록에 추가되었습니다!")
    
    # 상세 결과
    st.markdown("---")
    st.subheader("📋 상세 결과")
    
    for result in results['results']:
        question = result['question']
        
        with st.expander(f"문제 {result['question_num']} - {'✅ 정답' if result['is_correct'] else '❌ 오답'}"):
            if question['type'] == "idiom_to_inner":
                st.markdown(f"**문제**: 다음 사자성어의 속뜻은? **{question['question']}**")
            else:
                st.markdown(f"**문제**: 다음 속뜻에 해당하는 사자성어는? **{question['question']}**")
            
            if result['user_answer'] is not None:
                st.markdown(f"**내 답**: {question['choices'][result['user_answer']]}")
            else:
                st.markdown(f"**내 답**: 선택 안함")
            
            st.markdown(f"**정답**: {question['choices'][result['correct_answer']]}")
            
            # 상세 설명
            hanja_analysis = analyze_hanja_chars(question['idiom'])
            st.info(f"""
            **사자성어**: {question['idiom']} ({question['data']['korean']})
            **한자 분석**: {hanja_analysis}
            **겉뜻**: {question['data']['outer_meaning']}
            **속뜻**: {question['data']['inner_meaning']}
            """)

def show_statistics():
    st.header("📊 학습 통계")
    
    # 기본 퀴즈 통계
    if st.session_state.score["total"] > 0:
        total = st.session_state.score["total"]
        correct = st.session_state.score["correct"]
        wrong = total - correct
        accuracy = (correct / total) * 100
        
        st.subheader("🧠 퀴즈 모드 통계")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("총 문제 수", total)
        with col2:
            st.metric("정답 수", correct)
        with col3:
            st.metric("오답 수", wrong)
        with col4:
            st.metric("정답률", f"{accuracy:.1f}%")
        
        # 정답률 시각화
        if accuracy >= 80:
            st.success(f"🎉 훌륭합니다! 정답률이 {accuracy:.1f}%입니다.")
        elif accuracy >= 60:
            st.warning(f"👍 좋습니다! 정답률이 {accuracy:.1f}%입니다.")
        else:
            st.error(f"💪 더 열심히! 정답률이 {accuracy:.1f}%입니다.")
        
        # 진행률 바
        st.progress(accuracy / 100)
    
    # 스피드 퀴즈 통계
    if st.session_state.speed_quiz_total > 0:
        st.markdown("---")
        st.subheader("⚡ 스피드 퀴즈 통계")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("총 문제", st.session_state.speed_quiz_total)
        with col2:
            st.metric("정답", st.session_state.speed_quiz_score)
        with col3:
            speed_accuracy = (st.session_state.speed_quiz_score / st.session_state.speed_quiz_total) * 100
            st.metric("정답률", f"{speed_accuracy:.1f}%")
    
    # 시험 결과 통계
    if st.session_state.exam_results:
        st.markdown("---")
        st.subheader("📝 최근 시험 결과")
        
        results = st.session_state.exam_results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("점수", f"{results['score']}/{results['total']}")
        with col2:
            st.metric("정답률", f"{results['percentage']:.1f}%")
        with col3:
            if results['percentage'] >= 80:
                grade = "A"
            elif results['percentage'] >= 70:
                grade = "B"
            elif results['percentage'] >= 60:
                grade = "C"
            else:
                grade = "D"
            st.metric("등급", grade)
    
    # 복습 노트 통계
    st.markdown("---")
    st.subheader("💾 복습 노트 통계")
    
    total_wrong = len(st.session_state.wrong_answers)
    total_review = len(st.session_state.review_list)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("퀴즈 틀린 문제", total_wrong)
    with col2:
        st.metric("복습 목록", total_review)

def show_review_notes():
    st.header("💾 복습 노트")
    
    # 탭으로 구분
    tab1, tab2 = st.tabs(["🧠 퀴즈 틀린 문제", "📝 복습 목록"])
    
    with tab1:
        if not st.session_state.wrong_answers:
            st.info("아직 틀린 문제가 없습니다. 퀴즈를 풀어보세요!")
        else:
            st.markdown(f"**총 {len(st.session_state.wrong_answers)}개의 틀린 문제가 있습니다.**")
            
            # 복습 노트 초기화 버튼
            if st.button("🗑️ 퀴즈 틀린 문제 초기화"):
                st.session_state.wrong_answers = []
                st.success("퀴즈 틀린 문제가 초기화되었습니다.")
                st.rerun()
            
            # 틀린 문제들 표시
            for i, item in enumerate(st.session_state.wrong_answers):
                with st.expander(f"❌ 문제 {i+1} - {item['timestamp']}"):
                    st.markdown(f"**문제:** {item['question']}")
                    st.markdown(f"**내 답:** {item['user_answer']}")
                    st.markdown(f"**정답:** {item['correct_answer']}")
                    st.markdown(f"**설명:** {item['explanation']}")
    
    with tab2:
        if not st.session_state.review_list:
            st.info("복습 목록이 비어있습니다. 시험에서 틀린 문제를 추가해보세요!")
        else:
            st.markdown(f"**총 {len(st.session_state.review_list)}개의 복습 문제가 있습니다.**")
            
            # 복습 목록 초기화 버튼
            if st.button("🗑️ 복습 목록 초기화"):
                st.session_state.review_list = []
                st.success("복습 목록이 초기화되었습니다.")
                st.rerun()
            
            # 복습 문제들 표시
            for i, item in enumerate(st.session_state.review_list):
                with st.expander(f"📚 복습 {i+1} - {item['timestamp']}"):
                    st.markdown(f"**문제:** {item['question']}")
                    st.markdown(f"**내 답:** {item['user_answer']}")
                    st.markdown(f"**정답:** {item['correct_answer']}")
                    st.markdown(f"**설명:** {item['explanation']}")

def show_idiom_search():
    st.header("🔍 사자성어 검색")
    
    # 검색 기능
    if hasattr(st.session_state, 'search_term') and st.session_state.search_term:
        search_term = st.session_state.search_term
        
        # 검색 결과
        results = []
        for idiom, data in IDIOM_DATA.items():
            if (search_term.lower() in idiom.lower() or 
                search_term.lower() in data["korean"].lower() or
                search_term.lower() in data["outer_meaning"].lower() or
                search_term.lower() in data["inner_meaning"].lower()):
                results.append((idiom, data))
        
        if results:
            st.success(f"검색 결과: {len(results)}개")
            
            for idiom, data in results:
                with st.expander(f"📜 {idiom} ({data['korean']})"):
                    # 한자 분석
                    hanja_analysis = analyze_hanja_chars(idiom)
                    st.markdown(f"**한자 분석:** {hanja_analysis}")
                    
                    st.markdown(f"**겉뜻:** {data['outer_meaning']}")
                    st.markdown(f"**속뜻:** {data['inner_meaning']}")
        else:
            st.warning("검색 결과가 없습니다.")
    
    # 전체 사자성어 목록 보기
    if hasattr(st.session_state, 'show_all_idioms') and st.session_state.show_all_idioms:
        st.markdown(f"### 📚 전체 사자성어 ({len(IDIOM_DATA)}개)")
        
        for idiom, data in sorted(IDIOM_DATA.items()):
            st.markdown(f"**{idiom}** ({data['korean']}) - {data['outer_meaning']}")
    
    # 기본 안내 메시지
    if not hasattr(st.session_state, 'search_term') and not hasattr(st.session_state, 'show_all_idioms'):
        st.info("왼쪽 사이드바에서 검색어를 입력하거나 전체 목록을 확인하세요.")

if __name__ == "__main__":
    main()
