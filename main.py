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
    "法古創新": ("법고창신", "옛것에 토대를 두되 그것을 변화시킨줄 알고 새것을 만들어 가되 근본을 잃지 말아야한다"),
    "三水甲山": ("삼수갑산", "매우 힘들고 험난한 곳으로 가거나 어려운 지경에 이름(나중에야 삼수갑산을 갈지라도 최악의 경우를 각오하고 자기 하고 싶은 대로 어떤일을 단행할때 쓰는 말"),
    "三馬太守": ("삼마태수", ""),
    "鷄卵有骨": ("계간유골", "운수가 나쁜 사람은 모처럼 좋은 기회를 만나도 역시 일이 잘 안됨"),
    "不言長短": ("불언장단", "황희정승과 농부의 대화에서 유래"),
    "下馬評": ("하마평", "관직의 인사이동이나 관직에 임명될 후보자에 대한 풍문"),
    "落點": ("낙점", "여러 후보가 있을대 그중 마땅한 대상을 고름"),
    "鈍筆勝聰": ("둔필승총", "서툰 글이라도 기록하는것이 기억보다 낫다"),
    "借鷄騎還": ("차계기환", "손님을 박대하는 것을 빗대어 이르는 말"),
    "勝甲盜賊": ("슬갑도적", "남의 글이나 저술을 베껴 마치 제가 지은 것처럼 하는 사람"),
    "含人從蛙": ("사인종와", "위금 상황에 기지를 발휘하여 대처함"),
    "弘益人間": ("홍익인간", "옛날에 환인의 서자 환웅이 자주 하늘 아래에 뜻을 두어 인간 세상을 구하고자 했는데, 아버지가 아들의 뜻을 알고 삼위 태백에 내려보내니, 널리 인간을 이롭게 할만하여 곧 천부인 세 개를 주어 가서 그곳을 다스리게 하였다"),
    "見金如石": ("견금여석", "지나친 욕심을 절제함. 욕심 많은 사람은 재물이라면 목숨도 아랑곳하지 않고 좇음"),
    "八包大商": ("팔포대상", "생활에 걱정이 없는 사람"),
    "泥田鬪狗": ("이전투구", "강인한 성격의 함경도 사람. 자기 이익을 위하여 불썽사납게 싸움"),
    "碧昌牛": ("벽창우", "미련하고 고집이 센 사람"),
    "亂場": ("난장", "여러 사람이 어지러이 뒤섞여 떠들어대거나 뒤엉켜 뒤죽 박죽이 된곳"),
    "杜門不出": ("두문불출", "집에서 은거하면서 관직에 나가지 아니하거나 사회의 일을 하지 아니함 (조선에 반대하여 벼슬살이를 거부하고 은거하여 살던 곳으로 유명함"),
    "征明假道": ("정명가도", "어떤 일을 이루기 위해 말도 안되는 명분을 내세움"),
    "走肖爲王": ("주초위왕", "정적을 없애기 위해 갖은 술수를 씀"),
    "持斧上疏": ("지수상소", "왕의 실정에 대해 목숨을 걸고 지적하는 신하의 기개"),
    "淸白吏": ("청백리", "청렴하고 결백한 관리(재물에 대한 욕심이 없이 곧고 깨끗한 관리)"),
    "興淸亡淸": ("흥청망청", "돈이나 물건을 함부로 쓰며 마음껏 즐기는 모양"),
    "櫟木槁": ("노목계", "조금도 융통성이 없는 미련한 사람"),
    "刻舟求劍": ("각주구검", "어리석고 미련하여 융통성이 없음"),
    "守株待兔": ("수주대토", "요행으로 일이 성취되기를 바라거나 어떤 착각에 빠져 되지도 않을 일을 공연히 고집하는 어리석음"),
    "膠柱鼓瑟": ("교주고슬", "고지식하여 융통성이 전혀 없음"),
    "尾生之信": ("미생지신", "고지식하여 융통성이 전혀 없음"),
    "王不食言": ("왕불식언", "함부로 거짓말이나 빈말을 해선 안됨 평강공주가 자신을 상부고씨에게 시집보내려는 아버지에게 한 말"),
    "佩鈴自戒": ("패령자계", "나쁜 습관이나 단점을 고치기 위해 스스로 노력하는 자세"),
    "松都契員": ("송도계원", "하찮은 지위나 세력을 믿고 남을 멸시하고 오만하게 구는 사람"),
    "月沙夫人": ("월사부인", "남편의 지위가 높은데도 검소하여 타의 모범이 되는 부인"),
    "野鼠婚": ("야서혼", "제 분수에 넘치는 허영심. 동류는 동류끼리 가장 잘 어울림"),
    "夫妻詵鏡": ("부처승경", "가상과 실상의 혼란에 빠진 존재의 어리석음(참과 거짓에 혼동하는 어리석음)"),
    "高麗公事三日": ("고려공사삼일", "한번 시작한 일이 오래 계속되어 가지 못함"),
    "愾山寃牛": ("쾌산원우", "충성을 바쳤으나 도리어 죽음을 맞이함"),
    "錦繡江山": ("금수강산", "우리나라의 산천을 비유적으로 이르는 말"),
    "兄友弟恭": ("형우제공", "형제간에 서로 우애 깊게 지냄"),
    "南大門入納": ("남대문입납", "줄거리나 골자를 알 수 없는 말을 비유적으로 이르는 말(바보 같은 방법으로 자신의 목적을 이루려고 할 때 쓰는 표현"),
    "博學審問": ("박학심문", "학문을 하는 올바른 자세"),
    "韋編三絶": ("위편삼절", "책을 열심히 읽음, 부지런히 배우다, 학문에 힘씀"),
    "發憤忘食": ("발분망식", "끼니까지도 잊을 정도로 어떤일에 열중하여 노력함"),
    "自强不息": ("자강불식", "자신의 목표를 향해 끊임 없이 노력하는것"),
    "螢雪之功": ("형설지공", "어려운 환경에서도 부지런하고 꾸준하게 공부하여 성공함"),
    "手不釋卷": ("수불석권", "항상 손에 책을 들고 글을 읽으면서 공부함"),
    "謂學不暇者 雖暇 亦不能學矣": ("위학불가자는 수가 라도 역불능학의 라", "게으른 자들은 한결같이 바쁘고 시간이 없다는 핑계를 대지만 사실 시간이 없어서 공부를 하지 않은것은 아니다"),
    "勿謂今日不學 而有來日 / 勿謂今年不學 而有來年": ("무위금일불학 이유래일 하고 / 무위금년불학 이유래년 하라", ""),
    "讀書 / 必整襟齊容 / 專心易氣 / 毋生雜念 / 毋主先入": ("독서 에 / 필정금속용 하고 / 전심이기 하며 / 무생잡념 하라 / 무주선입 하라", ""),
    "桂林一枝": ("계림일지", "사람됨이 비범하면서 겸손함"),
    "外柔內剛": ("외유내강", "겉으로는 부드럽고 순하나 속은 곧고 꿋꿋함(단단하고 강함)"),
    "禮義廉恥": ("예의염치", "예절, 의리, 청렴, 부끄러움을 아는 태도. 부끄러운 것을 모르고 뻔뻔함"),
    "滿招損 / 謙受益": ("만초손 이요 / 검수익 이라", ""),
    "欲勝人者 必先自勝 / 欲論人者 必先自論": ("욕승인자는 필선자승 하고 / 욕론인자는 필선자론 이니라", ""),
    "太山 不讓土壤 故 能成其大 / 河海 不擇細流 故 能就其深": ("태산은 불양토양이라 고로 능성기대요 / 하해는 불택세류라 고로 능취기심이라", "배울 수 있는 점: 포용, 남을 너그럽게 감싸주거나 받아 들임"),
    "一心同體": ("일심동체", "둘 이상의 사람이 굳게 뭉치는 일"),
    "異口同聲": ("이구동성", "여러 사람의 말이 한결같음"),
    "渾然一體": ("혼연일체", "조금의 어긋남도 없이 한덩어리가 됨(생각, 행동, 의지 따위가 완전히 하나가 됨)"),
    "大同團結": ("대동단결", "여러 집단이나 사람이 어떤 목적을 이루려고 크게 한 덩어리로 뭉침"),
    "同床異夢": ("동상이몽", "겉으로는 같이 행동하면서도 속으로는 각각 딴생각을 하고 있음"),
    "咸興差使": ("함흥차사", "심부름을 간 사람이 소식이 아주 없거나 또는 회답이 좀처럼 오지 않음."),
    "烏飛梨落": ("오비이락", "우연의 일치로 의심을 받음. 아무 관계도 없이 한 일이 공교롭게도 때가 같아 억울하게 의심을 받거나 난처한 위치에 서게 됨"),
    "瓜田不納履 / 李下不整冠": ("과전불납리 / 이하부정관", "남의 의심을 받을 짓을 하지 말라"),
    "袖手傍觀": ("수수방관", "팔짱을 끼고 보고만 있다(간섭하거나 거들지 아니하고 그대로 버려둠)"),
    "過猶不及": ("과유불급", "정도를 지나침은 미치지 못함과 같다는 뜻, 지나치거나 모자라지 않고 한쪽으로 치우치지 않는 상태가 중요하다는 말. 중용이 중요함을 가리키는 말"),
    "時時刻刻": ("시시각각", "각가의 시각. 시간이 흐르는 시각, 시간이 흐름에 따라"),
    "桃園結義": ("도원결의", "의형제를 맺음. 서로 다른 사람들이 사욕을 버리고 목적을 향해 합심할 것을 결의함"),
    "管鮑之交": ("관포지교", "우정이 아주 돈독한 친구 관계"),
    "金蘭之交": ("금란지교", "친구 사이의 매우 두터운 정, 우정의 견고함과 아름다움"),
    "芝蘭之交": ("지란지교", "벗 사이의 맑고도 고귀한 사귐"),
    "水魚之交": ("수어지교", "매우 친밀하게 사귀어 떨어질 수 없는 사이"),
    "膠漆之交": ("교칠지교", "아주 친밀하여 서로 떨어지지 않고 마음이 변하지 않는 두터운 우정"),
    "伯牙絶絃": ("백아절현", "자기를 알아주는 절친한 벗의 죽음을 슬퍼함"),
    "刎頸之交": ("문경지교", "생사를 같이할 만큼 매우 친한 사람이 또는 그런 친구"),
    "塞翁之馬": ("새옹지마", "인생의 길흉화복은 늘 바뀌어 변화가 많음(인생은 언제 어떻게 될지 알 수 없다)"),
    "用意周到": ("용의주도", "어떤일을 하려고 뜻을 세우고 마음을 가짐에 있어 준비가 두루 미쳐 빈틈이 없음(계획 단계에서부터 일의 마무리 단계 까지 두루 잘 행해진다)"),
    "孤軍奮鬪": ("고군분투", "따로 떨어져 도움을 받지 못하게된 군사가 많은 수의 적군과 용감하게 잘 싸운다(남의 도움을 받지 아니하고 힘에 벅찬 일을 잘해 나가는 것을 비유)"),
    "名實相符": ("명실상부", "알려진 것과 실제 내용이 일치함"),
    "美辭麗句": ("미사여구", "내용은 없으면서 아름다운 말로 듣기 좋게 꾸민 글귀"),
    "前代未聞": ("전대미문", "이제껏 들어 본 적이 없다는 뜻, 아주 놀랍고 획기적인 일을 이르는 말"),
    "未曾有": ("미증유", "전례가 없음"),
    "人生無常": ("인생무상", "사람의 일생이 덧없이 흘러감. 변화가 심하여 아무 보장이 없는 인생"),
    "一場春夢": ("일장춘몽", "헛된 영화나 덧없는 일(인생의 허무함을 비유)"),
    "邯鄲之夢": ("한단지몽", "세상의 부귀영화가 허황된(인생의 부귀영화는 일장 춘몽과 같이 허무함)"),
    "南柯一夢": ("남가일몽", "인생이나 부귀영화의 덧없음(꿈과 같이 헛된 한때의 부귀영화)"),
    "胡蝶之夢": ("호접지몽", "몰아일체의 경지 또는 현실과 꿈의 구별이 안되어 허무함"),
    "三三五五": ("삼삼오오", "서너 사람 또는 대여섯 사람이 떼를 지어다니거나 무슨 일을 함. 또는 그런 모양"),
    "多多益善": ("다다익선", "중국 한나라의 장수 한신이 고조와 장수의 역량에 대해 얘기할대 고조는 10만 정도의 병사를 지휘할 수 있는 그릇이지만, 자신은 변사의 수가 많을수록 잘 지휘할 수 있다고 한 말에서 유래"),
    "同苦同樂": ("동고동락", "괴로움도 즐거움도 함께함"),
    "各自圖生": ("각자도생", "제각기 살아 나갈 방법을 꾀함"),
    "莫逆之友": ("막역지우", "허물없이 아주 친한 친구"),
    "百年佳約": ("백년가약", "남녀가 결혼하여 평생을 함께 지낼것을 다짐하는 아름다운 언약"),
    "喜喜樂樂": ("희희낙락", "매우 기뻐하고 즐거워함"),
    "非一非再": ("비일비재", "같은 현상이나 일이 한두 번이나 한 둘이 아니고 많음"),
    "事必歸正": ("사필귀정", "모든 일은 결국에는 반드시 바른 길로 돌아가게 되어 있음"),
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
