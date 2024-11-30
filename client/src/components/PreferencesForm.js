/*
A form to collect user preferences for fitness plans.
*/

import React, { useState } from "react";
import axios from "../services/api";

function PreferencesForm() {
  const [formData, setFormData] = useState({
    name: "",
    fitnessLevel: "",
    goal: "",
    equipment: "",
    timePerDay: "",
    focusAreas: "",
    injuries: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/preferences", formData);
      alert("Preferences submitted successfully!");
    } catch (error) {
      console.error("Error submitting preferences", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        placeholder="Name"
        onChange={handleChange}
      />
      <input
        type="text"
        name="fitnessLevel"
        placeholder="Fitness Level"
        onChange={handleChange}
      />
      <input
        type="text"
        name="goal"
        placeholder="Goal"
        onChange={handleChange}
      />
      <input
        type="text"
        name="equipment"
        placeholder="Available Equipment"
        onChange={handleChange}
      />
      <input
        type="text"
        name="timePerDay"
        placeholder="Time Per Day"
        onChange={handleChange}
      />
      <input
        type="text"
        name="focusAreas"
        placeholder="Focus Areas"
        onChange={handleChange}
      />
      <input
        type="text"
        name="injuries"
        placeholder="Injury Considerations"
        onChange={handleChange}
      />
      <button type="submit">Submit Preferences</button>
    </form>
  );
}

export default PreferencesForm;
