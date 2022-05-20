## 파일을 분리해서 만드는 앱 ##
## 개발할때 코드 수정의 시간을 단축시키기 위해서 한다.

import pandas as pd
import streamlit as st

from app9_home import run_home
from app9_eda import run_eda
from app9_ml import run_ml
from app9_about import run_about

def main() :
    st.title('파일 분리 앱')

    menu = ['Home', 'EDA', 'ML', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)

    # pass 하나당 파일을 따로 만들어서 작업하겠다
    # def로 정의한 함수를 불러오려면 run_home치면 나오는 auto-import를 눌러준다.
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()
    elif choice == menu[3] :
        run_about()



if __name__ == '__main__' :
    main()
