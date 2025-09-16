# Avalanche Streamlit App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://avalanche-app-app-v2.streamlit.app/)

## Overview

Avalanche Streamlit App is a web-based analytics dashboard for product reviews, powered by Streamlit and Snowflake. It enables interactive exploration and sentiment analysis of review data, including visualizations, product filtering, and an AI-powered Q&A assistant.

**Public Demo:**  
👉 [https://avalanche-app-app-v2.streamlit.app/](https://avalanche-app-app-v2.streamlit.app/)

## Features

- **Average Sentiment by Product:**  
  Horizontal bar chart displaying each product’s average sentiment score.

- **Product Filter:**  
  Select any product to view only its reviews and associated sentiment statistics.

- **Sentiment Distribution:**  
  Histogram of sentiment scores for the selected product.

- **Review Data Table:**  
  Interactive table showing review text, shipping date, sentiment score, and product.

- **Automatic Insights:**  
  Highlights the top 5 and bottom 5 products by sentiment score.

- **AI Chatbot for Data Q&A:**  
  Ask questions about your data. The built-in chatbot uses Snowflake Cortex (Claude 3.5 Sonnet model) to answer based on the first 100 rows of review data.

## Getting Started

To run the app locally:

```bash
# Clone the repository
git clone https://github.com/Ashutosh27ind/avalanche-streamlit-app.git

# Navigate to the project directory
cd avalanche-streamlit-app

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py
```

**Note:**  
- You’ll need valid Snowflake credentials in your `.streamlit/secrets.toml` for database connection.
- Python 3.x is required.

## Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Snowflake](https://www.snowflake.com/)
- Snowflake Cortex (AI/ML Q&A)

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- GitHub: [Ashutosh27ind](https://github.com/Ashutosh27ind)

## Acknowledgments

- Streamlit team for their intuitive web app framework
- Snowflake for scalable data warehousing and ML integration
