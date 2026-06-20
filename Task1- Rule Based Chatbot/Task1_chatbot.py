def show_menu():
    print("\n" + "=" * 45)
    print("Welcome to LearnMate AI")
    print("=" * 45)
    print("1. Learn a Topic")
    print("2. Take a Quiz")
    print("3. Viva Practice")
    print("4. Career Guidance")
    print("5. Daily Motivation")
    print("6. Exit")

def learn_topic():
    topic = input("\nWhich topic would you like to learn? (Python/AI/ML/ds/cyber/cloud): ").lower()

    if topic == "python":
        print("\nPython is one of the easiest programming languages.")
        print("It is widely used in web development, AI, and data science.")

    elif topic == "ai":
        print("\nAI stands for Artificial Intelligence.")
        print("It enables computers to think and solve problems like humans.")

    elif topic == "ml":
        print("\nMachine Learning is a part of AI.")
        print("It helps systems learn from data without explicit programming.")
  
    elif topic == "ds":
    	print("\nData science is the study of data ")
    	print("It helps in finding useful insights from data.")
    
    elif topic == "cyber":
    	print("\nCyber Security protects systems and data.")
    	print("It helps prevent hacking and cyber attacks.")

    elif topic == "cloud":
    	 print("\nCloud Computing provides services over the internet.")
    	 print("Examples are Google Drive and AWS.")
    else:
        print("\nSorry, this topic is not available right now.")
def quiz():
    print("\n--- Quick Quiz ---")
    
    print("\nWhich company created Python?")
    print("A. Microsoft")
    print("B. Google")
    print("C. Python Software Foundation")
    answer = input("Your Answer: ").upper()
    
    if answer == "C":
    	print("Correct!")
    else:
    	print("Wrong! Correct Answer: Python Software Foundation")
    	
    print("\nWhat does AI stand for?")
    print("A. Artificial Intelligence")
    print("B. Automatic Internet")
    print("C. Artificial Interface")
    answer = input("Your Answer: ").upper()
    if answer == "A":
    print("Correct!")
    else:
    print("Wrong! Correct Answer: Artificial Intelligence")
    if answer == "A":
        print("Great! That's the correct answer.")
        
    print("\nWhat does ML stand for?")
    print("A. Machine Learning")
    print("B. Main Logic")
    print("C. Machine Language")
    answer = input("Your Answer: ").upper()
    if answer == "A":
    print("Correct!")
    else:
    print("Wrong! Correct Answer: Machine Learning")

    print("\nWhat is Data Science used for?")
    print("A. Data Analysis")
    print("B. Gaming")
    print("C. Drawing")
    answer = input("Your Answer: ").upper()
    
    if answer == "A":
        print("Correct!")
    else:
        print("Wrong! Correct Answer: Data Analysis")	
      	
    print("\nWhich is an example of Cloud Computing?")
    print("A. Google Drive")
    print("B. Paint")
    print("C. Calculator")
    answer = input("Your Answer: ").upper()
    
    if answer == "A":
        print("Correct!")
    else:
        print("Wrong! Correct Answer: Google Drive")
        
    print("\nWhat is the purpose of Cyber Security?")
    print("A. Protecting Data")
    print("B. Playing Games")
    print("C. Watching Videos")
    answer = input("Your Answer: ").upper()
    
    if answer == "A":
    	print("Correct!")
    else:
    	print("Wrong! Correct Answer: Protecting Data")

def viva():
    print("\n--- Viva Practice ---")
    print("Question: What is Python?")
    input("\nPress Enter to see the answer...")
    print("Answer: Python is a high-level and easy-to-learn programming language.")
    
    print("\nQ7. What is the full form of CPU?")
    input("Press Enter to see the answer...")
    print("Answer: CPU stands for Central Processing Unit.")
    
    print("\nQ8. What is HTML?")
    input("Press Enter to see the answer...")
    print("Answer: HTML is used to create the structure of web pages.")
    
    print("\nQ9. What is CSS?")
    input("Press Enter to see the answer...")
    print("Answer: CSS is used to style web pages.")
    
    print("\nQ10. What is a Database?")
    input("Press Enter to see the answer...")
    print("Answer: A database is an organized collection of data.")


def career_roadmap():
    print("\nChoose a Career Path:")
    print("1. AI engineer")
    print("2. Data scientist")
    print("3. Web developer")
    print("4. Cyber security analiyst")
    print("5. cloud engineer")

    choice = input("Enter your choice: ")
    
    if choice == "1":
    	print("\nAI ENGINEER ROADMAP")
    	print("Step 1: Learn Python")
    	print("Step 2: Learn Machine Learning")
    	print("Step 3: Learn Deep Learning")
    	print("Step 4: Build AI Projects")
    	print("Step 5: Apply for Internships")

    elif choice == "2":
    	print("\nDATA SCIENTIST ROADMAP")
    	print("Step 1: Learn Python")
    	print("Step 2: Learn Statistics")
    	print("Step 3: Learn Data Analysis")
    	print("Step 4: Work on Projects")
    	print("Step 5: Build Portfolio")

    elif choice == "3":
    	print("\nWEB DEVELOPER ROADMAP")
    	print("Step 1: Learn HTML")
    	print("Step 2: Learn CSS")
    	print("Step 3: Learn JavaScript")
    	print("Step 4: Build Websites")
    	print("Step 5: Create Portfolio")
    	
    elif choice == "4":
    	print("\nCYBER SECURITY ROADMAP")
    	print("Step 1: Learn Networking")
    	print("Step 2: Learn Linux")
    	print("Step 3: Learn Ethical Hacking")
    	print("Step 4: Practice Security Tools")
    	print("Step 5: Get Certifications")
    	
    elif choice == "5":
    	print("\nCLOUD ENGINEER ROADMAP")
    	print("Step 1: Learn Linux")
    	print("Step 2: Learn Networking")
    	print("Step 3: Learn AWS or Azure")
    	print("Step 4: Build Cloud Projects")
    	print("Step 5: Apply for Jobs")

    else:
        print("Invalid choice.")


def motivation():
    quotes = [
        "Success comes from consistent effort.",
        "Keep learning, keep growing.",
        "Every expert was once a beginner."
    ]

    print("\nMotivation of the Day:")
    for quote in quotes:
        print("•", quote)


# Main Program
while True:
    show_menu()

    user_choice = input("\nSelect an option (1-6): ")

    if user_choice == "1":
        learn_topic()

    elif user_choice == "2":
        quiz()

    elif user_choice == "3":
        viva()

    elif user_choice == "4":
        career_roadmap()

    elif user_choice == "5":
        motivation()

    elif user_choice == "6":
        print("\nThank you for using LearnMate AI.")
        print("Have a great learning journey!")
        break

    else:
        print("\nPlease enter a valid option.")
