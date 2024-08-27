#Load libraries
from openai import OpenAI
import numpy as np
from typing import List
import pandas as pd
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import os
import PyPDF2

#Load the environment variables from the .env file
load_dotenv()
key = os.environ.get("OPENAI_API_KEY")

#Initialise client
client = OpenAI(api_key=key)

#Load documents
def load_documents(directory):
    documents = {}

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            with open(os.path.join(directory, filename), 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() + '\n'
                documents[filename] = text
    
    texts = list(documents.values())  # Take the values from the dict and turn them into a single list
    return texts

#get_embedding function
#Code from: https://platform.openai.com/docs/guides/embeddings/use-cases
def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

#get_embeddings function
def get_embeddings(texts, model="text-embedding-3-small"):
    return [get_embedding(text, model=model) for text in texts]

#retrieve_documents function
def retrieve_documents(query, document_embeddings, document_texts, model="text-embedding-3-small"):
    query_embedding = get_embedding(query, model=model)
    similarities = cosine_similarity([query_embedding], document_embeddings)
    most_similar_idx = np.argmax(similarities)
    return document_texts[most_similar_idx]