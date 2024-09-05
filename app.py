# Core PKG's
import streamlit as st

# Import Our Mini Apps
from eda_app import run_eda_app
from ml_app import run_ml_app


def main():
    st. title("Main App")
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice =="Home":
        st.subheader("Home")
    
    elif choice == "EDA":
        run_eda_app()
    
    else:
        run_ml_app()
    
if __name__ == '__main__':
    main()