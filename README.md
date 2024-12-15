```markdown
# Chat Assistant with LangGraph and Google Gemini API

This project implements a chat assistant using LangGraph, LangChain Google Generative AI (Gemini 1.5 Flash), and FastAPI. It features a structured state graph to process user queries and return responses.

---

## Features

- Utilizes **Google Gemini 1.5 Flash** for generating responses.
- Implements a **state graph** with LangGraph for message flow management.
- Built with **FastAPI** for a RESTful API interface.
- Includes memory-saving checkpoints with LangGraph's `MemorySaver`.

---

## Requirements

### Environment Setup

1. **Python Version**: `Python 3.9+`
2. **Environment Variables**:
   - `GOOGLE_API_KEY`: Your API key for accessing Google Gemini.

### Required Libraries

Install the required libraries using `pip`:

```bash
pip install fastapi uvicorn langchain-google-genai langgraph typing-extensions python-dotenv
```

---

## Usage

### Steps to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=<your-google-api-key>
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn <filename>:app --reload
   ```

   Replace `<filename>` with the name of the Python file containing the code.

5. Access the chat API endpoint:
   ```
   GET http://127.0.0.1:8000/chat/{query}
   ```
   Replace `{query}` with your input query.

---

## Example

### Input
```bash
GET http://127.0.0.1:8000/chat/Hello
```

### Response
```json
{
  "messages": ["<Response from Google Gemini API>"]
}
```

---

## Project Structure

- **FastAPI App**: Handles the RESTful API.
- **LangGraph**: Constructs a state graph for managing message flows.
- **LangChain Google Generative AI**: Integrates the Gemini model for LLM responses.

---

## Notes

- Ensure your Google API key has access to the Gemini API.
- Use `uvicorn` or any ASGI-compatible server to deploy the FastAPI app.
- The `MemorySaver` checkpoint mechanism enables stateful interactions.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributors

- **Hassan** (Project Lead)
```

If you need any changes or additional sections (e.g., deployment guides or advanced configurations), let me know!



# Agentic AI Chatbot Prototype 1

## Objective
Create a chatbot prototype that can:
- Engage in meaningful conversations.
- Remember context during interactions (short-term memory).
- Help users solve specific problems based on the chosen niche.

---

## Features

### **1. Niche-Specific Assistance**
- **Students**: Research assistance and study plan creation.
- **Customers**: Help in filing complaints.
- **Partygoers**: Provide outfit suggestions for events.
- **Healthcare Users**: Offer simple health tips and recommendations.

### **2. Smart Conversations**
- Utilizes advanced prompt engineering for context-aware responses.

### **3. Tool Integration**
- Complaint submission forms.
- Study schedule planner.
- Outfit suggestion engine.
- Health tips database.

### **4. Short-Term Memory**
- Retains conversational context within the session to improve user experience.

### **5. Platform**
- Built and tested in Google Colab.

---

## Deliverables

1. **Working Chatbot Prototype**
   - Hosted on Google Colab.
   - Fully functional conversational abilities.

2. **Tools and Examples**
   - Documentation of tools integrated with examples for users.

3. **Submission Form**
   - Submit the Google Colab link and supporting documents via the provided form.

---

## User Stories

| **User Role**     | **Feature**                                       | **Example Interaction**                                                                 |
|--------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Student**        | Research assistance & study planning             | "Help me prepare a study schedule for my math exam next week."                        |
| **Customer**       | Complaint submission                             | "File a complaint about a defective product."                                          |
| **Partygoer**      | Outfit suggestions for events                    | "What should I wear to a semi-formal evening party?"                                   |
| **Healthcare User**| Answer simple health questions                   | "What should I do for a mild fever?"                                                  |

---

## Competencies/Outcomes

1. **REACT Architecture**: Understanding how to build modular AI chatbots.
2. **Prompt Engineering**: Design prompts for smart, relevant responses.
3. **Tool Calling & Chat Management**: Demonstrate tool integration.
4. **Short-Term Memory**: Enhance interactions with memory retention.

---

## Technology Stack

- **Frontend**: Google Colab (Optional GUI for Prototype).
- **Backend**: Python, LangChain.
- **APIs**: OpenAI GPT or Google Gemini 1.5 Flash.
- **Memory Management**: LangChain memory modules.

---

## Installation and Usage

### Prerequisites
- Python 3.7+
- Google Colab account
- Required libraries: `langchain`, `openai`, `fastapi` (if applicable).

### Steps to Run

1. Clone the repository or copy the code into a Google Colab notebook.
2. Install dependencies in Colab:
   ```bash
   !pip install langchain openai fastapi
   ```
3. Set up API keys (OpenAI or Gemini):
   ```python
   import os
   os.environ['OPENAI_API_KEY'] = 'your_api_key_here'
   ```
4. Run the chatbot and test interactions.

---

## Example Code Outline

```python
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Initialize LLM
llm = OpenAI(model="gpt-4", temperature=0.7)

# Add memory to the chatbot
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Example Interaction
print(conversation.run("Hi, I am a student. Can you help me create a study plan?"))
```

---

## Future Enhancements

1. Expand memory to long-term storage.
2. Add advanced analytics for user interactions.
3. Introduce voice-based interaction using AI narration tools.

---

## Submission

- **Deliverable**: Google Colab Notebook Link.
- **Documentation**: Include examples of how the chatbot assists users.
- **Feedback Form**: Add any improvements or observations from user testing.
