# Import libraries
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from numpy.linalg import norm
from termcolor import colored
import pandas as pd
import numpy as np
import PyPDF2
import re
import plotly.graph_objects as go
import nltk
import customtkinter as ctk
import os
import shutil
import Datasets
from upload_file import upload_file


nltk.download('punkt')

def algorithm(jd, path):
    # Load data
    df = pd.read_csv(f'{path}Datasets/nyc-jobs-1.csv')
    # Check data
    df.head()
    
    # Show column name
    df.columns
    print(df.columns)
    
    df =df[['Business Title', 'Job Description', 'Minimum Qual Requirements', 'Preferred Skills']]
    df.head()
    print(df.columns)
    
    
    # Create a new column called 'data' and merge the values of the other columns into it
    df['data'] = df[['Business Title', 'Job Description', 'Minimum Qual Requirements', 'Preferred Skills']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
    # Drop the individual columns if you no longer need them
    df.drop(['Business Title', 'Job Description', 'Minimum Qual Requirements', 'Preferred Skills'], axis=1, inplace=True)
    # Preview the updated dataframe
    print(df.head())
    
    # Tag data
    data = list(df['data'])
    tagged_data = [TaggedDocument(words = word_tokenize(_d.lower()), tags = [str(i)]) for i, _d in enumerate(data)]
    
    # Model initialization
    model = Doc2Vec(vector_size = 50,
    min_count = 5,
    epochs = 100,
    alpha = 0.001
    )
    
    # Vocabulary building
    # model.build_vocab(tagged_data)
    # # Get the vocabulary keys
    # keys = model.wv.key_to_index.keys()
    # # Print the length of the vocabulary keys
    # print(len(keys))
    
    # # Train the model
    # for epoch in range(model.epochs):
    #     print(f"Training epoch {epoch+1}/{model.epochs}")
    #     model.train(tagged_data, 
    #                 total_examples=model.corpus_count, 
    #                 epochs=model.epochs)
    
    # model.save(f'{path}cv_job_maching.model')
    # print("Model saved")
    
    

    pdf = PyPDF2.PdfReader(f'{path}uploads/CV_to_be_rated.pdf')
    resume = ""
    for i in range(len(pdf.pages)):
        pageObj = pdf.pages[i]
        resume += pageObj.extract_text()
    
    # JD by input text:
    # jd = input("Paste your JD here: ")
    
    

    def preprocess_text(text):
        # Convert the text to lowercase
        text = text.lower()
        
        # Remove punctuation from the text
        text = re.sub('[^a-z]', ' ', text)
        
        # Remove numerical values from the text
        text = re.sub(r'\d+', '', text)
        
        # Remove extra whitespaces
        text = ' '.join(text.split())
        
        return text
    
    # Apply to CV and JD
    input_CV = preprocess_text(resume)
    input_JD = preprocess_text(jd)
    
    # Model evaluation
    model = Doc2Vec.load(f'{path}cv_job_maching.model')
    v1 = model.infer_vector(input_CV.split())
    v2 = model.infer_vector(input_JD.split())
    similarity = 100*(np.dot(np.array(v1), np.array(v2))) / (norm(np.array(v1)) * norm(np.array(v2)))
    print(round(similarity, 2))
    
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = similarity,
        mode = "gauge+number",
        title = {'text': "Matching percentage (%)"},
        #delta = {'reference': 100},
        gauge = {
            'axis': {'range': [0, 100]},
            'steps' : [
                {'range': [0, 50], 'color': "#FFB6C1"},
                {'range': [50, 70], 'color': "#FFFFE0"},
                {'range': [70, 100], 'color': "#90EE90"}
            ],
                 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 100}}))
    
    fig.update_layout(width=600, height=400)  # Adjust the width and height as desired
    fig.show()
    
    
    def on_button_click(app, form):
        app.destroy()
        os.system(f'python {form}')

    def init(app, title):
        app.title(f"{title}")
        app.geometry("400x200+700+400")
        ctk.set_appearance_mode("dark")
        # app.iconbitmap("../venv/Lib/site-packages/customtkinter/assets/icons/images.ico")
        app.resizable(False, False)
        
    print(similarity)
    # Print notification
    app = ctk.CTk()
    if similarity < 50:
        init(app, "Not Approved")
        label = ctk.CTkLabel(app, text="Low chance, need to modify your CV!", text_color="red", font=("Arial", 16))
        label.place(relx=0.5, rely=0.4, anchor="center")
        label = ctk.CTkLabel(app, text=f"Percentage: {round(similarity, 2)}", font=("Arial", 14))
        label.place(relx=0.5, rely=0.6, anchor="center")

        print(colored("Low chance, need to modify your CV!", "red", attrs=["bold"]))
    elif similarity >= 50 and similarity < 70:
        init(app, "Approved but needs to be modified")
        label = ctk.CTkLabel(app, text="Good you are Approved, but you can improve further!", text_color="yellow", font=("Arial", 16))
        label.place(relx=0.5, rely=0.4, anchor="center")
        label = ctk.CTkLabel(app, text=f"Percentage: {round(similarity, 2)}", font=("Arial", 14))
        label.place(relx=0.5, rely=0.6, anchor="center")

        print(colored("Good chance but you can improve further!", "yellow", attrs=["bold"]))
    else:
        init(app, "Congratulations you are Approved")
        label = ctk.CTkLabel(app, text="Excellent! Your CV is Approved.", text_color="green", font=("Arial", 16))
        label.place(relx=0.5, rely=0.4, anchor="center")
        label = ctk.CTkLabel(app, text=f"Percentage: {round(similarity, 2)}", font=("Arial", 14))
        label.place(relx=0.5, rely=0.6, anchor="center")
        
        print(colored("Excellent! You can submit your CV.", "green", attrs=["bold"]))
    app.mainloop()

# algorithm("""
# As our Python Developer, you would have the following responsibilities:
    
# Collaborate with technical and business experts to develop new KATE use cases and enhance existing functionalities.
# Train, maintain and deploy highly scalable NLU and NLP models.
# Help with integrations with data providers (internal systems and third-party applications).
# Analyze logs, debug code, identify technical issues, challenges, and bugs in the process.
# Deploy applications using CI/CD tools.
# Optimize the KATE system for maximum speed and scalability.
    
# Key competences that will help you succeed:
    
# Excellent English skills both spoken and written.
# 3+ years of experience in Software Development.
# Strong foundation in the Python programming language (at least 3 years of professional experience with Python, as well as experience with Python Frameworks and Libraries).
# Hands-on experience building and deploying chatbots.
# Experience with Machine Learning and AI.
# Relational / NoSQL databases (PostgreSQL / DynamoDB).
    
# You are a perfect fit for us if:
    
# You are eager to learn and have an open mind towards new tools, technologies, processes, and organizations.
# You are a team player who likes to help colleagues further and gets his energy from working together and acting in a solution-oriented way.
# You are a quick learner who can easily apply problem-solving, critical thinking, and analytical skills.
    
# A significant advantage would be to have:
    
# At least a bachelor’s degree in computer science or related field.
# Strong understanding of other AI tools.
# Knowledge of Rasa framework, Docker, CI/CD pipelines, Terraform, AWS Cloud Services, GitHub, Linux.
# """)
