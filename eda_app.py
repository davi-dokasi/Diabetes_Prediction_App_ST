import streamlit as st

# Exploratory Data Analysis packages
import pandas as pd

# Data Vizualisation PKG
import plotly.express as px

# Load Data
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    return df

def run_eda_app():
    select_distribuiton = ["Gender", "Age", "class", "Polyuria", "Polydipsia", "sudden weight loss", "weakness", "Polyphagia", "Genital thrush", "visual blurring", "Itching", "Irritability", "delayed healing", "partial paresis", "muscle stiffness", "Alopecia", "Obesity"]
    
    st.subheader("Exploratory Data Analysis")
    df = load_data("data/diabetes_data_upload.csv")
    df_encoded = load_data("data/diabetes_data_upload_clean.csv")
    freq_df = load_data("data/freqdist_of_age_data.csv")
    
    st.dataframe(df)
    
    
    submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
    if submenu == "Descriptive":
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("Data Types"):
                st.write(df.dtypes) 

        with col2:
            with st.expander("Class Distribuiton"):
                distribuition_button = st.selectbox("Select Distribuition", select_distribuiton)
                st.dataframe(df[distribuition_button].value_counts())
        
        with st.expander("Descriptive Summary"):
            st.write(df_encoded.describe())
    
    elif submenu == "Plots":
        st.subheader("Plots")
        col1, col2 = st.columns([1,2])
        with col1:
            with st.expander("Dist Plot of Selected Distribuition"):
                distribuition_button = st.selectbox("Select Distribuition", select_distribuiton)
                fig = px.histogram(df, x=distribuition_button, color="class", marginal="rug", hover_data=df.columns)
                st.plotly_chart(fig)
                
                df_dist = df[distribuition_button].value_counts().to_frame().reset_index()
                st.dataframe(df_dist, use_container_width=True)
                
                pl = px.pie(df_dist, names=f"{distribuition_button}", values=f"count")
                st.plotly_chart(pl, use_container_width=True) 
                
        with col2:
            with st.expander("Age Clean Plot"):
                
                st.dataframe(freq_df)
                fig = px.bar(freq_df, x="Age", y="count", color="Age", height=500)
                st.plotly_chart(fig)
                
        # Outlier Detection
        with st.expander("Outlier Detection Plot"):
            fig = px.box(df,  x="Age", color="class")
            st.plotly_chart(fig)
            
        with st.expander("Correlation Plot"):
            corr_df = df_encoded.corr()
            fig = px.imshow(corr_df, color_continuous_scale='Viridis', text_auto=True)
            st.plotly_chart(fig, use_container_width=True)