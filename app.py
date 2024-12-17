import streamlit as st
import requests
import pandas as pd
import pickle
import json

st.title("Books You'ld Love to read!")

book = st.text_input("Enter a book name")
# book = input("Enter a title")

with open('recommender_system/sim_test.pkl', 'rb') as file:
  sim_test = pickle.load(file)

response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={book}")
data = response.json()

json_data = json.dumps(data, indent=4)

# print(data)
list_of_books = []
image_links = []

for item in data.get('items', []):
  volumeInfo = item.get('volumeInfo', {})
  title = volumeInfo.get('title', '')
  imageLink = volumeInfo.get('imageLinks', {}).get('thumbnail', '')
  list_of_books.append(title)
  image_links.append(imageLink)

# print(list_of_books)
df = pd.DataFrame({"title": list_of_books, "link": image_links})

button = st.button("Read")

if button:

    if book in df["title"].values:

        idx = df[df["title"] == book].index[0]
        sim_scores = sorted(
            list(enumerate(sim_test[idx])), key=lambda x: x[1], reverse=True
        )
        first_elements = [item[0] for item in sim_scores]
        suggestions = df.iloc[first_elements]['title']
        
        df['title'] = df['title'][first_elements]
        print(df['title'])
        
 
        col1, col2, col3 = st.columns(3)
        
        
        with st.container():
            
            with col1:
                st.image(df['link'][0])
                st.text(df['title'][0])

            with col2:
                st.image(df['link'][1])
                st.text(df['title'][1])


            with col3:
                st.image(df['link'][2])
                st.text(df['title'][2])

                
        with st.container():
            
            with col1:
                st.image(df['link'][3])
                st.text(df['title'][3])
                

            with col2:
                st.image(df['link'][4])
                st.text(df['title'][4])

            with col3:
                st.image(df['link'][5])
                st.text(df['title'][5])
                
                
        

    else:
        print("Book not found in the dataset.")
        st.subheader("Book Not Found")
        st.text("Did You Mean This?")
        
        col1, col2, col3 = st.columns(3)
        
        
        with st.container():
            
            with col1:
                st.image(df['link'][0])
                st.text(df['title'][0])

            with col2:
                st.image(df['link'][1])
                st.text(df['title'][1])

            with col3:
                st.image(df['link'][2])
                st.text(df['title'][2])
                

        with st.container():
            
            with col1:
                st.image(df['link'][3])
                st.text(df['title'][3])

            with col2:
                st.image(df['link'][4])
                st.text(df['title'][4])

            with col3:
                st.image(df['link'][5])
                st.text(df['title'][5])
                
        
        
        
    