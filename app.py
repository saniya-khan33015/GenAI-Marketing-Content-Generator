import streamlit as st
import os
from dotenv import load_dotenv 
load_dotenv()

print("KEY:", os.getenv("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"))

from prompt_template import build_prompt
from llm_handler import generate_content
from vector_db import retrieve_similar_examples

# Page configuration
st.set_page_config(
    page_title="GenAI Marketing Content Generator",
    page_icon="✨",
    layout="wide"
)

# Initialize session state
if "generated_content" not in st.session_state:
    st.session_state["generated_content"] = ""

# ---------- HEADER ----------

st.title("✨ Generative AI Marketing Content Generator")

st.markdown(
"""
Create **high-quality marketing content instantly** using Generative AI.

This tool can generate:

• Ad Copy  
• Blog Posts  
• Email Marketing Content  
• Social Media Posts  

Simply enter your topic and customize the tone.
"""
)

st.divider()

# ---------- SIDEBAR INPUTS ----------

st.sidebar.header("⚙️ Content Settings")

# Load environment variables from .env file
load_dotenv()

# Test OpenRouter API integration
test_output = generate_content("Hello, test message")
st.write("Test API Output:", test_output)

topic = st.sidebar.text_input(
    "Topic",
    "AI Marketing Tool"
)

audience = st.sidebar.text_input(
    "Target Audience",
    "Small Business Owners"
)

content_type = st.sidebar.selectbox(
    "Content Type",
    [
        "Ad Copy",
        "Blog Post",
        "Email Marketing",
        "Social Media Post"
    ]
)

tone = st.sidebar.selectbox(
    "Brand Tone",
    [
        "Professional",
        "Friendly",
        "Luxury",
        "Technical"
    ]
)

length = st.sidebar.selectbox(
    "Content Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

st.sidebar.divider()

st.sidebar.info(
"""
Tip 💡  
Try different tones and content types to generate varied marketing ideas.
"""
)

# ---------- ACTION BUTTONS ----------

col1, col2, col3 = st.columns(3)

generate = col1.button("🚀 Generate Content", use_container_width=True)
regenerate = col2.button("🔄 Regenerate", use_container_width=True)
clear = col3.button("🗑 Clear Output", use_container_width=True)

# ---------- CONTENT GENERATION ----------

if generate:

    with st.spinner("Generating marketing content..."):

        examples = retrieve_similar_examples(topic)

        prompt = build_prompt(
            topic,
            audience,
            content_type,
            tone,
            length,
            examples
        )

        output = generate_content(prompt)

        st.session_state["generated_content"] = output

        st.success("Content generated successfully!")

        with st.expander("🔍 Prompt Used"):
            st.code(prompt)

if regenerate:

    with st.spinner("Regenerating content..."):

        examples = retrieve_similar_examples(topic)

        prompt = build_prompt(
            topic,
            audience,
            content_type,
            tone,
            length,
            examples
        )

        output = generate_content(prompt)

        st.session_state["generated_content"] = output

if clear:
    st.session_state["generated_content"] = ""

# ---------- OUTPUT DISPLAY ----------

st.subheader("📄 Generated Marketing Content")

st.text_area(
    "Output",
    st.session_state["generated_content"],
    height=300
)

# ---------- DOWNLOAD BUTTON ----------

if st.session_state["generated_content"]:

    st.download_button(
        label="⬇ Download Content",
        data=st.session_state["generated_content"],
        file_name=f"{topic.replace(' ','_')}_marketing_content.txt",
        mime="text/plain"
    )

# ---------- FOOTER ----------

st.divider()

st.caption(
"""
GenAI Marketing Content Generator  
Built with **Streamlit + OpenAI + FAISS**
"""
)