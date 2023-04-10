// src/api/conceptMaps.ts

import axios from "axios";

export async function generateConceptMap(topic: string): Promise<any> {
  try {
    const requestBody = {
      prompt: topic,
    };

    const response = await axios.post(
      "http://localhost:8000/generate_concept_map",
      requestBody
    );

    if (response.status === 200) {
      return response.data;
    } else {
      console.error("Error occurred while generating the concept map");
    }
  } catch (error) {
    console.error("Error occurred while making a request:", error);
  }
}
