import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("Best Company")
content = """
Collaborative Partnerships: InnovaTech believes in the power of collaboration.
 We actively engage in partnerships with other industry leaders, startups,
  and academic institutions to foster innovation and knowledge exchange.
"""
st.write(content)

st.subheader("Our team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv")


with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])





