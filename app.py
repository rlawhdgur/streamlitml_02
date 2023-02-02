# -*- coding : utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import plotly
import sklearn
import numpy as np


def main():

    # 코드작성
    st.title("streamlit : " + str(st.__version__))
    st.title("pandas : " + str(pd.__version__))
    st.title("matplotlib : " + str(mpl.__version__)) 
    st.title("seaborn : " + str(sns.__version__))
    st.title("plotly : " + str(sklearn.__version__))
    st.title("sklearen : " + str(np.__version__))
    st.title("numpy : " + str(plotly.__version__))
    st.title("과연!!!!??")


if __name__ == "__main__":
    main()
    