import pandas as pd

class Diseases:
    def __init__(self, vectorizer, model):
        self.model = model
        self.vectorizer = vectorizer
        self.quest_0 = ["Czy jesteś na coś uczulony? Jeśli tak, to na co ?",
                        "Czy nie możesz jeść niektórych potraw? Jeśli tak, to jakich?", 
                        "Czy objawy występują w określonej porze roku?"]
        self.quest_1 = ["Czy masz cukrzycę ?",
                        "Jak dawno miałaś/miałeś pobieraną krew do badań?",
                        "Czy masz przy sobie wyniki badań krwi?"]
        self.quest_2 = ["Kiedy zaczęły się objawy, które opisujesz?",
                       "Pamiętasz, jaka była ostatnia temperatura Twojego ciała, jeśli ją mierzyłaś/mierzyłeś?"]
        self.quest_3 = ["Czy jadłaś/jadłeś ostatnio coś nietypowego dla Ciebie, i co to było jeśli tak?",
                       "Czy miałaś/miałeś wcześniej problemy z trawieniem albo oddawaniem kału?"]
        self.quest_4 = ["Czy masz nadciśnienie?",
                        "Czy spożywasz dużo soli, przypraw ?",
                       "Czy palisz papierosy?",
                       "Czy często jesz tłuste, albo ogrzewane jedzenie?"]
        self.quest_5 = ["Kiedy zaczęły się objawy, które opisujesz?",
                       "Czy pracujesz w pomieszczeniu, czy poza nim?",]
        self.quest_6 = ["Czy miałaś/miałeś kiedyś wykonywaną kolonoskopię?",
                       "Czy wiadomo Ci, że ktoś z Twojej rodziny chorował na raka jelita ?",
                       "Jak często wystepują problemy z oddawaniem kału?"]
        self.quest_7 = ["Opisz przebieg zdarzenia, które doprowadziło do urazu, oraz podjęte przez Ciebie działania:"]
        self.quest_8 = ["Czy palisz papierosy?",
                       "Czy ktoś, z kim mieszkasz, pali?",
                       "Czy w miejscu pracy jesteś lub byłaś/byłaś narażona/y na dym lub pylenie?",
                       "Czy przechodziłaś/eś ostatnio grypę, przeziębienie?"]
        self.quest_9 = ["Kiedy zauważyłaś/eś pierwsze zmiany w kościach, stawach?",
                       "Kiedy zaczęły się objawy, które opisujesz?"]
        
        self.dictionary = {1: self.quest_1,
                           2: self.quest_2,
                           3: self.quest_3,
                           4: self.quest_4,
                           5: self.quest_5,
                           6: self.quest_6,
                           7: self.quest_7,
                           8: self.quest_8,
                           9: self.quest_9}
        
        
    def prepare_list_of_questions(self, text):
        list_3_top = self.predict_3_top_diseases(text)
        list_of_questions = []
        for list_element in list_3_top:
            for dict_element in self.dictionary[list_element]:
                list_of_questions.append(dict_element)
        list_of_questions_unique = list(set(list_of_questions))
        list_of_questions_unique.sort()
        return list_of_questions_unique
        
    def predict_3_top_diseases(self, text):
        predictions = self.model.predict_proba(self.vectorizer.transform([text]).toarray())
        predictions_table = pd.DataFrame(predictions.T, columns = ['pred_proba'])
        list_3_top = predictions_table.sort_values('pred_proba', ascending=False).head(3).index.tolist()
        return list_3_top
    
