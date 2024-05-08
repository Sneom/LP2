import streamlit as st
from typing import List

knowledge_base = {
    "domestic": [
        "1: Delta Airlines",
        "2: Southwest Airlines",
        "3: American Airlines",
        "4: United Airlines"
    ],
    "international": [
        "1: Emirates",
        "2: Singapore Airlines",
        "3: Qatar Airways",
        "4: Lufthansa"
    ],
    "budget": [
        "1: Spirit Airlines",
        "2: Ryanair",
        "3: EasyJet",
        "4: AirAsia"
    ],
    "luxury": [
        "1: Emirates First Class",
        "2: Singapore Airlines Suites",
        "3: Etihad Residence",
        "4: Qatar Airways Qsuite"
    ]
}

st.header("Flight Booking Expert System")

def respond(preferences: List[str]):
    if "domestic" in preferences:
        st.write("Here are some domestic flight options:")
        for flight in knowledge_base["domestic"]:
            st.write(flight)
    if "international" in preferences:
        st.write("Here are some international flight options:")
        for flight in knowledge_base["international"]:
            st.write(flight)
    if "budget" in preferences:
        st.write("Here are some budget-friendly flight options:")
        for flight in knowledge_base["budget"]:
            st.write(flight)
    if "luxury" in preferences:
        st.write("Here are some luxury flight options:")
        for flight in knowledge_base["luxury"]:
            st.write(flight)

if __name__ == "__main__":
    options = st.multiselect(
        'What are your flight preferences?',
        ["domestic", "international", "budget", "luxury"],
        [])

    col1, col2 = st.columns([1,0.1])
    with col1:
        ask = st.button("Find Flights")
    with col2:
        quit = st.button("Quit")
    if ask:
        respond(options)
    if quit:
        st.write("Thank you for using the Flight Booking Expert System!")
