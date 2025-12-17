# Architecture Overview of the mHealth Hepatitis B Adherence System

## Introduction
This document outlines the architecture of the mHealth Hepatitis B adherence system, which leverages Unstructured Supplementary Service Data (USSD) and SMS technologies to enhance patient adherence to treatment protocols. The system is designed to operate efficiently in low-bandwidth environments, ensuring accessibility for users.

## System Components
The architecture consists of the following key components:

1. **Frontend (React)**
   - A web-based user interface built with React that allows healthcare providers to monitor patient adherence and manage interactions.
   - Provides dashboards and reporting tools for visualizing patient data.

2. **Backend (FastAPI)**
   - A RESTful API developed using FastAPI that handles requests from the frontend and manages business logic.
   - Responsible for processing USSD and SMS interactions, managing patient records, and interfacing with the database.

3. **Database (PostgreSQL)**
   - A relational database that stores patient information, adherence records, and session data.
   - Ensures data integrity and supports complex queries for reporting and analytics.

4. **Messaging Services (Twilio)**
   - Utilizes Twilio's API for sending and receiving SMS messages.
   - Facilitates communication between patients and healthcare providers through SMS and USSD.

5. **Session Management (Redis)**
   - Redis is used for managing USSD session states, ensuring that interactions are stateless and can handle multiple concurrent sessions efficiently.

6. **Background Tasks (Celery)**
   - Celery is employed for handling asynchronous tasks, such as sending reminders and processing long-running operations without blocking the main application.

## Data Flow
1. **Patient Interaction**
   - Patients interact with the system via USSD or SMS, sending requests for information or updates on their treatment status.

2. **API Processing**
   - The FastAPI backend receives these requests, processes them, and interacts with the PostgreSQL database to retrieve or update patient records.

3. **Response Generation**
   - The backend generates appropriate responses, which are sent back to the patients via Twilio's messaging services.

4. **Monitoring and Reporting**
   - Healthcare providers access the frontend application to monitor patient adherence, view reports, and manage patient interactions.

## Security Considerations
- The system implements JWT for secure authentication and authorization of users.
- Sensitive patient data is encrypted and stored securely in the PostgreSQL database.

## Conclusion
This architecture provides a robust framework for the mHealth Hepatitis B adherence system, ensuring that patients receive timely support and healthcare providers can effectively monitor treatment adherence. The use of modern technologies and best practices ensures scalability, security, and ease of use in low-bandwidth environments.