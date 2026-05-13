# AI Daily Life Optimizer 🧠✨

The **AI Daily Life Optimizer** is a Streamlit-powered application designed to help users improve productivity, wellness, and daily routines. It integrates multiple data sources and machine learning techniques to provide actionable insights through an interactive dashboard.

---

## 📖 What is it?

This project combines **data science, machine learning, and visualization** to create a personal assistant dashboard. It detects focus patterns, forecasts activity trends, integrates health data from Google Fit, and provides weather insights — all in one place. The app is built to be lightweight, interactive, and visually engaging, making it easy for users to optimize their daily life.

---

## 🛠 Languages & Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web app framework for interactive dashboards
- **Plotly**: Interactive charts and visualizations
- **scikit-learn**: Machine learning (clustering, pattern detection)
- **Prophet**: Time-series forecasting
- **Google API Client & Auth**: Integration with Google Fit
- **python-dotenv**: Secure environment variable management
- **Lottie Animations**: Engaging UI animations
- **TensorFlow / PyTorch / Transformers**: For advanced ML/NLP extensions

---

## 🚀 Features

- **Focus Pattern Detection**: Uses clustering (KMeans) to identify productivity cycles.
- **Activity Forecasting**: Predicts future activity levels using Prophet.
- **Weather Insights**: Real-time weather data via API integration.
- **Google Fit Integration**: Securely fetches health metrics with Google APIs.
- **Interactive Visualizations**: Plotly charts for trends and comparisons.
- **Animations**: Lottie animations for a modern, engaging interface.
- **Modular Design**: Utilities split into `utils/` for clean code organization.

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/ai-daily-life-optimizer.git
cd ai-daily-life-optimizer
Create and activate a virtual environment:

bash
python -m venv venv
venv\Scripts\activate   # On Windows

Install dependencies:

bash
pip install -r requirements.txt

▶️ Usage
Run the app:

bash
streamlit run app.py
Open the link in your browser to explore the dashboard.

🔑 Environment Variables
Create a .env file in the project root with your API keys:

WEATHER_API_KEY=your_weather_api_key
GOOGLE_APPLICATION_CREDENTIALS=path/to/service_account.json

📂 Project Structure
ai-daily-life-optimizer/
│
├── app.py                  # Main Streamlit app
├── utils/
│   ├── weather_api.py      # Weather data integration
│   ├── health_api.py       # Google Fit integration
│   ├── pattern_detection.py# Focus clustering
│   ├── forecasting.py      # Activity forecasting
│
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
🌟 Why It’s Useful
Helps users track productivity patterns and identify focus times.

Provides forecasted activity trends for better planning.

Integrates health and fitness data for holistic wellness.

Offers weather insights to plan outdoor activities.

Delivers everything in a single interactive dashboard.

📜 License
This project is licensed under the MIT License.