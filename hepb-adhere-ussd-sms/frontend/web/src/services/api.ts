import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1'; // Update with your backend URL

// Function to get patient adherence data
export const getPatientAdherence = async (patientId) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/patients/${patientId}/adherence`);
        return response.data;
    } catch (error) {
        console.error('Error fetching patient adherence data:', error);
        throw error;
    }
};

// Function to send USSD request
export const sendUssdRequest = async (ussdData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/ussd`, ussdData);
        return response.data;
    } catch (error) {
        console.error('Error sending USSD request:', error);
        throw error;
    }
};

// Function to send SMS
export const sendSms = async (smsData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/sms`, smsData);
        return response.data;
    } catch (error) {
        console.error('Error sending SMS:', error);
        throw error;
    }
};