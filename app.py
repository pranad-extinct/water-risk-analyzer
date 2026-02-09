import streamlit as st

# Page setup
st.set_page_config(page_title="Water Risk Analyzer", layout="centered")

st.title("AI-based Water Contamination Risk Analyzer")
st.write("Estimate water contamination risk using environmental indicators.")

st.markdown("---")

# INPUT SECTION
area = st.selectbox(
    "Type of Area",
    ["Urban", "Rural", "Industrial"]
)

water_source = st.selectbox(
    "Main Water Source",
    ["River / Open well", "Borewell", "Municipal supply"]
)

sewage = st.selectbox(
    "Sewage Treatment Available?",
    ["Yes", "No"]
)

flood = st.selectbox(
    "Flooding or Heavy Rain in Last Year?",
    ["Yes", "No"]
)

st.markdown("---")

# SUBMIT BUTTON
if st.button("Analyze Water Risk"):

    # Base risk values
    pharma = 20
    bacteria = 20
    micro = 20

    # Area effect
    if area == "Urban":
        pharma += 25
    elif area == "Rural":
        bacteria += 25
    elif area == "Industrial":
        micro += 30

    # Water source effect
    if water_source == "River / Open well":
        bacteria += 30
        pharma += 10
    elif water_source == "Municipal supply":
        bacteria -= 10
        pharma -= 10

    # Sewage effect
    if sewage == "No":
        pharma += 20
        bacteria += 25
        micro += 15

    # Flooding effect
    if flood == "Yes":
        pharma += 20
        bacteria += 30

    # Limit scores to 100
    pharma = min(pharma, 100)
    bacteria = min(bacteria, 100)
    micro = min(micro, 100)

    # Risk label function
    def risk_label(score):
        if score <= 35:
            return "Low"
        elif score <= 65:
            return "Medium"
        else:
            return "High"

    # OUTPUT SECTION
    st.subheader("Results")

    st.success(
        f"🧪 Pharmaceutical Contamination: {pharma}/100 — {risk_label(pharma)} Risk"
    )
    st.warning(
        f"🦠 Pathogenic Microorganisms: {bacteria}/100 — {risk_label(bacteria)} Risk"
    )
    st.info(
        f"⚗️ Other Micropollutants: {micro}/100 — {risk_label(micro)} Risk"
    )

    st.markdown("---")
    st.caption("This model estimates risk probability, not direct concentration.")
