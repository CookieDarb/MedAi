from flask import Flask, render_template, request, jsonify
from Diseases_symp import disease_symptoms , disease_status , disease_cures
app = Flask(__name__)

# Questions to be asked in sequence
questions = [
    "Do you need any other assistance?",
    "What is your name?",
    "What is your age?",
    "Are you feeling well? (Yes/No)",
]
Symptoms=['fever','running_nose','Cough','Eye Irritation','Dizziness','Rashes','Stomach Cramps','Vomiting','Nausea',              'Shortness of Breath','Chills','Body Aches','Fatigue','Headache','Sore Throat']


# Home route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Backend route to handle chatbot responses
@app.route('/get-response', methods=['POST'])
def get_response():
    data = request.json
    user_message = data.get('message', '')
    step = data.get('step', 0)
    name = data.get('name', '')
    age = data.get('age', '')
    response = ""
    next_step = step

    print(step)
    print(data)

    # Step 0: Ask "Do you need any other assistance?"
    if step == 0:
        response = questions[0]
        
        if user_message.lower() == 'no':
            response = "You are good to surf the internet. Thank you!"
            next_step = 0  # End of conversation
        elif user_message.lower() == 'yes':
            response = questions[1]
            next_step = 1
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 0  # Repeat the same question

    # Step 1: Ask for the user's name
    elif step == 1:
        name = user_message  # Store user's name
        response = f"Nice to meet you, {name}. {questions[2]}"
        next_step = 2

    # Step 2: Ask for the user's age
    elif step == 2:
        try:
            age = int(user_message)  # Store user's age and validate it's a number
            response = f"Thank you, {name}. You are {age} years old. {questions[3]}"
            next_step=3
        except ValueError:
            response = "Please enter a valid number for your age."
            next_step = 2  # Repeat the age question
        
    elif step == 3:
        if user_message.lower() == 'yes':
            response = "You are good to surf the internet. Thank you!"
            next_step = 0 
        
        elif user_message.lower() == 'no':
        
            next_step = 4 
            response = "Do you have fever?"
        else:
            response = " Please answer with 'yes' or 'no'."
            next_step = 3  # Repeat the same question

    elif step == 4:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["fever"] == 1:
                    disease_status[disease] += 1
            next_step = 5

        elif user_message.lower() == 'no':
            next_step = 5  # Go to next symptom question
        else:
            response = "Please answer with4 'yes' or 'no'."
            next_step = 4  # Repeat the same question
        response = "Do you have a running nose?"

    elif step == 5:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["running_nose"] == 1:
                    disease_status[disease] += 1
            next_step = 6

        elif user_message.lower() == 'no':
            next_step =6  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 5  # Repeat the same question
        response = "Do you have a cough?"

    elif step == 6:
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Cough"] == 1:
                    disease_status[disease] += 1
            next_step = 7
                
        elif user_message.lower() == 'no':
            next_step = 7  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 6  # Repeat the same question
        response = "Do you have eye irritation?"

    elif step == 7:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Eye Irritation"] == 1:
                    disease_status[disease] += 1
            next_step = 8

        elif user_message.lower() == 'no':
            next_step = 8  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 7  # Repeat the same question
        response = "Do you feel dizzy?"

    elif step == 8:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Dizziness"] == 1:
                    disease_status[disease] += 1
            next_step = 9

        elif user_message.lower() == 'no':
            next_step = 9  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 8  # Repeat the same question
        response = "Do you have any rashes?"

    elif step == 9:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Rashes"] == 1:
                    disease_status[disease] += 1
            next_step = 10

        elif user_message.lower() == 'no':
            next_step = 10  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 9  # Repeat the same question
        response = "Do you have stomach cramps?"

    elif step == 10:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Stomach Cramps"] == 1:
                    disease_status[disease] += 1
            next_step = 11

        elif user_message.lower() == 'no':
            next_step = 11  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 10  # Repeat the same question
        response = "Do you feel nauseous?"    

    elif step == 11:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Nausea"] == 1:
                    disease_status[disease] += 1
            next_step = 12

        elif user_message.lower() == 'no':
            next_step = 12  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 11  # Repeat the same question
        response = "Do you have shortness of breath?"

    elif step == 12:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Shortness of Breath"] == 1:
                    disease_status[disease] += 1
            next_step = 13

        elif user_message.lower() == 'no':
            next_step = 13  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 12  # Repeat the same question
        response = "Do you have chills?"

    elif step == 13:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Chills"] == 1:
                    disease_status[disease] += 1
            next_step = 14

        elif user_message.lower() == 'no':
            next_step = 14  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 13  # Repeat the same question
        response = "Do you have body aches?"    

    elif step == 14:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Body Aches"] == 1:
                    disease_status[disease] += 1
            next_step = 15

        elif user_message.lower() == 'no':
            next_step = 15  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 14  # Repeat the same question
        response = "Do you feel fatigued?"    

    elif step == 15:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Fatigue"] == 1:
                    disease_status[disease] += 1
            next_step = 16

        elif user_message.lower() == 'no':
            next_step = 16  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 15  # Repeat the same question
            response = "Do you have a headache?"

    elif step == 16:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Headache"] == 1:
                    disease_status[disease] += 1
            next_step = 17

        elif user_message.lower() == 'no':
            next_step = 17  # Go to next symptom question
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 16  # Repeat the same question
        response = "Do you have a sore throat?"    

    elif step == 17:
        
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Sore Throat"] == 1:
                    disease_status[disease] += 1
            next_step = 18  # End of symptom collection

        elif user_message.lower() == 'no':
            next_step = 18  # End of symptom collection
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 17  # Repeat the same question
    
    elif step ==18 :
        if user_message.lower() == 'yes':
            for disease, symptoms in disease_symptoms.items():
                if symptoms["Cough"] == 1:
                    disease_status[disease] += 1
            

            max =-1
            for disease , probabilty in disease_status.items():
                if max < probabilty :
                    max =probabilty
            print(18, f'{max=}')
            output=''
            for disease , probabilty in disease_status.items():
                if probabilty == max :
                    output =output +  "<br><br>You may have " + disease + ":-" + "Cure for "+ disease_cures[disease]
            print(18, f'{output=}')
                
            response =output + "<br><br><br>SEEK FOR DOCTOR AS SOON AS POSSIBLE !"
            next_step = 0

        elif user_message.lower() == 'no':
            max =-1
            for disease , probabilty in disease_status.items():
                if max < probabilty :
                    max =probabilty
          
            output=''
            for disease , probabilty in disease_status.items():
                if probabilty == max :
                    output =output +  "<br><br>You may have " + disease + ":-" + "Cure for "+ disease_cures[disease]

                
            response =output + "<br><br><br>SEEK FOR DOCTOR AS SOON AS POSSIBLE !"
            next_step = 0
           
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 18



    return jsonify({
        "response": response,
        "next_step": next_step,
        "name": name,
        "age": age
    })

if __name__ == '__main__':
    app.run(debug=True, host='::')