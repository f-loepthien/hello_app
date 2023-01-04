import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tab1, tab2, tab3 = st.tabs(["Plot1", "Plot2", "Plot3"])

with st.sidebar:
    st.write("Sidebar")

with tab1:
    x = [1,2,3,4]
    y1 = [2,2,2,2]
    y2 = [3,8,7,2]
    y3 = [5,5,5,5]

    def plot_data(options):
        fig, ax = plt.subplots()
        cols = st.columns(3)
        if "Y1" in options:
            color_y1 = cols[0].color_picker('Pick A Color for Y1', '#D02B18')
            ax.plot(x,y1, color=color_y1)
        if "Y2" in options:
            color_y2 = cols[1].color_picker('Pick A Color for Y2', '#252CBF')
            ax.plot(x,y2, color=color_y2)
        if "Y3" in options:
            color_y3 = cols[2].color_picker('Pick A Color for Y3', '#00f900')
            ax.plot(x,y3, color_y3)
        return fig

    options = st.multiselect(
        'Choose Graphs',
        ['Y1','Y2','Y3'], ["Y1","Y2","Y3"])

    st.plotly_chart(plot_data(options))
