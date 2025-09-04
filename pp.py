import streamlit as st

# Example response from RAG
rag_response = "The user can be contacted via [email] for further information."

# Your placeholder mappings
data_mapping = {
    "[email]": "john.doe@example.com",
    "[phone]": "+1-202-555-0182"
}

# Split response into words
st.write("### RAG Response with Clickable Placeholders")
for word in rag_response.split():
    clean_word = word.strip(".,")  # handle punctuation
    
    # If it's a placeholder, make it clickable
    if clean_word in data_mapping:
        if st.button(clean_word):  
            st.success(f"{clean_word} → {data_mapping[clean_word]}")
    else:
        # Show normal text
        st.write(word, end=" ")
