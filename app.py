# Core PKG's
import streamlit as st
import streamlit.components.v1 as stc 

# Import Our Mini Apps
from eda_app import run_eda_app
from ml_app import run_ml_app

st.set_page_config(page_title="Early Stage DM Risk Data App", 
                    layout="wide", 
                    initial_sidebar_state="expanded")

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
		<h4 style="color:white;text-align:center;">Diabetes </h4>
		</div>
		"""
  
desc_temp = """
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			"""


def main():
    stc.html(html_temp)
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice =="Home":
        st.markdown(desc_temp, unsafe_allow_html=True)
    
    elif choice == "EDA":
        run_eda_app()
    
    else:
        run_ml_app()
    
if __name__ == '__main__':
    main()