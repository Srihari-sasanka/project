import streamlit as st
import requests

st.set_page_config(page_title="Agentic Claim Portal")

st.title("🧠 Raise a Support Claim - Agentic AI")

with st.form("claim_form"):
    skills = st.multiselect("Required Skills", ["Docker", "Jenkins", "Kubernetes", "Terraform", "AWS DevOps", "Azure DevOps"])
    mode = st.selectbox("Mode", ["remote", "on-site"])
    location = st.text_input("Client Location")
    submitted = st.form_submit_button("Submit Claim")

if submitted:
    if not skills or not location:
        st.warning("Please fill all required fields.")
    else:
        with st.spinner("Contacting technician agents..."):
            payload = {
                "required_skills": skills,
                "mode": mode,
                "client_location": location
            }
            # 🔁 Replace this with your actual Render backend URL
            response = requests.post("https://agentic-api.onrender.com/assign", json=payload)

            if response.status_code == 200:
                assigned = response.json()["assigned"]
                if assigned:
                    st.success(f"✅ Assigned Technician: {assigned['name']} (⭐ {assigned['rating']}) - {assigned['location']}")
                else:
                    st.error("❌ No suitable technician found.")
            else:
                st.error("⚠️ Server error. Please try again.")

st.markdown("---")
st.subheader("🧭 Agent Logic Flow")
st.image("https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/technician_agent_workflow.png", use_column_width=True)
