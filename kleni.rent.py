import streamlit as st

def main():
    st.title("Υπολογιστής Επένδυσης σε Ακίνητο")

    st.sidebar.header("Παράμετροι Επένδυσης")

    # Εισαγωγή αρχικού budget
    αρχικό_budget = st.sidebar.slider("Αρχικό Budget (€)", min_value=1000.0, max_value=100000.0, value=10000.0, step=1000.0)

    # Εισαγωγή αριθμού ετών επένδυσης
    ανάλυση_επένδυσης = st.sidebar.slider("Πόσα χρόνια σκοπεύετε να διατηρήσετε την επένδυση;", min_value=1, max_value=10, value=2, step=1)

    st.sidebar.subheader("Γιορτές Ενοικίασης")

    # Εισαγωγή δεδομένων για Γιορτές
    γιορτές = {
        "Πάσχα": {
            "μέρες": st.sidebar.slider("Πόσες μέρες θα νοικιάσεις κατά το Πάσχα ανά έτος;", min_value=0, max_value=30, value=10, step=1),
            "τιμή": st.sidebar.slider("Τιμή ενοικίου για το Πάσχα (€ ανά μέρα)", min_value=50.0, max_value=500.0, value=100.0, step=10.0)
        },
        "Χριστούγεννα": {
            "μέρες": st.sidebar.slider("Πόσες μέρες θα νοικιάσεις κατά τα Χριστούγεννα ανά έτος;", min_value=0, max_value=30, value=10, step=1),
            "τιμή": st.sidebar.slider("Τιμή ενοικίου για τα Χριστούγεννα (€ ανά μέρα)", min_value=50.0, max_value=500.0, value=120.0, step=10.0)
        },
        "Άλλες Γιορτές": {
            "μέρες": st.sidebar.slider("Πόσες μέρες θα νοικιάσεις για άλλες γιορτές ανά έτος;", min_value=0, max_value=60, value=20, step=1),
            "τιμή": st.sidebar.slider("Τιμή ενοικίου για άλλες γιορτές (€ ανά μέρα)", min_value=50.0, max_value=500.0, value=90.0, step=10.0)
        }
    }

    st.sidebar.subheader("Καλοκαίρι Ενοικίασης")

    # Εισαγωγή δεδομένων για Καλοκαίρι
    καλοκαίρι_μέρες = st.sidebar.slider("Πόσες μέρες θα νοικιάσεις το καλοκαίρι ανά έτος;", min_value=0, max_value=180, value=90, step=1)
    τιμή_καλοκαίρι = st.sidebar.slider("Τιμή ενοικίου για το καλοκαίρι (€ ανά μέρα)", min_value=50.0, max_value=500.0, value=80.0, step=10.0)

    st.sidebar.subheader("Κανονικές Περιόδους Ενοικίασης")

    # Υπολογισμός συνολικών ημερών σε γιορτές και καλοκαίρι
    συνολικές_γιορτές_μέρες = sum([γιορτή["μέρες"] for γιορτή in γιορτές.values()])
    συνολικές_καλοκαιρινές_μέρες = καλοκαίρι_μέρες

    # Υπολογισμός κανονικών ημερών
    συνολικές_κανονικές_μέρες = 365 - συνολικές_γιορτές_μέρες - συνολικές_καλοκαιρινές_μέρες
    συνολικές_κανονικές_μέρες = max(συνολικές_κανονικές_μέρες, 0)

    # Εισαγωγή δεδομένων για Κανονικές Περιόδους
    τιμή_κανονικές = st.sidebar.slider("Τιμή ενοικίου για τις κανονικές περιόδους (€ ανά μέρα)", min_value=20.0, max_value=300.0, value=50.0, step=10.0)

    st.sidebar.markdown("---")
    st.sidebar.write("**Σημείωση:** Οι ημέρες που δεν καλύπτονται από γιορτές ή καλοκαίρι θεωρούνται κανονικές περιόδους.")

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

    # Εμφάνιση Αποτελεσμάτων
    st.header("### Αποτελέσματα")

    st.subheader("Συνολικό Εισόδημα Ανά Έτος")
    st.write(f"**Γιορτές:** €{εισόδημα_γιορτές:.2f}")
    st.write(f"**Καλοκαίρι:** €{εισόδημα_καλοκαίρι:.2f}")
    st.write(f"**Κανονικές Περιόδους:** €{εισόδημα_κανονικές:.2f}")
    st.write(f"**Συνολικό Εισόδημα Ανά Έτος:** €{συνολικό_εισόδημα_ανά_έτος:.2f}")

    st.subheader("Συνολικό Εισόδημα για {0} Χρόνια".format(ανάλυση_επένδυσης))
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
    st.write(f"**Συνολικές Κανονικές Ημέρες:** {συνολικές_κανονικές_μέρες} μέρες με τιμή €{τιμή_κανονικές}/μέρα")

if __name__ == "__main__":
    main()