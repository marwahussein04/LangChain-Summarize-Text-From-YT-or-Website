# 🚀 LangChain Summarize: YouTube & Web Content

This is a Streamlit web application that leverages the power of **LangChain** and the **Groq API** to provide rapid and concise summaries of content from both YouTube videos and general web articles.

The application is built to help users quickly grasp the key points of large pieces of online content, making information consumption faster and more efficient.

## ✨ Key Features

* **Fast Summarization:** Utilizes high-speed Large Language Models (LLMs) like Mixtral-8x7B via the Groq API for near-instant summaries.
* **Dual Input Support:** Accepts both **YouTube URLs** (extracts transcript) and **General Web Article URLs** (extracts text content).
* **Structured Output:** Generates a summary with a clear title and bulleted key points for easy reading.
* **User-Provided API Key:** Securely handles the Groq API Key through a dedicated input field (sidebar) or Environment Variables.
* **Built with Streamlit:** Provides a clean, interactive, and easy-to-use web interface.

## 🛠️ Technologies Used

* **Framework:** [Streamlit](https://streamlit.io/)
* **LLM Orchestration:** [LangChain](https://www.langchain.com/) (using `langchain-core`, `langchain-classic`, `langchain-community`, `langchain-text-splitters`)
* **Language Model:** Groq API (`mixtral-8x7b-32768`)
* **Loaders:** `YoutubeLoader` and `UnstructuredURLLoader`

## ⚙️ Local Setup & Run

Follow these steps to get the application running on your local machine:

### Prerequisites

1.  **Python:** Ensure you have Python 3.8+ installed.
2.  **Groq API Key:** Get your key from [Groq Console](https://console.groq.com/keys).

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/marwahussein04/LangChain-Summarize-Text-From-YT-or-Website.git](https://github.com/marwahussein04/LangChain-Summarize-Text-From-YT-or-Website.git)
    cd LangChain-Summarize-Text-From-YT-or-Website
    ```
2.  **Create and Activate Environment (Recommended):**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate   # On Windows
    # source venv/bin/activate # On Linux/Mac
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

1.  **Set API Key (Optional but recommended):**
    Create a file named `.env` in the project root and add your key:
    ```
    GROQ_API_KEY="gfsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```
2.  **Run the Streamlit Application:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser.

## 🤝 Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request if you find any bugs or have suggestions for improvements.
