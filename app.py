
import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# ------------------------------
# Page Config
# ------------------------------

st.set_page_config(
    page_title="Flight Price Prediction",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Load Model & Encoders
# ------------------------------

@st.cache_resource
def load_model():
    model = joblib.load("flight_price_model.pkl")
    encoders = joblib.load("encoders.pkl")
    return model, encoders

model, encoders = load_model()

# ------------------------------
# Custom CSS
# ------------------------------

st.markdown("""
<style>

body{
    background:#0e1117;
}

.main{
    background:#0e1117;
}

h1,h2,h3,h4{
    color:white;
}

.block-container{
    padding-top:2rem;
}

.stButton>button{

background:#1f77ff;
color:white;
border-radius:10px;
height:55px;
width:100%;
font-size:20px;
font-weight:bold;
border:none;

}

.stButton>button:hover{

background:#005ce6;
color:white;

}

div[data-testid="stMetric"]{

background:#161b22;
padding:15px;
border-radius:15px;

}

.css-1d391kg{

background:#161b22;

}

.prediction{

padding:25px;
border-radius:15px;
background:#1f77ff;
color:white;
font-size:35px;
text-align:center;
font-weight:bold;

}

.summary{

background:#161b22;
padding:20px;
border-radius:15px;

}

</style>

""",unsafe_allow_html=True)

# ------------------------------
# Title
# ------------------------------

st.title("✈️ Flight Price Prediction")

st.write("Predict Flight Ticket Price using Machine Learning")

st.divider()

# ------------------------------
# Sidebar
# ------------------------------

st.sidebar.image(
"https://img.icons8.com/color/512/airplane-take-off.png",
width=120
)

st.sidebar.title("Flight Details")

# Airline

airline = st.sidebar.selectbox(

"Airline",

list(encoders["airline"].classes_)

)

# Source

source = st.sidebar.selectbox(

"Source City",

list(encoders["source_city"].classes_)

)

# Destination

destination = st.sidebar.selectbox(

"Destination City",

list(encoders["destination_city"].classes_)

)

# Departure

departure = st.sidebar.selectbox(

"Departure Time",

list(encoders["departure_time"].classes_)

)

# Arrival

arrival = st.sidebar.selectbox(

"Arrival Time",

list(encoders["arrival_time"].classes_)

)

# Stops

stops = st.sidebar.selectbox(

"Stops",

["zero","one","two_or_more"]

)

# Class

travel_class = st.sidebar.selectbox(

"Travel Class",

["Economy","Business"]

)

# Duration

duration = st.sidebar.slider(

"Duration (Hours)",

0.5,
50.0,
2.5

)

# Days Left

days_left = st.sidebar.slider(

"Days Left",

1,
49,
10

)
# ------------------------------------
# Encode Inputs
# ------------------------------------

airline = encoders["airline"].transform([airline])[0]
source = encoders["source_city"].transform([source])[0]
destination = encoders["destination_city"].transform([destination])[0]
departure = encoders["departure_time"].transform([departure])[0]
arrival = encoders["arrival_time"].transform([arrival])[0]

# Stops Encoding
stop_dict = {
    "zero": 0,
    "one": 1,
    "two_or_more": 2
}

# Class Encoding
class_dict = {
    "Economy": 0,
    "Business": 1
}

# ------------------------------------
# Predict Button
# ------------------------------------

if st.sidebar.button("✈ Predict Flight Price"):

    input_df = pd.DataFrame({

        "airline":[airline],
        "source_city":[source],
        "departure_time":[departure],
        "stops":[stop_dict[stops]],
        "arrival_time":[arrival],
        "destination_city":[destination],
        "class":[class_dict[travel_class]],
        "duration":[duration],
        "days_left":[days_left]

    })

    prediction = model.predict(input_df)[0]

    st.success("Prediction Generated Successfully ✅")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Estimated Price",
            f"₹ {prediction:,.0f}"
        )

    with col2:
        st.metric(
            "Travel Class",
            travel_class
        )

    with col3:
        st.metric(
            "Stops",
            stops.title()
        )

    st.markdown("---")

    st.markdown(
        f"""
        <div class="prediction">

        ✈ ₹ {prediction:,.0f}

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Flight Summary")

    c1, c2 = st.columns(2)

    with c1:

        st.info(f"🛫 Airline : {encoders['airline'].inverse_transform([airline])[0]}")
        st.info(f"📍 Source : {encoders['source_city'].inverse_transform([source])[0]}")
        st.info(f"🛬 Destination : {encoders['destination_city'].inverse_transform([destination])[0]}")
        st.info(f"🕒 Departure : {encoders['departure_time'].inverse_transform([departure])[0]}")
        st.info(f"🕗 Arrival : {encoders['arrival_time'].inverse_transform([arrival])[0]}")

    with c2:

        st.info(f"🧳 Stops : {stops}")
        st.info(f"💺 Class : {travel_class}")
        st.info(f"⏱ Duration : {duration} Hours")
        st.info(f"📅 Days Left : {days_left}")

