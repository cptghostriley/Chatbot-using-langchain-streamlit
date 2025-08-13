# AI Chatbot using Streamlit and LangChain

A modern, interactive chatbot application built with Streamlit and LangChain that supports multiple AI models including OpenAI's GPT-4o-mini and Google's Gemini-1.5-flash.

## 🚀 Features

- **Multi-Model Support**: Choose between OpenAI GPT-4o-mini and Google Gemini-1.5-flash
- **Interactive Chat Interface**: Modern chat UI with message history
- **Secure API Key Input**: Password-masked input for API keys
- **Real-time Responses**: Get instant responses from your chosen AI model
- **Session Management**: Conversation history is maintained throughout your session
- **Error Handling**: Robust error handling for API calls
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[LangChain](https://langchain.com/)**: Framework for developing applications with LLMs
- **[OpenAI API](https://openai.com/api/)**: GPT-4o-mini model integration
- **[Google Generative AI](https://ai.google.dev/)**: Gemini-1.5-flash model integration

## 📋 Prerequisites

Before running this application, you need:

1. **Python 3.8 or higher**
2. **API Keys** (at least one):
   - OpenAI API key (starts with `sk-`)
   - Google AI API key (starts with `AI`)

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cptghostriley/Chatbot-using-langchain-streamlit.git
   cd Chatbot-using-langchain-streamlit
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 🚀 Usage

1. **Select an AI Model**: Choose between Gemini-1.5-flash or GPT-4o-mini from the sidebar
2. **Enter API Key**: Input your corresponding API key in the password field
3. **Verify Key**: Click "Use key" to validate your API key
4. **Start Chatting**: Type your message in the chat input and press Enter
5. **View History**: Your conversation history is maintained throughout the session

## 🔑 Getting API Keys

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (starts with `sk-`)

### Google AI API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key (starts with `AI`)

## 📁 Project Structure

```
Chatbot-using-langchain-streamlit/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── LICENSE            # License file
```

## 🎯 Key Features Explained

### Multi-Model Support
Switch between different AI models seamlessly:
- **GPT-4o-mini**: Fast and efficient OpenAI model
- **Gemini-1.5-flash**: Google's latest generative AI model

### Security Features
- API keys are masked during input
- Keys are validated before use
- Error handling prevents exposure of sensitive information

### User Experience
- Real-time chat interface
- Message history preservation
- Intuitive model selection
- Clear status indicators

## 🛡️ Security Notes

- **Never commit API keys**: Keep your API keys secure and never push them to version control
- **Environment Variables**: Consider using environment variables for production deployments
- **Rate Limits**: Be aware of API rate limits for your chosen models

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**Import Errors**:
```bash
pip install --upgrade streamlit langchain-openai langchain-google-genai
```

**API Key Validation Fails**:
- Ensure OpenAI keys start with `sk-`
- Ensure Google AI keys start with `AI`
- Check for extra spaces or characters

**Connection Errors**:
- Verify internet connection
- Check API key permissions
- Ensure sufficient API credits

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/cptghostriley/Chatbot-using-langchain-streamlit/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## 🌟 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [LangChain](https://langchain.com/) for the LLM integration framework
- [OpenAI](https://openai.com/) for the GPT models
- [Google](https://ai.google.dev/) for the Gemini models

---

**Made with ❤️ using Streamlit and LangChain**
