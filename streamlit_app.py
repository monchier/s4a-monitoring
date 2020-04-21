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
    "tyler": "https://insight2020a.streamlit.io/DeepNeuralAI/RL-DeepQLearning-Trading/app/",
    "lalitha": "https://insight2020a.streamlit.io/starstorms9/shape/",
    "invalid": "https://insight2020a.streamlit.io/starst",
}

status = {}
for key, url in urls.items():
    try:
        r = requests.get(url)
        status[key] = r.status_code
    except:
        status[key] = -1

st.write(status)

def is_healthy(code):
    if code >= 200 and code < 400:
        return True
    return False

for key, url in urls.items():
    st.markdown("## %s" % key)
    st.markdown("@ %s" % url)
    st.line_chart([ is_healthy(x[key].status_code) if key in x and x[key] is not None else False for x in session_state.values[-100:]])

session_state.values.append({ k:Status(v) for k, v in status.items()})

time.sleep(1)

rerun()

