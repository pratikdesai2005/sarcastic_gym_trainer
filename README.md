💪 Sarcastic Gym Trainer AI Chatbot

A fun, interactive, terminal-based AI chatbot built with Python and Ollama. The chatbot acts as a sarcastic gym trainer who humorously challenges workout excuses, skipped gym sessions, and diet slip-ups while encouraging users to get back on track.

Powered by a locally running Ollama language model, the chatbot maintains conversation history to provide a more continuous and interactive experience.

✨ Features
🤖 AI-Powered Conversations: Generates responses using an Ollama language model.
💪 Sarcastic Gym Trainer Personality: Responds to workout excuses with humor and playful sarcasm.
😂 Motivational Responses: Encourages users to return to their fitness routines.
💬 Conversation Memory: Maintains conversation history during the current session.
🎯 Mini Workout Challenges: Ends every AI response with a short challenge, such as "20 squats. Now."
🖥️ Terminal-Based Interface: Interact with the chatbot directly through the command line.
🏠 Local Model Execution: Uses Ollama running on your computer to generate responses.
⚙️ Customizable AI Behavior: Adjust the system prompt and model parameters to change the chatbot's personality and response style.
🛡️ Error Handling: Displays an error message if communication with Ollama fails.
🛠️ Technologies Used
Python – Core programming language.
Ollama – Runs and serves the local language model.
Ollama Python Client – Connects the Python application to the Ollama API.
Qwen 3.5 0.8B – The configured language model, identified by the model tag qwen3.5:0.8b.
📂 Project Structure
sarcastic-gym-chatbot/
│
├── main.py
├── requirements.txt
└── README.md

main.py – Contains the chatbot logic and interactive conversation loop.
requirements.txt – Lists the required Python package.
README.md – Project documentation.
⚙️ Installation and Setup
1. Install Ollama

Download and install Ollama from the official website:

https://ollama.com/download

Follow the installation instructions for your operating system.

2. Download the AI Model

Open a terminal and run:

ollama pull qwen3.5:0.8b


This downloads the model used by the application. Ensure the model tag is available in your Ollama installation.

3. Verify Ollama Is Running

Ollama normally serves its local API at:

http://localhost:11434


Check the installed models:

ollama list


If Ollama is not already running as a background service, start it using:

ollama serve


Keep the Ollama service running while using the chatbot.

4. Clone the Repository
git clone <your-repository-url>
cd sarcastic-gym-chatbot


Replace <your-repository-url> with your actual Git repository URL.

5. Create a Virtual Environment (Optional)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

6. Install Dependencies

Create a requirements.txt file containing:

ollama


Install the dependency:

pip install -r requirements.txt

7. Run the Chatbot

Save your Python code as main.py and execute:

python main.py


You can now start chatting with your sarcastic AI gym trainer.

🚀 How to Use
Start the Ollama service.
Make sure the qwen3.5:0.8b model is downloaded.
Run the Python application.
Enter a workout excuse, fitness question, or diet-related message.
Read the chatbot's sarcastic but motivational response.
Continue the conversation; the chatbot retains previous messages during the session.
Type exit to end the conversation.
💻 Example Conversation
Welcome to Ollama AI Chatbot!
Type 'exit' to stop chatting.

You: I skipped the gym today because I was tired.

AI: Oh no, your couch must have put up an incredible fight.
Tomorrow, show those dumbbells who's boss instead of negotiating with your pillow.
20 squats. Now.

You: I ate pizza instead of my planned diet meal.

AI: One pizza and suddenly your meal plan has entered witness protection.
Enjoy your food, then get back to your routine instead of declaring a national holiday.
10 squats. Now.

You: exit
AI: Goodbye! Have a great day!


Example responses are illustrative; actual responses depend on the model's output.

🧠 How It Works
Initialize the Client: Connects to the Ollama API running at http://localhost:11434.
Define the System Prompt: Establishes the chatbot's sarcastic gym trainer personality and response rules.
Initialize Conversation History: Stores the system instructions in a message list.
Accept User Input: Reads messages from the terminal.
Handle Exit Commands: Stops the application when the user enters exit.
Generate AI Responses: Sends the conversation history to the configured Qwen model.
Display the Response: Prints the generated answer in the terminal.
Update Conversation History: Stores both user messages and assistant responses to maintain context.
Handle Errors: Catches exceptions that occur during communication with Ollama.
⚙️ Configuration

The chatbot can be customized by changing the following settings in main.py.

Setting	Purpose
host	Specifies the Ollama API address.
model	Selects the language model.
temperature	Controls response variability.
system prompt	Defines the trainer's personality and response rules.
think=False	Requests that the model not return a separate thinking process, where supported by the model and API.

For example, you can change the model by updating:

completion = client.chat(
    model="qwen3.5:0.8b",
    messages=messages,
    think=False,
    options={
        "temperature": 0.7
    }
)


Use a model tag that is available in your Ollama installation and supports the required chat functionality.

📋 Requirements
Python 3.9 or a compatible version supported by the installed Ollama client.
Ollama installed and running locally.
The configured language model downloaded in Ollama.
The Python package ollama.
Sufficient system memory and computing resources to run the selected model.
⚠️ Troubleshooting
Connection refused: Make sure Ollama is running and accessible at http://localhost:11434.
Model not found: Run ollama list to check installed models and pull the required model if necessary.
Package import error: Install the dependency using pip install ollama.
Slow responses: Model performance depends on available hardware and model size.
Unexpected responses: Adjust the system prompt or temperature to influence the chatbot's behavior.
🔮 Future Enhancements
Build a graphical interface using Streamlit.
Add selectable trainer personalities, such as friendly, strict, or humorous.
Save conversation history to a file.
Add workout tracking and daily fitness goals.
Include configurable workout challenges.
Add support for multiple Ollama models.
Allow users to clear or reset conversation history.
Add a fitness progress dashboard.
👨‍💻 Author

Developed as a Python project demonstrating local language models, prompt engineering, conversational AI, and interactive command-line applications.

📄 License

This project is intended for educational and personal use. Add an appropriate open-source license if you plan to distribute it under specific licensing terms.
