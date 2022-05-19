import streamlit as st
import pandas as pd


# 이미지 처리를 위한 라이브러리
from PIL import Image


def main() :
    # 1. 저장되어 있는 이미지 파일을, 화면에 표시하기
    img = Image.open('data2/image_03.jpg')
    
    
    st.image(img)

    st.image(img,use_column_width=True)

    # 2. 인터넷 상에 있는 이미지를 화면에 표시하기
    # url이 있는 이미지를 말한다.
    url = 'https://cdn.vox-cdn.com/thumbor/sF-No75nHmF8wKTwJhixxIiIzB4=/0x0:1920x1080/1200x800/filters:focal(807x387:1113x693)/cdn.vox-cdn.com/uploads/chorus_image/image/70865372/Google_Pixel_Watch_1.0.png'
    st.image(url)


    # 3. 비디오 파일 표시하기
    video_file = open('data2/secret_of_success.mp4', 'rb')
    st.video(video_file)


    # 4. 오디오 파일 표시하기
    audio_file = open('data2/song.mp3', 'rb')
    st.audio( audio_file.read(), format= 'audio/mp3')



if __name__ == '__main__' :
    main()