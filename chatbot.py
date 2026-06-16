import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Chatbot:
    def __init__(self, data_path):
        self.faqs = pandas.read_csv(data_path)
        self.vectorizer = TfidfVectorizer()
        self.kb_vectors = None
        

    def set_vector(self):
        """Convert the FAQ questions in the knowledge base into vectors"""
        self.kb_vectors = self.vectorizer.fit_transform(self.faqs['question'])


    def get_user_vector(self, user_question):
        """Convert the user's question into a vector"""
        return self.vectorizer.transform([user_question])

    def find_best_match(self, user_question):
        """Find the best matcching FAQ for the user's question"""

        user_vector = self.get_user_vector(user_question)

        """Use cosine similarity to find the most similar FAQ question for the user's question"""
        cosine_similarities = cosine_similarity(user_vector, self.kb_vectors)
        
        # Get the index of the highest score
        best_index = np.argmax(cosine_similarities)

        best_score = cosine_similarities[0][best_index]

        # Get corresponding question and answer pair
        best_question = self.faqs.iloc[best_index]['question']
        best_answer = self.faqs.iloc[best_index]['answer']

        return best_question, best_answer, best_score

    def get_response(self, user_question, threshold=0.6):
        """Get the chatbot response, Returns answer if the confidence is above the threshold"""

        best_question, best_answer, best_score = self.find_best_match(user_question)

        if best_score >= threshold:
            return best_answer
        else:
            return "I'm sorry, I don't have an answer for that question. Please contact our support team directly for assistance."

    def user_input(self):
        """Get user input"""
        return input("You:")
    
    def chatbot_loop(self):
        """Main loop for the chatbot"""
        print("Welcome to the FAQ Chatbot! Type 'exit' to quit.")
        while True:
            user_question = self.user_input()
            if user_question.lower() == 'exit':
                print("Goodbye!")
                break
            response = self.get_response(user_question)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot = Chatbot('faqs.csv')
    chatbot.set_vector()
    chatbot.chatbot_loop()