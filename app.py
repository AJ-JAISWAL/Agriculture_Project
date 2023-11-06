import streamlit as st
import pandas as pd
import numpy as np

model = pd.read_pickle('soil_fertility_model.pkl')
crop = pd.read_pickle('crop_grown_model.pkl')
group=pd.read_pickle('group.pkl')
data_soil=pd.read_pickle('data_soil.pkl')
new_data_soil=pd.read_pickle('new_data_soil.pkl')
data=pd.read_pickle('data.pkl')

nav = st.sidebar.radio("Navigation",["Home","Land_Fertility","Crop_Predictor","Farming_By_AJ_Tech"])

if nav == "Home":

    page = st.sidebar.radio("Go to", ["Introduction", "5 Most Component requiring crops", "5 Least Component requiring crops"])

    if page == "Introduction":
        st.write('<h1 style="color: blue;">About Our Website</h1>', unsafe_allow_html=True)
        page_bg_img = """
                            <style>
                            [data-testid="stAppViewContainer"] {
                            background-image: url('https://img.freepik.com/premium-vector/flat-design-farm-landscape-background_23-2148201943.jpg');
                            background-size: cover;
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                            background-color: rgba(255, 255, 255, 0.8);
                            </style>
                            """

        st.markdown(page_bg_img, unsafe_allow_html=True)

        st.write('<h5 style="color: red;">We are pleased to welcome you to our cutting-edge Agriculture Website,'
                 ' where tradition meets innovation. We harness the power of Machine Learning to revolutionize farming practices.'
                 ' We improve yield prediction, optimize crop management, and streamline resource allocation using advanced algorithms.'
                 ' Our technology enables precision agriculture, ensuring every inch of your land is utilized efficiently. '
                 'We are ushering in an era of sustainable, high-yield agriculture by combining age-old wisdom with the latest in artificial intelligence. '
                 'Become a part of the future of farming today!</h5>',unsafe_allow_html=True)

        st.title(':blue[How to Use the Website:]')

        points = [
            "**:red[Navigation: The website is designed for intuitive navigation. Use the menu bar to access different sections.]**",
            "**:red[Guided Tour: Take a virtual tour to learn how to utilize the features effectively.]**",
            "**:red[Interpreting Data: Familiarize yourself with how to interpret the information provided for land fertility and crop predictions.]**",
        ]
        for point in points:
            st.write(point)

        st.title(':blue[Home Section]')
        st.write('**:red[Home have 3 section]**')

        points = [
            "**:red[Introduction : How to use , About website.]**",
            "**:red[5 Most Component requiring crops : Component like Nitrogen ,Phosphorus , Potassium , pH, etc.]**",
            "**:red[5 Least Component requiring crops : Component as Nitrogen ,Phosphorus , Potassium , pH, etc.]**",
        ]
        for point in points:
            st.write(point)

        st.title(':blue[Land_Fertility Section]')
        st.write('**:red[Introduction to Land Fertility Checker]**')
        st.write(':red[Assessing land fertility is a critical step in successful farming.'
                 ' Our Land Fertility Checker section is designed to help you determine the fertility status of your land with accuracy and precision.]')
        st.write('**:red[How It Works:]**')
        points = [
            ":red[Input Data : Provide information about your land.]",
            ":red[Analysis : Our advanced algorithms process the data to assess the fertility level of your land.]",
            ":red[Results : Recommend the status of the land i.e. Land is Fertile or Non_Fertile.]",
        ]
        for point in points:
            st.write(point)

        st.title(':blue[Crop Predictor Section]')
        st.write('**:red[Introduction to Crop_Grown_Predictor]**')
        st.write(':red[Selecting the right crop for your land is a crucial decision for any farmer. '
                 'Our Crop Predictor section utilizes machine learning algorithms to offer accurate predictions'
                 ' on which crops are best suited to your specific conditions.]')
        st.write('**:red[How It Works:]**')
        points = [
            ":red[Input Data : Provide information about your land.]",
            ":red[Analysis :  Our algorithms analyze the data to generate personalized crop recommendations.]",
            ":red[Results : Recommend the best crop grown to the land.]",
        ]
        for point in points:
            st.write(point)

        st.title(':blue[Farming_By_AJ_Tech Section]')
        st.write('**:red[Introduction]**')
        st.write(':red[Developed a model predicting optimal land composition for specific crops, revolutionizing farming practices.'
                 ' Leverage insights to optimize crop growth, ensuring sustainable, high-yield agriculture. Explore the future of precision farming.]')
        st.write('**:red[How It Works:]**')
        points = [
            ":red[Input Data : Provide information about your land and Select the Crop to be grown.]",
            ":red[Analysis :  Our advanced algorithms process the data to assess the selected crop grown to the land..]",
            ":red[Results : Recommend the different land id and composition to grow selected crop.]"
        ]
        for point in points:
            st.write(point)
        st.write('<h5 style="color: red;">Mix the recommended land soil to the own land soil , to grow the crop of own!</h5>', unsafe_allow_html=True)

    elif page== "5 Most Component requiring crops":
        st.write('<h1 style="color: blue;">Top 5 Most Component requiring crops</h1>', unsafe_allow_html=True)
        page_bg_img = """
                    <style>
                    [data-testid="stAppViewContainer"] {
                    background-image: url('https://images.pexels.com/photos/158603/wheat-wheat-field-cereals-field-158603.jpeg?cs=srgb&dl=pexels-pixabay-158603.jpg&fm=jpg');
                    background-size: cover;
                    </style>
                    """

        st.markdown(page_bg_img, unsafe_allow_html=True)
        def values(element):
            l1 = []
            l2 = []
            for j, k in group.sort_values(by=element, ascending=False)[:5][['label', element]].values:
                l1.append(j)
                l2.append(k)
            data = {
                "crop": l1, " Requirement (kg per unit of yield)": l2
            }
            df = pd.DataFrame(data)
            return df

        col1, col2 = st.columns(2, gap="large")
        styles = [
            {"selector": "th", "props": " background: #4CAF50; color: white;"},
            {"selector": "td", "props": "background: #4CAF50; color: white;"},
        ]
        with col1:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Most Nitrogen requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('N').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        with col2:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Most Phosphorus requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('P').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        col3, col4 = st.columns(2, gap="large")
        with col3:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Most Potassium requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('K').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        with col4:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Most pH requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('ph').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        col5, col6 = st.columns(2, gap="large")
        with col5:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Most Rainfall requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('rainfall').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        with col6:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Most Humidity requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('humidity').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')

    elif page == "5 Least Component requiring crops":
        st.write('<h1 style="color: blue;">Top 5 Least Component requiring crops</h1>', unsafe_allow_html=True)
        page_bg_img = """
                    <style>
                    [data-testid="stAppViewContainer"] {
                    background-image: url('https://images.pexels.com/photos/158603/wheat-wheat-field-cereals-field-158603.jpeg?cs=srgb&dl=pexels-pixabay-158603.jpg&fm=jpg');
                    background-size: cover;
                    </style>
                    """

        st.markdown(page_bg_img, unsafe_allow_html=True)

        def values(element):
            l1 = []
            l2 = []
            for j, k in group.sort_values(by=element)[:5][['label', element]].values:
                l1.append(j)
                l2.append(k)
            data = {
                "crop": l1, " Requirement (kg per unit of yield)'": l2
            }
            df = pd.DataFrame(data)
            return df

        col1, col2 = st.columns(2, gap="large")
        styles = [
            {"selector": "th", "props": " background: #4CAF50; color: white;"},
            {"selector": "td", "props": "background: #4CAF50; color: white;"},
        ]
        with col1:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Least Nitrogen requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('N').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        with col2:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Least Phosphorus requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('P').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        col3, col4 = st.columns(2, gap="large")
        with col3:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Least Potassium requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('K').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        with col4:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Least pH requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('ph').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        col5, col6 = st.columns(2, gap="large")
        with col5:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Least Rainfall requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('rainfall').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')
        with col6:
            st.write('********************************')
            st.write('<h5 style="color: brown;">Top 5 Least Humidity requiring crops</h5>', unsafe_allow_html=True)
            st.table(values('humidity').style.set_table_styles(styles, overwrite=False))
            st.write('********************************')



if nav == "Land_Fertility":
    st.write('<h1 style="color: blue;">Land_Fertility_Checker</h1>', unsafe_allow_html=True)
    page_bg_img = """
            <style>
            [data-testid="stAppViewContainer"] {
            background-image: url('https://img.freepik.com/free-vector/brown-soil-texture-background_1308-20483.jpg');
            background-size: cover;
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-color: rgba(255, 255, 255, 0.8);
            </style>
            """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    pH = st.number_input('**:red[PH of the Soil(pH)]**',min_value=7.28, max_value=9.36)
    EC = st.number_input('**:red[Electrical Conductivity(EC) in the Soil(dS/m)]**',min_value=0.02, max_value=0.6612)
    OC = st.number_input('**:red[Organic Carbon(OC) in the Soil(g/kg)]**',min_value=0.01, max_value=0.48)
    OM = st.number_input('**:red[Organic Matter in the Soil(g/kg)]**',min_value=0.01, max_value=0.8299)
    N  = st.number_input('**:red[Nitrogen(N) in the Soil(ppm)]**',min_value=75.0, max_value=278.0)
    P  = st.number_input('**:red[Phosphorus(P) in the Soil(ppm)]**',min_value=1.8, max_value=34.6625)
    K  = st.number_input('**:red[Potassium(K) in the Soil(ppm)]**',min_value=70.0, max_value=446.875)
    Zn = st.number_input('**:red[Zinc(Zn) in the Soil(ppm)]**',min_value=0.04, max_value=1.08625)
    Fe = st.number_input('**:red[Iron(Fe) in the Soil(ppm)]**',min_value=1.0, max_value=9.1)
    Cu = st.number_input('**:red[Copper(Cu) in the Soil(ppm)]**',min_value=0.01, max_value=0.73)
    Mn = st.number_input('**:red[Manganese(Mn) in the Soil(pH)]**',min_value=0.2, max_value=7.5)
    Sand = st.number_input('**:red[Sand in the Soil(%)]**',min_value=77.2, max_value=96.2)
    Silt = st.number_input('**:red[Silt in the Soil(%)]**',min_value=1.1, max_value=13.3875)
    Clay = st.number_input('**:red[Clay in the Soil(%)]**',min_value=2.0, max_value=13.8)
    CaCO3 = st.number_input('**:red[Calcium Carbonate(CaCO3) in the Soil(%)]**',min_value=0.0, max_value=15.7925)
    CEC = st.number_input('**:red[Cation Exchange Capacity(CEC) of the Soil(meq/100g)]**',min_value=1.2, max_value=12.64375)

    values=np.array([pH,EC,OC,OM,N,P,K,Zn,Fe,Cu,Mn,Sand,Silt,Clay,CaCO3,CEC])

    values=values.reshape(1,16)

    if st.button('Check Fertility'):
        if (model.predict(values)==0):
            st.title('Land is Fertile!👌👌👌')
        else:
            st.title('Land is Not Fertile!😓😓😓')

if nav == "Crop_Predictor":
    st.write('<h1 style="color: blue;">Crop_Grown_Predictor</h1>', unsafe_allow_html=True)
    page_bg_img = """
        <style>
        [data-testid="stAppViewContainer"] {
        background-image: url('https://img.freepik.com/premium-photo/spring-grain-concept-agriculture-healthy-eating-organic-food-generative-ai_58409-32489.jpg');
        background-size: cover;
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: rgba(255, 255, 255, 0.8);
        </style>
        """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    l={20: 'rice', 11: 'maize', 3: 'chickpea', 9: 'kidneybeans', 18: 'pigeonpeas', 13: 'mothbeans', 14: 'mungbean',
       2: 'blackgram', 10: 'lentil', 19: 'pomegranate', 1: 'banana', 12: 'mango', 7: 'grapes', 21: 'watermelon',
       15: 'muskmelon', 0: 'apple', 16: 'orange', 17: 'papaya', 4: 'coconut', 6: 'cotton', 8: 'jute', 5: 'coffee'}
    pH = st.number_input('**:red[PH of the Soil(pH)]**', min_value=3.50475,max_value=9.93509)
    N = st.number_input('**:red[Nitrogen(N) in the Soil(ppm)]**', min_value=0.0, max_value=140.0)
    P = st.number_input('**:red[Phosphorus(P) in the Soil(ppm)]**', min_value=5.0, max_value=145.0)
    K = st.number_input('**:red[Potassium(K) in the Soil(ppm)]**', min_value=5.0, max_value=205.0)

    values = np.array([N,P,K,pH])
    values = values.reshape(1, 4)

    if st.button('Check Crop Grown'):
        prediction = crop.predict(values)
        ans=prediction.item()
        st.title(l[np.round(ans)])

if nav == "Farming_By_AJ_Tech":

    st.write('<h1 style="color: blue;">Farming_By_AJ_Tech</h1>', unsafe_allow_html=True)
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url('https://i.pinimg.com/originals/98/98/58/9898587b451d4bdeeeb42e8832550587.jpg');
    background-size: cover;
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-color: rgba(255, 255, 255, 0.8);
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    def euclidean_distance(point1, point2):
        return np.sqrt(np.sum((point1 - point2) ** 2))

    def similarity_score(data_point, desired_output):
        return 1 / (1 + euclidean_distance(data_point, desired_output))

    pH = st.number_input('**:red[PH of the Soil(pH)[0]]**',min_value=7.28, max_value=9.36)
    N = st.number_input('**:red[Nitrogen(N) in the Soil(ppm)[1]]**', min_value=75.0, max_value=278.0)
    P = st.number_input('**:red[Phosphorus(P) in the Soil(ppm)[2]]**', min_value=1.8, max_value=34.6625)
    K = st.number_input('**:red[Potassium(K) in the Soil(ppm)[3]]**', min_value=70.0, max_value=446.875)

    values = np.array([N, P, K, pH])
    values = values.reshape(1, 4)

    Selected_crop = st.selectbox("**:red[Type or select a crop to be grown!]**", data['label'].unique())

    if st.button('Aj_Tech'):

        # code for find most similar row in crop_grown dataset
        selected_data=data[data['label']==Selected_crop]
        df = pd.DataFrame(selected_data)
        df=df.drop(columns='label')
        np_array = df.values
        similarity_scores = [similarity_score(data_point, values) for data_point in np_array]
        new_values=np_array[np.argmax(similarity_scores)]
        new_values = new_values.reshape(1, 4)

        # code for find most similar row in soil dataset
        similarity_scores = [similarity_score(data_point, new_values) for data_point in new_data_soil]
        top_indices = np.argpartition(similarity_scores, -4)[-4:]
        for idx in top_indices:
            st.write(idx,new_data_soil[idx].reshape(1, 4))
