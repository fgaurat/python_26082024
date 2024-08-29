import streamlit as st
from CustomerDAO import CustomerDAO

# streamlit run main_streamlit.py
def main():
    st.write("Hello, *World!* :sunglasses:")

    title = st.text_input("Movie title", "Life of Brian")
    
    if st.button("Movie"):
        st.write("The current movie title is", title)

    dao = CustomerDAO(r'../customers.db')
    customers = dao.find_all()
    st.table(customers)

if __name__ == '__main__':
    main()