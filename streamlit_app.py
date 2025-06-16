import streamlit as st

st.set_page_config(page_title="프로젝트 작성", layout="wide")
# with st.sidebar.expander("마우스를 올리세요", expanded=True):
#     st.markdown("""
#     <div class="st-emotion-cache-4rp1ik">
#         <div class="st-emotion-cache-8atqhb">
#             <img src="https://cdn.pixabay.com/photo/2017/08/30/01/01/cat-2695560_1280.jpg" alt="Cat Image" width="100%">
#         </div>
#         <div class="st-emotion-cache-1clstc5">
#             <h2>고양이 사진</h2>
#             <p>이곳에 마우스를 올리면 고양이 사진이 나타납니다.</p> 
#             <p>이 사진은 Pixabay에서 가져온 것입니다.</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
# st.markdown("""
# <style> 
# .st-emotion-cache-4rp1ik{
#     position: relative; /* 자식 요소의 위치를 기준으로 설정 */
    
# }
# .st-emotion-cache-1clstc5{
#     opacity: 0;
#     transition: 0.3s ease-out;
            
# }
# .st-emotion-cache-8atqhb:hover .st-emotion-cache-1clstc5{
#     display: block;
#     opacity: 100%;
#             }
# </style>
# """,
# unsafe_allow_html=True)

# 스트림릿 배경

st.markdown(f"""
<style>
.stApp{{
        background-image: url("https://cdn.pixabay.com/photo/2024/05/30/19/37/girl-8799169_1280.jpg");
            background-attachment: fixed;
             background-size: cover;}}
.stAppHeader{{background-image:url("https://cdn.pixabay.com/photo/2024/05/30/19/37/girl-8799169_1280.jpg");
             background-attachment: fixed;
             background-size: cover}}
</style>
""", unsafe_allow_html=True)
st.markdown("""
            
            <style>
              @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
            .contents{
              font-family: "Jua", sans-serif;
              justify-content:center;
              position:absolute;
              backdrop-filter:blur(10px);
              width:100%;
              height:845px;
              text-align:center;
              border-radius:20px;
              box-shadow: 0px 0px 15px #010101;
            }
            .contents h1{
              text-align: center;
            }
            img{
              width:100%;
              height:100%;
            }
            .slider {
              width: 100%;
              height: 500px;
              overflow: hidden;
              position: relative;
              
            }
            .slides {
                display: flex;
                width: 50%;
                animation: slide 6s infinite;
                
            }

            .slides img {
                width: 100%;
                height:500px;
                opacity:0.94;
            }

            @keyframes slide {
                0% { transform: translateX(0); }
                33% { transform: translateX(-100%); }
                66% { transform: translateX(-200%); }
                100% { transform: translateX(0); }
            }
            .head-menu{
              width:100%;
              height:75px;
              border-radius:20px 20px 0px 0px;
              background-color:#F5DCB7;
              opacity:0.9;
              position:relative;
              
            }
            .footer-contents{
              width:100%;
              height:75px;
              background-color:#F5DCB7;
              border-radius: 0px 0px 20px 20px;
              opacity:0.9;
            }
            .middle-contents{
              width:100%;
              height:195px;
              background:linear-gradient(to bottom,#F7F0E9,#F5DCB7);
              border-radius: 1px;
              opacity:0.9;
            }
            .head-menu div{
              margin-top:1px;
              display:inline-block;
              opacity: 0.7;
              backdrop-filter: blur(20px);
              padding : 20px;
              height:73px;
            }
            .head-menu div a{
              color: black;
              font-size: 1.4rem;
              font-weight: bold;
            }
            .head-menu div:hover{
              display:inline-block;
              margin:-2px;
              box-shadow: 0px 0px 7px #9f8473;
              background-color:#FBE5BC;
              padding : 20px;
              opacity: 1;
            }
            .middle-contents{
              text-align:left;
            }
            .middle-contents div{
              padding:0;
              margin:2px;
              width:48%;
              height:195px;
              display:inline-block;
            }
            .middle-contents div ul{
              text-align: center;
              width:100%;
            }
            .middle-contents div ul p{
              color:black;
              font-size:30px;
              font-weight:bold;
              margin:0px;
            }
            .middle-contents div ul li a{
              color:black;
              font-size:18px;
            }
            .middle-contents div ul li a:hover{
              color:black;
              font-size:19px;
              font-weight:bold;

            }
            .footer-contents> p{
              display:inline-block;
              align-items:center;
              padding:15px;
              font-size:30px;
              font-weight:bold;
              color: black;
              text-shadow: 0px 0px 10px beige;
            }
            .icon{
              width:75px;
              height:75px;
              position:absolute;
            }
            </style>
            <div class="contents">
              <div class="head-menu">
                <div><a herf="https://bobtong-sub-one.streamlit.app/" target="_self">비교 자료보기</a></div>
                <div><a herf="https://bobtong-sub-two.streamlit.app/" target="_self">발생위치 보기</a></div>
                <div><a herf="https://bobtong-sub-three.streamlit.app/" target="_self">지역별 건수 보기</a></div>
                <div><a herf="https://bobtong-sub-four.streamlit.app/" target="_self">연도별 건수 보기</a></div>
              </div>
              <div class="slider">
                  <div class="slides">
                      <img src="https://cdn.pixabay.com/photo/2015/08/19/05/17/large-895567_1280.jpg" alt="publicdata">
                      <img src="https://cdn.pixabay.com/photo/2024/08/30/08/24/ai-generated-9008727_1280.jpg" alt="data scientist">
                      <img src="https://cdn.pixabay.com/photo/2018/05/04/23/31/grass-3375344_1280.jpg" alt="forestfire">
                  </div>
              </div>
              <div class="middle-contents">
                 <div>
                  <ul>
                    <li><p>[공공 데이터 활용하기]</p>
                    <li>
                        <a href ="https://www.data.go.kr/"> 공공 데이터 가져오기</a>
                      </li>
                      <li>
                        <a href ="https://wikidocs.net/book/7188"> pandas 공부하기(위키독스) </a>
                      </li>
                      <li>
                        <a href="https://colab.google/">활용환경</a>
                      </li>
                      <li>
                        <a href ="https://pandas.pydata.org/docs/user_guide/index.html"> 참고 사이트</a>
                      </li>
                    </li>
                  </ul>
                </div>
                <div>
                  <ul>
                    <li><p>[streamlit 공부하기]</p>
                      <li>
                        <a href ="https://streamlit.io/"> 대시보드 만들기</a>
                      </li>
                      <li>
                        <a href ="https://wikidocs.net/book/17846"> streamlit(위키독스) </a>
                      </li>
                      <li>
                        <a href="https://github.com/">활용환경</a>
                      </li>
                      <li>
                        <a href ="https://docs.streamlit.io/develop/api-reference"> 참고 사이트</a>
                      </li>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="footer-contents">
                <p>기말 과제 streamlit을 이용한 데이터 분석 대시보드 만들기!</p>
                <p>--[팀원: 남경태, 김태홍, 이도영]--</p>
              </div>  
            </div>
""", unsafe_allow_html=True)
# 사이드 바
st.markdown("""
<style>
/* 노멀라이즈 시작 */
body, ul, li {
  margin: 0;
  padding: 0;
  list-style: none;   	    /* 해당 태그의 list-style을 none으로 하는 것으로 ●을 제거한다 */
}

a {
  color: inherit;   	    /* 부모 엘리먼트의 값을 물려받는다 */
  text-decoration: none !important;    /* 해당 태그의 text-decoration 속성을 none 값으로 하는 것으로 밑줄을 제거한다 */
}
/* 노멀라이즈 끝 */
/* 2차 이상의 메뉴를 숨기기 */
.side-bar > ul ul {
  display: none;
}

/* 사이드바의 너비와 높이를 변수를 통해 통제 */
:root {
  --side-bar-width: 270px;
  //--side-bar-height: 90vh;
}
aside ul {
    margin-top: 20%;}
.side-bar {
  position: fixed;    /* 스크롤을 따라오도록 지정 */
  background-image: url("https://cdn.pixabay.com/photo/2021/12/01/21/32/mountains-6839168_1280.jpg");
  background-size: cover;
  background-position: right center;    /* 배경 이미지의 위치를 오른쪽 중앙으로 지정 */
  width: var(--side-bar-width);
  min-height: 80%;   /* 사이드바의 높이를 전체 화면 높이의 90%로 지정 */
  //margin-top: calc((100vh - var(--side-bar-height)) / 2);    /* 사이드바 위와 아래의 마진을 동일하게 지정 */
}

/* 모든 메뉴의 a에 속성값 부여 */
.side-bar ul > li > a {
  display: block;
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 50px;
}
/* 자식의 position이 absolute일 때 자식을 영역 안에 가두어 준다 */
.side-bar > ul > li {
  margin: 0;
  padding: 0;
  position: relative;
}

/* 모든 메뉴가 마우스 인식 시 반응 */
.side-bar ul > li:hover > a {
  backdrop-filter:blur(10px);    /* 배경 흐림 효과 */;
  border: 0.2px solid gray;
}

/* 사이드바 너비의 80%만큼 왼쪽으로 이동 */
.side-bar {
  box-shadow: 0px 0px 30px black;
  border-radius: 20px;
  transform: translate(calc(var(--side-bar-width) * -1), 0);  /* X축 이동, Y축 고정 */
  transition: .5s;
}

/* 마우스 인식 시 원래의 위치로 이동 */
.side-bar:hover {
  transform: translate(-30px, 0);   /* 둥근 모서리의 너비만큼 X축 이동, Y축 고정 */
}
.side-bar_footer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 20px;
  background-color: rgba(0, 0, 0, 0.2); /* 반투명 배경 */
  color: white;
  text-align: left;
}
.side-bar_footer >.information {
    text-align: center;
    margin-top: 20px;
    font-size: 0.8rem;
    color: lightgray;
}
</style>
<aside class="side-bar">
  <section class="side-bar__icon-box">
    <section class="side-bar__icon-1">
      <div></div>
      <div></div>
      <div></div>
    </section>
  </section>
  <ul>
    <li>
      <a href="https://bobtong-sub-one.streamlit.app/" target="_self"><i class="fa-solid fa-cat"></i>비교 자료보기</a>
    </li>
    <li>
      <a href="https://bobtong-sub-two.streamlit.app/" target="_self">발생위치 보기</a>
    </li>
    <li>
      <a href="https://bobtong-sub-three.streamlit.app/" target="_self">지역별 건수 보기</a>
    </li>
    <li>
      <a href="https://bobtong-sub-four.streamlit.app/" target="_self">연도별 건수 보기</a>
    </li>
  </ul>
  <div class="side-bar_footer">
    <p>팀명 : 밥통</p>
    <p>팀원 : 남경태, 김태홍, 이도영</p>
    <p>주제 : 산불 발생 현황</p>         
    <p class="information">© 22~23년 산불 발생 현황</p>
  </div>
</aside>

""",
    unsafe_allow_html=True
)
