import streamlit as st

# Example RAG response
rag_response = "The user can be contacted via [email] or call [phone] for more information."

# Placeholder mappings
data_mapping = {
    "[email]": "john.doe@example.com",
    "[phone]": "+1-202-555-0182"
}

# Display paragraph with inline clickable placeholders
st.write("### RAG Response with Clickable Placeholders")

# Build paragraph dynamically
paragraph = []
for word in rag_response.split():
    clean_word = word.strip(".,")  # strip punctuation
    
    if clean_word in data_mapping:
        # Render as button, keep inline using markdown + unsafe_html
        if st.button(clean_word, key=clean_word):
            st.session_state[clean_word] = data_mapping[clean_word]
        
        # If clicked, replace placeholder with actual value
        if clean_word in st.session_state:
            paragraph.append(f"**{st.session_state[clean_word]}**")
        else:
            paragraph.append(f"[{clean_word}]")
    else:
        paragraph.append(word)

# Show final inline text
st.markdown(" ".join(paragraph))
