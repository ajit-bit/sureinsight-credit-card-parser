import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const uploadStatement = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return API.post("/parse/", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};
