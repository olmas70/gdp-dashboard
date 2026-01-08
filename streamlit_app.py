import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime, time
import time as time_module

# 페이지 설정: 브라우저 탭에 표시되는 제목과 아이콘을 설정합니다.
st.set_page_config(
    page_title='Streamlit Elements Showcase',
    page_icon=':rocket:',
    layout='wide'  # 전체 너비 레이아웃 사용
)

# 메인 타이틀: 페이지의 주요 제목을 표시합니다.
st.title('🚀 Streamlit Elements Showcase')

# 서브헤더: 섹션을 나누는 데 사용됩니다.
st.subheader('이 페이지는 Streamlit의 다양한 요소들을 보여줍니다.')

# 텍스트 요소 섹션
st.header('📝 텍스트 요소', divider='blue')

# 일반 텍스트: 단순한 텍스트를 표시합니다.
st.text('이것은 st.text()로 표시된 일반 텍스트입니다.')

# 마크다운: 마크다운 형식을 지원합니다.
st.markdown('''
### 마크다운 예시
- **굵은 글씨**
- *기울임 글씨*
- `코드`
- [링크](https://streamlit.io)
''')

# LaTeX 수식: 수학 수식을 표시합니다.
st.latex(r'''
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
''')

# 코드 블록: 코드 스니펫을 표시합니다.
st.code('''
def hello_world():
    print("Hello, World!")
''', language='python')

# write: 다양한 데이터 타입을 자동으로 표시합니다.
st.write('st.write()는 텍스트, 데이터프레임, 차트 등을 자동으로 렌더링합니다.')
st.write(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}))

# 데이터 표시 요소 섹션
st.header('📊 데이터 표시 요소', divider='green')

# 데이터프레임: 판다스 데이터프레임을 인터랙티브하게 표시합니다.
df = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'])
st.dataframe(df)

# 테이블: 정적 테이블로 표시합니다.
st.table(df.head())

# JSON: JSON 데이터를 표시합니다.
st.json({'key': 'value', 'list': [1, 2, 3]})

# 메트릭: KPI를 표시합니다.
st.metric(label="온도", value="70 °F", delta="1.2 °F")

# 입력 위젯 섹션
st.header('🎛️ 입력 위젯', divider='orange')

# 버튼: 클릭 가능한 버튼입니다.
if st.button('클릭하세요'):
    st.write('버튼이 클릭되었습니다!')

# 체크박스: 참/거짓 값을 입력받습니다.
agree = st.checkbox('동의합니다')
if agree:
    st.write('동의하셨습니다.')

# 라디오 버튼: 여러 옵션 중 하나를 선택합니다.
genre = st.radio(
    "좋아하는 장르를 선택하세요",
    ('코미디', '드라마', '다큐멘터리'))

# 셀렉트박스: 드롭다운 메뉴입니다.
option = st.selectbox(
    '어떤 옵션을 선택하시겠습니까?',
    ('옵션 1', '옵션 2', '옵션 3'))

# 멀티셀렉트: 여러 옵션을 선택할 수 있습니다.
options = st.multiselect(
    '여러 옵션을 선택하세요',
    ['녹색', '노란색', '빨간색', '파란색'],
    ['녹색', '노란색'])

# 슬라이더: 숫자 범위를 선택합니다.
age = st.slider('나이를 선택하세요', 0, 130, 25)

# 셀렉트 슬라이더: 옵션 리스트에서 범위를 선택합니다.
color = st.select_slider(
    '색상을 선택하세요',
    options=['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라'])

# 텍스트 입력: 한 줄 텍스트를 입력받습니다.
title = st.text_input('영화 제목', '스타워즈')

# 텍스트 영역: 여러 줄 텍스트를 입력받습니다.
text = st.text_area('자기소개', '여기에 입력하세요...')

# 숫자 입력: 숫자를 입력받습니다.
number = st.number_input('숫자를 입력하세요', min_value=0.0, max_value=100.0, value=50.0)

# 날짜 입력: 날짜를 선택합니다.
d = st.date_input("생일", datetime.date(2019, 7, 6))

# 시간 입력: 시간을 선택합니다.
t = st.time_input('회의 시간', time(8, 45))

# 파일 업로더: 파일을 업로드합니다.
uploaded_file = st.file_uploader("파일을 선택하세요")
if uploaded_file is not None:
    st.write("파일이 업로드되었습니다:", uploaded_file.name)

# 미디어 요소 섹션
st.header('🎥 미디어 요소', divider='purple')

# 이미지: 이미지를 표시합니다.
st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', caption='Streamlit 로고')

# 오디오: 오디오 파일을 재생합니다.
# st.audio('path/to/audio.mp3')  # 실제 파일 경로 필요

# 비디오: 비디오 파일을 재생합니다.
# st.video('path/to/video.mp4')  # 실제 파일 경로 필요

# 차트 요소 섹션
st.header('📈 차트 요소', divider='red')

# 라인 차트: 선 그래프를 표시합니다.
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# 바 차트: 막대 그래프를 표시합니다.
st.bar_chart(chart_data)

# 영역 차트: 영역 그래프를 표시합니다.
st.area_chart(chart_data)

# 산점도: 산점도를 표시합니다.
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})
st.scatter_chart(scatter_data, x='x', y='y', color='category')

# 지도: 지도에 데이터를 표시합니다.
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

# Matplotlib 차트: matplotlib을 사용하여 커스텀 차트를 표시합니다.
fig, ax = plt.subplots()
ax.hist(np.random.normal(0, 1, 1000), bins=50)
st.pyplot(fig)

# Plotly 차트: Plotly를 사용하여 인터랙티브 차트를 표시합니다.
plotly_fig = px.scatter(x=np.random.randn(100), y=np.random.randn(100))
st.plotly_chart(plotly_fig)

# 레이아웃 요소 섹션
st.header('🏗️ 레이아웃 요소', divider='gray')

# 컬럼: 페이지를 여러 컬럼으로 나눕니다.
col1, col2, col3 = st.columns(3)
with col1:
    st.header("컬럼 1")
    st.write("첫 번째 컬럼입니다.")
with col2:
    st.header("컬럼 2")
    st.write("두 번째 컬럼입니다.")
with col3:
    st.header("컬럼 3")
    st.write("세 번째 컬럼입니다.")

# 컨테이너: 요소들을 그룹화합니다.
with st.container():
    st.write("컨테이너 내부입니다.")
    st.button("컨테이너 안의 버튼")

# 사이드바: 사이드바에 요소를 배치합니다.
with st.sidebar:
    st.header("사이드바")
    st.write("이것은 사이드바입니다.")
    sidebar_option = st.selectbox("사이드바 옵션", ["A", "B", "C"])

# 탭: 탭으로 콘텐츠를 나눕니다.
tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])
with tab1:
    st.header("탭 1")
    st.write("첫 번째 탭의 콘텐츠입니다.")
with tab2:
    st.header("탭 2")
    st.write("두 번째 탭의 콘텐츠입니다.")
with tab3:
    st.header("탭 3")
    st.write("세 번째 탭의 콘텐츠입니다.")

# 폼: 입력 요소들을 그룹화하여 한 번에 제출합니다.
with st.form("my_form"):
    st.write("폼 내부")
    slider_val = st.slider("폼 슬라이더", 0, 100, 50)
    checkbox_val = st.checkbox("폼 체크박스")
    submitted = st.form_submit_button("제출")
    if submitted:
        st.write("폼이 제출되었습니다!")

# 상태 및 기타 요소 섹션
st.header('🔄 상태 및 기타 요소', divider='rainbow')

# 프로그레스 바: 진행 상황을 표시합니다.
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time_module.sleep(0.01)

# 스피너: 작업 중임을 표시합니다.
with st.spinner('작업 중...'):
    time_module.sleep(1)
st.success('완료되었습니다!')

# 알림 메시지: 성공, 정보, 경고, 오류 메시지를 표시합니다.
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("오류 메시지")

# 예외: 예외를 표시합니다.
try:
    1 / 0
except ZeroDivisionError as e:
    st.exception(e)

# 빈 요소: 나중에 채울 수 있는 플레이스홀더입니다.
placeholder = st.empty()
placeholder.text("이것은 빈 요소입니다.")
# 나중에 업데이트 가능: placeholder.text("업데이트된 텍스트")

# 세션 상태: 앱의 상태를 유지합니다.
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('카운터 증가'):
    st.session_state.counter += 1

st.write(f"카운터: {st.session_state.counter}")

# 종료 메시지
st.header('🎉 끝났습니다!')
st.write('이 페이지에서 Streamlit의 주요 요소들을 모두 살펴보았습니다.')
