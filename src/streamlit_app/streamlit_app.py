import streamlit as st
from io import StringIO
import pandas as pd
from src.data.mock_api import get_event_data
from src.utils.line_chart import line_chart

st.title('Paralymics data')
st.dataframe(data=None, width="stretch", height="auto", *, 
    use_container_width=None, hide_index=None, column_order=None, 
    column_config=None, key=None, on_select="ignore", 
    selection_mode="multi-row", row_height=None, placeholder=None
)
st.plotly_chart(figure_or_data, use_container_width=None, *, 
    width="stretch", height="content", theme="streamlit", key=None, 
    on_select="ignore", selection_mode=('points', 'box', 'lasso'), 
    config=None, **kwargs
)
chart = line_chart("participants", df)

@st.cache_data
def load_data():
    """
    Read the JSON structured data into a pandas DataFrame.

    @st.cache_data allows the data to be cached

    Returns:
        df pandas DataFrame with the unstructured paralympics data i.e. single
        table.
    """
    para_data = get_event_data()
    df = pd.read_json(StringIO(para_data))
    df['start'] = pd.to_datetime(df['start'], dayfirst=True)
    df['end'] = pd.to_datetime(df['end'], dayfirst=True)
    return df

