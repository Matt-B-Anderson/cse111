# The Emotional State Tracker is a command-line tool that allows users to log and analyze their mood over time. 
# Users input their mood each day (e.g., happy, sad, anxious, excited), and the program stores these entries in a file. It also includes functionality to view mood history, calculate the most common mood, and display how moods have changed over a specified range of dates.
# This project is focused on trying to help individuals be more aware of their mental health, and even possibly provide a good reference for those that are in therapy.

import os
import datetime

DATA_FILE = "emotion_log.txt"

def get_today_date():
    return datetime.date.today()

def get_user_input(prompt):
    try:
        return input(prompt).strip()
    except Exception as e:
        print(f"Error getting input: {e}")
        return None
    
def log_emotions():
    emotion = get_user_input("Enter your emotion for today (e.g., happy, sad): ").strip().lower()

    if not emotion or any(char.isdigit() for char in emotion):
        print("Invalid input. Emotion must not contain numbers.")
        return

    date = get_today_date().isoformat()
    with open(DATA_FILE, "a") as file:
        file.write(f"{date},{emotion}\n")
    print("Emotion logged successfully.")
    
def load_emotion_data():
    if not os.path.exists(DATA_FILE):
        return []
    
    data = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            try:
                date_str, emotion = line.strip().split(",")
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                data.append((date, emotion))
            except ValueError as e:
                print(f"Skipping bad line: {line.strip()} - Reason: {e}")
                continue
    return data

def view_emotion_history():
    data = load_emotion_data()
    if not data:
        print("No emotion log history found.")
        return
    
    for date, emotion in data:
        print(f"{date}: {emotion}")
        
def calculate_emotion_stats():
    from collections import Counter
    
    data = load_emotion_data()
    if not data:
        print("No data available.")
        return
    
    emotions = [emotion for _, emotion in data]
    counter = Counter(emotions)
    most_common = counter.most_common(1)[0] if counter else ("None", 0)
    
    print("Emotion Frequency:")
    for emotion, count in counter.items():
        print(f"{emotion}: {count}")
        
    print(f"Most Common Emotion: {most_common[0]} ({most_common[1]} times)")
    
if __name__ == "__main__":
    while True:
        print("\n--- Emotional State Tracker ---")
        print("1. Log Emotion")
        print("2. View Emotion History")
        print("3. Calculate Emotion Stats")
        print("4. Exit")
        
        choice = get_user_input("Choose an option: ")

        if choice == "1":
            log_emotions()
        elif choice == "2":
            view_emotion_history()
        elif choice == "3":
            calculate_emotion_stats()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")