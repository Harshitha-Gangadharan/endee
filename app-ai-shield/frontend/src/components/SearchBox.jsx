import React, { useState } from "react";
import { Search, Sparkles } from "lucide-react";
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
		<div className="flex flex-col gap-3">
			<div className="relative group">
				<div className="absolute inset-y-0 left-3 flex items-center pointer-events-none">
					<Sparkles
						size={18}
						className="text-blue-500 group-focus-within:animate-pulse"
					/>
				</div>
				<input
					type="text"
					value={query}
					onChange={(e) => setQuery(e.target.value)}
					onKeyDown={(e) => e.key === "Enter" && handleSearch()}
					placeholder="Search for skills (e.g. Python, Docker)..."
					className="w-full pl-10 pr-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all placeholder:text-slate-400"
				/>
			</div>
			<button
				onClick={handleSearch}
				className="w-full flex items-center justify-center gap-2 py-3 bg-blue-600 hover:bg-blue-700 active:scale-[0.98] text-white font-bold rounded-xl shadow-lg shadow-blue-200 transition-all"
			>
				<Search size={18} />
				<span>Execute Semantic Search</span>
			</button>
		</div>
	);
};

export default SearchBox;
