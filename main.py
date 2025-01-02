import streamlit as st
from scarpe import scarpeWebsite, splitContent,cleanBodyContent, extractBodyContent
from parse import parseWithOllama


st.title('AI Web Scraper')
url = st.text_input('Enter a Website Url')

if st.button("Scrape Site"):
    st.write("Scraping the Website")
    result = scarpeWebsite(url)
    print(result)

    bodyContent = extractBodyContent(result)
    cleanedBodyContent = cleanBodyContent(bodyContent)
    
    st.session_state.dom_content = cleanedBodyContent

    with st.expander('View DOM content'):
        st.text_area('DOM Content', cleanedBodyContent, height=300)



if 'dom_content' in st.session_state:
    parseDescription = st.text_area('Describe what you want to parse? ')

    if st.button('Parse Content'):
        if parseDescription:
            st.write('Parsing Content')

            dom_chunks = splitContent(st.session_state.dom_content)
            result = parseWithOllama(dom_chunks, parseDescription)
            st.write(result)