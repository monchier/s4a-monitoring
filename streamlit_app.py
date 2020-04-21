"""Simple sliding window dashboard-style
plot that updates periodically pulling from
a random generator
"""
import streamlit as st
import time
import random
# session_state from https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92
from session_state import get
# st_rerun from https://gist.github.com/tvst/ef477845ac86962fa4c92ec6a72bb5bd
from st_rerun import rerun
import requests
from collections import namedtuple

session_state = get(values=[])

if len(session_state.values) == 0:
  session_state.values.append(dict())

Status = namedtuple("Status", ["status_code"])

urls = {
    "Tyler": "https://insight2020a.streamlit.io/DeepNeuralAI/RL-DeepQLearning-Trading/app/",
    "Lalitha": "https://insight2020a.streamlit.io/starstorms9/shape/",
    "Sidhartha": "https://insight2020a.streamlit.io/sidhartha-roy/2D-views-to-3D-Objects/Insight_MVP/streamlit/", 
    "Aaron": "https://insight2020a.streamlit.io/DeepNeuralAI/RL-DeepQLearning-Trading/app/",
    "Alireza": "https://insight2020a.streamlit.io/alistar/STTM-Insight/",
    "Fang": "https://insight2020a.streamlit.io/FangFeng-077/Explainable_Lending_Decision",

}

status = {}
for key, url in urls.items():
    try:
        r = requests.get(url)
        status[key] = r.status_code
    except:
        status[key] = -1

def is_healthy(code):
    if code >= 200 and code < 400:
        return 1
    return 0

for key, url in urls.items():
    st.markdown("## %s" % key)
    st.markdown("@ %s" % url)
    st.area_chart([ is_healthy(x[key].status_code) if key in x and x[key] is not None else 0 for x in session_state.values[-100:]])

session_state.values.append({ k:Status(v) for k, v in status.items()})

period = st.sidebar.slider("Polling period [s]", 5, 60, 5)
time.sleep(period)

rerun()

