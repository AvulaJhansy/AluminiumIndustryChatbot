import streamlit as st
import json
import openai
import requests
import numpy as np
import faiss
import pandas as pd
from datetime import datetime

# Retrieve API key
email = "avulajhansy6@gmail.com"
response = requests.post("http://52.66.239.27:8504/get_keys", json={"email": email})
response_json = response.json()
api_key = response_json.get('key')

# Set OpenAI API key
openai.api_key = api_key

# Load embeddings
with open('embeddings.json', 'r') as f:
    embeddings_json = json.load(f)

titles = [entry['Title'] for entry in embeddings_json]
description_embeddings = [entry['Title_Embedding'] for entry in embeddings_json]
embeddings_array = np.array(description_embeddings, dtype=np.float32)
dimension = 1536
index = faiss.IndexFlatL2(dimension)
index.add(embeddings_array)

# Load CSV file
df = pd.read_csv('preprocessdata.csv')

df['Date'] = df['Date'].str.strip()

def get_answer(query):
    # Get embedding for query
    response = openai.Embedding.create(
        input=[query],
        model="text-embedding-ada-002"
    )
    query_embedding = np.array(response['data'][0]['embedding'], dtype=np.float32)

    _, indices = index.search(np.array([query_embedding]), k=1)
    closest_idx = indices[0][0]

    
    return {
        'Title': titles[closest_idx],
        'Description': embeddings_json[closest_idx]['Description'],
        'Link': embeddings_json[closest_idx]['Link']
    }
\
st.sidebar.title('Aluminum Industry Chatbot')
option = st.sidebar.selectbox('Select a page:', ['Query', 'Check News'])

if option == 'Query':
    st.title('Aluminum Industry Chatbot - Query')

    user_query = st.text_input("Enter your query:")

    if st.button("Submit"):
        if user_query:
            answer = get_answer(user_query)
            st.write(answer['Description'])
            if 'Link' in answer:
                st.write(f"[Get Link]({answer['Link']})")

elif option == 'Check News':
    st.title('Check News by Date and Time')

   
    min_date = datetime(2024, 6, 17)
    max_date = datetime(2024, 8, 1)
    selected_date = st.date_input("Select a date:", min_date, min_value=min_date, max_value=max_date)

    
    date_str = selected_date.strftime('%Y-%m-%d')  
    filtered_data = df[df['Date'] == date_str]

    

    if filtered_data.empty:
        st.write("Sorry, no information available for this date.")
    else:
       
        time_options = sorted(filtered_data['Time'].dropna().unique())
        selected_time = st.selectbox("Select a time:", options=time_options)
        selected_row = filtered_data[filtered_data['Time'] == selected_time]
        if not selected_row.empty:
            st.write(f"**Title:** {selected_row.iloc[0]['Title']}")
            st.write(f"**Description:** {selected_row.iloc[0]['Description']}")
            st.write(f"[Get Link]({selected_row.iloc[0]['Link']})")
        else:
            st.write("Sorry, no information available for this time.")
