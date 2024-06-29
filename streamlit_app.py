# import streamlit as sl

# sl.set_page_config(
#     page_title="Streamlit App",
#     layout='centered',
#     initial_sidebar_state='auto',
#     menu_items={
#         "Get Help": 'https://asifshahzad.me', 
#         'About': 'https://asifshahzad.me'}
# )

# sl.markdown('<h1 style="font-family: Product Sans;">Hugging <span style="color: #ff4b4b;">Face</span></h1>',unsafe_allow_html=True)


# sl.markdown('<p style="font-family: Product Sans;">First run this command for step one.</p>', unsafe_allow_html=True)

# sl.markdown("""```bash
#              $ sudo apt update""")
# sl.text("Then after completing this runt this command.")

# sl.markdown("""```bash
#              $ pip install transformers""")


import streamlit as st

# Title
st.title("To-Do List")

# Initialize session state for the tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input for new task
new_task = st.text_input("Add a new task", "")

# Add new task
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Added task: {new_task}")
    else:
        st.warning("Please enter a task before adding.")

# Display tasks
if st.session_state.tasks:
    st.subheader("Your Tasks")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        col1.write(f"{i + 1}. {task}")
        if col2.button("Remove", key=task):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()

