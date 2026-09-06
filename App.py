import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="AI Landslide Early Warning System",
    page_icon="🚨",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0B0F19; color: #FFFFFF; }
    </style>
""", unsafe_allow_html=True)

# Top Bar Header
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("🚨 AI Landslide Detection System")
    st.caption("Real-Time Telemetry & Control Room | Sector 4-B Bhoumik Ridge")
with col_head2:
    st.metric(label="System Status", value="ACTIVE", delta="LoRa Mesh Online")

st.divider()

# Main Layout: Map & Risk Gauge
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📍 Live Topographic Risk Map")
    map_data = pd.DataFrame({
        'lat': [30.3165, 30.3180, 30.3150, 30.3200],
        'lon': [78.0322, 78.0350, 78.0300, 78.0380],
        'Status': ['Normal', 'Critical Warning', 'Advisory', 'Normal'],
        'Risk_Score': [12, 87, 45, 10]
    })
    fig_map = px.scatter_mapbox(
        map_data, 
        lat="lat", 
        lon="lon", 
        color="Status",
        size="Risk_Score",
        color_discrete_map={'Normal': '#00E676', 'Advisory': '#FFD600', 'Critical Warning': '#FF1744'},
        zoom=13,
        height=400
    )
    fig_map.update_layout(mapbox_style="carto-darkmatter")
    st.plotly_chart(fig_map, use_container_width=True)

with col_right:
    st.subheader("🧠 AI Risk Model Assessment")
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=87.4,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Landslide Probability (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#FF1744"},
            'steps': [
                {'range': [0, 40], 'color': "#00E676"},
                {'range': [40, 70], 'color': "#FFD600"},
                {'range': [70, 100], 'color': "#FF1744"}
            ]
        }
    ))
    fig_gauge.update_layout(height=260, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(fig_gauge, use_container_width=True)

st.divider()

# Telemetry Metrics
st.subheader("📡 Live Sensor Telemetry (Sector 4-B)")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Pore Pressure", "82.4 kPa", "+12.1 kPa (Spike)", delta_color="inverse")
m2.metric("Soil Tilt", "Δ 4.2°", "+2.1°/hr", delta_color="inverse")
m3.metric("Rainfall Rate", "48 mm/hr", "Heavy Downpour", delta_color="inverse")
m4.metric("Vibrations", "HIGH", "Micro-seismic", delta_color="inverse")

st.warning("⚠️ CRITICAL ALERT: AI model predicts imminent slope failure within 3 hours.")
if st.button("🚨 TRIGGER EMERGENCY EVACUATION BROADCAST"):
    st.error("ACTION EXECUTED: Emergency SMS sent to citizens. Sirens activated.")
