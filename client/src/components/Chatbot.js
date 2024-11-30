import React, { useState } from "react";
import axios from "../services/api";

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    try {
      const response = await axios.post("/chat", { message: input });
      setMessages([
        ...messages,
        { role: "user", content: input },
        response.data,
      ]);
      setInput("");
    } catch (error) {
      console.error("Error sending message", error);
    }
  };

  return (
    <div>
      <div className="chat-window">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={msg.role === "user" ? "user-message" : "bot-message"}
          >
            {msg.content}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chatbot;
