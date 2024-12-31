#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:31:24 2024

@author: thodoreskourtales
"""

import streamlit as st

def main():
    # -- Ρύθμιση Σελίδας --
    st.set_page_config(
        page_title="Υπολογιστής Επένδυσης σε Ακίνητο", 
        layout="wide"
    )
    
    # -- Τίτλος Εφαρμογής --
    st.title("Υπολογιστής Επένδυσης σε Ακίνητο")

    # -- Sidebar για εισαγωγή δεδομένων --
    st.sidebar.header("Παράμετροι Επένδυσης")

    # Εισαγωγή αρχικού budget
    αρχικό_budget = st.sidebar.number_input(
        "Αρχικό Budget (€)",
        min_value=1000.0,
        max_value=100000.0,
        value=10000.0,  # Προεπιλεγμένη τιμή
        step=1000.0
    )

    # Εισαγωγή αριθμού ετών επένδυσης
    ανάλυση_επένδυσης = st.sidebar.slider(
        "Για πόσα χρόνια θα είναι διαθέσιμο το ακίνητο;",
        min_value=1,
        max_value=30,
        value=2,  # Προεπιλεγμένη τιμή
        step=1
    )

    st.sidebar.markdown("---")

    # Εισαγωγή δεδομένων για Εορτές
    st.sidebar.subheader("Εορτές Ενοικίασης")

    γιορτές = {
        "Πάσχα": {
            "μέρες": st.sidebar.slider(
                "Πόσες ημέρες θα νοικιάζεται το ακίνητο το Πάσχα (ανά έτος);",
                min_value=0,
                max_value=30,
                value=10,  # Προεπιλεγμένη τιμή
                step=1
            ),
            "τιμή": st.sidebar.number_input(
                "Τιμή ενοικίου κατά το Πάσχα (€ ανά ημέρα)",
                min_value=50.0,
                max_value=500.0,
                value=100.0,  # Προεπιλεγμένη τιμή
                step=10.0
            )
        },
        "Χριστούγεννα": {
            "μέρες": st.sidebar.slider(
                "Πόσες ημέρες θα νοικιάζεται το ακίνητο τα Χριστούγεννα (ανά έτος);",
                min_value=0,
                max_value=30,
                value=10,  # Προεπιλεγμένη τιμή
                step=1
            ),
            "τιμή": st.sidebar.number_input(
                "Τιμή ενοικίου κατά τα Χριστούγεννα (€ ανά ημέρα)",
                min_value=50.0,
                max_value=500.0,
                value=120.0,  # Προεπιλεγμένη τιμή
                step=10.0
            )
        },
        "Άλλες Γιορτές": {
            "μέρες": st.sidebar.slider(
                "Πόσες ημέρες θα νοικιάζεται το ακίνητο σε άλλες γιορτές (ανά έτος);",
                min_value=0,
                max_value=60,
                value=20,  # Προεπιλεγμένη τιμή
                step=1
            ),
            "τιμή": st.sidebar.number_input(
                "Τιμή ενοικίου για άλλες γιορτές (€ ανά ημέρα)",
                min_value=50.0,
                max_value=500.0,
                value=90.0,  # Προεπιλεγμένη τιμή
                step=10.0
            )
        }
    }

    st.sidebar.markdown("---")

    # Εισαγωγή δεδομένων για Καλοκαίρι
    st.sidebar.subheader("Καλοκαιρινή Περίοδος Ενοικίασης")

    καλοκαίρι_μέρες = st.sidebar.slider(
        "Πόσες ημέρες θα νοικιάζεται το ακίνητο το καλοκαίρι (ανά έτος);",
        min_value=0,
        max_value=180,
        value=90,  # Προεπιλεγμένη τιμή
        step=1
    )
    τιμή_καλοκαίρι = st.sidebar.number_input(
        "Τιμή ενοικίου για το καλοκαίρι (€ ανά ημέρα)",
        min_value=50.0,
        max_value=500.0,
        value=80.0,  # Προεπιλεγμένη τιμή
        step=10.0
    )

    st.sidebar.markdown("---")

    # Εισαγωγή δεδομένων για Κανονικές Περιόδους
    st.sidebar.subheader("Κανονικές Περίοδοι Ενοικίασης")
    # Αρχικοποίηση της τιμής κανονικών περιόδων σε 0, θα οριστεί στη συνέχεια
    if "απαραίτητη_τιμή_κανονικές" not in st.session_state:
        st.session_state["απαραίτητη_τιμή_κανονικές"] = 50.0  # Προεπιλεγμένη τιμή

    τιμή_κανονικές = st.sidebar.number_input(
        "Τιμή ενοικίου για τις κανονικές περιόδους (€ ανά ημέρα)",
        min_value=0.0,
        max_value=300.0,
        value=st.session_state["απαραίτητη_τιμή_κανονικές"],  # Προεπιλεγμένη τιμή
        step=10.0
    )

    st.sidebar.markdown("---")
    st.sidebar.info(
        "**Σημείωση:** Οι ημέρες που δεν καλύπτονται από γιορτές ή καλοκαίρι,"
        " θεωρούνται κανονικές περίοδοι."
    )

    # -- Υπολογισμοί --
    εισόδημα_γιορτές = sum([γιορτές[γ]["μέρες"] * γιορτές[γ]["τιμή"] for γ in γιορτές])
    συνολικές_γιορτές_μέρες = sum([γιορτές[γ]["μέρες"] for γ in γιορτές])
    συνολικές_καλοκαιρινές_μέρες = καλοκαίρι_μέρες
    εισόδημα_καλοκαίρι = συνολικές_καλοκαιρινές_μέρες * τιμή_καλοκαίρι
    συνολικές_κανονικές_μέρες = max(365 - συνολικές_γιορτές_μέρες - συνολικές_καλοκαιρινές_μέρες, 0)
    εισόδημα_κανονικές = συνολικές_κανονικές_μέρες * τιμή_κανονικές

    συνολικό_εισόδημα_ανά_έτος = εισόδημα_γιορτές + εισόδημα_καλοκαίρι + εισόδημα_κανονικές
    συνολικό_εισόδημα = συνολικό_εισόδημα_ανά_έτος * ανάλυση_επένδυσης

    συνολικό_κόστος = αρχικό_budget
    κέρδος = συνολικό_εισόδημα - συνολικό_κόστος
    απόδοση = (κέρδος / συνολικό_κόστος) * 100 if συνολικό_κόστος != 0 else 0

    συνολικό_έσοδο = συνολικό_κόστος + κέρδος

    # Υπολογισμός Απαραίτητης Τιμής Κανονικών Περιόδων για ROI=0
    # (Όταν το συνολικό εισόδημα = συνολικό κόστος)
    if συνολικές_κανονικές_μέρες > 0:
        roi_zero_income_for_normal = συνολικό_κόστος - εισόδημα_γιορτές - εισόδημα_καλοκαίρι
        απαραίτητη_τιμή_κανονικές = roi_zero_income_for_normal / συνολικές_κανονικές_μέρες
        απαραίτητη_τιμή_κανονικές = max(απαραίτητη_τιμή_κανονικές, 0)
        st.session_state["απαραίτητη_τιμή_κανονικές"] = απαραίτητη_τιμή_κανονικές
    else:
        απαραίτητη_τιμή_κανονικές = 0
        roi_zero_income_for_normal = 0
        st.session_state["απαραίτητη_τιμή_κανονικές"] = 0

    # ---------------- Εμφάνιση Αποτελεσμάτων ---------------- #
    st.header("Αποτελέσματα")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Συνολικό Εισόδημα Ανά Έτος")
        st.write(f"**Γιορτές:** €{εισόδημα_γιορτές:.2f}")
        st.write(f"**Καλοκαίρι:** €{εισόδημα_καλοκαίρι:.2f}")
        st.write(f"**Κανονικές Περίοδοι:** €{εισόδημα_κανονικές:.2f}")
        st.write(f"**Συνολικό Εισόδημα Ανά Έτος:** €{συνολικό_εισόδημα_ανά_έτος:.2f}")

    with col2:
        st.subheader(f"Συνολικό Εισόδημα για {ανάλυση_επένδυσης} χρόνια")
        st.write(f"**Συνολικό Εισόδημα:** €{συνολικό_εισόδημα:.2f}")

    st.subheader("Κέρδος και Απόδοση")
    st.write(f"**Κέρδος:** €{κέρδος:.2f}")
    st.write(f"**Απόδοση (ROI):** {απόδοση:.2f}%")

    st.subheader("Συνολικό Έσοδο")
    st.write(f"**Συνολικό Έσοδο:** €{συνολικό_έσοδο:.2f}")

    st.subheader("Λεπτομέρειες Περιόδων")
    st.write(f"**Συνολικές Ημέρες Γιορτών:** {συνολικές_γιορτές_μέρες} ημέρες")
    for γ in γιορτές:
        st.write(
            f"- {γ}: {γιορτές[γ]['μέρες']} ημέρες με τιμή €{γιορτές[γ]['τιμή']:.2f}/ημέρα"
        )
    st.write(
        f"**Συνολικές Καλοκαιρινές Ημέρες:** {συνολικές_καλοκαιρινές_μέρες} ημέρες "
        f"με τιμή €{τιμή_καλοκαίρι:.2f}/ημέρα"
    )
    st.write(
        f"**Συνολικές Κανονικές Ημέρες:** {συνολικές_κανονικές_μέρες} ημέρες "
        f"με τιμή €{τιμή_κανονικές:.2f}/ημέρα"
    )
    st.write(
        f"**Απαραίτητη Τιμή Κανονικών Περιόδων για ROI=0:** "
        f"€{απαραίτητη_τιμή_κανονικές:.2f}/ημέρα"
    )

    # -------- Επεξήγηση Όρων (με σωστή εμφάνιση LaTeX) -------- #
    st.header("Επεξήγηση Όρων")

    with st.expander("Τι είναι η Απόδοση (ROI);"):
        st.markdown(r"""
            **Απόδοση (ROI - Return on Investment)** είναι ένα μέτρο που χρησιμοποιείται 
            για να αξιολογήσει την αποδοτικότητα μιας επένδυσης. 
            
            Υπολογίζεται ως το ποσοστό του κέρδους σε σχέση με το αρχικό κόστος της επένδυσης:
            
            \[
            ROI (\%) = \left( \frac{\text{Κέρδος}}{\text{Αρχικό Κόστος}} \right) \times 100
            \]
            
            **Παράδειγμα:**  
            Αν επενδύσεις 10.000€ και κερδίσεις 2.000€, τότε:
            
            \[
            ROI = \left( \frac{2000}{10000} \right) \times 100 = 20\%
            \]
        """)

    # -------- Υπολογισμός Απαιτούμενων Τιμών για ROI=0 -------- #
    st.header("Υπολογισμός Απαιτούμενων Τιμών Ενοικίασης για ROI=0")

    st.write("""
        Παρακάτω βλέπεις ποια πρέπει να είναι η τιμή ενοικίου για **όλες** τις περιόδους 
        (συμπεριλαμβανομένων και των κανονικών περιόδων), ώστε η Απόδοση (ROI) να είναι 0.
        Δηλαδή το συνολικό εισόδημα να καλύπτει ακριβώς το αρχικό σου budget.
    """)

    # -- Δημιουργούμε ένα ενοποιημένο λεξικό για να δείξουμε όλες τις περιόδους με ενιαίο "μηχανισμό" --
    periods_for_roi = {
        "Πάσχα": {
            "days": γιορτές["Πάσχα"]["μέρες"],
            "price": γιορτές["Πάσχα"]["τιμή"],
            "income": γιορτές["Πάσχα"]["μέρες"] * γιορτές["Πάσχα"]["τιμή"],
        },
        "Χριστούγεννα": {
            "days": γιορτές["Χριστούγεννα"]["μέρες"],
            "price": γιορτές["Χριστούγεννα"]["τιμή"],
            "income": γιορτές["Χριστούγεννα"]["μέρες"] * γιορτές["Χριστούγεννα"]["τιμή"],
        },
        "Άλλες Γιορτές": {
            "days": γιορτές["Άλλες Γιορτές"]["μέρες"],
            "price": γιορτές["Άλλες Γιορτές"]["τιμή"],
            "income": γιορτές["Άλλες Γιορτές"]["μέρες"] * γιορτές["Άλλες Γιορτές"]["τιμή"],
        },
        "Καλοκαίρι": {
            "days": συνολικές_καλοκαιρινές_μέρες,
            "price": τιμή_καλοκαίρι,
            "income": εισόδημα_καλοκαίρι,
        },
        "Κανονικές Περίοδοι": {
            "days": συνολικές_κανονικές_μέρες,
            "price": τιμή_κανονικές,
            "income": εισόδημα_κανονικές,
        }
    }

    # -- Μετατρέπουμε το dictionary σε λίστα για να μπορούμε να κάνουμε "μπαλαριστή" παρουσίαση --
    all_periods = list(periods_for_roi.items())  
    # π.χ. [("Πάσχα", {...}), ("Χριστούγεννα", {...}), ...]

    # -- Φτιάχνουμε “σελίδες” των 3 στηλών ανά σειρά: π.χ. πρώτη σειρά έως 3 περίοδοι, δεύτερη σειρά οι υπόλοιπες --
    def chunk_list(data, chunk_size=3):
        return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    period_chunks = chunk_list(all_periods, 3)

    for chunk in period_chunks:
        # Δημιουργούμε στήλες ανά αριθμό περιόδων στο chunk
        cols = st.columns(len(chunk))
        
        for idx, (period_name, info) in enumerate(chunk):
            with cols[idx]:
                st.subheader(period_name)
                
                days = info["days"]
                price = info["price"]
                income = info["income"]
                
                if days > 0:
                    # -- Απαιτούμενο Εισόδημα (ανά έτος) = days * price --
                    st.write(f"**Απαιτούμενο Εισόδημα (ανά έτος):** €{income:.2f}")
                    st.write(f"**Τρέχουσα Τιμή Ενοικίου:** €{price:.2f}/ημέρα")

                    # Αν είναι Κανονικές Περίοδοι, δείχνουμε το ROI=0 specifically.
                    if period_name == "Κανονικές Περίοδοι":
                        st.write(
                            f"**Απαιτούμενο Εισόδημα για ROI=0 (ανά έτος):** "
                            f"€{roi_zero_income_for_normal:.2f}"
                        )
                        # Απαραίτητη τιμή ενοικίου για ROI=0
                        if days > 0:
                            required_price = roi_zero_income_for_normal / days
                            required_price = max(required_price, 0)
                            st.write(
                                f"**Απαραίτητη Τιμή Ενοικίου:** "
                                f"€{required_price:.2f}/ημέρα"
                            )
                else:
                    st.write("Δεν υπάρχει ενοικίαση σε αυτή την περίοδο.")

    st.write("---")

    # -------- Συνολική Ανασκόπηση -------- #
    st.header("Συνολική Ανασκόπηση")

    col6, col7 = st.columns(2)

    with col6:
        st.subheader("Συνολικό Εισόδημα")
        st.write(
            f"**Συνολικό Εισόδημα για {ανάλυση_επένδυσης} χρόνια:** "
            f"€{συνολικό_εισόδημα:.2f}"
        )

    with col7:
        st.subheader("Συνολικό Κέρδος")
        st.write(f"**Κέρδος:** €{κέρδος:.2f}")

    col8, col9 = st.columns(2)

    with col8:
        st.subheader("Απόδοση (ROI)")
        st.write(f"**{απόδοση:.2f}%**")

    with col9:
        st.subheader("Συνολικό Έσοδο")
        st.write(f"**€{συνολικό_έσοδο:.2f}**")

    # -- Προαιρετικά μπορούμε να προσθέσουμε κι άλλες ενότητες αν θέλουμε --
    st.header("Συμβουλές για μία Αποτελεσματική Επένδυση")
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
