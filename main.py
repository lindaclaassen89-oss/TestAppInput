import streamlit as st
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"Current time1:{datetime.now()}")

st.write("Current time:", datetime.now())
print(f"Current time2:{datetime.now()}")
