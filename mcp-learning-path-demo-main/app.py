import streamlit as st
import toml
from utils import run_agent_sync

config = toml.load("config.toml")

st.set_page_config(page_title="MCP POC", page_icon="🤖", layout="wide")

st.title("Model Context Protocol(MCP) - Learning Path Generator")


# Initialize session state
if 'current_step' not in st.session_state:
    st.session_state.current_step = ""
if 'progress' not in st.session_state:
    st.session_state.progress = 0
if 'last_section' not in st.session_state:
    st.session_state.last_section = ""
if 'is_generating' not in st.session_state:
    st.session_state.is_generating = False

# --- Predefined Credentials ---
google_api_key = config["api_keys"]["google_api_key"]
youtube_pipedream_url = config["pipedream_urls"]["youtube"]
drive_pipedream_url = config["pipedream_urls"]["drive"]
notion_pipedream_url = config["pipedream_urls"]["notion"]

# --- Sidebar for Display ---
st.sidebar.header("🔐 Credentials (Read-Only)")

st.sidebar.text_input("Google API Key", value=google_api_key, disabled=True)
st.sidebar.text_input("YouTube URL", value=youtube_pipedream_url, disabled=True)

secondary_tool = st.sidebar.radio("Secondary Tool", ["Drive", "Notion"])

if secondary_tool == "Drive":
    st.sidebar.text_input("Drive URL", value=drive_pipedream_url, disabled=True)
else:
    st.sidebar.text_input("Notion URL", value=notion_pipedream_url, disabled=True)

# --- Quick Guide ---
st.info("""
**Quick Guide:**
1. Pre-integrated credentials are used for Google API, YouTube, Drive, and Notion.
2. Just enter your learning goal, and click Generate.
3. Example:
    - "I want to learn python basics in 3 days"
    - "I want to learn data science basics in 10 days"
""")

# --- Main Input ---
st.header("Enter Your Goal")
user_goal = st.text_input("Enter your learning goal:",
                          help="Describe what you want to learn, and we'll generate a structured path.")

# --- Progress UI ---
progress_container = st.container()
progress_bar = st.empty()

def update_progress(message: str):
    st.session_state.current_step = message

    if "Setting up agent with tools" in message:
        section = "Setup"
        st.session_state.progress = 0.1
    elif "Added Google Drive integration" in message or "Added Notion integration" in message:
        section = "Integration"
        st.session_state.progress = 0.2
    elif "Creating AI agent" in message:
        section = "Setup"
        st.session_state.progress = 0.3
    elif "Generating your learning path" in message:
        section = "Generation"
        st.session_state.progress = 0.5
    elif "Learning path generation complete" in message:
        section = "Complete"
        st.session_state.progress = 1.0
        st.session_state.is_generating = False
    else:
        section = st.session_state.last_section or "Progress"

    st.session_state.last_section = section
    progress_bar.progress(st.session_state.progress)

    with progress_container:
        if section != st.session_state.last_section and section != "Complete":
            st.write(f"**{section}**")

        if message == "Learning path generation complete!":
            st.success("All steps completed! 🎉")
        else:
            prefix = "✓" if st.session_state.progress >= 0.5 else "→"
            st.write(f"{prefix} {message}")

# --- Generate Button ---
if st.button("Generate Learning Path", type="primary", disabled=st.session_state.is_generating):
    if not user_goal:
        st.warning("Please enter your learning goal.")
    else:
        try:
            st.session_state.is_generating = True
            st.session_state.current_step = ""
            st.session_state.progress = 0
            st.session_state.last_section = ""

            result = run_agent_sync(
                google_api_key=google_api_key,
                youtube_pipedream_url=youtube_pipedream_url,
                drive_pipedream_url=drive_pipedream_url if secondary_tool == "Drive" else None,
                notion_pipedream_url=notion_pipedream_url if secondary_tool == "Notion" else None,
                user_goal=user_goal,
                progress_callback=update_progress
            )

            st.header("Your Learning Path")
            if result and "messages" in result:
                for msg in result["messages"]:
                    st.markdown(f"📚 {msg.content}")
            else:
                st.error("No results were generated. Please try again.")
                st.session_state.is_generating = False
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please check your configuration and try again.")
            st.session_state.is_generating = False
