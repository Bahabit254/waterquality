from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import sklearn
import plotly
import plotly.express as px
import joblib
st.set_page_config(layout="wide")


def main():
    filename = 'random_forest.pkl'
    model_loaded = joblib.load(filename)
    
    st.title('Water Potability Analysis')
    @st.cache
    def data_reader():
        df = pd.read_csv('new_water_data.csv')
        return df
    df = data_reader()

    with st.sidebar:
        selected = option_menu("MENU", ['HOME', 'DATA', 'PREDICTION'], icons=['Home', 'Dataset', 'Data Thresholding'], menu_icon='cast', default_index=0)

    if selected == 'HOME':
        st.subheader('Background Information')
        st.write('Potable water is drinking water that has been filtered and treated for bacteria and residues to the desired standards. Growing population is a serious threat to potable water and waste management poses an even greater threat. According to UNEP about 89 countries manage data on water quality and only 52 out of this countries have data on groundwater which majorly is a representation of the largest share of fresh water in a country.')
        water_image = Image.open('water_img.jpg')
        st.image(water_image, caption="child at the tap")

    elif selected == 'DATA':
        st.subheader('Visulization of Data')
        viz_list = ['ph', 'hardness', 'solids', 'chloramines', 'sulfate', 'conductivity', 'organic carbon', 'trihalomethanes', 'turbidity']
        data_selector = st.selectbox('Data Option', viz_list)

        

        if data_selector == 'ph':
            st.write('This is the acid-base balance in water to determine the alkalinity or acidity of water. The maximum permissible rate of ph is between 6.5 and 8.5 according to WHO.')
            def figure_1():
                fig = px.histogram(df, x = 'ph', marginal='box', hover_data=df.columns, color = 'Potability')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)

            figure_1()

        elif data_selector == 'hardness':
            def figure_2():
                fig = px.histogram(df, x = 'Hardness', marginal='violin', hover_data=df.columns, color = 'Potability')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)
            figure_2()

        elif data_selector == 'solids':
            def figure_3():
                fig = px.histogram(df, x = 'Solids')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)


            figure_3()

        elif data_selector == 'chloramines':
            def figure_4():
                fig = px.histogram(df, x = 'Chloramines', marginal='violin', hover_data=df.columns, color = 'Potability')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)
            figure_4()

        elif data_selector == 'sulfate':
            def figure_5():
                fig = px.histogram(df, x = 'Sulfate')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)
            figure_5()

        elif data_selector == 'conductivity':
            def figure_6():
                fig = px.histogram(df, x = 'Conductivity', marginal='violin', hover_data=df.columns, color = 'Potability')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)
            figure_6()

        elif data_selector == 'organic carbon':
            def figure_7():
                fig = px.histogram(df, x = 'Organic_carbon', marginal='violin', hover_data=df.columns, color = 'Potability')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)
            figure_7()

        elif data_selector == 'trihalomethanes':
            def figure_8():
                fig = px.histogram(df, x = 'Trihalomethanes', marginal='violin', hover_data=df.columns, color = 'Potability')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)
            figure_8()

        elif data_selector == 'turbidity':
            def figure_9():
                fig = px.histogram(df, x = 'Turbidity', marginal='violin', hover_data=df.columns, color = 'Potability')
                fig.show()
                st.plotly_chart(fig, use_container_width = True)
            figure_9()

    
    elif selected == 'PREDICTION':
        col1, col2, col3 = st.columns(3)

        with col1:
            ph = st.number_input('Enter ph level', min_value=0.000, max_value=14.000, value=7.450)

            Hardness = st.number_input('Enter hardness value', min_value=40.000, max_value=350.000, value=193.042)

            Solids = st.number_input('Enter amount of solids', min_value=250.000, max_value=65000.000, value=32251.360)

        with col2:
            Chloramines = st.number_input('Level of chloramines', min_value=0.000, max_value=20.000, value=6.087)

            Sulfate = st.number_input('Sulfate levels', min_value=100.000, max_value=600.000, value=324.383)

            Conductivity = st.number_input('EC level', min_value=100.000, max_value=1000.000, value=521.321)

        with col3:
            Organic_carbon = st.number_input('Levels of organic matter', min_value=0.000, max_value=100.000, value=16.174)

            Trihalomethanes = st.number_input('Enter trihalomethanes level', min_value=0.000, max_value=200.000, value=57.401)

            Turbidity = st.number_input('Enter turbidity', min_value=0.000, max_value=15.000, value=4.370)


        input_dict = {'ph':ph, 'Hardness':Hardness, 'Solids':Solids, 'Chloramines':Chloramines, 'Sulfate':Sulfate, 'Conductivity':Conductivity, 'Organic_carbon':Organic_carbon, 'Trihalomethanes':Trihalomethanes, 'Turbidity':Turbidity}
        input_df = pd.DataFrame(input_dict, index=[0])

        predict_button = st.button('Predict Quality')

        if predict_button:
            result = model_loaded.predict(input_df)
            if result == 0:
                st.write('Requires filtration')

            else:
                st.write('Quality is good')


        






main()