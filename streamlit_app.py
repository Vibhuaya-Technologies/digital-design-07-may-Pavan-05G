import streamlit as st
import importlib.util
import os

st.set_page_config(page_title="Digital Design Quiz", layout="wide")
st.title("Digital Design Interview Quiz")

current_dir = os.path.dirname(__file__)
assign_dir = os.path.join(current_dir, "assignments")

# Discover sets
sets = sorted(int(f.replace("digital_design_set", "").replace(".py",""))
              for f in os.listdir(assign_dir)
              if f.startswith("digital_design_set") and f.endswith(".py"))
set_num = st.sidebar.selectbox("Select Question Set", sets)

# Load selected set
mod_path = os.path.join(assign_dir, f"digital_design_set{set_num}.py")
spec = importlib.util.spec_from_file_location("quiz_mod", mod_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
questions = mod.questions

# Display questions
st.header(f"Digital Design Set {set_num}")
for idx, q in enumerate(questions, start=1):
    st.markdown(f"**{idx}. {q}**")