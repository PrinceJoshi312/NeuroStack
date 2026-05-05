import React, { useState, useEffect, useRef } from 'react';
import './App.css';
import { chatService, ChatResponse } from './services/api';
import { Send, Trash2, Brain, Activity } from 'lucide-react';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId] = useState(() => Math.random().toString(36).substring(7));
  const [logs, setLogs] = useState<any[]>([]);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const result: ChatResponse = await chatService.sendChatMessage({
        session_id: sessionId,
        message: input,
        provider: 'gemini'
      });

      setMessages((prev) => [...prev, { role: 'assistant', content: result.response }]);
      setLogs((prev) => [...prev, ...result.actions_taken]);
    } catch (error) {
      console.error('Failed to send message:', error);
      setMessages((prev) => [...prev, { role: 'assistant', content: 'Sorry, I encountered an error.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = async () => {
    await chatService.clearSession(sessionId);
    setMessages([]);
    setLogs([]);
  };

  return (
    <div className="app-container">
      {/* Sidebar / Chat Section */}
      <div className="chat-section">
        <header style={{ padding: '1rem', borderBottom: '1px solid #334155', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Brain color="#38bdf8" />
            <h1 style={{ margin: 0, fontSize: '1.25rem' }}>AgentOS</h1>
          </div>
          <button onClick={handleClear} style={{ background: 'transparent', color: '#ef4444', padding: '0.5rem' }}>
            <Trash2 size={20} />
          </button>
        </header>

        <div className="messages-container">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.role}`}>
              {msg.content}
            </div>
          ))}
          {isLoading && <div className="message assistant">Thinking...</div>}
          <div ref={messagesEndRef} />
        </div>

        <div className="input-container">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            placeholder="Talk to AgentOS..."
          />
          <button onClick={handleSend} disabled={isLoading}>
            <Send size={20} />
          </button>
        </div>
      </div>

      {/* Action Logs Section */}
      <div className="action-log-section">
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
          <Activity size={20} color="#38bdf8" />
          <h2 style={{ margin: 0, fontSize: '1.1rem' }}>Action Logs</h2>
        </div>
        
        {logs.length === 0 ? (
          <div style={{ color: '#94a3b8', fontSize: '0.9rem', textAlign: 'center', marginTop: '2rem' }}>
            No actions taken yet.
          </div>
        ) : (
          logs.map((log, idx) => (
            <div key={idx} className="log-item">
              <span style={{ color: '#38bdf8' }}>[{log.type}]</span> {log.description}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;
