from streamlit.ScriptRequestQueue import RerunData
from streamlit.ScriptRunner import RerunException
from streamlit.server.Server import Server
import streamlit.ReportThread as ReportThread


def rerun():
    """Rerun a Streamlit app from the top!"""
    #widget_states = _get_widget_states()
    #raise RerunException(RerunData(widget_states))
    raise RerunException(RerunData(None))


def _get_widget_states():
    # Hack to get the session object from Streamlit.

    ctx = ReportThread.get_report_ctx()

    session = None
    session_infos = Server.get_current()._session_info_by_id
    import streamlit as st
    st.write(session_infos.keys())

    for session_info in session_infos:
        session_info.session.request_rerun()
    #for session_info in session_infos:
    #    import streamlit as st
    #    st.write(dir(session_info.session))
    #    session_info.session.request_rerun()
    #    st.write(dir(ctx))
    #    #if session_info.session._main_dg == ctx.main_dg:
    #    #    session = session_info.session

    #if session is None:
    #    raise RuntimeError(
    #        "Oh noes. Couldn't get your Streamlit Session object"
    #        'Are you doing something fancy with threads?')
    ## Got the session object!

    return session._widget_states

