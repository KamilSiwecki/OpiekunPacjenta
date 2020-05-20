import streamlit as st

medicines_list = ["Paracetamol", "Apap", "Insulina", "Neurofuragina", "Vibin", "Claritine"]
diseases_list = ["Cukrzyca", "Rak płuc", "Zawał serca", "Rak jelita", "Rak trzustki", "Alergia", "Astma", "Grypa",\
                 "Odra", "Ospa", "Świnka", "Różyczka"]

def ask_questions_for_all():
    pesel = ask_for_pesel()
    permanently_taken_medicines = ask_for_permanently_taken_medicines()
    constant_diseases, previous_diseases = ask_for_previous_or_constant_diseases()
    return pesel, permanently_taken_medicines, constant_diseases, previous_diseases


def ask_for_permanently_taken_medicines():
    list_of_pacient_medicines = st.multiselect("Czy zażywasz stale jakieś leki? Wypisz, jakie:", medicines_list)
    return list_of_pacient_medicines
                  
                  
def ask_for_previous_or_constant_diseases():
    constant_diseases = st.multiselect("Czy leczysz się stale na jakąś chorobę? Jeśli tak, to na jaką?", diseases_list)
    previous_diseases = st.multiselect("Czy przechodziłeś/aś ostatnio jakąs chorobę? Jeśli tak, to jaką?", diseases_list)
    return constant_diseases, previous_diseases
                                      

def ask_for_pesel():
    pesel = st.text_input("Podaj swój numer Pesel:")
    if validate_pesel(pesel):
        valid_pesel = pesel
    else:
        valid_pesel = None
    return valid_pesel
    
    
def validate_pesel(p):
    l=int(p[10])
    suma =((1*int(p[0]))+3*int(p[1])+(7*int(p[2]))+(9*int(p[3]))+(1*int(p[4]))+(3*int(p[5]))+\
           (7*int(p[6]))+(9*int(p[7]))+(1*int(p[8]))+(3*int(p[9])))
    lm = (suma%10) ## dzielenie wyniku modulo 10
    kontrola=(10-lm) #sprawdzenie ostatniej liczby kontrolnej
    if (kontrola==10) or (l==kontrola): #w przypadku liczby kontrolnej 10 i 0 sa jednoznaczne a 0 moze byc wynikiem odejmowania
        return 1 ##domyslana wartosc logczna dla ifa klasy roboczej
    else:
        return 0 ##domyslna wartosc logiczna dla elsa