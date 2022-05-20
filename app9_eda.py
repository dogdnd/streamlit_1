import streamlit as st
from PIL import Image
import pandas as pd

def run_eda() :
    st.subheader('EDA 화면')

    df = pd.read_csv('data2/iris.csv')

    # 컬럼이름 보여주시고
    # 여러 컬럼들 선택 가능토록 하여,
    # 선택한 컬럼들만 화면에 보여줍니다.

    column_list = st.multiselect('컬럼 선택', df.columns)
    # 아무것도 선택안했을때 이상한 데이터프레임이 나오지 않게 하기
    # 리스트니까 비어있는 경우는 길이가 0일때로 조건문을 써준다.
    if len(column_list) != 0 :
        st.dataframe(df[column_list])


    # 상관계수를 구하여 화면에 보여줍니다.

    if len(column_list) != 0 :
        st.dataframe(df[column_list].corr())