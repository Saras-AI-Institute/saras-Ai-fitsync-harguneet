import streamlit as st
st.set_page_config(layout="wide", page_title="FitSync")



# Set custom CSS for styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 3em;
        color: #2E86C1;
        font-weight: bold;
        animation: fadeIn 2s ease-in-out;
    }
    .sub-title {
        font-size: 1.5em;
        color: #148F77;
        margin-bottom: 20px;
    }
    .sidebar-text {
        font-size: 1.2em;
        color: #A93226;
    }
    .content-box {
        border-radius: 15px;
        background-color: #2C3E50;
        color: #ECF0F1;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 8px 2px #ccc;
        animation: slideIn 1s ease-in-out;
    }
    .page-container {
        padding: 40px;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes slideIn {
        from {transform: translateY(30px);}
        to {transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page container for overall layout
st.markdown("<div class='page-container'>", unsafe_allow_html=True)

# Main title with animation and style
st.markdown("<div class='main-title'>✨ Welcome to FitSync ✨</div>", unsafe_allow_html=True)

# Subtitle with style
st.markdown("<div class='sub-title'>Your personal health analytics dashboard awaits!</div>", unsafe_allow_html=True)

# Main content with decorative boxes
st.markdown(
    """
    <div class='content-box'>
    🚀 **Get Started:** Use the sidebar to navigate between pages and discover insightful analytics of your health data.
    </div>
    <div class='content-box'>
    📈 **Features:**
    - **Dashboard:** View KPIs and interactive charts.
    - **Trends:** Explore data through insightful histograms and more.
    </div>
    <div class='content-box'>
    🤖 **Built with AI:** Enhance your health insights using AI-driven technology.
    </div>
    """,
    unsafe_allow_html=True
)

# Close page container
st.markdown("</div>", unsafe_allow_html=True)

# ... rest of the code ...

