import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export interface ChatRequest {
  session_id: string;
  message: string;
  provider?: string;
}

export interface ChatResponse {
  response: string;
  session_id: string;
  actions_taken: any[];
  plan: any[];
}

export const chatService = {
  sendChatMessage: async (data: ChatRequest): Promise<ChatResponse> => {
    const response = await axios.post(`${API_BASE_URL}/agent/chat`, data);
    return response.data;
  },

  clearSession: async (sessionId: string) => {
    await axios.delete(`${API_BASE_URL}/agent/session/${sessionId}`);
  }
};
