import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/chat">Chatbot</Link>
        </li>
        <li>
          <Link to="/weekly-plan">Weekly Plan</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
