# intranet_chatbot

The deployed app is available here: https://intranetchatbot-gqljoc98v6yaqyhlexwqpe.streamlit.app/

## How the app works

This is a simple RAG (retrieval augmented generation) chatbot for question and answering over documents from Kingston's intranet pages.

The main application code is available in app.py, while various core functionality is defined in utils.py.

Note: this app is less developed than the ASC chatbot, which is here: https://github.com/RoyalBoroughKingston/asc_rag_chatbot. This chatbot has further functionality including caching, prompting, better formatting of links and various other things.

Both apps have the same foundational code, so a first step to improving this app would be to add in some of the functionality from the ASC chatbot.

## Data

The data that has been used is from Kingston's intranet pages on Filling Your Vacancy, Starting a New Role, and Pay and Expenses. 

Since this information is not public and potentially sensitive it hasn't been uploaded to this repository. However, if you wanted to run the app locally it is just a case of PDF'ing any documents or web pages you want included and putting them in the downloaded_pdfs folder.

There are also probably some better ways of doing this that doesn't require the data to be uploaded to GitHub e.g. reading directly from an S3 bucket.

## running the app locally

First clone this repository on to your local machine.

Next, ensure that you are running the correct version of Python, which is 3.9.7.

Then, in your terminal create a virtual environment and install the required packages:

```
python -m venv intranet_chatbot_venv
source intranet_chatbot_venv/bin/activate
pip install -r requirements.txt
```

Next, create a file called .env and put your OpenAI API key inside e.g.:

```
OPENAI_API_KEY= 'your key goes here'
```

Then create a folder called .streamlit and inside it create a file called secrets.toml. Also put your OpenAI API key inside this e.g.:

```
OPENAI_API_KEY= 'your key goes here'
```

Next, run the app using the command:

```
streamlit run app.py
```

## Deploying the app to Streamlit

Deploying the app to Streamlit is very straighforward
1. First go to platform.openai.com and create an account
2. Got to dashboard > API keys > Create secret key
3. Create a key and make a copy of it
4. Visit streamlit.io and create an account
5. Connect your Streamlit account to the relevant GitHub account that has the app code
6. Click on Create App and then 'Yup, I have an app'
7. Select the relevant repository, branch and file path
8. Select 'Advanced settings', select Python version 3.9, and in the Secrets section enter OPENAI_API_KEY= ''. Enter your OpenAI API key between the apostrophes
9. Click on 'Deploy!'