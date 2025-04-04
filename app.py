import streamlit as st
import pandas as pd
import difflib

# Load SHL data (assume a sample CSV is available)
@st.cache_data
def load_data():
    return pd.read_csv("shl_catalog_sample.csv")

def find_similar_assessments(query, df):
    # Very basic similarity matching for demonstration
    scores = []
    for i, row in df.iterrows():
        combined_text = f"{row['Assessment Name']} {row['Test Type']}"
        ratio = difflib.SequenceMatcher(None, query.lower(), combined_text.lower()).ratio()
        scores.append(ratio)
    df['score'] = scores
    return df.sort_values(by="score", ascending=False).head(10)

# Streamlit UI
st.title("SHL Assessment Recommendation Tool")

st.write("Enter a job description or hiring requirement below:")
user_query = st.text_area("Job Description / Query")

if st.button("Get Recommendations") and user_query:
    data = load_data()
    results = find_similar_assessments(user_query, data)

    st.subheader("Recommended Assessments")
    st.dataframe(results[[
        "Assessment Name", "URL", "Remote Testing", "Adaptive/IRT", "Duration", "Test Type"
    ]].reset_index(drop=True))

    st.success("Top recommendations based on your input shown above.")
    print("Updates logic")
