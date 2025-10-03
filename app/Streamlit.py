import streamlit as st
from streamlit_option_menu import option_menu
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

class Page:
    def __init__(self, config: dict, storage: None | object):
        self.config = config
        
        with st.sidebar:
            try:
                OPTIONS = ["RESOURCES", "RAGENT", "NOTHING"]
                sidebar = option_menu(menu_title="RAGSANDBOX APEPE", options=OPTIONS, default_index=0)
            except:
                st.write("streamlit_option_menu module not found")
                st.write("Please install the module using the following command")
                st.write("`pip install streamlit-option-menu`")
            
        if sidebar == OPTIONS[0]:
            self.tab_resources()
        elif sidebar == OPTIONS[1]:
            self.tab_ragent()
        elif sidebar == OPTIONS[2]:
            self.tab_secret()
        else:
            st.write("Something went wrong")
    
    def tab_resources(self):
        st.header("RAGSANDBOX RESOURCES")
        
        uploaded_file = st.file_uploader(
           "Choose a file to upload to GCS",
            type=['pdf', 'txt']
        )
        
        # todo: ADD GCS INTEGRATION :"

    @st.cache_resource
    def __convo_chain(_self):
        llm = ChatGoogleGenerativeAI(
            model=_self.config["MODEL"]["MODEL_NAME"],
            google_api_key=_self.config["CREDS"]["GOOGLE_API_KEY"],
            temperature=0.7
        )
        
        memory = ConversationBufferWindowMemory(
            k=5, 
            memory_key="history", 
            return_messages=True
        )
        
        conversation_chain = ConversationChain(
            llm=llm,
            memory=memory,
            verbose=False
        )
        
        return conversation_chain
        
    def tab_ragent(self):
        st.header("RAGENT")
        convo = self.__convo_chain()

        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi! How can I help you today?"}
            ]

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("What's on your mind?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = convo.predict(input=prompt)
                    st.markdown(response)
            
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        
    def tab_secret(self):
        with st.form("my_form"):
            something = st.text_input(label="Anything", type="password")        
            submitted = st.form_submit_button("Submit")
            
        if submitted and (something == self.config["CREDS"]["APP_CRED"]):
            st.write(self.config)        
        elif submitted:
            st.write("NOTHING")