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
    # 상관계수 차트 plt.scatter

    fig = plt.figure() # 이 함수 밑에는 차트영역이다. 라는 코드 
    plt.scatter(data = df , x ='sepal_length' , y ='sepal_width')
    plt.title('sepal_length vs sepal_width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    st.pyplot(fig) # 여기까지 차트를 그려라 라는 코드

    fig2 = plt.figure()
    sns.scatterplot(data = df , x ='sepal_length' , y ='sepal_width')
    st.pyplot(fig2)

    # 상관계수차트에서 선을 그어주는 차트
    # regplot
    fig3 = plt.figure()
    sns.regplot(data = df , x ='sepal_length' , y ='sepal_width')
    st.pyplot(fig3)

    
    # 히스토그램 sepal_length로 bin의 개수는 20
    # df에서 한개의 컬럼의 갯수분포 세주는 함수

    fig4 = plt.figure()
    plt.hist(data = df , x ='sepal_length', bins= 20, rwidth= 0.8)
    st.pyplot(fig4)
    
    
    # sepal_length 히스토그램
    # bin의 갯수를 10개와 20개로
    # 두개의 차트를 수평으로 보여주기
    # plt.subplot(1,2,1)
    # plt.subplot(1,2,2)


    fig5 = plt.figure(figsize= (10,4))
    plt.subplot(1,2,1)
    plt.hist(data = df , x ='sepal_length', bins= 10, rwidth= 0.8)
    
    plt.subplot(1,2,2)
    plt.hist(data = df , x ='sepal_length', bins= 20, rwidth= 0.8)
    st.pyplot(fig5)
    

    # species가 각각 몇개의 종씩 있는지 그려라
    # 한개의 컬럼안에 들어있는 카테고리들의 갯수를 세는차트는 countplot
    fig6 = plt.figure(figsize= (3,2))
    sns.countplot(data = df, x = 'species' )
    st.pyplot(fig6)
    
    # 지금까지 한건, plt와 seaborn 차트를 streamlit에 그리는 방법

    # 데이터프레임뒤에 바로 쓸수있게 제공하는 차트함수도 streamlit에 그릴수 있다.

    # species 는 각각 몇개인지 데이터프레임의 차트로 그리는 방법
    # df.value_counts().plot()
    fig7 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig7)


    # sepal_length 컬럼을 히스토그램으로!
    # df.hist()
    fig8 = plt.figure()
    df['sepal_length'].hist(bins=40)
    st.pyplot(fig8)

    




if __name__ == '__main__' :
    main()