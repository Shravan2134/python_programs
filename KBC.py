questions = [
    {
        "question": "What is the capital of India?",
        "options": {
            "A": "Mumbai",
            "B": "Delhi",
            "C": "Kolkata",
            "D": "Chennai"
        },
        "answer": "B",
        "prize": 1000
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": {
            "A": "Earth",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Saturn"
        },
        "answer": "C",
        "prize": 2000
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": {
            "A": "Charles Dickens",
            "B": "Mark Twain",
            "C": "William Shakespeare",
            "D": "Jane Austen"
        },
        "answer": "C",
        "prize": 3000
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": {
            "A": "CO2",
            "B": "H2O",
            "C": "O2",
            "D": "NaCl"
        },
        "answer": "B",
        "prize": 4000
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": {
            "A": "Gold",
            "B": "Diamond",
            "C": "Iron",
            "D": "Platinum"
        },
        "answer": "B",
        "prize": 5000
    },
    {        "question": "What is the largest mammal?",
        "options": {
            "A": "Elephant",
            "B": "Blue Whale",
            "C": "Giraffe",
            "D": "Great White Shark"
        },
        "answer": "B",
        "prize": 6000   
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": {
            "A": "Tomato",
            "B": "Avocado",
            "C": "Onion",
            "D": "Pepper"
        },
        "answer": "B",
        "prize": 7000
    },
    {
        "question": "What is the capital of France?",
        "options": {
            "A": "Berlin",
            "B": "Madrid",
            "C": "Paris",
            "D": "Rome"
        },
        "answer": "C",
        "prize": 8000
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": {
            "A": "Atlantic Ocean",
            "B": "Indian Ocean",
            "C": "Arctic Ocean",
            "D": "Pacific Ocean"
        },
        "answer": "D",
        "prize": 9000
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": {
            "A": "Vincent van Gogh",
            "B": "Pablo Picasso",
            "C": "Leonardo da Vinci",
            "D": "Claude Monet"
        },
        "answer": "C",
        "prize": 10000
    },
    {
        "question": "What is the smallest country in the world?",
        "options": {
            "A": "Monaco",
            "B": "Vatican City",
            "C": "San Marino",
            "D": "Liechtenstein"
        },
        "answer": "B",
        "prize": 20000
    
    },
    {        "question": "What is the main language spoken in Brazil?",
        "options": {
            "A": "Spanish",
            "B": "Portuguese",
            "C": "English",
            "D": "French"
        },
        "answer": "B",
        "prize": 30000
    },
    {        "question": "What is the largest desert in the world?",
        "options": {
            "A": "Sahara Desert",
            "B": "Arabian Desert",
            "C": "Gobi Desert",
            "D": "Kalahari Desert"
        },
        "answer": "A",
        "prize": 50000
    },
    {        "question": "What is the currency of Japan?",
        "options": {
            "A": "Yen",
            "B": "Won",
            "C": "Dollar",
            "D": "Euro"
        },
        "answer": "A",
        "prize": 100000
    },
    {        "question": "What is the largest continent by land area?",
        "options": {
            "A": "Africa",
            "B": "Asia",
            "C": "North America",
            "D": "South America"
        },
        "answer": "B",
        "prize": 200000
    }
]

def Start_the_game():
    print("Welcome to Kon Banega Karodpati!")
    print("You will be asked a series of questions. Answer correctly to win prizes.")
    print("You can quit at any time by typing 'quit'.")
    print("Let's begin!\n")
    def Ask_questions():
        total_prize = 0
        for i, question in enumerate(questions):
            print(f"Question {i + 1}: {questions[i]['question']}")
            print("Options:")
            for option, answer in question["options"].items():
                print(f"{option}: {answer}")
            answer = input("Your answer (A/B/C/D): ").strip().upper()
    
            if answer == "QUIT":
                print("You chose to quit the game.")
                break
            if answer == question["answer"]:
                total_prize += question["prize"]
                print(f"Correct! You have won ₹{question['prize']}. Total prize: ₹{total_prize}\n")
                print("If You want to Quit the game You can QUit here with amout", total_prize)
            else:
                print(f"Wrong answer! The correct answer was {question['answer']}. You won ₹{total_prize}.\n")
                break
        else:
            print(f"Congratulations! You answered all questions correctly. Your total prize is ₹{total_prize}.")
    return Ask_questions()






print(Start_the_game())