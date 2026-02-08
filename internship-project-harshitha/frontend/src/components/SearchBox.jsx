import React, { useState } from "react";
import { Search } from "lucide-react";
import { resumeService } from "../services/api";

const SearchBox = ({ setResults }) => {
	const [query, setQuery] = useState("");

	const handleSearch = async () => {
		if (!query) return;
		try {
			const data = await resumeService.search(query);
			setResults(data.results);
		} catch (error) {
			console.error("Search failed:", error);
		}
	};

	return (
		<div className="search-container" style={{ display: "flex", gap: "10px" }}>
			<input
				type="text"
				value={query}
				onChange={(e) => setQuery(e.target.value)}
				placeholder="Search for skills (e.g. Python, Docker)..."
				style={{
					flex: 1,
					padding: "10px",
					borderRadius: "4px",
					border: "1px solid #ccc",
				}}
			/>
			<button
				onClick={handleSearch}
				style={{
					padding: "10px 20px",
					background: "#2563eb",
					color: "white",
					borderRadius: "4px",
					border: "none",
				}}
			>
				<Search size={20} />
			</button>
		</div>
	);
};

export default SearchBox;
