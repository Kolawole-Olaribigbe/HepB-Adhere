# Hepatitis B Adherence System

This project is a low-bandwidth mHealth system designed to improve adherence to Hepatitis B treatment using Unstructured Supplementary Service Data (USSD) and SMS. The system leverages a modern tech stack including Python 3.11, FastAPI, PostgreSQL, Twilio, Redis, and React.

## Project Structure

```
hepb-adhere-ussd-sms
├── backend                # Backend application
│   ├── app                # FastAPI application code
│   ├── migrations          # Database migration scripts
│   ├── alembic.ini        # Alembic configuration file
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Dockerfile for backend
│   └── .env.example        # Example environment variables
├── frontend               # Frontend application
│   ├── web                # React application code
│   └── Dockerfile          # Dockerfile for frontend
├── docker-compose.yml      # Docker Compose configuration
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
└── docs                   # Documentation
    └── architecture.md     # System architecture overview
```

## Features

- **USSD and SMS Integration**: Allows patients to interact with the system using basic mobile phones.
- **Patient Management**: Enables the creation and retrieval of patient records.
- **Adherence Tracking**: Monitors patient adherence to treatment schedules.
- **Notifications**: Sends reminders and updates to patients via SMS.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd hepb-adhere-ussd-sms
   ```

2. **Backend Setup**:
   - Navigate to the `backend` directory.
   - Create a virtual environment and activate it:
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Set up the database by configuring the `.env` file based on `.env.example`.
   - Run migrations:
     ```
     alembic upgrade head
     ```

3. **Frontend Setup**:
   - Navigate to the `frontend/web` directory.
   - Install npm dependencies:
     ```
     npm install
     ```

4. **Running the Application**:
   - Start the backend server:
     ```
     uvicorn app.main:app --reload
     ```
   - Start the frontend application:
     ```
     npm start
     ```

5. **Docker Setup** (optional):
   - Use Docker Compose to build and run the application:
     ```
     docker-compose up --build
     ```

## Usage

- Access the frontend application at `http://localhost:3000`.
- Interact with the USSD and SMS features as per the defined routes in the backend.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


🌍 Vision

Drugs cure diseases. Systems deliver cures.

HBV-Adhere aims to be a building block for hepatitis elimination, starting with adherence and extending to smarter delivery, monitoring, and policy decisions.

📬 Contact

Created as a public, impact-driven project.

For collaboration, research, or deployment discussions:

Open an issue

Reach out via GitHub

Email: kolawoleolari@outlook.com

If you’re a policymaker, NGO, or clinician and want to pilot this system, let’s talk.