from snowflake.snowpark import Session
import streamlit as st

@st.cache
def create_session():
    for attempt in range(3):  # Retry 3 times
        try:
            return Session.builder.configs(st.secrets.snowflake).create()
        except Exception as e:
            if attempt < 2:
                st.warning(f"Attempt {attempt + 1} failed, retrying...")
            else:
                st.error("All connection attempts failed.")
                raise e
