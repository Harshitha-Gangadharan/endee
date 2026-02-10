import { useState } from "react";
import SearchBox from "./components/SearchBox";
import UploadZone from "./components/UploadZone";

function App() {
	const [results, setResults] = useState([]);

	const handleNewUpload = (data) => console.log("New Resume Indexed:", data);

	const getScoreStyles = (score) => {
		if (score >= 80)
			return "bg-emerald-100 text-emerald-700 border-emerald-200";
		if (score >= 50) return "bg-amber-100 text-amber-700 border-amber-200";
		return "bg-rose-100 text-rose-700 border-rose-200";
	};

	return (
		<div className="min-h-screen bg-slate-50 font-sans selection:bg-blue-100">
			{/* Top Navigation / Header */}
			<nav className="sticky top-0 z-10 bg-white/80 backdrop-blur-md border-b border-slate-200 px-4 py-3">
				<div className="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-4">
					<div className="flex items-center gap-3">
						<div className="bg-blue-600 p-2 rounded-lg text-white shadow-lg shadow-blue-200">
							<span className="text-xl font-bold">RS</span>
						</div>
						<div>
							<h1 className="text-lg font-black tracking-tight text-slate-900">
								RESUME-SHIELD <span className="text-blue-600">AI</span>
							</h1>
						</div>
					</div>

					{/* Unique Status Badge (Option 1 style) */}
					<div className="flex items-center gap-3 px-4 py-1.5 bg-slate-900 rounded-full border border-slate-700">
						<div className="relative flex h-2 w-2">
							<span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
							<span className="relative inline-flex rounded-full h-2 w-2 bg-cyan-500"></span>
						</div>
						<span className="text-[10px] font-mono text-cyan-400 uppercase tracking-widest">
							Endee-Core :: Optimal
						</span>
					</div>
				</div>
			</nav>

			<main className="max-w-7xl mx-auto p-4 md:p-8 grid grid-cols-1 lg:grid-cols-12 gap-8">
				{/* Side Control Panel */}
				<aside className="lg:col-span-4 space-y-6">
					<div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
						<h3 className="text-sm font-black text-slate-400 uppercase tracking-tighter mb-4">
							Ingestion Engine
						</h3>
						<UploadZone onUploadSuccess={handleNewUpload} />
					</div>

					<div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
						<h3 className="text-sm font-black text-slate-400 uppercase tracking-tighter mb-4">
							Query Interface
						</h3>
						<SearchBox setResults={setResults} />
					</div>
				</aside>

				{/* Main Results Panel */}
				<section className="lg:col-span-8">
					<div className="flex items-center justify-between mb-6">
						<h2 className="text-xl font-bold text-slate-800">Vector Matches</h2>
						<div className="px-3 py-1 bg-white border border-slate-200 rounded-lg text-xs font-bold text-slate-500">
							{results.length} Candidates
						</div>
					</div>

					<div className="grid gap-4">
						{results.length === 0 ? (
							<div className="bg-white rounded-2xl p-20 border border-slate-200 text-center">
								<p className="text-slate-400 font-medium">
									Ready for semantic query input...
								</p>
							</div>
						) : (
							results.map((res, index) => (
								<div
									key={index}
									className="bg-white p-6 rounded-2xl border border-slate-200 hover:shadow-md hover:border-blue-200 transition-all group"
								>
									<div className="flex justify-between items-start mb-4">
										<h4 className="font-bold text-slate-900 group-hover:text-blue-600 transition-colors">
											{res.meta.filename}
										</h4>
										<div
											className={`px-2.5 py-1 rounded-md text-[10px] font-black uppercase tracking-wider border ${getScoreStyles(
												res.meta.compliance_score
											)}`}
										>
											{res.meta.compliance_score}% Privacy Score
										</div>
									</div>
									<div className="bg-slate-50 rounded-xl p-4 mb-4 text-sm text-slate-600 leading-relaxed border border-slate-100">
										"{res.meta.preview}..."
									</div>
									<div className="flex items-center justify-between border-t border-slate-50 pt-4">
										<span className="text-xs font-bold text-slate-400 uppercase">
											LVL: {res.meta.exp_level || "Junior"}
										</span>
										<button className="px-5 py-2 bg-slate-900 text-white text-xs font-bold rounded-lg hover:bg-blue-600 transition-colors">
											SECURE VIEW
										</button>
									</div>
								</div>
							))
						)}
					</div>
				</section>
			</main>
		</div>
	);
}

export default App;
