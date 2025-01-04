# End to End AI Agent Chatbot with LangGraph, FastAPI, and Streamlit UI

This project demonstrates how to create a powerful AI chatbot using LangGraph, FastAPI, and Streamlit. The chatbot integrates LangGraph agents with dynamic model selection and provides an intuitive Streamlit UI for user interaction.

## Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Workflow](#workflow)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Hosting](#hosting)
- [Testing](#testing)
- [Conclusion](#conclusion)

## Introduction
In this project, we will build an AI chatbot that leverages LangGraph for agent management, FastAPI for backend processing, and Streamlit for the frontend UI. This setup allows for dynamic model selection and interactive user experiences.

## Demo
Watch the demo of the AI Agent Chatbot [here](https://www.youtube.com/watch?v=TO_j16jS5w4&t=1101s&ab_channel=BALAGOPALREDDYPEDDIREDDY).

## Workflow
The workflow of the AI Agent Chatbot involves the following steps:
1. Define the FastAPI backend endpoint to process requests.
2. Integrate LangGraph agents with dynamic model selection.
3. Build an intuitive Streamlit UI for user interaction.

## Setup
Follow these steps to set up the project:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Vi-fly/AI-Agent-Chatbot.git
   cd AI-Agent-Chatbot
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the project directory and add the following environment variables:
   ```
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

4. **Run the FastAPI Server**:
   ```sh
   uvicorn main:app --reload
   ```

5. **Run the Streamlit UI**:
   ```sh
   streamlit run app.py
   ```

## API Endpoints
The FastAPI backend provides the following endpoints:

- **POST /chat**: Interact with the chatbot using LangGraph and tools.
  - Request Body:
    ```json
    {
      "model_name": "llama-3.1-70b-versatile",
      "system_prompt": "Your system prompt here",
      "messages": ["Hello", "How can I help you?"]
    }
    ```

## Hosting
The project can be hosted on a Unicorn server. Follow the instructions in the video to set up hosting.

## Testing
You can test the AI Agent Chatbot using the Swagger UI provided by FastAPI. Access it at `http://127.0.0.1:8000/docs`.

## Conclusion
This project demonstrates how to build an end-to-end AI chatbot using LangGraph, FastAPI, and Streamlit. By following the steps outlined in this README, you can create a powerful and interactive AI application.
