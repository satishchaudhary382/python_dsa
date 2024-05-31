import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy    as np

with st.sidebar:
    st.    subheader("Input parameters")
    value_time = st.number_input("X values: ", min_value=0, max_value=100)
# if slider_time:
time = np.arange(0, value_time, 0.1)
power_consumed = np.sin(time) + np.random.normal(0, 0.1, len(time))

fig1 = plt.figure(figsize=(10, 5))
plt.plot(time, power_consumed)
plt.title("Power consumed vs Time")
plt.xlabel("Time (days)")
plt.ylabel("Power consumed (watts)")
plt.grid()
st.title("Chart for Power consumed vs Time")
st.pyplot(fig1)

st.text(
    "This is chart for the power consumed vs time (days) and the formula used are as follows."
)
st.markdown("power_consumed: $$\sin(time) + random$$")


for i in name:
    for j in sex:
        for k in city:
            print(k)
        print(j)
    print(i)

