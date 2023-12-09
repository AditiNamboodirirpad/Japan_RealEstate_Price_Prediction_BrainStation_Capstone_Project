#import statements

import streamlit as st
import pandas as pd
import numpy as np
from statistics import mode
import pickle
import xgboost as xgb
import plotly.express as px
import time



# Load the main dataset and model pickle file
file_path = "./Streamlit/cleaned_dataset.csv"
df = pd.read_csv(file_path)
model_path = "./Streamlit/xgboost_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def main():
    #Sidebar navigation
    st.sidebar.title("Navigation")
    pages = st.sidebar.radio("Go to", ("Home", "Visualizations", "Prediction of Trade Price"))
    
    if pages == "Home":
        st.image('./Streamlit/img1.jpg')
        st.header("Prediction of real estate prices in Japan", divider='rainbow')
        st.write("Welcome to the Japan Real Estate Analytics and Prediction App!")
        st.write("Through this Streamlit application, we can visualize and explore trends and factors that have shaped the Japanese real estate landscape over the 15-year period. This app also provides a prediction of real estate prices based on different factors!")
        st.subheader("About Data", divider='rainbow')
        st.markdown("""
                    - This dataset was surveyed by the Ministry of Land, Infrastructure, Transport, and Tourism of Japan (MLIT).
                    - Dataset contains :red[**600k records.**]
                    - It contains transaction data of real estate spanning from 2005 to 2019.
                    - Project steps taken:
                        1. Data exploration including the cleaning and preprocessing of this massive amount of data.
                        2. Descriptive, Time, Spatial analysis and investigating other factors affecting these Trade Prices.
                        3. Used different models to predict trade prices.
        """)
        st.subheader("More Info", divider='rainbow')
        st.image('./Streamlit/qrFinal.png', caption="Link to this project repo in GitHub", width=300)
        
    elif pages == "Visualizations":
      
        st.subheader("Visualize Factors affecting the Trade Prices", divider='rainbow')
        #Select box for different visualization with Trade Price from cleaned_dataset.csv
        selected_column = st.selectbox("Visualizations with Trade Prices", ['Prefectures','Time To Nearest Station', 'Floor Plan', 'Area in Square Feet', 'Construction Year'], index=None,placeholder="Select a visualization") 
        if not selected_column:
           st.warning('Please select the values!', icon="⚠️")
           #For multiselect visualizations             
        elif selected_column in ['Prefectures']:            
            prefecturemeans = pd.read_csv("./Streamlit/prefecturemeans.csv")
            # Sorting the bars by the y-values (TradePriceCAD) in descending order
            figpre = px.bar(prefecturemeans, x='PrefectureName', y='TradePriceCAD', title=f'Trade Price by {selected_column}')
            figpre.update_xaxes(categoryorder='total descending')
            st.plotly_chart(figpre)

        elif selected_column in ['Floor Plan']:
            floorplanmeans = pd.read_csv("./Streamlit/floorplanmeans.csv")
            figflo = px.bar(floorplanmeans, x='FloorPlan', y='TradePriceCAD', title=f'Trade Price by {selected_column}')
            figflo.update_xaxes(categoryorder='total descending')
            st.plotly_chart(figflo)

           
        elif selected_column in ['Time To Nearest Station']: 
            stationemeans = pd.read_csv("./Streamlit/stationemeans.csv")
            figsta = px.scatter(stationemeans, x='TimeToNearestStation', y='TradePriceCAD', title=f'Trade Price by {selected_column}')
            st.plotly_chart(figsta)

        elif selected_column in ['Area in Square Feet']:
            areameans = pd.read_csv("./Streamlit/areameans.csv")
            figarea = px.scatter(areameans, x='SurveyedAreaSqFt', y='TradePriceCAD', title=f'Trade Price by {selected_column}')                
            st.plotly_chart(figarea)
        
        elif selected_column in ['Construction Year']:
            constructionmeans = pd.read_csv("./Streamlit/constructionmeans.csv")
            figcon = px.line(constructionmeans, x='ConstructionYear', y='TradePriceCAD', title=f'Trade Price by {selected_column}')                
            st.plotly_chart(figcon)
    
        st.subheader("Visualize Average Trade Prices", divider='rainbow')
        st.write("Toggle to display average trade prices!")

        # Sidebar options
        selected_prefectures = st.multiselect("Select Prefectures*", df['PrefectureName'].unique())
        selected_floor_plans = st.multiselect("Select Floor Plans*", df['FloorPlan'].unique())
        time_bins = st.slider("Select Time to Nearest Station", min_value=df['TimeToNearestStation'].astype('int64').min(), max_value=df['TimeToNearestStation'].astype('int64').max(),value= (df['TimeToNearestStation'].astype('int64').min(),df['TimeToNearestStation'].astype('int64').max()),step=1)
        area_bins =  st.slider("Select Areain Square Feet", min_value=df['SurveyedAreaSqFt'].astype('int64').min(), max_value=df['SurveyedAreaSqFt'].astype('int64').max(), value=(df['SurveyedAreaSqFt'].astype('int64').min(),df['SurveyedAreaSqFt'].astype('int64').max()) ,step=1)
        construction_bins =  st.slider("Select Construction Year", min_value=df['ConstructionYear'].astype('int64').min(), max_value=df['ConstructionYear'].astype('int64').max(),value=(df['ConstructionYear'].astype('int64').min(),df['ConstructionYear'].astype('int64').max()) ,step=1)
        # Filtering the data based on selections
        filtered_data = df[
            (df['PrefectureName'].isin(selected_prefectures)) &
            (df['FloorPlan'].isin(selected_floor_plans)) &
            (df['TimeToNearestStation'] >= time_bins[0]) &
            (df['TimeToNearestStation'] <= time_bins[1]) &
            (df['SurveyedAreaSqFt'] >= area_bins[0])&
            (df['SurveyedAreaSqFt'] <= area_bins[1])&
            (df['ConstructionYear'] >= construction_bins[0])&
            (df['ConstructionYear'] <= construction_bins[1])

        ]
       
       #Plot
        fig = px.bar(
            filtered_data,
            x='PrefectureName',
            y='TradePriceCAD',
            color='FloorPlan',
            barmode='group',
            title='Mean Trade Price in CAD',
        )
        if filtered_data.empty is True:
           st.warning('Please select the values!', icon="⚠️")
                
        else:
           st.plotly_chart(fig)


        

        
    elif pages == "Prediction of Trade Price":
        st.header("Prediction of real estate prices in Japan", divider='rainbow')      
        
        
        
        # Dropdown for PrefectureName
        selected_prefecture_prediction = st.selectbox("Prefecture", list(df['PrefectureName'].unique()), index=None,placeholder= "Select a Prefecture Name")
        # Dropdown for FloorPlan
        selected_prefecture_floorplan = st.selectbox("Floor Plan",list(df['FloorPlan'].unique()), index=None,placeholder= "Select a Floor Plan")
        # Textbox for SurveyedAreaM2
        sq_ft = st.number_input("Area in Square Feet", min_value=0, max_value=None, value=0, step=1)
        selected_prefecture_SurveyedAreaM2 = sq_ft/10.764        
        # Textbox for ConstructionYear
        selected_prefecture_ConstructionYear = st.number_input("Construction Year",min_value=0, max_value=None, value=0, step=1)
        # Textbox for TimeToNearestStation
        selected_prefecture_TimeToNearestStation = st.number_input("Time To the nearest Station",min_value=0, max_value=None, value=0, step=1)  
            
            
        #  Few defaults so that users doesn't have to enter everything
        selected_prefecture_CityPlanningCategory = "Commercial Zone"
        selected_prefecture_MaxBuildingCoverageRatioPercent = 60
        selected_prefecture_MaxFloorAreaRatioPercent = 200
        selected_prefecture_RenovationStatus ="Not yet"    
        selected_prefecture_FutureUsePurpose = "House"
        selected_prefecture_CurrentUsage = "House"
        selected_prefecture_TransactionYear = 2023
        selected_prefecture_TransactionYearQuarter = 1
        selected_prefecture_BuildingStructure="RC"


        
        #Predict button
        if st.button("Predict"):
                #Inputting into the model. This is because I have a lot of dummies. 100 odd columns
                input_data = pd.DataFrame({
                    'TimeToNearestStation': [selected_prefecture_TimeToNearestStation],
                    'SurveyedAreaM2':[selected_prefecture_SurveyedAreaM2],
                    'ConstructionYear':[float(selected_prefecture_ConstructionYear)],
                    'MaxBuildingCoverageRatioPercent':[float(selected_prefecture_MaxBuildingCoverageRatioPercent)],
                    'MaxFloorAreaRatioPercent': [float(selected_prefecture_MaxFloorAreaRatioPercent)],
                    'TransactionYear':[selected_prefecture_TransactionYear],
                    'TransactionYearQuarter':[selected_prefecture_TransactionYearQuarter],
                    'PrefectureName_Akita': [1 if selected_prefecture_prediction == 'Akita' else 0],
                    'PrefectureName_Aomori': [1 if selected_prefecture_prediction == 'Aomori' else 0],
                    'PrefectureName_Chiba': [1 if selected_prefecture_prediction == 'Chiba' else 0],
                    'PrefectureName_Ehime': [1 if selected_prefecture_prediction == 'Ehime' else 0],
                    'PrefectureName_Fukui': [1 if selected_prefecture_prediction == 'Fukui' else 0],
                    'PrefectureName_Fukuoka': [1 if selected_prefecture_prediction == 'Fukuoka' else 0],
                    'PrefectureName_Fukushima': [1 if selected_prefecture_prediction == 'Fukushima' else 0],
                    'PrefectureName_Gifu': [1 if selected_prefecture_prediction == 'Gifu' else 0],
                    'PrefectureName_Gunma': [1 if selected_prefecture_prediction == 'Gunma' else 0],
                    'PrefectureName_Hiroshima': [1 if selected_prefecture_prediction == 'Hiroshima' else 0],
                    'PrefectureName_Hokkaido': [1 if selected_prefecture_prediction == 'Hokkaido' else 0],
                    'PrefectureName_Hyogo': [1 if selected_prefecture_prediction == 'Hyogo' else 0],
                    'PrefectureName_Ibaraki': [1 if selected_prefecture_prediction == 'Ibaraki' else 0],
                    'PrefectureName_Ishikawa': [1 if selected_prefecture_prediction == 'Ishikawa' else 0],
                    'PrefectureName_Iwate': [1 if selected_prefecture_prediction == 'Iwate' else 0],
                    'PrefectureName_Kagawa': [1 if selected_prefecture_prediction == 'Kagawa' else 0],
                    'PrefectureName_Kagoshima': [1 if selected_prefecture_prediction == 'Kagoshima' else 0],
                    'PrefectureName_Kanagawa': [1 if selected_prefecture_prediction == 'Kanagawa' else 0],
                    'PrefectureName_Kochi': [1 if selected_prefecture_prediction == 'Kochi' else 0],
                    'PrefectureName_Kumamoto': [1 if selected_prefecture_prediction == 'Kumamoto' else 0],
                    'PrefectureName_Kyoto': [1 if selected_prefecture_prediction == 'Kyoto' else 0],
                    'PrefectureName_Mie': [1 if selected_prefecture_prediction == 'Mie' else 0],
                    'PrefectureName_Miyagi': [1 if selected_prefecture_prediction == 'Miyagi' else 0],
                    'PrefectureName_Miyazaki': [1 if selected_prefecture_prediction == 'Miyazaki' else 0],
                    'PrefectureName_Nagano': [1 if selected_prefecture_prediction == 'Nagano' else 0],
                    'PrefectureName_Nagasaki': [1 if selected_prefecture_prediction == 'Nagasaki' else 0],
                    'PrefectureName_Nara': [1 if selected_prefecture_prediction == 'Nara' else 0],
                    'PrefectureName_Niigata': [1 if selected_prefecture_prediction == 'Niigata' else 0],
                    'PrefectureName_Oita': [1 if selected_prefecture_prediction == 'Oita' else 0],
                    'PrefectureName_Okayama': [1 if selected_prefecture_prediction == 'Okayama' else 0],
                    'PrefectureName_Okinawa': [1 if selected_prefecture_prediction == 'Okinawa' else 0],
                    'PrefectureName_Osaka': [1 if selected_prefecture_prediction == 'Osaka' else 0],
                    'PrefectureName_Saga': [1 if selected_prefecture_prediction == 'Saga' else 0],
                    'PrefectureName_Saitama': [1 if selected_prefecture_prediction == 'Saitama' else 0],
                    'PrefectureName_Shiga': [1 if selected_prefecture_prediction == 'Shiga' else 0],
                    'PrefectureName_Shimane': [1 if selected_prefecture_prediction == 'Shimane' else 0],
                    'PrefectureName_Shizuoka': [1 if selected_prefecture_prediction == 'Shizuoka' else 0],
                    'PrefectureName_Tochigi': [1 if selected_prefecture_prediction == 'Tochigi' else 0],
                    'PrefectureName_Tokushima': [1 if selected_prefecture_prediction == 'Tokushima' else 0],
                    'PrefectureName_Tokyo': [1 if selected_prefecture_prediction == 'Tokyo' else 0],
                    'PrefectureName_Tottori': [1 if selected_prefecture_prediction == 'Tottori' else 0],
                    'PrefectureName_Toyama': [1 if selected_prefecture_prediction == 'Toyama' else 0],
                    'PrefectureName_Wakayama': [1 if selected_prefecture_prediction == 'Wakayama' else 0],
                    'PrefectureName_Yamagata': [1 if selected_prefecture_prediction == 'Yamagata' else 0],
                    'PrefectureName_Yamaguchi': [1 if selected_prefecture_prediction == 'Yamaguchi' else 0],
                    'PrefectureName_Yamanashi': [1 if selected_prefecture_prediction == 'Yamanashi' else 0],
                    'FloorPlan_1K': [1 if selected_prefecture_floorplan == '1K' else 0],
                    'FloorPlan_1LDK': [1 if selected_prefecture_floorplan == '1LDK' else 0],
                    'FloorPlan_1LDK+S': [1 if selected_prefecture_floorplan == '1LDK+S' else 0],
                    'FloorPlan_1R': [1 if selected_prefecture_floorplan == '1R' else 0],
                    'FloorPlan_2DK': [1 if selected_prefecture_floorplan == '2DK' else 0],
                    'FloorPlan_2DK+S': [1 if selected_prefecture_floorplan == '2DK+S' else 0],
                    'FloorPlan_2K': [1 if selected_prefecture_floorplan == '2K' else 0],
                    'FloorPlan_2LDK': [1 if selected_prefecture_floorplan == '2LDK' else 0],
                    'FloorPlan_2LDK+S': [1 if selected_prefecture_floorplan == '2LDK+S' else 0],
                    'FloorPlan_3DK': [1 if selected_prefecture_floorplan == '3DK' else 0],
                    'FloorPlan_3K': [1 if selected_prefecture_floorplan == '3K' else 0],
                    'FloorPlan_3LDK': [1 if selected_prefecture_floorplan == '3LDK' else 0],
                    'FloorPlan_3LDK+S': [1 if selected_prefecture_floorplan == '3LDK+S' else 0],
                    'FloorPlan_4DK': [1 if selected_prefecture_floorplan == '4DK' else 0],
                    'FloorPlan_4K': [1 if selected_prefecture_floorplan == '4K' else 0],
                    'FloorPlan_4LDK': [1 if selected_prefecture_floorplan == '4LDK' else 0],
                    'FloorPlan_4LDK+S': [1 if selected_prefecture_floorplan == '4LDK+S' else 0],
                    'FloorPlan_5LDK': [1 if selected_prefecture_floorplan == '5LDK' else 0],
                    'FloorPlan_Open Floor': [1 if selected_prefecture_floorplan == 'Open Floor' else 0],
                    'FloorPlan_Other': [1 if selected_prefecture_floorplan == 'Other' else 0],
                    'BuildingStructure_RC': [1 if selected_prefecture_BuildingStructure == 'RC' else 0],
                    'BuildingStructure_RC, S': [1 if selected_prefecture_BuildingStructure == 'RC, S' else 0],
                    'BuildingStructure_S': [1 if selected_prefecture_BuildingStructure == 'S' else 0],
                    'BuildingStructure_SRC': [1 if selected_prefecture_BuildingStructure == 'SRC' else 0],
                    'BuildingStructure_SRC, RC': [1 if selected_prefecture_BuildingStructure == 'SRC, RC' else 0],
                    'BuildingStructure_SRC, S': [1 if selected_prefecture_BuildingStructure == 'SRC, S' else 0],
                    'CurrentUsage_Office': [1 if selected_prefecture_CurrentUsage == 'Office' else 0],
                    'CurrentUsage_Other': [1 if selected_prefecture_CurrentUsage == 'Other' else 0],
                    'CurrentUsage_Shop': [1 if selected_prefecture_CurrentUsage == 'Shop' else 0],
                    'FutureUsePurpose_Office': [1 if selected_prefecture_FutureUsePurpose == 'Office' else 0],
                    'FutureUsePurpose_Other': [1 if selected_prefecture_FutureUsePurpose == 'Other' else 0],
                    'FutureUsePurpose_Shop': [1 if selected_prefecture_FutureUsePurpose == 'Shop' else 0],
                    'CityPlanningCategory_Category I Exclusively Medium-high Residential Zone': [1 if selected_prefecture_CityPlanningCategory == 'Category I Exclusively Medium-high Residential Zone' else 0],
                    'CityPlanningCategory_Category I Residential Zone': [1 if selected_prefecture_CityPlanningCategory == 'Category I Residential Zone' else 0],
                    'CityPlanningCategory_Category II Exclusively Low-story Residential Zone': [1 if selected_prefecture_CityPlanningCategory == 'Category II Exclusively Low-story Residential Zone' else 0],
                    'CityPlanningCategory_Category II Exclusively Medium-high Residential Zone': [1 if selected_prefecture_CityPlanningCategory == 'Category II Exclusively Medium-high Residential Zone' else 0],
                    'CityPlanningCategory_Category II Residential Zone': [1 if selected_prefecture_CityPlanningCategory == 'Category II Residential Zone' else 0],
                    'CityPlanningCategory_Commercial Zone': [1 if selected_prefecture_CityPlanningCategory == 'Commercial Zone' else 0],
                    'CityPlanningCategory_Exclusively Industrial Zone': [1 if selected_prefecture_CityPlanningCategory == 'Exclusively Industrial Zone' else 0],
                    'CityPlanningCategory_Industrial Zone': [1 if selected_prefecture_CityPlanningCategory == 'Industrial Zone' else 0],
                    'CityPlanningCategory_Neighborhood Commercial Zone': [1 if selected_prefecture_CityPlanningCategory == 'Neighborhood Commercial Zone' else 0],
                    'CityPlanningCategory_Non-divided City Planning Area': [1 if selected_prefecture_CityPlanningCategory == 'Non-divided City Planning Area' else 0],
                    'CityPlanningCategory_Quasi-city Planning Area': [1 if selected_prefecture_CityPlanningCategory == 'Quasi-city Planning Area' else 0],
                    'CityPlanningCategory_Quasi-industrial Zone': [1 if selected_prefecture_CityPlanningCategory == 'Quasi-industrial Zone' else 0],
                    'CityPlanningCategory_Quasi-residential Zone': [1 if selected_prefecture_CityPlanningCategory == 'Quasi-residential Zone' else 0],
                    'CityPlanningCategory_Urbanization Control Area': [1 if selected_prefecture_CityPlanningCategory == 'Urbanization Control Area' else 0],
                    'RenovationStatus_Not yet': [1 if selected_prefecture_RenovationStatus == 'Not yet' else 0]
                })


                # Use the model to predict TradePriceYen
                with st.spinner('Predicting...'):
                    time.sleep(1)
                    predicted_trade_price = model.predict(input_data)

                import locale

                # Set the locale to format numbers as Canadian dollars
                locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
                # Converting to CAD using an exchange rate of 0.0092
                predicted_trade_price_cad = predicted_trade_price * 0.0092
                # Formatting the CAD value as currency with 2 decimal places
                formatted_price_cad = locale.currency(round(predicted_trade_price_cad[0], 2), grouping=True)
                st.header(f":green[**Trade Price in CAD:** {formatted_price_cad}]")

                # Set the locale to format numbers as Japanese yen
                locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
                # Display the predicted TradePriceYen rounded to the nearest integer
                formatted_price_yen = locale.currency(round(predicted_trade_price[0]), grouping=True)
                # Display the formatted value in Japanese yen
                st.header(f"**Trade Price in Yen:** {formatted_price_yen}")


       

if __name__ == "__main__":
    main()
