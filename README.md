# Cold Email Generator

This project generates customized cold emails by analyzing the "About Us" pages of companies. Designed specifically for TrueFoundry, the tool automates the process of email generation using advanced NLP models.

## Features
- **Custom Cold Emails**: Automatically generates company-specific cold emails.
- **Powered by Advanced Models**: Utilizes Llama 3.1 and Langchain for streamlined results.
- **Vector Database Integration**: Leverages ChromaDB for fast querying of company details.

## Technologies Used
- **Langchain**
- **GroqCloud**
- **Llama 3.1**
- **ChromaDB**
- **Streamlit**

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
     
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Project Structure
- app.py: Main application file. Run using Streamlit.
- chains.py: Implements LLM Chains using ChatGroq, PromptTemplates, and JsonOutputParser.
- portfolio.py: Handles ChromaDB's vector database operations, including querying.
- utils.py: Provides text cleaning functionalities for processing output.
- requirements.txt: Lists the dependencies for the project.

## Usage
Once the app is running, input the URL of the company's "About Us" page, and the model will generate a tailored cold email for outreach.

## License
This project is licensed under the MIT License.
