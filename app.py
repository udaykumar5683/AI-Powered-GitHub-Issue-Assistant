import streamlit as st
from github_client import fetch_github_issue
from llm_service import analyze_issue_with_ai

st.set_page_config(page_title="GitHub Issue Assistant")
st.title("🤖 AI-Powered GitHub Issue Assistant")

repo_url = st.text_input("GitHub Repository URL")
issue_number = st.text_input("Issue Number")

if st.button("Analyze Issue"):
    if not repo_url or not issue_number:
        st.error("Please enter both fields")
    else:
        # Step 1: Fetch GitHub issue
        with st.spinner("Fetching GitHub issue..."):
            issue_data, error = fetch_github_issue(repo_url, issue_number)

        if error:
            st.error(error)
        else:
            st.success("Issue fetched successfully!")

            st.subheader("Issue Title")
            st.write(issue_data["title"])

            st.subheader("Issue Body")
            st.write(issue_data["body"])

            st.subheader("Comments")
            st.write(issue_data["comments"])

            # Step 2: Analyze with AI
            with st.spinner("Analyzing with AI..."):
                ai_result = analyze_issue_with_ai(issue_data)

            st.subheader("AI Analysis")
            st.code(ai_result, language="json")

            if st.button("Copy JSON"):
                st.toast("JSON copied to clipboard!")
                components.html(f"""
                    <script>
                        navigator.clipboard.writeText({json.dumps(ai_result)});
                    </script>
                """, height=0)
