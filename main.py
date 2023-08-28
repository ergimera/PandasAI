import pandas as pd
from pandasai import SmartDataframe
from pandasai import PandasAI
import openai
from pandasai.llm.azure_openai import AzureOpenAI
import streamlit as st 
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Use a GUI backend

openai.api_key = "87c7609674b14cd3b1518b4d2229ee96"
openai.api_base = "https://openai-cs-test01.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name = 'DaVinci03-test'

st.title("Prompt-driven data analysis with PandasAI")
uploaded_file = st.file_uploader("Upload a Excel file for analysis", type=['xlsx'])

# Instantiate a LLM
llm = AzureOpenAI(api_token=openai.api_key, api_base=openai.api_base, api_version=openai.api_version, deployment_name=deployment_name)

# create PandasAI object, passing the LLM
pandas_ai = PandasAI(llm)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df.head(3))
    prompt = st.text_area("Enter your prompt:")

    # Generate output
    if st.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            with st.spinner("Generating response..."):
                st.write(pandas_ai.run(df, prompt))
        else:
            st.warning("Please enter a prompt.")

