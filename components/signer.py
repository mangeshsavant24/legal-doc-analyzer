import streamlit as st

def sign_ui(score, recommendations):
    st.metric(label="Risk Score", value=f"{score}/100")

    if score > 80:
        st.success("This document looks safe to sign.")
        st.button("✅ Sign Document")
    else:
        st.warning("Review recommended before signing.")
        st.button("❌ Reject Document")
        for issue in recommendations:
            st.error(f"Issue: {issue}")
