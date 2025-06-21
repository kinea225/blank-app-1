import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import koreanize_matplotlib
import pandas as pd
from IPython.display import display
import plotly.express as px
import geopandas as gpd
import folium
from folium.features import GeoJsonTooltip
from streamlit_folium import st_folium
import altair as alt

st.set_page_config(page_title="산불 발생 시기/시간대/피해 분석", layout="wide")

option2 = ["경기도", "서울", "부산", "인천", "경상남도", "경상북도", "대구",
    "충청남도", "전라남도", "전라북도", "충청북도", "강원도", "대전", "광주",
    "울산", "세종"]
#산불 가져오고 데이터 전처리
@st.cache_data
def dataPreprocessing():
    #데이터 가져오기
    file = pd.read_csv('fire.csv',encoding='cp949')
    fire = pd.DataFrame(file)
    #지워야할 데이터
    del1 = ['발생일시_년','발생일시_월','발생일시_일','발생일시_시간','발생일시_요일','진화종료시간_년','진화종료시간_월','진화종료시간_일','진화종료시간_시간','발생장소_동리','발생장소_읍면',"발생장소_관서"]
    for i in fire.columns:
        if i in del1:
            fire.drop(i,axis=1, inplace=True)
        else:
            try:
                for j in fire[i]:
                    j.replace(" ","",inplace=True)
            except:
                print()
        del2 = i[i.index('_')+1:]
        fire.rename(columns={i:del2},inplace=True)
    fire.fillna("",inplace=True)
    fire['구분'].replace("",'기타',inplace=True)    
    return fire

index_list=['기','기타','담','쓰','입']
@st.cache_data
def local(data1,lo):
    data = data1
    if not lo:
        for i in data.columns:
            data[i] = 0
    else:
        join = '|'.join(lo)
        data = data[data['시도'].str.contains(join)].sort_values(by=['시도'])
    return data

@st.cache_data
def local2(data1, lo):
    data = [None] * (len(lo) + 1)
    cnt = 0
    for i in lo:
        grouped = data1[data1['시도'].str.contains(i)].groupby(['구분']).agg(
            발생건수=('합계', 'count'),
            평균피해면적=('합계', 'mean'),
            피해면적합계=('합계', 'sum')
        ).reset_index()
        # 구분값 누락된 것 추가
        grouped = grouped.set_index('구분').reindex(index_list, fill_value=0).reset_index()
        data[cnt] = grouped
        cnt += 1
    return data
def local3(data1):
    data = data1
    data =data.groupby(['세부원인','기타']).agg(
        건수 = ('합계','count'),
        평균피해면적=('합계', 'mean')
    ).reset_index().sort_values(by=['건수'],ascending=False)
    return data
def chart(cause_group):
    st.subheader("원인 구분별 산불 건수 및 평균 피해면적")
    fig, ax1 = plt.subplots(figsize=(16,3))
    ax2 = ax1.twinx()
    bars=ax1.bar(cause_group['구분'], cause_group['발생건수'], color='orange', alpha=0.7, label='발생건수')
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}건'))  # y축 건수 포맷
    ax2.plot(cause_group['구분'], cause_group['평균피해면적'], color='red', marker='o', label='평균피해면적')
    ax1.set_xlabel("구분")
    ax1.set_ylabel("건수")
    ax2.set_ylabel("평균 피해면적(ha)")
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))  # y축 비율 포맷
    plt.title("원인 구분별 산불 건수 및 평균 피해면적")
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.xticks(rotation=30)
    for bar, count in zip(bars, cause_group['발생건수']):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height()/2, str(count)+'건', 
                ha='center', va='bottom', fontsize=12, color='black', fontweight='bold')
    for i, txt in enumerate(cause_group['평균피해면적']):
        ax2.text(cause_group['구분'][i], cause_group['평균피해면적'][i] + 0.5, f'{txt:.1f}%', ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')
    st.pyplot(fig)

#지역별 비교
def chart2(cause_group2):
    try:
        df_list = []
        for i, df in enumerate(cause_group2):
            if df is not None and not df.empty:
                temp_df = df.copy()
                temp_df['x'] = x  # 각 그룹에 동일한 x값 적용 (x의 길이가 df와 일치해야 합니다)
                temp_df['group'] = option2[i]  # 범례에 표시될 그룹명
                df_list.append(temp_df)

        # 모든 데이터를 하나의 DataFrame으로 합칩니다.
        df_all = pd.concat(df_list, ignore_index=True)

        # Plotly Express로 라인 차트 생성 (markers=True로 각 데이터 포인트에도 마커 표시, text 인자를 이용해 값 표시)
        fig = px.line(
            df_all,
            x='x',
            y='발생건수',
            color='group',
            markers=True,
            text='발생건수'
        )

        # 각 데이터 포인트의 텍스트 위치를 위쪽 가운데로 조정
        fig.update_traces(textposition='top center',textfont_size=14)

        # 모든 라인의 스타일을 점선으로 변경
        for trace in fig.data:
            trace.line.dash = 'solid'

        # 레이아웃 설정: 그림 크기, y축 제목, 격자선, 여백 등
        fig.update_layout(
            title="지역별 산불 원인 구분별 발생 건수 비교",
            width=1600,
            height=400,
            yaxis_title="발생건수",
            xaxis_title="",
            template="simple_white",  # 깔끔한 배경과 격자선을 제공합니다.
            margin=dict(l=50, r=50, t=50, b=50),
        )

        # y축 하한을 0으로 설정하고 격자선 스타일 지정
        fig.update_yaxes(rangemode="tozero", gridcolor='lightgray', gridwidth=1)

        st.plotly_chart(fig)
    except:
        st.write('조회되는 데이터가 없습니다.')

# 연도별 인구 차이를 계산하는 함수
def calculate_population_difference(input_df,input_df2, input_div):
    # 선택한 발생건수의 데이터 추출
    if input_df2 is not None :
        selected_year_data = input_df[input_df['구분'] == input_div].reset_index()
        # 지역별 데이터 추출
        previous_year_data = input_df2[input_df2['구분'] == input_div].reset_index()
        previous_year_data['건수백분'] = (previous_year_data['발생건수']/selected_year_data['발생건수'])*100
        selected_year_data['건수백분'] = (selected_year_data['발생건수']/selected_year_data['발생건수'])*100
        # 이전 연도 대비 인구 차이 계산
        selected_year_data['건수조정'] = abs(previous_year_data.건수백분.sub(
            selected_year_data.건수백분, fill_value=0).astype(int))
    else: 
        selected_year_data['건수백분'] = 100
        # 결과로 states, id, population, population_difference를 포함한 데이터프레임 반환
    return pd.concat([
        selected_year_data.구분,
        selected_year_data.발생건수,
        selected_year_data.건수조정
    ], axis=1).sort_values(by="건수조정", ascending=False)

# 도넛형 차트를 생성하는 함수 (Altair 사용)
colorborn = ['blue','green','orange','red','alpha']
def make_donut(input_response, input_text, input_color):
    # 입력된 색상에 따라 차트 색상 정의
    if input_color == 'blue':
        chart_color = ['#29b5e8', '#155F7A']
    if input_color == 'green':
        chart_color = ['#27AE60', '#12783D']
    if input_color == 'orange':
        chart_color = ['#F39C12', '#875A12']
    if input_color == 'red':
        chart_color = ['#E74C3C', '#781F16']
    if input_color == 'alpha':
        chart_color = ['#455345', '#233123']
    
    # 도넛 차트의 전경 (사용자 값 포함)
    source = pd.DataFrame({
        "Topic": [input_text],               # 공백은 빈 영역을 의미함
        "% value": [input_response]
    })

    # 배경 차트 (100% 회색 배경용)
    source_bg = pd.DataFrame({
        "Topic": ['', input_text],
        "% value": [100, 0]  # 전경이 없고 전체가 빈 값
    })

    # 전경 도넛 차트 생성
    plot = alt.Chart(source).mark_arc(
        innerRadius=45, cornerRadius=20
    ).encode(
        theta="% value",  # 비율로 각도 설정
        color=alt.Color("Topic:N",
                        scale=alt.Scale(
                            domain=[input_text, ''],
                            range=chart_color),
                        legend=None)
    ).properties(width=150, height=150)

    # 가운데 텍스트 표시
    text = plot.mark_text(
        align='center', color="#29b5e8",
        font="Lato", fontSize=32,
        fontWeight=700, fontStyle="italic"
    ).encode(text=alt.value(f'{input_response} %'))

    # 배경 도넛 차트 생성
    plot_bg = alt.Chart(source_bg).mark_arc(
        innerRadius=45, cornerRadius=20
    ).encode(
        theta="% value",
        color=alt.Color("Topic:N",
                        scale=alt.Scale(
                            domain=[input_text, ''],
                            range=chart_color),
                        legend=None)
    ).properties(width=150, height=150)

    # 배경 + 전경 + 텍스트 차트 결합 후 반환
    return plot_bg + plot + text

#-----------------------------------------------------------------------------
#구분선
#_----------------------------------------------------------------------------

firePs = dataPreprocessing()
title = ['원인 구분 별 데이터 표','원인 구분 별 차트','지역별 원인 구분 차트']
#상위 메뉴
col = st.columns([2,2,5])
with col[0]:
    st.title("산불발생원인")
    st.subheader('지역을 골라주세요')
with col[1]:
    # cval = st.checkbox('데이터 표 보기')
    # cval2 = st.checkbox('차트 보기')
    mval2 = st.multiselect('',title, default=title)
with col[2]:
    mval=st.multiselect('',option2,default=option2)

#중간 콘텐츠
#데이터 보관
cause_group = local(firePs,mval).groupby('구분').agg(
        발생건수=('합계', 'count'),
        평균피해면적=('합계', 'mean'),
        피해면적합계=('합계', 'sum')
    ).reset_index().sort_values('평균피해면적', ascending=False)
cause_group2 = local2(firePs,mval)
cause_group3 = local3(firePs)

donut = local(firePs,mval).groupby('구분').agg(
        발생건수=('합계', 'count'),
        평균피해면적=('합계', 'mean'),
        피해면적합계=('합계', 'sum')
    ).reset_index().sort_values('평균피해면적', ascending=False)
donut2 = firePs.groupby('구분').agg(
        발생건수=('합계', 'count'),
        평균피해면적=('합계', 'mean'),
        피해면적합계=('합계', 'sum')
    ).reset_index().sort_values('평균피해면적', ascending=False)

column_config = {
    '세부원인': st.column_config.TextColumn(
        "세부원인",
        help="세부원인",
        width='medium' # small, medium, large
    ),
    '기타': st.column_config.TextColumn(
        "기타",
        help="설명",
        width='medium'
    ),
    '건수': st.column_config.NumberColumn(
        "건수",
        help="세부 원인별 건수",
        width='large'
    )
}
x = index_list
col2 = st.columns([3,8])
with col2[0]:
    elect = cause_group3[cause_group3['기타'].isin(['낙뢰'])].rename(columns={'기타':'자연피해'})
    elect2 = cause_group3['기타'].count()
    
    df_top_area = cause_group3[
    (~cause_group3['기타'].isin(["미상"])) & (~cause_group3['기타'].str.startswith('입산자'))
    ].head(10)

    st.markdown('상위 산불 발생 원인(입산자로 인한 산불은 제외)')
    st.dataframe(
        df_top_area,
        column_order=("기타", "건수"),
        hide_index=True,
        column_config={
            "기타": st.column_config.TextColumn("기타"),
            "건수": st.column_config.ProgressColumn(
                "건수",
                format="%.2f",
                min_value=0,
                max_value=float(df_top_area['건수'].max()),
            ),
        },height=388
    )
    st.subheader('자연적으로 피해를 입는 경우')
    st.dataframe(
        elect,
        column_order=("자연피해", "건수"),
        hide_index=True,
        column_config={
            "자연피해": st.column_config.TextColumn("자연피해"),
            "건수": st.column_config.ProgressColumn(
                "건수",
                format="%.2f",
                min_value=0,
                max_value=float(df_top_area['건수'].max()),
            ),
        },height=75
    )
    st.subheader('구분에 따른 지역별 건수 비율')
    col3 = st.columns([1,1])
    
    for i in range(0,len(index_list)):
        with col3[i%2]:
            st.markdown(index_list[i]+'에 대한 건수 비율')
            a= calculate_population_difference(donut2,donut,index_list[i])
            if not a.empty:
                b= a['건수조정'][0]
            st.altair_chart(make_donut(100-b,'건수조정',colorborn[i]), use_container_width=True)
    with col3[1]:
            st.markdown('자연피해 낙뢰에 대한 건수 비율')
            a=  ((elect['건수'][253]/elect2)*100).astype(int)
            b= a
            st.altair_chart(make_donut(b,'건수조정','blue'), use_container_width=True)
with col2[1]:
    if title[0] in mval2:
        st.title('가장 많이 일어나는 산불 발생 원인 상위 10개 입니다.')
        st.markdown('상위 산불 발생 원인(입산자로 인한 산불 포함)')
        st.dataframe(cause_group3.set_index('세부원인').head(10),height=213, column_config = column_config)
    else :
        st.title("산불원인 구분에 따른 데이터 프레임입니다.")
        st.dataframe(cause_group.set_index('구분'), height=213)
    if title[1] in mval2:
        chart(cause_group)
    if title[2] in mval2:
        chart2(cause_group2)
