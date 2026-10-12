import streamlit as st
import pandas as pd
from crm_database import init_crm_db, fetch_crm_data
from classifier import classify_sentiment
import sqlite3

st.set_page_config(page_title="Indian Customer Satisfaction CRM", page_icon="🇮🇳", layout="wide")

init_crm_db()
df = fetch_crm_data()

st.title("🇮🇳 Indian Customer Satisfaction CRM Dashboard")
st.markdown("NLP-powered classification system tracking local customer feedback and metrics.")

# Metrics
col1, col2, col3, col4 = st.columns(4)
total = len(df)
sat = len(df[df['classification'] == 'Satisfied'])
neu = len(df[df['classification'] == 'Neutral'])
dis = len(df[df['classification'] == 'Dissatisfied'])

col1.metric("Total Surveys", total)
col2.metric("Satisfied Rate", f"{(sat/total)*100:.1f}%" if total > 0 else "0%")
col3.metric("Neutral Feedback", neu)
col4.metric("Dissatisfied", dis)

st.markdown("---")
st.subheader("📝 Survey Database Records")
st.dataframe(df, use_container_width=True)

st.subheader("➕ Test Live Customer Feedback")
with st.form("live_form"):
    c_name = st.text_input("Customer Name (e.g., Rajesh Sharma)")
    tier_val = st.selectbox("Tier", ["Enterprise", "Pro", "Standard", "Free"])
    comment_val = st.text_area("Feedback Comment (English / Hinglish)")
    sub = st.form_submit_button("Classify Feedback")
    
    if sub and c_name and comment_val:
        score, cl = classify_sentiment(comment_val)
        new_id = int(df['survey_id'].max() + 1) if not df.empty else 1
        
        conn = sqlite3.connect("crm_database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO surveys VALUES (?, ?, ?, ?, ?, ?, datetime('now'))",
                       (new_id, c_name, tier_val, comment_val, score, cl))
        conn.commit()
        conn.close()
        
        st.success(f"Classified as **{cl}** (Compound Score: {score})")
        st.rerun()
