# Restaurant_Bot
Chatbot 

This restaurant chatbot can be used for locating different restaurants based on cuisine, city, neighborhood. You can find the name of the restaurants that served the cuisines asked by the user. 
Dataset(https://www.kaggle.com/yelp-dataset/yelp-dataset#yelp_business_attributes.csv). The dataset is a subset of Yelp businesses, reviews, and user data. 
The tool we used for developing the chatbot is Rasa Stack. Rasa Stack consists of two modules; Rasa-core and Rasa-NLU.  Rasa-core is used for basic context and dialogue flow management. Rasa-NLU is for Natural Language Understanding. It extracts different entities from the phrases and specifies to which intents it belongs to. 
At the backend, we used python pandas dataframe for user query extraction. 

Dependencies: 

1: Python 2.7

2: Rasa-Core

3: Rasa-NLU for training 
