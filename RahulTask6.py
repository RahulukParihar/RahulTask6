import streamlit as st



import google.generativeai as genai





# Configure Google GenAI


genai.configure(api_key="AIzaSyCsXFgJ3f71_RACmoW-CPmAjQStzc5AMFg")





# Function to get travel recommendations


def get_travel_options(source, destination):


    prompt = f"Find me the best travel options from {source} to {destination} with estimated prices."


    response = genai.generate_text(prompt)


    return response.text





# Streamlit UI


st.title("🗺️ AI-Powered Travel Planner")


st.markdown("Find the best travel options between cities!")





# User input


source = st.text_input("Enter Source Location")


destination = st.text_input("Enter Destination Location")





if st.button("Find Travel Options"):


    if source and destination:


        result = get_travel_options(source, destination)


        st.success(result)


    else:


        st.warning("Please enter both source and destination.")
