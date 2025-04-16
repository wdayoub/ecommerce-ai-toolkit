
import streamlit as st
import openai

# Insert your OpenAI key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# Sample FAQ data (customize for each store)
faq_info = '''
Shipping Time: Orders ship in 2–4 business days.
Return Policy: Returns accepted within 30 days of delivery.
Tracking Info: Use order number and email to track orders at our website.
'''

def get_chat_response(user_question):
    prompt = f"""
You are a helpful eCommerce customer support agent. Answer questions using the following policy:

{faq_info}

Customer: {user_question}
Answer:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content']

def summarize_reviews(reviews):
    prompt = f"""
Summarize the key points from these customer reviews and analyze the overall sentiment.

Reviews:
{reviews}

Summary and sentiment:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']

st.set_page_config(page_title="eCommerce AI Toolkit", layout="centered")
st.title("🛍️ AI Customer Support + Review Analyzer")

tab1, tab2 = st.tabs(["💬 Chatbot", "📝 Review Analyzer"])

with tab1:
    st.subheader("Customer Support Bot")
    user_input = st.text_input("Ask a question like: 'Where's my order?'")
    if user_input:
        response = get_chat_response(user_input)
        st.success(response)

with tab2:
    st.subheader("Review Summarizer")
    reviews = st.text_area("Paste customer reviews here", height=200)
    if st.button("Summarize"):
        result = summarize_reviews(reviews)
        st.info(result)
