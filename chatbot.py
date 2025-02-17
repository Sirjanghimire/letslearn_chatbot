from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a dictionary for chatbot commands
course_info = {
    "Python": {"price": "NPR 10000", "duration": "2 months"},
    "UI/UX": {"price": "NPR 7000", "duration": "3 months"},
    "Web Development": {"price": "NPR 10000", "duration": "3 months"},
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Basic greetings
    if "hi" in user_input or "hello" in user_input:
        return "Hello! I'm Let's Learn's assistant. How may I help you today?"

    # Course information
    for course in course_info:
        if course.lower() in user_input:
            info = course_info[course]
            return f"{course} course costs {info['price']} and takes {info['duration']} to complete."

    # Ask for more information
    if "course" in user_input:
        available_courses = ", ".join(course_info.keys())
        return f"We offer the following courses: {available_courses}. Which one are you interested in?"
    if 'location' in user_input or 'place' in user_input:
        return "Our location is opposite to PK campus, bagbazar Kathmandu"
    if 'contact' in user_input or 'number' in user_input:
        return "contact us at 9762955625"

    # Default response
    return "I'm sorry, I didn't understand that. Please ask about our courses, prices, durations or opportunities."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
