import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(
    page_title="GeoShield AI | Landslide Control Room",
    page_icon="🌋",
    layout="wide"
)

# Dark Theme Custom Styling
st.markdown("""
    <style>
    .stApp { background-color: #0B0F19; color: #FFFFFF; }
    .stMetric { 
        background: #1E293B; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #334155;
    }
    .citizen-card {
        background-color: #1E293B;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #EF4444;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Control
with st.sidebar:
    st.title("🌐 GeoShield AI")
    st.caption("Early Warning & Telemetry Engine")
    st.divider()
    view_mode = st.radio(
        "🖥️ Select System Mode:",
        ["🕹️ Emergency Control Room", "📱 Citizen Mobile App View"]
    )
    st.divider()
    st.write("🟢 **LoRa Mesh:** 14/14 Online")
    st.write("🧠 **AI Engine:** GeoPredict-LSTM v4.2")
    st.write("⏱️ **Sync:** " + datetime.now().strftime("%H:%M:%S UTC"))

# ----------------- VIEW 1: CONTROL ROOM -----------------
if view_mode == "🕹️ Emergency Control Room":
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("🚨 Landslide Monitoring & Control Room")
        st.caption("Sector 4-B: Bhoumik Ridge | Dehradun-Mussoorie Array")
    with c2:
        st.metric(label="CRITICAL THREAT LEVEL", value="SECTOR 4-B", delta="87.4% Failure Probability", delta_color="inverse")

    st.divider()

    col_map, col_ai = st.columns([2, 1])

    with col_map:
        st.subheader("📍 Real-Time Topographic Sensor Map")
        # Native Streamlit Map (100% Reliable, No Black Boxes)
        sensor_locations = pd.DataFrame({
            'lat': [30.3165, 30.3220, 30.3190, 30.3140],
            'lon': [78.0322, 78.0380, 78.0350, 78.0300]
        })
        st.map(sensor_locations, zoom=12, use_container_width=True)
        st.caption("🔴 Node #02 (Peak Sector) reporting severe displacement.")

    with col_ai:
        st.subheader("🧠 AI Predictive Risk Gauge")
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=87.4,
            domain={'x': [0, 1], 'y': [0, 1]},
            number={'suffix': "%", 'font': {'color': "#FF1744", 'size': 44}},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': "white"},
                'bar': {'color': "#FF1744"},
                'steps': [
                    {'range': [0, 35], 'color': "#00E676"},
                    {'range': [35, 70], 'color': "#FFD600"},
                    {'range': [70, 100], 'color': "#FF1744"}
                ]
            }
        ))
        fig_gauge.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_gauge, use_container_width=True)
        st.error("⚡ **XAI Insight:** Soil Saturation (72%) + Micro-Seismic Vibration (28%).")

    st.divider()

    # Telemetry
    st.subheader("📡 Live Sensor Telemetry (Node #02 Array)")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Pore Water Pressure", "82.4 kPa", "+14.2 kPa (Spike)", delta_color="inverse")
    m2.metric("Inclinometer Tilt", "Δ 4.8°", "+2.3°/hr Displacement", delta_color="inverse")
    m3.metric("Rainfall Rate", "52 mm/hr", "Heavy Downpour", delta_color="inverse")
    m4.metric("Micro-Seismic Anomaly", "HIGH", "Micro-Fractures", delta_color="inverse")

    st.divider()

    # Trend Line Chart
    st.subheader("📈 Telemetry Escalation vs AI Forecast Horizon")
    times = [datetime.now() - timedelta(hours=i) for i in range(5, -1, -1)]
    df_trend = pd.DataFrame({
        'Time': [t.strftime("%H:%M") for t in times],
        'Pore Pressure (kPa)': [45, 52, 60, 72, 82.4, 91.0],
        'Tilt Angle (deg)': [0.8, 1.2, 1.8, 2.9, 4.8, 6.2]
    })
    fig_line = px.line(df_trend, x='Time', y=['Pore Pressure (kPa)', 'Tilt Angle (deg)'], markers=True, color_discrete_sequence=['#FF1744', '#FFD600'])
    fig_line.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
    st.plotly_chart(fig_line, use_container_width=True)

    # Actionable Alert
    st.warning("⚠️ **AUTOMATED ACTION SUGGESTION:** Imminent failure horizon estimated within 2.5 Hours.")
    if st.button("🔥 DISPATCH EMERGENCY BROADCAST & SIRENS"):
        st.success("✅ **ACTION EXECUTED:** Emergency SMS dispatched to 1,420 registered citizens. Local sirens activated.")

# ----------------- VIEW 2: CITIZEN APP -----------------
else:
    st.title("📱 Citizen Safety Mobile Portal")
    st.caption("Public Emergency Dashboard & Safe Route Planner")
    st.divider()

    st.markdown("""
        <div class="citizen-card">
            <h2 style="color: #EF4444; margin:0;">⚠️ CRITICAL EVACUATION WARNING</h2>
            <p><b>Target Zone:</b> Bhoumik Ridge Sector 4-B</p>
            <p>High landslide threat detected within 2-3 hours due to slope saturation.</p>
        </div>
    """, unsafe_allow_html=True)

    ca1, ca2 = st.columns(2)
    with ca1:
        st.subheader("🟢 Safe Assembly Points")
        st.success("📍 **Shelter #1:** Community Hall Sector 2 (1.8 km)")
        st.info("🚗 **Evacuation Route:** Highway 07 Eastbound")
    with ca2:
        st.subheader("🆘 Emergency Assistance")
        st.button("🔴 TAP TO TRANSMIT SOS LOCATION TO FIRST RESPONDERS", use_container_width=True)
        st.write("📞 **Disaster Helpline:** 1077 / 112")
