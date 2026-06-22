import streamlit as st
import pandas as pd

df = pd.read_csv("heart_failure.csv")

# st.subheader(" 환자 데이터")
# st.dataframe(df.head())

# st.metric(
#     label="전체 환자 수",
#     value=f"{len(df)}명",
#     delta="299건 수집")

# import streamlit as st
# import pandas as pd
# df = pd.read_csv("heart_failure.csv")
# age_max = st.slider("최대 나이", 40, 95, 70)
# filtered = df[df['age'] <= age_max]
# st.write(f"{len(filtered)}명이 조건에 맞아요")
# st.dataframe(filtered)

# choice = st.selectbox(
#     "성별",["남성","여성"])
# code = 1 if choice == "남성" else 0
# result = df[df['sex'] == code]
# st.write(f"{len(result)}명")
# st.dataframe(result)

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.rcParams['axes.unicode_minus'] = False
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("heart_failure.csv")

# fig, ax = plt.subplots()
# ax.hist(df['age'],bins=20,
#         color='#5BAFB8')
# ax.set_xlabel("나이" "age")
# ax.set_ylabel("환자 수")

# st.pyplot(fig)


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# df= pd.read_csv("heart_failure.csv")

# fig, ax = plt.subplots()

# count = df["DEATH_EVENT"].value_counts()

# ax.bar(["생존","사망"], [count[0], count[1]])

# ax.set_title("생존자와 사망자 수")

# st.pyplot(fig)

# import streamlit as st
# import pandas as pd
# df = pd.read_csv("heart_failure.csv")
# # 왼쪽 사이드바에 필터를 둔다
# st.sidebar.header(" 필터")
# age = st.sidebar.slider("최대 나이",
# 40, 95, 70)
# df = df[df['age'] <= age]
# # 본문을 둘로 나눈다
# c1, c2 = st.columns(2)
# c1.metric("환자 수", len(df))
# c2.metric("평균 나이", f"{df.age.mean():.0f}")



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("heart_failure.csv")

st.sidebar.header(" 필터")

tab1, tab2 = st.tabs(["표", "차트"])
with tab1:
    st.dataframe(df)

with tab2:
    fig, ax = plt.subplots()
    ax.hist(df['age'])
    st.pyplot(fig)