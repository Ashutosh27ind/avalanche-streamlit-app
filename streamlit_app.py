import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the Streamlit app
st.title("Avalanche Streamlit App")

# Connect to Snowflake (using secrets.toml)
session = st.connection("snowflake").session()

# Load data
query = """
SELECT
    PRODUCT,
    SENTIMENT_SCORE,
    SHIPPING_DATE,
    REVIEW_TEXT
FROM
    REVIEWS_WITH_SENTIMENT
"""
df_reviews = session.sql(query).to_pandas()

# Convert dates
df_reviews['SHIPPING_DATE'] = pd.to_datetime(df_reviews['SHIPPING_DATE'], errors="coerce")
#df_reviews['REVIEW_DATE'] = pd.to_datetime(df_reviews['REVIEW_DATE'], errors="coerce")

# --- Visualization: Average Sentiment by Product ---
st.subheader("Average Sentiment by Product")
product_sentiment = df_reviews.groupby("PRODUCT")["SENTIMENT_SCORE"].mean().sort_values()

fig, ax = plt.subplots()
product_sentiment.plot(kind="barh", ax=ax, title="Average Sentiment by Product")
ax.set_xlabel("Sentiment Score")
fig.tight_layout()
st.pyplot(fig)

# --- Product Filter ---
st.subheader("Filter by Product")
product = st.selectbox("Choose a product", ["All Products"] + list(df_reviews["PRODUCT"].unique()))

if product != "All Products":
    filtered_data = df_reviews[df_reviews["PRODUCT"] == product]
else:
    filtered_data = df_reviews

# Display filtered table
st.subheader(f"📁 Reviews for {product}")
st.dataframe(filtered_data)

# --- Visualization: Sentiment Distribution ---
st.subheader(f"Sentiment Distribution for {product}")
fig, ax = plt.subplots()
filtered_data['SENTIMENT_SCORE'].hist(ax=ax, bins=20)
ax.set_title("Distribution of Sentiment Scores")
ax.set_xlabel("Sentiment Score")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# --- Automatic Insights ---
st.subheader("📊 Automatic Insights")

# Top 5 products by sentiment
top_products = product_sentiment.tail(5).reset_index()
st.write("⭐ Top 5 Products by Sentiment")
st.dataframe(top_products)

# Bottom 5 products by sentiment
bottom_products = product_sentiment.head(5).reset_index()
st.write("⚠️ Bottom 5 Products by Sentiment")
st.dataframe(bottom_products)

# --- Chatbot for Q&A ---
st.subheader("💬 Ask Questions About Your Data")
user_question = st.text_input("Enter your question here:")

if user_question:
    # Limit dataset context
    df_json = df_reviews.head(100).to_json(orient="records")

    prompt = f"""
    You are a helpful data assistant.
    Use the following dataset (first 100 rows) to answer the user's question.

    Question: {user_question}
    Context: {df_json}
    """

    # Safe parameterized SQL call to Cortex
    response = session.sql(
        "SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', ?)",
        params=[prompt]
    ).collect()[0][0]

    st.write(response)


