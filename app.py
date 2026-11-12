import streamlit as st


DEMO_USERNAME = "admin"
DEMO_PASSWORD = "password123"

st.set_page_config(page_title="Login", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f3f6fb 0%, #e8eef8 100%);
    }
    [data-testid="stForm"] {
        padding: 1.5rem;
        border: 1px solid #e3e8f0;
        border-radius: 14px;
        background: #ffffff;
        box-shadow: 0 12px 32px rgba(31, 45, 61, 0.08);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.session_state.get("authenticated"):
    st.title("Welcome back")
    st.success(f"You are logged in as **{DEMO_USERNAME}**.")
    if st.button("Log out"):
        st.session_state.authenticated = False
        st.rerun()
else:
    _, login_column, _ = st.columns([1, 1.4, 1])
    with login_column:
        st.title("Welcome back")
        st.caption("Sign in to continue to your account.")

        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input(
                "Password", type="password", placeholder="Enter your password"
            )
            submitted = st.form_submit_button("Log in", use_container_width=True)

        if submitted:
            if username == DEMO_USERNAME and password == DEMO_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect username or password.")

        st.caption("Demo credentials: `admin` / `password123`")
