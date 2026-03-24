import streamlit as st
import requests

st.set_page_config(page_title="AI Incident Copilot", layout="wide")

st.title("🤖 AI Incident Copilot")
st.info("🚀 AI-powered analysis for faster incident resolution")

st.write("Analyze production incidents and reduce MTTR using AI")

# Sample log button
if st.button("Use Sample Log"):
    st.session_state["log_input"] = "Database connection timeout in payment-service"

log = st.text_area("Paste incident log", height=200, key="log_input")

if st.button("Analyze Incident 🚀"):
    if log:
        try:
            res = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"log": log}
            )

            if res.status_code == 200:
                data = res.json()
                analysis = data.get("analysis", "")

                st.success("Analysis generated successfully ✅")

                # Mode indicator
                if "[MOCK MODE]" in analysis:
                    st.warning("⚠️ Running in Mock Mode (No API credits)")
                else:
                    st.success("✅ Running in AI Mode")

                st.subheader("🧠 AI Analysis")

                # Clean formatting
                st.markdown(f"```\n{analysis}\n```")

            else:
                st.error("API Error. Check backend.")

        except Exception as e:
            st.error(f"Connection Error: {e}")
    else:
        st.warning("Please enter a log first")