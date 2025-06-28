import streamlit as st
import json
import random
from typing import Dict, List, Tuple

# 페이지 설정
st.set_page_config(
    page_title="한문 학습 도우미",
    page_icon="📚",
    layout="wide"
)

# 한자 데이터
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
    "數": ("세다", "수")
}

# 사자성어 데이터 (이미지에서만 추출)
IDIOM_DATA = {
    # 첫 번째 이미지의 사자성어들
    "法古創新": ("법고창신", "옛 법을 본받아 새로운 것을 창조함"),
    "三水甲山": ("삼수갑산", "함경도의 험한 산골, 유배지"),
    "三馬太守": ("삼마태수", "태수의 탐욕을 비유"),
    "鷄卵有骨": ("계란유골", "있을 수 없는 일"),
    "不言長短": ("불언장단", "장단점을 말하지 않음"),
    "下馬評": ("하마평", "길에서 떠도는 소문"),
    "落點": ("낙점", "점수가 떨어짐"),
    "鈍筆借騎": ("둔필차기", "둔한 붓으로 말을 빌려 탐"),
    "還盜賊風": ("환도적풍", "도둑질한 것을 돌려주는 바람"),
    "聞諷刺剽": ("문풍자표", "풍자를 듣고 찌르며 겁박함"),
    "竊舍從蛙": ("절사종와", "훔쳐서 버리고 개구리를 따름"),
    "弘益間見": ("홍익간견", "크게 이익이 되는 것을 사이에서 봄"),
    "金如石八": ("금여석팔", "금이 돌 여덟과 같음"),
    "商泥田狗": ("상니전구", "장사하는 진흙 밭의 개"),
    "碧昌牛場": ("벽창우장", "푸른 창성한 소의 마당"),
    "機智致貪": ("기지치탐", "기지로써 탐욕을 이룸"),
    "夫徇財固": ("부순재고", "남편이 재물을 쫓아 굳어짐"),
    "執通杜門": ("집통두문", "잡고 통하여 문을 막음"),
    "出征明假": ("출정명가", "출정하여 명나라에서 빌림"),
    "道走肖爲": ("도주초위", "길을 달려 닮기 위함"),
    "王持斧疏": ("왕지부소", "왕이 도끼를 잡고 소통함"),
    "淸吏興亡": ("청리흥망", "맑은 관리의 흥망"),
    "櫨櫃刻求": ("노궤각구", "옻나무 궤짝에 새겨 구함"),
    "劍株待兎": ("검주대토", "칼과 그루터기로 토끼를 기다림"),
    "膠柱鼓瑟": ("교주고슬", "기둥에 아교를 붙이고 거문고를 두드림"),
    "尾生之信": ("미생지신", "미생의 신의"),
    "食言佩鈴": ("식언패령", "말을 어기고 방울을 참"),
    "誡松都員": ("계송도원", "소나무를 경계하고 도원의 인원"),
    "沙野鼠婚": ("사야서혼", "모래 들판의 쥐 혼인"),
    "妻高麗公": ("처고려공", "아내가 고려의 공주"),
    "快錦兄友": ("쾌금형우", "쾌활한 비단과 형의 우애"),
    "弟南入納": ("제남입납", "아우가 남쪽으로 들어가 받아들임"),
    "審問編發": ("심문편발", "자세히 묻고 머리를 땋음"),
    "忘息功者": ("망식공자", "쉬는 것을 잊은 공이 있는 자"),
    "亦能學勿": ("역능학물", "또한 능히 배우되 말라"),
    "今而年讀": ("금이년독", "이제 그리고 해마다 읽음"),
    "必氣念主": ("필기념주", "반드시 기운을 생각의 주인으로"),
    "先桂枝外": ("선계지외", "먼저 계수나무 가지 밖"),
    "內剛禮義": ("내강예의", "안이 굳센 예의"),
    "恥招受益": ("치초수익", "부끄러워하며 이익을 받음"),
    "者論故其": ("자론고기", "자를 논하니 옛 그것"),
    "海擇流深": ("해택류심", "바다가 흐름을 가려 깊게 함"),
    "破心同體": ("파심동체", "마음을 깨뜨려 같은 몸"),
    "異聲渾然": ("이성혼연", "다른 소리가 모두 그러함"),
    "團床異夢": ("단상이몽", "평상에 모여 다른 꿈"),
    "咸差使烏": ("함차사오", "모두 다르게 까마귀를 시킴"),
    "飛梨落瓜": ("비리락과", "배가 날고 오이가 떨어짐"),
    "田履李冠": ("전리이관", "밭의 신과 오얏의 갓"),
    "袖手傍觀": ("수수방관", "소매에 손을 넣고 곁에서 봄"),
    "管鮑交蘭": ("관포교란", "관중과 포숙아의 사귐과 난초"),
    "漆伯牙絃": ("칠백아현", "옻칠과 백아의 거문고 줄"),
    "刎頸過猶": ("문경과유", "목을 베어도 지나침은 여전"),
    "及時刻桃": ("급시각도", "때에 미쳐 복숭아를 새김"),
    "園義生常": ("원의생상", "동산의 의로 항상 삶"),
    "邯鄲柯胡": ("한단가호", "조나라 서울의 가지와 나비"),
    "蝶塞翁用": ("접새옹용", "나비 변방의 늙은이가 씀"),
    "意周到孤": ("의주도고", "뜻이 두루 이르러 외로움"),
    "奮五多苦": ("분오다고", "다섯을 떨쳐 많이 괴로워함"),
    "各圖莫逆": ("각도막역", "각자 꾀하되 거스르지 않음"),
    "實相符辭": ("실상부사", "실제 모습이 말과 부합함"),
    "句前代未": ("구전대미", "글귀가 앞 시대에 없었음"),
    "曾有佳約": ("증유가약", "일찍이 아름다운 약속이 있음"),
    "喜再歸姻": ("희재귀인", "기뻐하며 다시 혼인으로 돌아감"),
    "婚數": ("혼수", "혼인의 수"),
    
    # 두 번째, 세 번째 이미지의 사자성어들
    "自强不息": ("자강불식", "스스로 강해지기를 쉬지 않음"),
    "螢雪之功": ("형설지공", "반딧불과 눈빛으로 공부한 공로"),
    "手不釋卷": ("수불석권", "손에서 책을 놓지 않음"),
    "請學不厭者": ("청학불염자", "배우기를 싫어하지 않는 자를 청함"),
    "雖眠": ("수면", "비록 잠들어도"),
    "亦不能學矣": ("역불능학의", "또한 배울 수 없다"),
    "幼讀今日不學": ("유독금일불학", "어려서 오늘 배우지 않으면"),
    "而有來日": ("이유래일", "다음날이 있더라도"),
    "幼讀今年不學": ("유독금년불학", "어려서 올해 배우지 않으면"),
    "而有來年": ("이유래년", "다음해가 있더라도"),
    "讀書": ("독서", "독서"),
    "必整襟肅容": ("필정금숙용", "반드시 옷깃을 정돈하고 용모를 숙연히 함"),
    "專心易氣": ("전심이기", "마음을 전일하게 하여 기운을 바꿈"),
    "毋生雜念": ("무생잡념", "잡념을 일으키지 말라"),
    "毋主先入": ("무주선입", "선입견을 주장하지 말라"),
    "桂林一枝": ("계림일지", "계수나무 숲의 한 가지"),
    "外柔內剛": ("외유내강", "겉은 부드럽고 속은 굳셈"),
    "禮義廉恥": ("예의염치", "예의와 염치"),
    "滿招損": ("만초손", "가득 차면 손해를 불러들임"),
    "謙受益": ("겸수익", "겸손하면 이익을 받음"),
    "一心回體": ("일심회체", "한 마음으로 몸을 돌이킴"),
    "欲勝人者": ("욕승인자", "남을 이기고자 하는 자"),
    "必先自勝": ("필선자승", "반드시 먼저 자기를 이겨야 함"),
    "欲論人者": ("욕론인자", "남을 논하고자 하는 자"),
    "必先自論": ("필선자론", "반드시 먼저 자기를 논해야 함"),
    "太山不讓土壤": ("태산불양토양", "태산은 흙을 마다하지 않음"),
    "故能成其大": ("고능성기대", "그러므로 능히 그 큰 것을 이룸"),
    "河海不擇細流": ("하해불택세류", "강과 바다는 가는 물줄기를 가리지 않음"),
    "故能就其深": ("고능취기심", "그러므로 능히 그 깊음에 이름"),
    "異口同聲": ("이구동성", "다른 입 같은 소리"),
    "渾然一體": ("혼연일체", "모두 하나의 몸과 같음"),
    "大同團結": ("대동단결", "크게 같이하여 단결함"),
    "同床異夢": ("동상이몽", "같은 침상에서 다른 꿈"),
    "感興差使": ("감흥차사", "감흥이 차서 사신을 보냄"),
    "烏飛梨落": ("오비이락", "까마귀가 날고 배가 떨어짐"),
    "瓜田不納履": ("과전불납리", "오이밭에서는 신을 신지 않음"),
    "李下不整冠": ("이하불정관", "오얏나무 아래서는 갓을 고쳐 쓰지 않음"),
    "袖手傍觀": ("수수방관", "소매 속에 손을 넣고 곁에서 봄"),
    "伯牙絶絃": ("백아절현", "백아가 거문고 줄을 끊음"),
    "過猶不及": ("과유불급", "지나침은 미치지 못함과 같음"),
    "時時刻刻": ("시시각각", "때때로 순간순간"),
    "桃園結義": ("도원결의", "복숭아 동산에서 의를 맺음"),
    
    # 마지막 이미지의 사자성어들
    "管鮑之交": ("관포지교", "관중과 포숙아의 우정"),
    "金蘭之交": ("금란지교", "금석같이 견고한 우정"),
    "芝蘭之交": ("지란지교", "지초와 난초 같은 고결한 교제"),
    "水魚之交": ("수어지교", "물과 물고기 같은 뗄 수 없는 관계"),
    "膠漆之交": ("교칠지교", "아교와 옻칠 같은 견고한 우정"),
    "刎頸之交": ("문경지교", "목을 베어도 변치 않는 우정"),
    "塞翁之馬": ("새옹지마", "변방 늙은이의 말, 인생의 길흉화복"),
    "用意周到": ("용의주도", "뜻을 씀이 두루 미침"),
    "孤軍奮鬪": ("고군분투", "외로운 군대가 힘써 싸움"),
    "名實相符": ("명실상부", "이름과 실제가 서로 부합함"),
    "美錦麗句": ("미금려구", "아름다운 비단과 고운 글귀"),
    "前代未聞": ("전대미문", "앞 시대에 들어보지 못한 일"),
    "未曾有": ("미증유", "일찍이 없었던 일"),
    "人生無常": ("인생무상", "인생은 변함이 없지 않음"),
    "一場春夢": ("일장춘몽", "한바탕 봄꿈"),
    "邯鄲之夢": ("한단지몽", "조나라 서울의 꿈"),
    "南柯一夢": ("남가일몽", "남쪽 가지의 한 꿈"),
    "胡蝶之夢": ("호접지몽", "호접의 꿈"),
    "三三五五": ("삼삼오오", "삼삼오오 모여 있음"),
    "多多益善": ("다다익선", "많을수록 더욱 좋음"),
    "同苦同樂": ("동고동락", "괴로움과 즐거움을 함께 함"),
    "各自圖生": ("각자도생", "각자가 제 살 길을 도모함"),
    "莫逆之友": ("막역지우", "거스름이 없는 친구"),
    "百年佳約": ("백년가약", "백 년의 아름다운 약속"),
    "喜喜樂樂": ("희희낙락", "기쁘고 즐거움"),
    "非一非再": ("비일비재", "하나가 아니고 둘이 아님, 매우 많음"),
    "事必歸正": ("사필귀정", "일은 반드시 바른 데로 돌아감")
    "桃園結義": ("도원결의", "복숭아 동산에서 의를 맺음")
}

def initialize_session_state():
    """세션 상태 초기화"""
    if 'current_mode' not in st.session_state:
        st.session_state.current_mode = 'flashcard'
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quiz_total' not in st.session_state:
        st.session_state.quiz_total = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = None
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False

def get_random_hanja():
    """랜덤 한자 반환"""
    hanja = random.choice(list(HANJA_DATA.keys()))
    meaning, reading = HANJA_DATA[hanja]
    return hanja, meaning, reading

def get_random_idiom():
    """랜덤 사자성어 반환"""
    idiom = random.choice(list(IDIOM_DATA.keys()))
    meaning, explanation = IDIOM_DATA[idiom]
    return idiom, meaning, explanation

def create_quiz_question(quiz_type):
    """퀴즈 문제 생성"""
    if quiz_type == "한자":
        hanja, meaning, reading = get_random_hanja()
        # 선택지 생성
        wrong_answers = random.sample([v[0] for k, v in HANJA_DATA.items() if k != hanja], 3)
        choices = [meaning] + wrong_answers
        random.shuffle(choices)
        return {
            'question': hanja,
            'correct_answer': meaning,
            'choices': choices,
            'type': 'hanja'
        }
    else:
        idiom, meaning, explanation = get_random_idiom()
        wrong_answers = random.sample([v[0] for k, v in IDIOM_DATA.items() if k != idiom], 3)
        choices = [meaning] + wrong_answers
        random.shuffle(choices)
        return {
            'question': idiom,
            'correct_answer': meaning,
            'choices': choices,
            'type': 'idiom',
            'explanation': explanation
        }

def main():
    initialize_session_state()
    
    st.title("📚 한문 학습 도우미")
    st.markdown("---")
    
    # 사이드바 메뉴
    st.sidebar.title("📖 학습 메뉴")
    mode = st.sidebar.selectbox(
        "학습 모드를 선택하세요:",
        ["플래시카드", "퀴즈", "전체 한자 목록", "사자성어 목록"]
    )
    
    if mode == "플래시카드":
        flashcard_mode()
    elif mode == "퀴즈":
        quiz_mode()
    elif mode == "전체 한자 목록":
        hanja_list_mode()
    elif mode == "사자성어 목록":
        idiom_list_mode()

def flashcard_mode():
    st.header("🎴 플래시카드 모드")
    
    col1, col2 = st.columns(2)
    
    with col1:
        card_type = st.selectbox("카드 유형:", ["한자", "사자성어"])
    
    with col2:
        if st.button("🔄 새 카드"):
            st.session_state.show_answer = False
    
    st.markdown("---")
    
    if card_type == "한자":
        hanja, meaning, reading = get_random_hanja()
        
        # 카드 스타일링
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            margin: 20px 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        ">
            <h1 style="color: white; font-size: 4em; margin: 0;">{hanja}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💡 답 보기", key="show_hanja_answer"):
            st.session_state.show_answer = True
        
        if st.session_state.show_answer:
            st.success(f"**뜻:** {meaning}")
            st.info(f"**음:** {reading}")
    
    else:  # 사자성어
        idiom, meaning, explanation = get_random_idiom()
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            margin: 20px 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        ">
            <h1 style="color: white; font-size: 2.5em; margin: 0;">{idiom}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💡 답 보기", key="show_idiom_answer"):
            st.session_state.show_answer = True
        
        if st.session_state.show_answer:
            st.success(f"**뜻:** {meaning}")
            st.info(f"**설명:** {explanation}")

def quiz_mode():
    st.header("🎯 퀴즈 모드")
    
    # 점수 표시
    if st.session_state.quiz_total > 0:
        accuracy = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
        st.metric("정답률", f"{accuracy:.1f}%", f"{st.session_state.quiz_score}/{st.session_state.quiz_total}")
    
    quiz_type = st.selectbox("퀴즈 유형:", ["한자", "사자성어"])
    
    if st.button("🎲 새 문제") or st.session_state.current_question is None:
        st.session_state.current_question = create_quiz_question(quiz_type)
        st.session_state.show_answer = False
    
    if st.session_state.current_question:
        question = st.session_state.current_question
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin: 20px 0;
        ">
            <h2 style="color: white; margin: 0;">다음 {quiz_type}의 뜻은?</h2>
            <h1 style="color: white; font-size: 3em; margin: 10px 0;">{question['question']}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # 선택지
        selected_answer = st.radio("정답을 선택하세요:", question['choices'], key="quiz_choice")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ 답안 제출"):
                st.session_state.quiz_total += 1
                if selected_answer == question['correct_answer']:
                    st.session_state.quiz_score += 1
                    st.success("🎉 정답입니다!")
                else:
                    st.error(f"❌ 틀렸습니다. 정답: {question['correct_answer']}")
                
                if question['type'] == 'idiom':
                    st.info(f"**설명:** {question['explanation']}")
                
                st.session_state.show_answer = True
        
        with col2:
            if st.button("🔄 다음 문제"):
                st.session_state.current_question = create_quiz_question(quiz_type)
                st.session_state.show_answer = False
                st.rerun()

def hanja_list_mode():
    st.header("📝 전체 한자 목록")
    
    # 검색 기능
    search_term = st.text_input("🔍 한자 검색:")
    
    # 정렬 옵션
    sort_option = st.selectbox("정렬 기준:", ["한자순", "음순", "뜻순"])
    
    # 데이터 필터링 및 정렬
    filtered_data = {}
    for hanja, (meaning, reading) in HANJA_DATA.items():
        if (search_term.lower() in hanja.lower() or 
            search_term.lower() in meaning.lower() or 
            search_term.lower() in reading.lower()):
            filtered_data[hanja] = (meaning, reading)
    
    if sort_option == "음순":
        filtered_data = dict(sorted(filtered_data.items(), key=lambda x: x[1][1]))
    elif sort_option == "뜻순":
        filtered_data = dict(sorted(filtered_data.items(), key=lambda x: x[1][0]))
    
    st.write(f"총 {len(filtered_data)}개의 한자")
    
    # 한자 목록 표시 (3열로)
    cols = st.columns(3)
    for i, (hanja, (meaning, reading)) in enumerate(filtered_data.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 15px;
                margin: 5px 0;
                text-align: center;
                background: #f9f9f9;
            ">
                <h2 style="margin: 0; color: #333;">{hanja}</h2>
                <p style="margin: 5px 0; color: #666;"><strong>{meaning}</strong></p>
                <p style="margin: 0; color: #999; font-size: 0.9em;">{reading}</p>
            </div>
            """, unsafe_allow_html=True)

def idiom_list_mode():
    st.header("📜 사자성어 목록")
    
    # 검색 기능
    search_term = st.text_input("🔍 사자성어 검색:")
    
    # 데이터 필터링
    filtered_idioms = {}
    for idiom, (meaning, explanation) in IDIOM_DATA.items():
        if (search_term.lower() in idiom.lower() or 
            search_term.lower() in meaning.lower() or 
            search_term.lower() in explanation.lower()):
            filtered_idioms[idiom] = (meaning, explanation)
    
    st.write(f"총 {len(filtered_idioms)}개의 사자성어")
    
    # 사자성어 목록 표시
    for idiom, (meaning, explanation) in filtered_idioms.items():
        with st.expander(f"**{idiom}** - {meaning}"):
            st.write(explanation)
            
            # 각 한자 분석
            st.markdown("**한자 분석:**")
            hanja_analysis = []
            for char in idiom:
                if char in HANJA_DATA:
                    char_meaning, char_reading = HANJA_DATA[char]
                    hanja_analysis.append(f"{char}({char_reading}): {char_meaning}")
                else:
                    hanja_analysis.append(f"{char}: 데이터 없음")
            
            for analysis in hanja_analysis:
                st.write(f"- {analysis}")

if __name__ == "__main__":
    main()
