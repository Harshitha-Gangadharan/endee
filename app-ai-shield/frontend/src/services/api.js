import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

const apiClient = axios.create({
	baseURL: API_BASE_URL,
});

export const resumeService = {
	// Upload and Redact (Matches your Day 3 milestone)
	upload: async (file) => {
		const formData = new FormData();
		formData.append("file", file);
		const response = await apiClient.post("/upload-compliant", formData, {
			headers: { "Content-Type": "multipart/form-data" },
		});
		return response.data;
	},

	// Semantic Search (Matches your Day 4 milestone)
	search: async (query) => {
		const response = await apiClient.get("/search", {
			params: { query },
		});
		return response.data;
	},
};
