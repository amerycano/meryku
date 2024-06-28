import streamlit as st
import pandas as pd

# Load the CSV file
house = pd.read_csv('house_clean.csv')

def main():
    st.header('Halaman Streamlit Mery')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown')
    st.write('Some Pythagorean Equation:')
    st.latex('c^2 = a^2 + b^2')
    st.dataframe(house)

if __name__ == '__main__':
    main()


