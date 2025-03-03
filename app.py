import streamlit as st

# --- Helper Functions ---
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361, "Miles": 0.000621371
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Grams": 1, "Kilograms": 0.001, "Milligrams": 1000,
        "Pounds": 0.00220462, "Ounces": 0.035274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        ("Celsius", "Fahrenheit"): lambda v: (v * 9/5) + 32,
        ("Celsius", "Kelvin"): lambda v: v + 273.15,
        ("Fahrenheit", "Celsius"): lambda v: (v - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda v: (v - 32) * 5/9 + 273.15,
        ("Kelvin", "Celsius"): lambda v: v - 273.15,
        ("Kelvin", "Fahrenheit"): lambda v: (v - 273.15) * 9/5 + 32,
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

# --- Streamlit UI ---
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.markdown("<h1 style='text-align: center;'>🌍 Universal Unit Converter</h1>", unsafe_allow_html=True)
st.sidebar.header("⚙️ Converter Settings")

category = st.sidebar.radio("Select Conversion Type", ["Length", "Weight", "Temperature"])

# --- Conversion Logic ---
units = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"],
    "Weight": ["Grams", "Kilograms", "Milligrams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

st.subheader(f"{category} Converter")
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit", units[category])
with col2:
    to_unit = st.selectbox("To Unit", units[category])

value = st.number_input("Enter Value", min_value=0.0 if category != "Temperature" else None, value=1.0, step=0.1)

# --- Conversion ---
if value is not None:
    if category == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif category == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif category == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    
    st.success(f"✅ **{value} {from_unit}** = **{result:.2f} {to_unit}**")
