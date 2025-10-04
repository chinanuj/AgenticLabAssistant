# AgentX: An Agentic AI for Smart Lab Scheduling

### A Multi-Agent System for Intelligent Laboratory Booking

AgentX is an intelligent, real-time web platform designed to solve the complex challenges of laboratory management at academic institutions like IIT Jodhpur. It replaces outdated manual booking systems with a fluid, conversational interface powered by a sophisticated multi-agent AI.

The system empowers students and faculty to check lab availability, view schedules, and book resources using simple, natural language. Behind the scenes, a team of autonomous software agents collaborates to interpret requests, enforce constraints, and manage bookings, delivering an efficient, conflict-free, and intelligent scheduling experience.

-----

### Table of Contents

  - [About The Project](https://www.google.com/search?q=%23about-the-project)
  - [Live Demo](https://www.google.com/search?q=%23live-demo)
  - [Core Features](https://www.google.com/search?q=%23core-features)
  - [System Architecture](https://www.google.com/search?q=%23system-architecture)
  - [Technology Stack](https://www.google.com/search?q=%23technology-stack)
  - [Getting Started](https://www.google.com/search?q=%23getting-started)
      - [Prerequisites](https://www.google.com/search?q=%23prerequisites)
      - [Local Installation](https://www.google.com/search?q=%23local-installation)
  - [Usage Guide](https://www.google.com/search?q=%23usage-guide)
      - [User Roles](https://www.google.com/search?q=%23user-roles)
  - [Deployment](https://www.google.com/search?q=%23deployment)

-----

## About The Project

This project originated from a real-world challenge at IIT Jodhpur: the inefficiency of discovering lab availability and the cumbersome process of manually booking slots. AgentX was built to provide a centralized, intelligent solution to this problem.

The core of AgentX is its **Multi-Agent System (MAS)**. Instead of a traditional monolithic backend, the system's intelligence is distributed among autonomous agents. A central `HeadLabAssistantAgent` acts as the primary liaison, communicating with users, while multiple `LabAgents` each represent and manage a physical laboratory. This decentralized architecture enables advanced features like conversational search and creates a foundation for future capabilities such as automated negotiation and adaptive learning among agents.

-----

## Live Demo

A live version of the project is deployed on Render. You can interact with AgentX here:

[https://smart-lab-assistant.onrender.com](https://smart-lab-assistant.onrender.com)

-----

## Core Features

AgentX is equipped with a powerful feature set designed for administrators, faculty, and students.

#### For All Users:

  * **Real-Time Dashboard**: A dynamic dashboard that updates instantly for all connected users via WebSockets, ensuring everyone sees the latest schedule.
  * **Conversational Search**: Ask for labs in plain English (e.g., `"Find a lab with a Raspberry Pi available tomorrow morning"`). The system understands and filters results accordingly.
  * **Voice-Activated Queries**: Interact with the system hands-free by using your voice to ask for lab availability.
  * **Interactive Weekly Schedule**: A clear, comprehensive grid view showing all bookings for all labs for the current week.
  * **User Profile Management**: A personal profile page where users can view details, change their password, and export their information as a vCard.
  * **Dark Mode**: A sleek, modern interface with a toggle for an eye-friendly dark theme.

#### For Teachers:

  * **Effortless Lab Booking**: Book available lab slots directly from search results or a manual booking form.
  * **Booking Management**: Easily edit the student count or cancel bookings you have personally made.
  * **Automated Priority System**: Bookings are automatically prioritized based on the student group (PhD \> B.Tech \> M.Tech), determined from the teacher's email domain.

#### For the Super Admin:

  * **Comprehensive Admin Panel**: A secure, dedicated dashboard for managing the entire system from a single interface.
  * **Complete User Control**: The admin can **add** and **delete** both student and teacher accounts at will.
  * **Total Lab Management**: The admin has full authority to **create**, **update**, and **delete** labs, including their capacity, descriptions, and equipment lists.
  * **Global Booking Oversight**: The admin can view and **delete any booking** across the entire system.

-----

## System Architecture

AgentX is built on a robust, modern architecture designed for real-time interaction and intelligent, agent-based decision-making.

  * **Frontend (Client)**: A dynamic single-page application built with HTML, JavaScript, and Bootstrap. It communicates with the backend exclusively through a persistent **WebSocket** connection for instantaneous updates.
  * **Backend (FastAPI Server)**: A high-performance Python server that serves the frontend application, handles secure user authentication, and manages all WebSocket communications.
  * **Multi-Agent System (MAS)**: The cognitive core of the application.
      * `HeadLabAssistantAgent`: The central coordinator. It receives user queries in natural language, uses a Large Language Model (LLM) to parse them into structured commands, and delegates tasks to the appropriate lab agents.
      * `LabAgents`: Each lab in the real world is represented by a dedicated agent. These agents autonomously manage their schedules, interact with the database, and respond to availability requests from the head agent.
  * **Database (PostgreSQL)**: A cloud-based PostgreSQL database acts as the persistent memory for the entire system, reliably storing all user, lab, and booking information.

-----

## Technology Stack

  * **Backend**: Python, FastAPI, Uvicorn
  * **Real-Time Communication**: WebSockets
  * **Multi-Agent System**: `autogen-agentchat`
  * **Database**: PostgreSQL, SQLAlchemy, `databases` library
  * **Authentication**: JWT (JSON Web Tokens), `passlib` for hashing
  * **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
  * **Deployment**: Render

-----

## Getting Started

Follow these instructions to set up and run the project on your local machine for development and testing.

### Prerequisites

  * Python 3.11+
  * A package manager like `pip`
  * A **Google Gemini API Key** for the agent's natural language understanding capabilities.

### Local Installation

1.  **Clone the repository:**

    ```sh
    git clone [Your Repository URL]
    cd mas_visualization
    ```

2.  **Create and activate a virtual environment:**

      * On Windows:
        ```sh
        python -m venv .venv
        .venv\Scripts\activate
        ```
      * On macOS/Linux:
        ```sh
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure your Environment Variables:**

      * In the `mas_visualization` directory, create a file named `.env`.
      * Copy the following content into it, replacing the placeholder values with your own secrets.
        ```env
        # .env file

        # LLM API Key
        GEMINI_API_KEY="AIzaSy...Your...Key...Here"

        # JWT Authentication Secrets
        SECRET_KEY="a_very_long_random_and_secret_string_for_security"
        ALGORITHM="HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES=30

        # Default Super Admin Credentials (used on first run)
        ADMIN_USERNAME="admin"
        ADMIN_EMAIL="admin@example.com"
        ADMIN_PASSWORD="admin123"

        # For local development, we use SQLite. Leave this blank.
        # DATABASE_URL=
        ```

5.  **Run the application:**

    ```sh
    uvicorn main:app --reload
    ```

6.  **Access the application:** Open your browser and navigate to `http://127.0.0.1:8000`.

-----

## Usage Guide

Once the application is running, you can interact with it according to the defined user roles.

### User Roles

  * **Super Admin**:
      * Logs in with the credentials set in the `.env` file.
      * Accesses the **Admin Panel** from the user dropdown to manage all system data.
      * Possesses all permissions of a Teacher.
  * **Teacher**:
      * Registers for an account with a valid `@iitj.ac.in` email, selecting the "Teacher" role.
      * Can find and book labs using either conversational search or the manual booking form.
      * Can manage their own bookings (edit student count or cancel).
  * **Student**:
      * Registers with a valid `@iitj.ac.in` email, selecting the "Student" role.
      * Can view the dashboard, check lab schedules, and search for availability.
      * Cannot book labs or access booking management controls.

-----

## Deployment

This project is pre-configured for easy deployment on **Render**.

1.  **Create a PostgreSQL database** on Render and copy the "Internal Database URL".
2.  **Create a Web Service** on Render and connect it to your GitHub repository.
3.  **Configure the service** with the following settings:
      * **Root Directory**: `mas_visualization`
      * **Build Command**: `pip install -r requirements.txt`
      * **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000 --workers 1`
4.  **Add all environment variables** from your local `.env` file (including the `DATABASE_URL` from Render) to the "Environment Variables" section in your Render service settings.
5.  **Deploy**. Render will automatically build and launch your application.
