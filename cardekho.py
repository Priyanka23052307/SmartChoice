from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import streamlit as st
import pandas as pd
from PIL import Image
import base64
#Reading data from excel sheet to data frame
final_df=pd.read_excel(r"C:\Users\Priyanka\OneDrive\Desktop\practice\CarDekho\after_null.xlsx")
#Identifying numerical columns
after_null=pd.DataFrame()
#Dropping the columns which are not dependent on target column
after_null=final_df.drop(['Engine Displacement','Year of Manufacture','Torque','Super Charger','Turbo Charger', 
                          'model','No of Cylinder', 'Centeral Locking','Engine Type','Drive Type',
                          'Displacement','Gross Weight', 'Gear Box', 'Top Speed','Front Brake Type','Rear Brake Type',
                          'Acceleration', 'Power Steering','Anti Lock Braking System','Air Conditioner','Adjustable Head Lights',
                          'Child Safety Locks','Cd Player','Radio','Speakers Front','Speakers Rear','Integrated2Din Audio', 
                          'Usb Auxiliary Input','Bluetooth', 'Number Of Speaker', 'Touch Screen'],axis=1)

#Filtering all numerical columns
numerical_columns = after_null.select_dtypes(include=['number']).columns
#Finding out categorical columns 
categorical_columns=after_null.columns.difference(numerical_columns)

#Standardization
after_null['km_sta']=(after_null['km']-after_null['km'].mean())/after_null["km"].std()
after_null['Mileage_sta']=(after_null['Mileage']-after_null['Mileage'].mean())/after_null["Mileage"].std()
after_null['MaxPower_sta']=(after_null['Max Power']-after_null['Max Power'].mean())/after_null["Max Power"].std()
after_null = after_null[
    (after_null['km_sta'] > -1) & 
    (after_null['km_sta'] < 1) &
    (after_null['Mileage_sta'] > -1) & 
    (after_null['Mileage_sta'] < 1) &
    (after_null['MaxPower_sta'] > -1) & 
    (after_null['MaxPower_sta'] < 1)
]

#One-Hot Encoding
city_dummies=pd.get_dummies(after_null['City'])
bt_dummies=pd.get_dummies(after_null['bt'])
ft_dummies=pd.get_dummies(after_null['ft'])
oem_dummies=pd.get_dummies(after_null['oem'])
Transmission_dummies=pd.get_dummies(after_null['Transmission'])

#after_null=pd.concat([after_null,encoding_df],axis=1)
#Dropping main columns after encoding
after_null=after_null.drop(['City', 'Transmission', 'bt', 'ft', 'oem','Mileage', 'Max Power','km'],axis=1)
#Concating all the dataframes
after_null=pd.concat([after_null,city_dummies,bt_dummies,ft_dummies,oem_dummies,Transmission_dummies],axis=1)
image_path = 'car_image.jpg'
#Setting background image for streamlit page
def set_background_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    # Inject CSS for background image
    background_css = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

# Set the background image
set_background_image("car_image.jpg")
st.markdown("""
    <style>
    

    /* Style the container of the main content */
    .css-1d391kg {
        background-color: rgba(255, 255, 255, 0.8); /* White background with slight transparency */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Style for selectboxes (dropdowns) */
    .stSelectbox {
        background-color: #c72b2b0a
        /*border-radius: 5px;
        border: 1px solid #cccccc;
        padding: 10px;*/
        font-size: 16px;
    }
    .stSelectbox > div {
        background-color: transparent !important;
    }

    /* Style for sliders */
    .stSlider {
       background-color: #26273005;
       border-radius: 0px;
       border: 0px solid #cccccc;
       padding: 0px;
    }

    /* Style for the slider's track */
    .stSlider .track {
        background-color: #007bff; /* Track color */
    }

    /* Style the labels and values */
    .stSlider .stSlider-value {
        color: #007bff;
    }

    /* Style the slider handle */
    .stSlider .slider-handle {
        background-color: #007bff; /* Handle color */
        border: 2px solid #ffffff; /* Handle border color */
    }
    
    .st-emotion-cache-ue6h4q {
            color: white; 
    }
    .st-ay {
        font-size: 0.8rem;
    }
    .st-b6{
        color:#ff4b4b
    }
    .st-bc {
        height: 2.0rem !important;
    }
    .st-bi {
        color: #ff4b4b;
    }
    h1 {
        color: #049489;
        text-align: center;
    }
    .st-emotion-cache-1r4qj8v{
        color: #ff4b4b;
        font-size: 2.5rem;
    }
    .output{
        color:white;
    }
    .st-c3{
        color: rgb(255, 75, 75);
    }
    }
    </style>
""", unsafe_allow_html=True)
#Heading for streamlit page
st.markdown("<h1>CAR QUEST</h1>", unsafe_allow_html=True)

#Initialising streamlit elements in columns order
col1,col2,col3=st.columns([1,1,1])
#Slider for selecting KMs ran by car
with col1:
    km = st.slider(
            'Kms:',
            min_value=0,
            max_value=100000,
            value=10000,
            step=1
        )
#Slider for selecting Mileage 
with col2:
    mileage=st.slider(
            'Mileage:',
            min_value=5,
            max_value=30,
            value=10,
            step=1
        )
#Slider for selecting Max power
with col3:
    maxpower=st.slider(
            'Max Power:',
            min_value=20,
            max_value=200,
            value=100,
            step=1
        )
col4,col5,col6=st.columns([4,4,4])
#Dropdown for selecting count of owners used particular car
with col4:
    ownerno = st.selectbox('Owner No', sorted(after_null["ownerNo"].unique()),key="selectowner")
#Dropdown for selecting year of manufacture
with col5:
    modelyear = st.selectbox('Year of Manufacture', sorted(after_null["modelYear"].unique()),key="selectyear")
#Dropdown for selecting seating capacity
with col6:
    seats = st.selectbox('No.of Seats', sorted(after_null["Seating Capacity"].unique()),key="selectseat")

    
col7,col8,col9=st.columns([1,1,1])
#Dropdown for selecting city
with col7:
    city = st.selectbox('City', city_dummies.columns,key="selectcity")
#Dropdown for selecting body type
with col8:
    bt = st.selectbox('Body Type', bt_dummies.columns,key="selectbt")
#Dropdown for selecting fuel type
with col9:
    ft = st.selectbox('Fuel Type', ft_dummies.columns,key="selectft")
col10,col11,col12=st.columns([1,1,1])
#Dropdown for selecting model
with col10:
    model = st.selectbox('Model', oem_dummies.columns,key="selectmodel")
#Dropdown for selecting transmission type
with col11:
    transmission = st.selectbox('Transmission', Transmission_dummies.columns,key="selecttrans")
initial_data = {
    'ownerNo': ownerno,
    'modelYear': modelyear,
    'Seating Capacity': seats
}

x_test_single = pd.DataFrame({
    'km_sta': km,
    'Mileage_sta': mileage,
    'MaxPower_sta': maxpower
},index=[0])

#City
city_user_input = city
#Making 0 for all the city names 
city_dict = {city: 0 for city in city_dummies}
#Making 1 for the city which user has selected
city_dict[city_user_input] = 1
#Intialising data frame for all the cities
city_df = pd.DataFrame([city_dict])
#bt
bt_user_input = bt
#Making 0 for all the body type names 
bt_dict = {bt: 0 for bt in bt_dummies}
#Making 1 for the body type which user has selected
bt_dict[bt_user_input] = 1
#Intialising data frame for all the body types
bt_df = pd.DataFrame([bt_dict])
#ft
ft_user_input = ft
#Making 0 for all the fuel type names 
ft_dict = {ft: 0 for ft in ft_dummies}
#Making 1 for the fuel type which user has selected
ft_dict[ft_user_input] = 1
#Intialising data frame for all the fuel types
ft_df = pd.DataFrame([ft_dict])
#merged_df = pd.concat([x_test_single_scaled_df, city_df,bt_df,ft_df], axis=1)
#oem
oem_user_input = model
#Making 0 for all the OEM types 
oem_dict = {oem: 0 for oem in oem_dummies}
#Making 1 for the OEM type which user has selected
oem_dict[oem_user_input] = 1
#Intialising data frame for all the OEM types
oem_df = pd.DataFrame([oem_dict])
#Transmission
Transmission_user_input = transmission
#Making 0 for all the transmission types
Transmission_dict = {Transmission: 0 for Transmission in Transmission_dummies}
#Making 1 for the transmission type which user has selected
Transmission_dict[Transmission_user_input] = 1
#Intialising data frame for all the transmission types
Transmission_df = pd.DataFrame([Transmission_dict])

merged_df = pd.DataFrame(initial_data,index=[0])
scaler=StandardScaler()
#Standardisation for the columns in x_test_single data frame
x_test_single_scaled = scaler.fit_transform(x_test_single)
x_test_single_scaled_df = pd.DataFrame(x_test_single_scaled,index=[0], columns=x_test_single.columns)
#Merging all the dataframes
merged_df = pd.concat([merged_df,x_test_single_scaled_df,city_df,bt_df,ft_df,oem_df,Transmission_df], axis=1)
test_pred=[]
#Creating LASSO model for predicting car price depending on user inputs
with col12:
    if st.button("Estimate"):
        #Dropping target column
        x=after_null.drop(["price"],axis=1) 
        y=after_null["price"] 
        # Initialize the Lasso model
        model=RandomForestRegressor(random_state=42)
        # Splitting the data into training and validation sets
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) 
        # Fit the model on training data (already standardized)
        model.fit(x_train,y_train) 
        x_test=merged_df
        # Predict on user input data (x_test / merged_df)
        test_pred=model.predict(x_test) 
        if test_pred:# This checks if test_pred is not empty
            col13 = st.columns([1]) 
            with col13[0]:
                 # Display the rounded prediction value
                st.markdown(f'<p class="output">The prediction value is: {test_pred[0].round(2)}</p>', unsafe_allow_html=True)
