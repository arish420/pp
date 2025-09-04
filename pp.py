import streamlit as st

# Example RAG response
rag_response = "The user can be contacted via [email] or call [phone] for more information."

# Placeholder mappings
data_mapping = {
    "[email]": "john.doe@example.com",
    "[phone]": "+1-202-555-0182"
}

# Replace placeholders with clickable HTML spans
html_content = rag_response
for placeholder, value in data_mapping.items():
    html_content = html_content.replace(
        placeholder,
        f'<span class="placeholder" onclick="this.innerText=\'{value}\'">{placeholder}</span>'
    )

# Add styles for clickable placeholders
st.markdown(
    f"""
    <style>
    .placeholder {{
        color: blue;
        cursor: pointer;
        text-decoration: underline;
    }}
    </style>
    <p>{html_content}</p>
    """,
    unsafe_allow_html=True
)
