from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatOpenAI(model="gpt-5.5")
st.header("Research Tool")

#static prompt
# userInput = st.text_input("Enter your prompt")

#dynamic prompt
#creating dropdown in streamlit
paperInput = st.selectbox("Select Research Paper Name", ["Select...", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

styleInput = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Techinal", "Code-Oriented", "Mathematical"])

lengthInput = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraph)", "Long (detailed explanation)"])

#template
template = load_prompt("template.json")


if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        "paperInput": paperInput,
        "styleInput": styleInput,
        "lengthInput": lengthInput
    })

    # st.write(result.content)
    st.write(result.content)



