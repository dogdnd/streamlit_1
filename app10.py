import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    st.title('차트 그리기 1')

    df = pd.read_csv('data2/iris.csv')

    st.dataframe( df )

    # 차트 그리기
    # sepal_length 와 sepal_width 의 관계를
    # 차트로 나타내시오

    plt.scatter(df[sepal_length] , df[sepal_width] )





if __name__ == '__main__' :
    main()