from flask import Flask, render_template, request, jsonify
from Diseases_symp import disease_symptoms, disease_status, disease_cures

app = Flask(__name__)

# Questions to be asked in sequence
questions = [
    "Do you need any other assistance?",
    "What is your name?",
    "What is your age?",
    "Are you feeling well? (Yes/No)",
]
print("hello")
# Define the symptoms
symptoms = [
    "fever", "running_nose", "Cough", "Eye Irritation", "Dizziness", 
    "Rashes", "Stomach Cramps", "Vomiting", "Nausea", 
    "Shortness of Breath", "Chills", "Body Aches", "Fatigue", 
    "Headache", "Sore Throat"
]

# Home route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

def check_symptom(user_message, symptom):
    """Check if the user has the symptom and update the disease status."""
    if user_message.lower() == 'yes':
        for disease, symptom_data in disease_symptoms.items():
            if symptom_data[symptom] == 1:
                disease_status[disease] += 1

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
    if step == 0:
        response = questions[0]
        next_step=1 if user_message.lower() == 'yes' else 6
    if step == 1:
        
        next_step = 2 if user_message.lower() == 'yes' else 0 if user_message.lower() == 'no' else 0
        response =questions[1]

    elif step == 2:
        name = user_message
        response = f"Nice to meet you, {name}. {questions[2]}"
        next_step = 3

    elif step == 3:
        try:
            age = int(user_message)
            response = f"Thank you, {name}. You are {age} years old. {questions[3]}"
            next_step = 4
        except ValueError:
            response = "Please enter a valid number for your age."
            next_step = 2

    elif step == 4:
        if user_message.lower() == 'yes':
            next_step = 0
        elif user_message.lower() == 'no':
            response = "Do you have fever?"
            next_step = 5
        else:
            response = "Please answer with 'yes' or 'no'."
            next_step = 4

    # Check symptoms sequentially
    for idx, symptom in enumerate(symptoms):
        if step == 5 + idx:
            check_symptom(user_message, symptom)
            next_step = 6 + idx if user_message.lower() == 'yes' else 6 + len(symptoms) - 1

            # Move to the next symptom question or conclude
            response = f"Do you have {symptoms[min(idx + 1, len(symptoms) - 1)]}?" if user_message.lower() == 'yes' else ""
            break

    # Final evaluation step
    if step == 5 + len(symptoms) - 1:
        output = ""
        max_prob = max(disease_status.values(), default=-1)

        for disease, probability in disease_status.items():
            if probability == max_prob:
                output += f"<br><br>You may have {disease}:- Cure for {disease_cures[disease]}"

        response = output + "<br><br><br>SEEK FOR DOCTOR AS SOON AS POSSIBLE !" if output else "No matching diseases found."
        next_step = 0
    if step == 6:
        response= "Thank you!! Visit Again!!"
    return jsonify({
        "response": response,
        "next_step": next_step,
        "name": name,
        "age": age
    })

if __name__ == '__main__':
    app.run(debug=True, host='::')
