
import openai
import streamlit as st

st.set_page_config(page_title="AI Review Buster", page_icon="🕵️")
st.title("🕵️ AI Review Buster")

st.markdown("### Paste an Amazon review to detect if it's Human, AI, or Spammy:")

review = st.text_area("✍️ Amazon Review")

api_key = st.text_input("🔑 Your OpenAI API Key", type="password", help="This key is not stored anywhere.")

if st.button("Analyze"):
    if not api_key or not review:
        st.warning("Please enter both a review and your OpenAI API key.")
    else:
        try:
            openai.api_key = api_key

            prompt = f'''
You are a review authenticity detector. Given the following Amazon review, classify it as one of the following:
- HUMAN (genuine customer)
- AI-GENERATED (chatbot sounding)
- SPAMMY/FAKE (copypasted or bot-generated hype)

Also give a confidence percentage and a short explanation.

Review:
{review}
'''

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )

            result = response.choices[0].message.content.strip()
            st.success("✅ Analysis Complete")
            st.markdown("### 🧠 Result")
            st.markdown(result)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
