import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Marks Analyzer", layout="centered")

st.title("🎓 Student Marks Analyzer")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Try reading CSV
        df = pd.read_csv(uploaded_file)

        # Check if dataframe is empty
        if df.empty:
            st.warning("⚠️ The uploaded CSV file is empty.")
        else:
            st.subheader("📊 Dataset")
            st.dataframe(df)

            # Validate required columns
            required_cols = {"Name", "Subject", "Marks"}
            if not required_cols.issubset(df.columns):
                st.error("CSV must contain columns: Name, Subject, Marks")
            else:
                # Convert Marks to numeric
                df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

                st.subheader("📈 Insights")

                col1, col2, col3 = st.columns(3)
                col1.metric("Average Marks", round(df["Marks"].mean(), 2))
                col2.metric("Highest Marks", df["Marks"].max())
                col3.metric("Lowest Marks", df["Marks"].min())

                st.subheader("🎯 Filter by Subject")
                subject = st.selectbox(
                    "Select Subject",
                    df["Subject"].dropna().unique()
                )

                filtered_df = df[df["Subject"] == subject]
                st.dataframe(filtered_df)

                st.subheader("📊 Student Marks Bar Chart")
                st.bar_chart(filtered_df.set_index("Name")["Marks"])

    except pd.errors.EmptyDataError:
        st.error("❌ Uploaded CSV has no data or headers.")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

else:
    st.info("👆 Please upload a CSV file to continue")

