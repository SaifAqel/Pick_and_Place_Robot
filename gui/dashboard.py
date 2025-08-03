"""Simple Streamlit dashboard for the robot arm."""

from __future__ import annotations

import streamlit as st
from typing import List


def run_dashboard() -> None:
    st.title("Pick-and-Place Robot Arm")
    if 'running' not in st.session_state:
        st.session_state.running = False

    col1, col2 = st.columns(2)
    if col1.button("Start"):
        st.session_state.running = True
    if col2.button("Stop"):
        st.session_state.running = False

    st.markdown("### Joint Angles")
    angles: List[float] = []
    for i in range(3):
        val = st.slider(f"Joint {i+1}", -3.14, 3.14, 0.0, key=f"joint{i}")
        angles.append(val)
    st.write("Angles", angles)
    st.write("Running:" , st.session_state.running)


if __name__ == "__main__":
    run_dashboard()