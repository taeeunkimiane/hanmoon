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

# 기본 사자성어 데이터
IDIOM_DATA = {
    "一石二鳥": ("하나의 돌로 두 마리의 새를 잡는다", "한 번의 행동으로 두 가지 이익을 얻음"),
    "溫故知新": ("옛것을 익히고 새것을 안다", "옛것을 연구하여 새로운 지식을 얻음"),
    "四面楚歌": ("사방에서 초나라 노래가 들린다", "사방이 모두 적으로 둘러싸여 고립된 상태"),
    "自業自得": ("자기가 지은 업을 자기가 받는다", "자기가 한 행동의 결과를 자기가 받음"),
    "三人三色": ("세 사람이면 세 가지 색깔", "사람마다 각기 다른 개성과 취향을 가짐"),
    "漁父之利": ("어부의 이익", "두 편이 싸우는 사이에 제3자가 이익을 얻음"),
    "破釜沈舟": ("솥을 깨뜨리고 배를 가라앉힌다", "결사의 각오로 일에 임함"),
    "同床異夢": ("같은 침상에 누워 다른 꿈을 꾼다", "겉으로는 같이 행동하나 속마음은 다름"),
    "井中之蛙": ("우물 안의 개구리", "견문이 좁아 사리를 제대로 알지 못함"),
    "背水之陣": ("물을 등지고 진을 친다", "퇴로를 끊고 결사적으로 싸움"),
    "雞鳴狗盜": ("닭 울음소리와 개 도둑질", "하찮은 기술이라도 때로는 큰 도움이 됨"),
    "刻舟求劍": ("배에 표시하고 칼을 찾는다", "융통성 없이 고지식하게 행동함"),
    "塞翁之馬": ("변방 늙은이의 말", "인생의 길흉화복은 예측하기 어려움"),
    "胡蝶之夢": ("호접의 꿈", "인생의 덧없음, 현실과 꿈의 구별이 모호함"),
    "孤軍奮鬪": ("외로운 군대가 힘써 싸운다", "도움 없이 혼자서 어려운 일과 맞서 싸움")
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
