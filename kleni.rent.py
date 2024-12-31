#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:31:24 2024

@author: thodoreskourtales
"""

import streamlit as st

def main():
    st.set_page_config(page_title="Υπολογιστής Επένδυσης σε Ακίνητο", layout="wide")
    st.title("Υπολογιστής Επένδυσης σε Ακίνητο")

    # Sidebar για εισαγωγή δεδομένων
    st.sidebar.header("Παράμετροι Επένδυσης")

    # Εισαγωγή αρχικού budget
    αρχικό_budget = st.sidebar.number_input(
        "Αρχικό Budget (€)",
        min_value=1000.0,
        max_value=100000.0,
        value=10000.0,
        step=1000.0
    )

    # Εισαγωγή αριθμού ετών επένδυσης
    ανάλυση_επένδυσης = st.sidebar.slider(
        "Πόσα χρόνια θα έχει το ακίνητο διαθέσιμο;",
        min_value=1,
        max_value=30,
        value=2,
        step=1
    )

    st.sidebar.markdown("---")

    # Εισαγωγή δεδομένων για Γιορτές
    st.sidebar.subheader("Γιορτές Ενοικίασης")

    γιορτές = {
        "Πάσχα": {
            "μέρες": st.sidebar.slider(
                "Πόσες μέρες θα νοικιάσεις κατά το Πάσχα ανά έτος;",
                min_value=0,
                max_value=30,
                value=10,
                step=1
            ),
            "τιμή": st.sidebar.number_input(
                "Τιμή ενοικίου για το Πάσχα (€ ανά μέρα)",
                min_value=50.0,
                max_value=500.0,
                value=100.0,
                step=10.0
            )
        },
        "Χριστούγεννα": {
            "μέρες": st.sidebar.slider(
                "Πόσες μέρες θα νοικιάσεις κατά τα Χριστούγεννα ανά έτος;",
                min_value=0,
                max_value=30,
                value=10,
                step=1
            ),
            "τιμή": st.sidebar.number_input(
                "Τιμή ενοικίου για τα Χριστούγεννα (€ ανά μέρα)",
                min_value=50.0,
                max_value=500.0,
                value=120.0,
                step=10.0
            )
        },
        "Άλλες Γιορτές": {
            "μέρες": st.sidebar.slider(
                "Πόσες μέρες θα νοικιάσεις για άλλες γιορτές ανά έτος;",
                min_value=0,
                max_value=60,
                value=20,
                step=1
            ),
            "τιμή": st.sidebar.number_input(
                "Τιμή ενοικίου για άλλες γιορτές (€ ανά μέρα)",
                min_value=50.0,
                max_value=500.0,
                value=90.0,
                step=10.0
            )
        }
    }

    st.sidebar.markdown("---")

    # Εισαγωγή δεδομένων για Καλοκαίρι
    st.sidebar.subheader("Καλοκαίρι Ενοικίασης")

    καλοκαίρι_μέρες = st.sidebar.slider(
        "Πόσες μέρες θα νοικιάσεις το καλοκαίρι ανά έτος;",
        min_value=0,
        max_value=180,
        value=90,
        step=1
    )
    τιμή_καλοκαίρι = st.sidebar.number_input(
        "Τιμή ενοικίου για το καλοκαίρι (€ ανά μέρα)",
        min_value=50.0,
        max_value=500.0,
        value=80.0,
        step=10.0
    )

    st.sidebar.markdown("---")

    # Υπολογισμός συνολικών ημερών σε γιορτές και καλοκαίρι
    συνολικές_γιορτές_μέρες = sum([γιορτές[γ]["μέρες"] for γ in γιορτές])
    συνολικές_καλοκαιρινές_μέρες = καλοκαίρι_μέρες

    # Υπολογισμός κανονικών ημερών
    συνολικές_κανονικές_μέρες = 365 - συνολικές_γιορτές_μέρες - συνολικές_καλοκαιρινές_μέρες
    συνολικές_κανονικές_μέρες = max(συνολικές_κανονικές_μέρες, 0)

    # Εισαγωγή δεδομένων για Κανονικές Περιόδους
    st.sidebar.subheader("Κανονικές Περιόδους Ενοικίασης")
    τιμή_κανονικές = st.sidebar.number_input(
        "Τιμή ενοικίου για τις κανονικές περιόδους (€ ανά μέρα)",
        min_value=20.0,
        max_value=300.0,
        value=50.0,
        step=10.0
    )

    st.sidebar.markdown("---")
    st.sidebar.info("**Σημείωση:** Οι ημέρες που δεν καλύπτονται από γιορτές ή καλοκαίρι θεωρούνται κανονικές περιόδους.")

    # Υπολογισμοί
    εισόδημα_γιορτές = sum([γιορτές[γ]["μέρες"] * γιορτές[γ]["τιμή"] for γ in γιορτές])
    εισόδημα_καλοκαίρι = συνολικές_καλοκαιρινές_μέρες * τιμή_καλοκαίρι
    εισόδημα_κανονικές = συνολικές_κανονικές_μέρες * τιμή_κανονικές

    συνολικό_εισόδημα_ανά_έτος = εισόδημα_γιορτές + εισόδημα_καλοκαίρι + εισόδημα_κανονικές
    συνολικό_εισόδημα = συνολικό_εισόδημα_ανά_έτος * ανάλυση_επένδυσης

    συνολικό_κόστος = αρχικό_budget
    κέρδος = συνολικό_εισόδημα - συνολικό_κόστος
    απόδοση = (κέρδος / συνολικό_κόστος) * 100 if συνολικό_κόστος != 0 else 0

    συνολικό_έσοδο = συνολικό_κόστος + κέρδος
    ποσοστό_απόδοσης = (συνολικό_έσοδο / συνολικό_κόστος) * 100 if συνολικό_κόστος != 0 else 0

    # Υπολογισμός για ROI=0
    # Το συνολικό εισόδημα πρέπει να ισούται με το συνολικό κόστος
    # Δηλαδή: εισόδημα_γιορτές + εισόδημα_καλοκαίρι + εισόδημα_κανονικές = αρχικό_budget
    # Αν οι τιμές για γιορτές και καλοκαίρι είναι δοσμένες, υπολογίζουμε την τιμή για κανονικές περιόδους

    # Έλεγχος αν υπάρχουν κανονικές μέρες
    if συνολικές_κανονικές_μέρες > 0:
        απαραίτητη_τιμή_κανονικές = (συνολικό_κόστος - εισόδημα_γιορτές - εισόδημα_καλοκαίρι) / συνολικές_κανονικές_μέρες
        απαραίτητη_τιμή_κανονικές = max(απαραίτητη_τιμή_κανονικές, 0)
    else:
        απαραίτητη_τιμή_κανονικές = 0

    # ---------------- Εμφάνιση Αποτελεσμάτων ---------------- #

    st.header("### Αποτελέσματα")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Συνολικό Εισόδημα Ανά Έτος")
        st.write(f"**Γιορτές:** €{εισόδημα_γιορτές:.2f}")
        st.write(f"**Καλοκαίρι:** €{εισόδημα_καλοκαίρι:.2f}")
        st.write(f"**Κανονικές Περιόδους:** €{εισόδημα_κανονικές:.2f}")
        st.write(f"**Συνολικό Εισόδημα Ανά Έτος:** €{συνολικό_εισόδημα_ανά_έτος:.2f}")

    with col2:
        st.subheader(f"Συνολικό Εισόδημα για {ανάλυση_επένδυσης} χρόνια")
        st.write(f"**Συνολικό Εισόδημα:** €{συνολικό_εισόδημα:.2f}")

    st.subheader("Κέρδος και Απόδοση")
    st.write(f"**Κέρδος:** €{κέρδος:.2f}")
    st.write(f"**Απόδοση (ROI):** {απόδοση:.2f}%")

    st.subheader("Συνολικό Έσοδο και Ποσοστό Απόδοσης")
    st.write(f"**Συνολικό Έσοδο:** €{συνολικό_έσοδο:.2f}")
    st.write(f"**Ποσοστό Απόδοσης:** {ποσοστό_απόδοσης:.2f}%")

    st.subheader("Λεπτομέρειες Περιόδων")
    st.write(f"**Συνολικές Γιορτές Ημέρες:** {συνολικές_γιορτές_μέρες} μέρες")
    for γ in γιορτές:
        st.write(f" - {γ}: {γιορτές[γ]['μέρες']} μέρες με τιμή €{γιορτές[γ]['τιμή']}/μέρα")
    st.write(f"**Συνολικές Καλοκαιρινές Ημέρες:** {συνολικές_καλοκαιρινές_μέρες} μέρες με τιμή €{τιμή_καλοκαίρι}/μέρα")
    st.write(f"**Συνολικές Κανονικές Ημέρες:** {συνολικές_κανονικές_μέρες} μέρες με τιμή €{τιμή_κανονικές:.2f}/μέρα")
    st.write(f"**Απαραίτητη Τιμή Κανονικών Περιόδων για ROI=0:** €{απαραίτητη_τιμή_κανονικές:.2f}/μέρα")

    # -------- Επεξήγηση Όρων (με σωστή εμφάνιση LaTeX) -------- #
    st.header("### Επεξήγηση Όρων")

    with st.expander("Τι είναι η Απόδοση (ROI);"):
        st.markdown(r"""
            **Απόδοση (ROI - Return on Investment)** είναι ένα μέτρο που χρησιμοποιείται για να αξιολογήσει την 
            αποδοτικότητα μιας επένδυσης. 
            
            Υπολογίζεται ως το ποσοστό του κέρδους σε σχέση με το αρχικό κόστος της επένδυσης:
            
            \[
            ROI (\%) = \left( \frac{\text{Κέρδος}}{\text{Αρχικό Budget}} \right) \times 100
            \]
            
            **Παράδειγμα:**  
            Αν επενδύσεις 10.000€ και κερδίσεις 2.000€, τότε:
            
            \[
            ROI = \left( \frac{2000}{10000} \right) \times 100 = 20\%
            \]
        """)

    with st.expander("Τι είναι το Συνολικό Έσοδο;"):
        st.markdown(r"""
            **Συνολικό Έσοδο** είναι το συνολικό ποσό που λαμβάνεις από την επένδυσή σου, συμπεριλαμβανομένου 
            του αρχικού budget και του κέρδους.
            
            \[
            \text{Συνολικό Έσοδο} = \text{Αρχικό Budget} + \text{Κέρδος}
            \]
            
            **Παράδειγμα:**  
            Αν το αρχικό budget είναι 10.000€ και το κέρδος είναι 2.000€, τότε:
            
            \[
            \text{Συνολικό Έσοδο} = 10000 + 2000 = 12000
            \]
        """)

    # -------- Υπολογισμός Απαιτούμενων Τιμών για ROI=0 -------- #
    st.header("### Υπολογισμός Απαιτούμενων Τιμών Ενοικίασης για ROI=0")

    st.write("""
        Παρακάτω μπορείς να δεις ποια είναι η απαραίτητη τιμή ενοικίου για τις κανονικές περιόδους ώστε η Απόδοση (ROI) να είναι 0 
        (δηλαδή το συνολικό εισόδημα να καλύπτει το αρχικό budget).
    """)

    col3, col4, col5 = st.columns(3)

    with col3:
        st.subheader("Πάσχα")
        if γιορτές["Πάσχα"]["μέρες"] > 0:
            st.write(f"**Απαιτούμενο Εισόδημα:** €{γιορτές['Πάσχα']['μέρες'] * γιορτές['Πάσχα']['τιμή']:.2f}")
            st.write(f"**Απαιτούμενη Τιμή Ενοικίου:** €{γιορτές['Πάσχα']['τιμή']:.2f}/μέρα")
        else:
            st.write("Δεν υπάρχει ενοικίαση κατά το Πάσχα.")

    with col4:
        st.subheader("Καλοκαίρι")
        if συνολικές_καλοκαιρινές_μέρες > 0:
            st.write(f"**Απαιτούμενο Εισόδημα:** €{εισόδημα_καλοκαίρι:.2f}")
            st.write(f"**Απαιτούμενη Τιμή Ενοικίου:** €{τιμή_καλοκαίρι:.2f}/μέρα")
        else:
            st.write("Δεν υπάρχει ενοικίαση το καλοκαίρι.")

    with col5:
        st.subheader("Κανονικές Περιόδους")
        if συνολικές_κανονικές_μέρες > 0:
            st.write(f"**Απαιτούμενο Εισόδημα για ROI=0:** €{συνολικό_κόστος - εισόδημα_γιορτές - εισόδημα_καλοκαίρι:.2f}")
            st.write(f"**Απαραίτητη Τιμή Ενοικίου:** €{απαραίτητη_τιμή_κανονικές:.2f}/μέρα")
        else:
            st.write("Δεν υπάρχει κανονική περίοδος ενοικίασης.")

    st.write("---")

    # -------- Συνολική Ανασκόπηση -------- #
    st.header("### Συνολική Ανασκόπηση")

    col6, col7 = st.columns(2)

    with col6:
        st.subheader("Συνολικό Εισόδημα")
        st.write(f"**Συνολικό Εισόδημα για {ανάλυση_επένδυσης} χρόνια:** €{συνολικό_εισόδημα:.2f}")

    with col7:
        st.subheader("Συνολικό Κέρδος")
        st.write(f"**Κέρδος:** €{κέρδος:.2f}")

    col8, col9 = st.columns(2)

    with col8:
        st.subheader("Απόδοση (ROI)")
        st.write(f"**Απόδοση (ROI):** {απόδοση:.2f}%")

    with col9:
        st.subheader("Συνολικό Έσοδο")
        st.write(f"**Συνολικό Έσοδο:** €{συνολικό_έσοδο:.2f}")

    col10, col11 = st.columns(2)

    with col10:
        st.subheader("Ποσοστό Απόδοσης")
        st.write(f"**Ποσοστό Απόδοσης:** {ποσοστό_απόδοσης:.2f}%")

    st.header("### Συμβουλές για Αποτελεσματική Επένδυση")

    st.write("""
        - **Αξιολόγηση Τοποθεσίας:** Επιλέξτε μια περιοχή με υψηλή ζήτηση για ενοικιάσεις, 
          είτε για μόνιμους ενοικιαστές είτε για τουριστικές περιόδους.
        - **Διαχείριση Ακινήτου:** Εξετάστε το ενδεχόμενο χρήσης υπηρεσιών διαχείρισης 
          ακινήτων για να διευκολύνετε τη διαδικασία ενοικίασης.
        - **Νομικά Θέματα:** Βεβαιωθείτε ότι κατανοείτε όλες τις νομικές διαδικασίες για 
          την αγορά και ενοικίαση ακινήτων στην περιοχή σας.
        - **Φορολογία:** Κατανοήστε τις φορολογικές υποχρεώσεις που προκύπτουν από 
          την ενοικίαση ακινήτων.
    """)

if __name__ == "__main__":
    main()
