import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import time

# Load environment variables
load_dotenv()

# --- API Configuration Section ---
gemini_api_key = os.environ.get("GEMINI_API_KEY")

if not gemini_api_key:
    st.error("🔑 GEMINI_API_KEY not found in environment variables")
    st.stop()

# Configure both global and Agno-specific settings
genai.configure(api_key=gemini_api_key)

# Test API connection first
try:
    test_model = genai.GenerativeModel('gemini-2.0-flash')
    test_response = test_model.generate_content("Connection test")
except Exception as e:
    st.error(f"❌ API Connection Failed: {str(e)}")
    st.stop()

# --- Agent Setup ---
web_agent = Agent(
    name="🌐 Web Researcher",
    role="Gather real-time web data",
    model=Gemini(
        id="gemini-2.0-flash",
        api_key=gemini_api_key
    ),
    tools=[DuckDuckGoTools()],
    instructions="Always cite sources with [1] notation",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="💰 Financial Analyst",
    role="Analyze stock market data",
    model=Gemini(
        id="gemini-2.0-flash",
        api_key=gemini_api_key
    ),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Format numbers with $ symbols and ▲/▼ indicators",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Gemini(
        id="gemini-2.0-flash",
        api_key=gemini_api_key
    ),
    instructions=[
        "Combine web and financial data for comprehensive analysis",
        "Use 💹 for positive trends and 🔻 for negative ones",
        "Include timestamps for all data points"
    ],
    show_tool_calls=True,
    markdown=True,
)

# --- Streamlit UI ---
st.set_page_config(
    page_title="AI Financial Analyst",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        margin-top: 1em;
    }
    .stTextArea>div>div>textarea {
        background-color: white;
        color: black;
    }
    .stMarkdown {
        background-color: white;
        padding: 1em;
        border-radius: 5px;
        margin: 0.5em 0;
        color: black;
    }
    .stMarkdown pre {
        color: black;
    }
    .stMarkdown div {
        color: black;
    }
    .stMarkdown h4 {
        color: black;
    }
    .stMarkdown p {
        color: black;
    }
    .stMarkdown code {
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("### 🎯 Analysis Options")
    temperature = st.slider("🧠 Temperature", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("📝 Max Tokens", 1000, 5000, 3000, 500)
    
    st.markdown("### 📊 Agent Selection")
    use_web_agent = st.checkbox("🌐 Web Research", value=True)
    use_finance_agent = st.checkbox("💰 Financial Analysis", value=True)
    
    st.markdown("### ℹ️ About")
    st.info("""
    This app uses Gemini 2.0 Flash to provide real-time financial analysis.
    Select your preferred agents and adjust settings for customized results.
    """)

# Main Content
st.title("📈 AI Financial Analysis Suite")

# Create three columns for the header
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""
        <div style='text-align: center; padding: 1em; background-color: #e6f3ff; border-radius: 10px;'>
            <h3>Powered by Gemini 2.0 Flash</h3>
            <p>Real-time market analysis & insights</p>
        </div>
    """, unsafe_allow_html=True)

# Activity Monitor with enhanced styling
class ActivityTracker:
    def __init__(self, container):
        self.container = container
        
    def on_thought(self, agent, thought):
        with self.container:
            st.markdown(f"""
                <div style='background-color: #f8f9fa; padding: 1em; border-radius: 5px; margin: 0.5em 0;'>
                    <h4 style='color: black;'>🧠 {agent} Thinking</h4>
                    <pre style='background-color: white; padding: 1em; border-radius: 3px; color: black;'>{thought}</pre>
                </div>
            """, unsafe_allow_html=True)
            
    def on_action(self, agent, action, inputs):
        with self.container:
            st.markdown(f"""
                <div style='background-color: #e3f2fd; padding: 1em; border-radius: 5px; margin: 0.5em 0;'>
                    <h4 style='color: black;'>⚡ {agent} Action: {action}</h4>
                    <pre style='background-color: white; padding: 1em; border-radius: 3px; color: black;'>{inputs}</pre>
                </div>
            """, unsafe_allow_html=True)
            
    def on_result(self, agent, result):
        with self.container:
            st.markdown(f"""
                <div style='background-color: #e8f5e9; padding: 1em; border-radius: 5px; margin: 0.5em 0;'>
                    <h4 style='color: black;'>✅ {agent} Result</h4>
                    <div style='background-color: white; padding: 1em; border-radius: 3px; color: black;'>{result}</div>
                </div>
            """, unsafe_allow_html=True)

# Query Input with enhanced styling
st.markdown("### 📝 Your Analysis Query")
query = st.text_area(
    "Enter your financial query:",
    "Analyze NVIDIA's current market position in AI chips including stock performance and recent news",
    height=100,
    key="query_input"
)

# Create two columns for the buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Generate Analysis", type="primary"):
        if not query.strip():
            st.warning("⚠️ Please enter a valid query")
        else:
            with st.spinner("🧠 Analyzing financial data..."):
                try:
                    # Progress bar
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.01)
                        progress_bar.progress(i + 1)
                    
                    response = agent_team.run(
                        query,
                        callbacks=[ActivityTracker(st.expander("🔍 Live Agent Activity", expanded=True))],
                        temperature=temperature,
                        max_tokens=max_tokens
                    )
                    
                    st.markdown("---")
                    st.subheader("📊 Analysis Report")
                    st.markdown(response.content.replace("$", "\$"))
                    
                except Exception as e:
                    st.error(f"❌ Analysis failed: {str(e)}")
                    st.stop()

with col2:
    if st.button("🔄 Clear Results"):
        st.experimental_rerun()

# Footer with enhanced styling
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 1em; background-color: #f8f9fa; border-radius: 10px; margin-top: 2em;">
        <p style="color: #666; margin: 0;">Powered by Gemini 2.0 Flash | Real-time market analysis</p>
        <p style="color: #999; font-size: 0.8em; margin: 0.5em 0 0 0;">© 2024 AI Financial Analysis Suite</p>
    </div>
    """, unsafe_allow_html=True)