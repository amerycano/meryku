import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
# Load the CSV file
house = pd.read_csv('house_clean.csv')

def main():
    st.header('This is Header')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown')
    st.write('Some Pythagorean Equation:')
    st.latex('c^2 = a^2 + b^2')
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    st.write('Displaying Data using AgGrid:')
    AgGrid(house)  # Use AgGrid to display the DataFrame

if __name__ == '__main__':
    main()
