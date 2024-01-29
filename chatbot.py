import os
import subprocess
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def create_chatbot():
    # Create a chatbot instance
    chatbot = ChatBot('MyBot')

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot on English language data
    trainer.train('chatterbot.corpus.english')

    return chatbot

def save_script_to_github(repo_name, script_content, commit_message='Initial commit'):
    # Create a new directory for the script
    os.makedirs(repo_name, exist_ok=True)
    
    # Save the script to the new directory
    script_path = os.path.join(repo_name, 'chatbot_script.py')
    with open(script_path, 'w') as script_file:
        script_file.write(script_content)
    
    # Initialize a new Git repository
    subprocess.run(['git', 'init', repo_name])

    # Stage and commit the script
    subprocess.run(['git', '-C', repo_name, 'add', '.'])
    subprocess.run(['git', '-C', repo_name, 'commit', '-m', commit_message])

    # Create a new GitHub repository
    subprocess.run(['gh', 'repo', 'create', repo_name, '--public'])

    # Push the changes to GitHub
    subprocess.run(['git', '-C', repo_name, 'remote', 'add', 'origin', f'https://github.com/your-username/{repo_name}.git'])
    subprocess.run(['git', '-C', repo_name, 'push', '-u', 'origin', 'master'])

if __name__ == "__main__":
    bot_script = '''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Main loop for chatting
print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)
'''

    repository_name = 'chatbot_repository'
    commit_message = 'Initial commit'

    create_chatbot()
    save_script_to_github(repository_name, bot_script, commit_message)

    print(f"Chatbot script has been saved to a new GitHub repository: https://github.com/your-username/{repository_name}")
