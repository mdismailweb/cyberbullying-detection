# 🛡️ Cyberbullying Detection System

An AI-powered web application that detects cyberbullying in social media text using Machine Learning.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)
![Accuracy](https://img.shields.io/badge/Accuracy-92%25-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📸 Screenshots

### Main Interface
The app provides a clean, user-friendly interface for analyzing social media text.

### Detection Results
Real-time detection with confidence scores and recommendations.

## 🎯 Features

- **Real-time Detection**: Instant analysis of social media text
- **High Accuracy**: 92% accuracy using Multinomial Naive Bayes
- **User-Friendly Interface**: Clean, intuitive web interface built with Streamlit
- **Confidence Scores**: Shows prediction confidence for transparency
- **Example Texts**: Pre-loaded examples to try
- **Detailed Analysis**: View preprocessed text and probability scores

## 🚀 Try It Live

👉 **[Live Demo](https://your-app-name.streamlit.app)** *(Deploy first, then add link)*

## 📊 Performance

- **Model**: Multinomial Naive Bayes
- **Accuracy**: 92%
- **Precision**: 91%
- **Recall**: 93%
- **F1-Score**: 92%
- **Dataset**: 47,692 social media posts

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/cyberbullying-detection.git
cd cyberbullying-detection
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```

4. **Open in browser**
```
http://localhost:8501
```

## 📁 Project Structure

```
cyberbullying-detection/
├── app.py                      # Main Streamlit application
├── training_notebook.ipynb     # Model training process
├── requirements.txt            # Python dependencies
├── models/
│   ├── naive_bayes_model.pkl  # Trained ML model
│   └── tfidf_vectorizer.pkl   # TF-IDF vectorizer
├── README.md                   # This file
└── LICENSE                     # MIT License
```

## 📓 Training Notebook

Check out [`training_notebook.ipynb`](training_notebook.ipynb) to see the complete model training process:
- Data preprocessing
- Feature extraction (TF-IDF)
- Model training (4 algorithms compared)
- Performance evaluation
- Model selection

## 💡 How It Works

1. **Text Preprocessing**
   - Converts to lowercase
   - Removes URLs, mentions, hashtags
   - Removes punctuation
   - Normalizes whitespace

2. **Feature Extraction**
   - TF-IDF (Term Frequency-Inverse Document Frequency)
   - Converts text to numerical features

3. **Classification**
   - Multinomial Naive Bayes model
   - Outputs: Cyberbullying / Not Cyberbullying
   - Provides confidence score

## 🎓 Academic Project

This project was developed as part of:
- **Program**: Master of Computer Applications (MCA)
- **Institution**: Amity University Online
- **Session**: 2025-2026
- **Author**: Mohd Ismail
- **Guide**: Mr. Sahabe Alam (Senior Software Developer)

## 📖 Usage Example

```python
from app import preprocess_text, load_model

# Load model
model, vectorizer = load_model()

# Analyze text
text = "You're so ugly, nobody likes you"
cleaned = preprocess_text(text)
features = vectorizer.transform([cleaned])
prediction = model.predict(features)[0]

if prediction == 1:
    print("⚠️ Cyberbullying detected!")
else:
    print("✅ Text is safe")
```

## 🌐 Deploy to Cloud

### Option 1: Streamlit Cloud (Recommended - Free)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Deploy!

### Option 2: Heroku

```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
```

### Option 3: Render

1. Go to [render.com](https://render.com)
2. Connect GitHub repo
3. Select "Web Service"
4. Deploy

## 📝 Citation

If you use this project, please cite:

```bibtex
@misc{ismail2026cyberbullying,
  author = {Ismail, Mohd},
  title = {Cyberbullying Detection in Social Media Using Machine Learning},
  year = {2026},
  institution = {Amity University Online},
  type = {MCA Major Project}
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

**Mohd Ismail**
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- GitHub: [@yourusername](https://github.com/yourusername)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Guide**: Mr. Sahabe Alam
- **Institution**: Amity University Online
- **Dataset**: Kaggle Cyberbullying Dataset
- **Libraries**: scikit-learn, Streamlit, pandas, numpy

---

<div align="center">
  <p>Built with ❤️ for a safer internet</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>
