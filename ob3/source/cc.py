import streamlit as st
import requests
response=requests.get("http://localhost/jaya.php")
if response.status_code == 200:
    data=response.json()
    st.write(" data from php " , data)
else:
    st.error("fail to retrive data fromphp")

    