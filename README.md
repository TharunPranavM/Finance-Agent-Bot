# 📈 AI Financial Analysis Suite

## 🚀 Overview
AI Financial Analysis Suite is an advanced AI-powered financial analytics tool that provides real-time insights into stock market trends, company performances, and financial forecasts. Built with **Gemini 2.0 Flash**, this app leverages state-of-the-art AI and web scraping technologies to assist traders, investors, and financial analysts in making data-driven decisions.

## 🎯 Features
- ✅ **Real-time Web Research** using AI-powered agents to fetch financial and business news.
- 💰 **Stock Market Analysis** with up-to-date stock trends, price predictions, and analyst recommendations.
- 🌐 **Live Web-Based Data Retrieval** using DuckDuckGo for retrieving the latest financial news and reports.
- 📊 **Stock Performance Insights** powered by **Yahoo Finance**, including historical trends and key indicators.
- 🔄 **Multi-Agent System** that allows financial research from multiple perspectives.
- 🎨 **Interactive and User-Friendly UI** built using **Streamlit** for seamless navigation.
- 🔒 **Secure API Integration** with environment-based authentication to protect sensitive credentials.
- 📈 **Customizable Query System** for users to input their own financial analysis questions.
- ⏳ **Progress Monitoring** with live status updates on data retrieval and analysis tasks.
- 🧠 **Smart AI-Based Recommendations** using machine learning for deeper financial insights.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python)
- **AI Model:** Gemini 2.0 Flash (Google Generative AI)
- **Data Sources:** DuckDuckGo API, Yahoo Finance API
- **Backend:** Python, FastAPI
- **Security:** API key authentication, `.env` configuration for credential management
- **Visualization:** Matplotlib, Pandas, Seaborn for financial charts and graphs
- **Multi-Agent System:** Agno AI for collaborative research between multiple AI agents

## 📌 Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pip package manager
- A valid **Gemini API key** for AI processing
- An active internet connection

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/AI-Financial-Analysis.git
   cd AI-Financial-Analysis
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**
   - Create a `.env` file and add the following:
     ```env
     GEMINI_API_KEY=your_api_key_here
     ```
5. **Run the Application**
   ```bash
   streamlit run app.py
   ```
6. **Access the Web App**
   - Open `http://localhost:8501` in your browser.

## 🔄 Workflow Diagram
```plaintext
┌───────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐      ┌───────────────────────┐
│  User Inputs Query   │ ─▶  │   AI Agent (Gemini)   │ ─▶  │  API Calls & Data Fetch │ ─▶  │  AI-based Analysis      │
└───────────────────────┘      └──────────────────────┘      └──────────────────────┘      └───────────────────────┘
       ▲                          │                              │                                  ▼
       │                          ▼                              ▼                                  │
 ┌───────────────────────────────────────────────────────────────────────────────────────────────┐
 │                                       Streamlit UI Display                                     │
 └───────────────────────────────────────────────────────────────────────────────────────────────┘
```

## 📊 Example Queries You Can Ask
- "Analyze NVIDIA’s current stock performance and future outlook."
- "Compare Tesla and Ford’s financial growth over the last five years."
- "Retrieve the latest news on cryptocurrency regulations."
- "Predict Apple’s stock trend for the next quarter based on AI insights."
- "Summarize key financial takeaways from recent Google earnings reports."

---
