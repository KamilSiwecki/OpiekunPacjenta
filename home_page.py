import streamlit as st
import pickle
import diseases
import questions_for_all

with open("saved_vectorizer.pickle", 'rb') as saved_vectorizer:
    vectorizer = pickle.load(saved_vectorizer)
    
with open("saved_model.pickle", 'rb') as saved_model:
    model = pickle.load(saved_model)
    
dis_detector = diseases.Diseases(vectorizer, model)

def main():

    st.title("Pomocnik Lekarza")
    st.header("Pierwszy internetowy serwis skracający kolejki do lekarza! \nCzekając w kolejce, uzupełnij poniższe pola z pytaniami. \n ")


    age = st.slider("Zaznacz swój wiek:", 5, 120, 18)
    try:
        if int(age) < 13:
            par_among = st.selectbox("Czy są z Tobą rodzice lub opiekunowie prawni ?", ['tak', 'nie', ''], index=2)
            if par_among=='tak':
                medical_history = prepare_medical_history()
                st.write(medical_history)
            else:
                why_kid_alone = st.text_input("Napisz, z jakiego powodu przyszłaś/przyszedłeś tutaj sam/a ?")
                medical_history = prepare_medical_history()
                st.write(medical_history)    
        elif int(age) < 60:
            medical_history = prepare_medical_history()
            st.write(medical_history)
        else:
            st.write("Poproś pracownika obsługi o pomoc w uzupełnieniu formularza")
            medical_history = prepare_medical_history()
            st.write(medical_history)

    except Exception as exc:
        print(exc)


def prepare_medical_history():
    pesel, permanently_taken_medicines, constant_diseases, previous_diseases = questions_for_all.ask_questions_for_all()
    description, specific_questions_answers = get_description_and_ask_specific_questions()
    medical_history = dict()
    medical_history["pesel"] = pesel
    medical_history["stałe_leki"] = permanently_taken_medicines
    medical_history["stałe_choroby"] = constant_diseases
    medical_history["przebyte_choroby"] = previous_diseases
    medical_history["opis_dolegliwości"] = description
    medical_history["odpowiedzi_na_pytania"] = specific_questions_answers
    return medical_history

    
    
def get_description_and_ask_specific_questions():
    specific_questions_answers = dict()
    diseases_description = st.text_input("Opisz dokładnie, co Ci dolega ?")
    if len(diseases_description) > 20:
        list_of_questions = dis_detector.prepare_list_of_questions(diseases_description)
        for question in list_of_questions:
            answer = st.text_input(question)
            specific_questions_answers[question] = answer
   
    return diseases_description, specific_questions_answers


if __name__ == "__main__":
    main()
    