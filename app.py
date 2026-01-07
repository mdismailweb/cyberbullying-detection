"""
Cyberbullying Detection System - Web Demo
Author: Mohd Ismail
Project: MCA Major Project, Amity University Online
"""

import streamlit as st
import pickle
import re
import string
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Cyberbullying Detection System",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS - Better contrast and readability
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    .result-box {
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem 0;
    }
    .cyberbullying {
        background-color: #ffcdd2;
        border-left: 5px solid #f44336;
    }
    .safe {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
    }
</style>
""", unsafe_allow_html=True)

# Text preprocessing function
def preprocess_text(text):
    """Clean and normalize text for prediction"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove user mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

# Load model (you'll need to create these files)
@st.cache_resource
def load_model():
    """Load trained model and vectorizer"""
    try:
        # Try to load the model
        with open('models/naive_bayes_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('models/tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        return model, vectorizer
    except FileNotFoundError:
        st.error("⚠️ Model files not found. Please train the model first.")
        return None, None

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🛡️ Cyberbullying Detection System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-Powered Social Media Safety Tool</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("About This Project")
        st.write("""
        Built as part of my MCA final year project to tackle 
        cyberbullying on social media platforms.
        
        **Model Performance:**
        - Accuracy: 92%
        - Algorithm: Naive Bayes
        - Training Data: 47,692 tweets
        
        **Developer:** Mohd Ismail  
        **Email:** mdismailzzz02@gmail.com
        **GitHub:** [mdismailweb](https://github.com/mdismailweb)
        **University:** Amity University Online  
        **Year:** 2025-26
        """)
        
        st.header("How to Use")
        st.write("""
        1. Type or paste text
        2. Click Analyze
        3. View results
        4. Check confidence score
        """)
        
        st.header("📝 Examples")
        if st.button("Example 1: Cyberbullying"):
            st.session_state.example_text = "You're so ugly, nobody likes you, go die"
        if st.button("Example 2: Harassment"):
            st.session_state.example_text = "You're such a loser, everyone hates you"
        if st.button("Example 3: Normal"):
            st.session_state.example_text = "Great job on your presentation today!"
        if st.button("Example 4: Friendly"):
            st.session_state.example_text = "Thanks for helping me with the homework!"
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Enter Text to Analyze")
        
        # Get example text if button was clicked
        default_text = st.session_state.get('example_text', '')
        
        user_input = st.text_area(
            "Paste social media text here:",
            value=default_text,
            height=150,
            placeholder="Example: 'You're so stupid, nobody likes you'"
        )
        
        analyze_button = st.button("🔍 Analyze Text", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("Tips")
        st.info("""
        **What you can check:**
        - Social media posts
        - Comments
        - Direct messages
        - Tweets
        
        **What it finds:**
        - Insults
        - Threats
        - Harassment
        - Hate speech
        """)
    
    # Analysis
    if analyze_button and user_input:
        with st.spinner("Analyzing text..."):
            # Load model
            model, vectorizer = load_model()
            
            if model is not None and vectorizer is not None:
                # Preprocess
                cleaned_text = preprocess_text(user_input)
                
                # Predict
                features = vectorizer.transform([cleaned_text])
                prediction = model.predict(features)[0]
                probabilities = model.predict_proba(features)[0]
                
                # Model has reversed labels: ['cyberbullying', 'not_cyberbullying']
                # So we need to check the string value
                is_cyberbullying = (prediction == 'cyberbullying')
                confidence = probabilities[0] if is_cyberbullying else probabilities[1]
                
                # Display results
                st.markdown("---")
                st.subheader("📊 Analysis Results")
                
                if is_cyberbullying:
                    st.markdown(f"""
                    <div class="result-box cyberbullying">
                        <h2 style="color: #c62828; font-weight: bold;">⚠️ CYBERBULLYING DETECTED</h2>
                        <h3 style="color: #d32f2f; font-weight: bold;">Confidence: {confidence*100:.1f}%</h3>
                        <p style="color: #000; font-size: 16px;"><strong>This content appears harmful.</strong> You might want to:</p>
                        <ul style="color: #000; font-size: 15px;">
                            <li>Report it to moderators</li>
                            <li>Block the user</li>
                            <li>Talk to someone if this affects you</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="result-box safe">
                        <h2 style="color: #2e7d32; font-weight: bold;">✅ NO CYBERBULLYING DETECTED</h2>
                        <h3 style="color: #388e3c; font-weight: bold;">Confidence: {confidence*100:.1f}%</h3>
                        <p style="color: #000; font-size: 16px;">This text looks safe.</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Show details
                with st.expander("🔍 View Details"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("**Original Text:**")
                        st.code(user_input)
                    with col2:
                        st.write("**Cleaned Text:**")
                        st.code(cleaned_text)
                    
                    st.write("**Prediction Probabilities:**")
                    st.write(f"- Cyberbullying: {probabilities[0]*100:.2f}%")
                    st.write(f"- Not Cyberbullying: {probabilities[1]*100:.2f}%")
            else:
                st.error("Model not loaded. Please check model files.")
    
    elif analyze_button:
        st.warning("⚠️ Please enter some text to analyze")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Developed by Mohd Ismail | MCA Project 2025-26</p>
        <p>Amity University Online</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
