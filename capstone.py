from sklearn.preprocessing import StandardScaler

import streamlit as st
import pandas as pd

st.markdown("""
    <h1>CAPSTONE</h1>
    """, unsafe_allow_html=True)
col1,col2,col3=st.columns([3,2,1])
with col1:
        ownerno = st.selectbox('Select the Owner No', sorted(after_null["ownerNo"].unique()),key="selectbox")
initial_data = {
    'ownerNo': ownerno,
    'modelYear': [2020],
    'Seating Capacity': [5]
}
merged_df = pd.DataFrame(initial_data)
x_test_single = pd.DataFrame({
    'km_sta': [30000],
    'Mileage_sta': [10],
    'MaxPower_sta': [142]
})
scaler=StandardScaler()
x_test_single_scaled = scaler.fit_transform(x_test_single)
x_test_single_scaled_df = pd.DataFrame(x_test_single_scaled, columns=x_test_single.columns)
#City
city_user_input = 'Bangalore'
city_dict = {city: 0 for city in city_dummies}
city_dict[city_user_input] = 1
city_df = pd.DataFrame([city_dict])
#bt
bt_user_input = 'SUV'
bt_dict = {bt: 0 for bt in bt_dummies}
bt_dict[bt_user_input] = 1
bt_df = pd.DataFrame([bt_dict])
#ft
ft_user_input = 'Petrol'
ft_dict = {ft: 0 for ft in ft_dummies}
ft_dict[ft_user_input] = 1
ft_df = pd.DataFrame([ft_dict])
#merged_df = pd.concat([x_test_single_scaled_df, city_df,bt_df,ft_df], axis=1)
#oem
oem_user_input = 'Renault'
oem_dict = {oem: 0 for oem in oem_dummies}
oem_dict[oem_user_input] = 1
oem_df = pd.DataFrame([oem_dict])
#Transmission
Transmission_user_input = 'Manual'
Transmission_dict = {Transmission: 0 for Transmission in Transmission_dummies}
Transmission_dict[Transmission_user_input] = 1
Transmission_df = pd.DataFrame([Transmission_dict])
merged_df = pd.concat([merged_df,x_test_single_scaled_df,city_df,bt_df,ft_df,oem_df,Transmission_df], axis=1)


print(merged_df)
#x_test=[3,2017,9,50000,10,70,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0]
#x_test=[]
