import streamlit as st
from app.rca_engine import RCAEngine
from dotenv import load_dotenv
import re

load_dotenv()

st.set_page_config(page_title="AI Defect RCA Assistant", layout="wide")

st.title("🤖 AI Defect RCA Assistant")

engine = RCAEngine()


# -----------------------------
# Helper: Format RCA Output
# -----------------------------
def format_rca_output(rca_text: str):
    sections = {
        "Root Cause": "",
        "Impact": "",
        "Suggested Fix": "",
        "5-Why Analysis": ""
    }

    for section in sections.keys():
        pattern = rf"{section}:(.*?)(?=\n[A-Z][a-zA-Z\- ]+:|\Z)"
        match = re.search(pattern, rca_text, re.DOTALL)
        if match:
            sections[section] = match.group(1).strip()

    return sections


# -----------------------------
# Inputs
# -----------------------------
issue_key = st.text_input("Enter Jira Issue Key (e.g., QA-123)")
new_issue = st.text_area("Enter Failure Log:", height=200)


# -----------------------------
# Analyze Only
# -----------------------------
if st.button("🔍 Analyze Failure"):

    if not new_issue.strip():
        st.warning("Please enter failure log.")
    else:
        with st.spinner("Analyzing defect log..."):
            rca_text, cost = engine.analyze_failure(new_issue)

        sections = format_rca_output(rca_text)

        st.success("RCA Generated Successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔎 Root Cause")
            st.write(sections["Root Cause"])

            st.subheader("⚠ Impact")
            st.write(sections["Impact"])

        with col2:
            st.subheader("🛠 Suggested Fix")
            st.write(sections["Suggested Fix"])

            st.subheader("📊 5-Why Analysis")
            st.write(sections["5-Why Analysis"])

        st.info(f"💰 Cost for this RCA: ${cost}")


# -----------------------------
# Analyze + Update Jira
# -----------------------------
if st.button("🚀 Generate RCA & Update Jira"):

    if not issue_key.strip():
        st.warning("Please enter Jira issue key.")
    elif not new_issue.strip():
        st.warning("Please enter failure log.")
    else:
        with st.spinner("Generating RCA and updating Jira..."):
            output = engine.analyze_and_update_jira(issue_key, new_issue)

        st.success("Jira Updated Successfully!")

        st.subheader("📄 Generated RCA")
        st.write(output["rca"])

        st.subheader("💰 Cost")
        st.write(f"${output['cost']}")