import validators
import streamlit as st
import os
# 1. PromptTemplate: تم نقلها إلى المسار الدقيق داخل langchain_core
from langchain_core.prompts.prompt import PromptTemplate 

# 2. ChatGroq: تم إستيرادها بشكل صحيح من حزمتها الخاصة
from langchain_groq import ChatGroq

# 3. load_summarize_chain: تم نقل السلاسل الكلاسيكية إلى langchain-classic
from langchain_classic.chains.summarize import load_summarize_chain

# 4. YoutubeLoader و UnstructuredURLLoader: يتم استيرادهما من حزمة المجتمع
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# 2. قم بقراءة المفتاح من متغيرات البيئة (سيصبح متغير groq_api_key يحمل القيمة النصية للمفتاح)
groq_api_key = os.getenv("GROQ_API_KEY") 

## sstreamlit APP
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')



## Get the Groq API Key and url(YT or website)to be summarized
with st.sidebar:
    groq_api_key=st.text_input("Groq API Key",value="",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")

## Gemma Model USsing Groq API
llm =ChatGroq(model="qwen/qwen3-32b", groq_api_key=groq_api_key)

prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}

"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid Url. It can may be a YT video utl or website url")

    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()

                ## Chain For Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)

                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception:{e}")
                    