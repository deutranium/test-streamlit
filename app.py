import streamlit as st
import pandas as pd
import plotly.express as px

st.header("This is a header")
df = pd.read_csv("sleep_health_and_lifestyle_dataset.csv")
# st.write(df)
# st.dataframe(df)
df
# st.table(df)

# 1. scatter plot b/w any two columns
# st.scatter_chart(data=df, x="Age", y="Sleep Duration", color="Occupation")

# ---
st.markdown(
    """## A very cool dashboard
we want to discuss the following :
1. User input
2. A plot created using user input
3. Some magic commands
4. sidebar
5. divider
6. link to multipage resources
7. example dashboards
            """
)
# ---

# 2. make the above code work with plotly
# plot = px.scatter(df, x="Age", y="Sleep Duration", color="Occupation")
# st.plotly_chart(plot)

# 3. create select boxes to get user input and add it to the plot above
x_axis = st.selectbox("Select a column for x-axis", df.columns)
y_axis = st.selectbox("Select a column for y-axis", df.columns)
color_by = st.selectbox("Select a column to color by", df.columns)

plot = px.scatter(df, x=x_axis, y=y_axis, color=color_by)
st.plotly_chart(plot)
