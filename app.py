import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="LeetLens", page_icon="🔍", layout="wide")

st.title("🔍 LeetLens - My LeetCode Analytics")
st.markdown("### Analyzing my coding journey 🚀")
st.markdown("---")

# Top Stats
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Solved", "8", "+1")
col2.metric("Easy", "5", "+2")
col3.metric("Medium", "3", "+1")
col4.metric("Hard", "0", "0")

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    st.subheader("📈 Daily Progress")
    chart_data = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Today'],
        'Problems': [1, 2, 0, 1, 3, 2, 1]
    })
    fig = px.bar(chart_data, x='Day', y='Problems', color='Problems', color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

with colB:
    st.subheader("📊 Topic Wise")
    topic_data = pd.DataFrame({
        'Topic': ['Array', 'String', 'DP', 'Hash Table', 'Two Pointers'],
        'Count': [4, 2, 1, 1, 2]
    })
    fig2 = px.pie(topic_data, values='Count', names='Topic', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.success("✅ Built with Python + Streamlit + Plotly | Auto-deployed via GitHub")
st.markdown("**Developer:** Sarayu | Rajahmundry")
