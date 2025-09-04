import streamlit as st

# Example RAG response
rag_response = "The user can be contacted via [email] or call [phone] for more information."

# Placeholder mappings
data_mapping = {
    "[email]": "john.doe@example.com",
    "[phone]": "+1-202-555-0182"
}

# Replace placeholders with real values
for placeholder, value in data_mapping.items():
    rag_response = rag_response.replace(placeholder, value)

# Display final response
st.write("### Final Response")
st.write(rag_response)
