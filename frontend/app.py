import streamlit as st
import requests

st.set_page_config(page_title="Agentic AI Claim System", layout="centered")
st.title("📨 Raise a Support Claim - Agentic AI")

with st.form("claim_form"):
    skills = st.multiselect("Required Skills", ["Docker", "Jenkins", "Kubernetes", "Terraform", "AWS DevOps", "Azure DevOps"])
    mode = st.selectbox("Mode", ["remote", "on-site"])
    location = st.text_input("Client Location")
    submitted = st.form_submit_button("Submit Claim")

if submitted:
    if not skills or not location:
        st.warning("Please fill all required fields.")
    else:
        payload = {
            "required_skills": skills,
            "mode": mode,
            "client_location": location
        }
        try:
            # 🔁 Use this for local testing
            response = requests.post("http://127.0.0.1:8000/assign", json=payload)
            # 🚨 Replace the above line with this when deployed:
            # response = requests.post("https://your-backend.onrender.com/assign", json=payload)

            if response.status_code == 200:
                result = response.json()
                assigned = result.get("assigned")
                if assigned:
                    st.success(f"✅ Assigned: {assigned['name']} (⭐ {assigned['rating']}) - {assigned['location']}")
                else:
                    st.error("❌ No suitable technician found.")
            else:
                st.error(f"⚠️ Error: {response.status_code}")
        except Exception as e:
            st.error(f"🚨 Request failed: {e}")

st.markdown("---")
st.subheader("📊 Agent Decision Flow")

# ✅ Replace with the raw GitHub image link
st.image("https://raw.githubusercontent.com/Srihari-sasanka/project/main/backend/technician_agent_workflow.png", use_column_width=True)
