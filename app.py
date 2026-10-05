import streamlit as st
import pandas as pd

st.set_page_config(page_title="LeetLens", page_icon="🔍", layout="wide")

st.title("🔍 LeetLens - My LeetCode Analytics")
st.markdown("Analyzing my coding journey 🚀")
st.markdown("---")

# Top Stats
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Solved", "8", "+1")
col2.metric("Easy", "5", "2")
col3.metric("Medium", "3", "1")
col4.metric("Hard", "0", "0")

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    st.subheader("📈 Daily Progress")
    chart_data = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Today'],
        'Problems': [1, 2, 0, 1, 3, 2, 1]
    })
    st.bar_chart(chart_data.set_index('Day'))

with colB:
    st.subheader("📊 Topic Wise")
    topic_data = pd.DataFrame({
        'Topic': ['Array', 'String', 'DP', 'Hash Table'],
        'Count': [4, 2, 1, 1]
    })
    st.bar_chart(topic_data.set_index('Topic'))

st.markdown("---")
st.subheader("🔥 Recent Solved Problems")
st.table(pd.DataFrame({
    'Problem': ['0001 - Two Sum', '0002 - Add Two Numbers'],
    'Difficulty': ['Easy', 'Medium'],
    'Language': ['Python', 'Python'],
    'Status': ['✅ Accepted', '✅ Accepted']
}))

st.markdown("Made with ❤️ by Sarayu")
