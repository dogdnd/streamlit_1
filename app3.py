# 스트림릿 라이브러리를 사용하기 위한 임포트
import streamlit as st
import pandas as pd
# 웹 대시보드 개발 라이브러리인, 스트림릿은,
# main 함수가 있어야 한다.

def main() :
    df = pd.read_csv('data2/iris.csv')

    st.dataframe(df)

    species = df['species'].unique()

    st.text('아이리스 꽃은 ' + species + '으로 되어있다.')



if  __name__ == '__main__' :
    main()