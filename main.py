import streamlit as st
import langchain_helper
st.title("Restaurant Name Genrator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",(" ","Indian","Italian","maxican","Arabic","Amarican"))
cuisine = st.sidebar.text_area("or Type a Cuisine",(" "))


if cuisine:
    response = langchain_helper.genrate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = (response['menu_items'].strip().split(","))
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)