import random
import json
import datetime

RESPONSES_FILE = "responses.json"  # Load responses from a JSON file

def load_responses():
    """ Load responses.json without this file program only reply in default responses which doesn't provide info"""
    try:
        with open(RESPONSES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {RESPONSES_FILE} not found.")
        return {"default": ["I'm not sure how to respond to that."]}

def save_chat_log(log, user_name, agent_name):
    """ Save conversation between user and agent in separate .txt file with time"""
    log_filename = f"chat_log_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.txt"
    with open(log_filename, "w") as file:
        for entry in log:
            file.write(f"{user_name} (User): {entry['user']}\n{agent_name} (Agent): {entry['agent']}\n\n")

def get_user_name():
    """ Ask name to the user if name doen't given then show error """
    while True:
        user_name = input("Welcome to Poppleton University Chat! What's your name? ").strip()
        if user_name:
            return user_name.capitalize() # Capitalize the first letter of the user_name if user type apeal it convert to Apeal
        print("Please enter a name to continue.")

def toggle_listening_mode(current_mode):
    """ For listening mode user don't need reply from the program """
    new_mode = not current_mode
    mode_status = "ON" if new_mode else "OFF"
    print(f"Listening mode is now {mode_status}.")
    return new_mode

def handle_blank_input(blank_count):
    """ auto disconnect if user give more than 3 empty reply """
    blank_count += 1
    if blank_count >= 3:
        print("Oops! The agent has disconnected. Please try again later.")
        return blank_count, True
    return blank_count, False

def get_agent_response(user_input, responses, user_name, agent_name):
    """ Reply from agent and in responses add user_name and agent_name in reply """
    lower_input = user_input.lower()
    for keyword, replies in responses.items():
        if keyword in lower_input:
            return random.choice(replies).replace("{name}", user_name).replace("{agent_name}", agent_name) # name in responses
    return random.choice(responses["default"]).replace("{name}", user_name) # if keywords doesn't found than reply from default

def chatbot():
    """ This part of code for main code """
    responses = load_responses()
    agent_names = ["Steve Smith", "Rohit Sharma", "Travis Head", "Virat Kohli", "MS Dhoni"]
    random_disconnect_chance = 0.1

    user_name = get_user_name()
    agent_name = random.choice(agent_names)
    print(f"Hello, {user_name}! My name is {agent_name}. How can I assist you today?")
    print("You can type 'listening mode' to enter a mode where I will not respond to your inputs.")

    chat_log = []
    blank_input_count = 0
    listening_mode = False

    while True:
        user_input = input(f"{user_name}: ").strip()

        if user_input.lower() in ["bye", "quit", "exit"]:
            print("Thank you for chatting with us! Have a great day!")
            break

        if user_input.lower() == "listening mode":
            listening_mode = toggle_listening_mode(listening_mode)
            continue

        if listening_mode:
            print("Agent is listening...")
            chat_log.append({"user": user_input, "agent": "Agent is listening..."})
            continue

        if not user_input:
            blank_input_count, should_disconnect = handle_blank_input(blank_input_count)
            if should_disconnect:
                break
        else:
            blank_input_count = 0

        if random.random() < random_disconnect_chance:
            print("Oops! The agent has disconnected. Please try again later.")
            break

        response = get_agent_response(user_input, responses, user_name, agent_name)
        print(f"Agent ({agent_name}): {response}")
        chat_log.append({"user": user_input, "agent": response})

    save_chat_log(chat_log, user_name, agent_name)

if __name__ == "__main__":
    chatbot()
