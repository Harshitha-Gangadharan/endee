import { useState } from "react";
import SearchBox from "./components/SearchBox";
import UploadZone from "./components/UploadZone";
import "./App.css";

function App() {
	const [results, setResults] = useState([]);

	const handleNewUpload = (data) => {
		console.log("New Resume Indexed:", data);
	};

	// Helper function for score colors
	const getScoreColor = (score) => {
		if (score >= 80) return "#22c55e"; // Green
		if (score >= 50) return "#eab308"; // Yellow
		return "#ef4444"; // Red
	};

	return (
		<div className="dashboard-wrapper">
			<div className="container">
				{/* Modern Header */}
				<header className="main-header">
					<div className="logo-section">
						<span className="shield-icon">🛡️</span>
						<div>
							<h1>
								Resume-Shield <span className="badge">AI v1.0</span>
							</h1>
							<p>Privacy-First Semantic Talent Discovery</p>
						</div>
					</div>
					<div className="system-status">
						<span className="status-dot"></span> Endee Engine Active
					</div>
				</header>

				<main className="dashboard-grid">
					{/* Left Column: Management */}
					<div className="control-panel">
						<section className="card">
							<h3>Inbound Pipelines</h3>
							<p className="section-desc">
								Upload resumes to trigger PII redaction and vector indexing.
							</p>
							<UploadZone onUploadSuccess={handleNewUpload} />
						</section>

						<section className="card">
							<h3>Intelligent Search</h3>
							<p className="section-desc">
								Search by intent (e.g., "Senior Python Dev with Docker").
							</p>
							<SearchBox setResults={setResults} />
						</section>
					</div>

					{/* Right Column: Insights & Results */}
					<div className="results-panel">
						<div className="results-header">
							<h3>Talent Pool matches</h3>
							<span className="count-tag">{results.length} found</span>
						</div>

						<div className="results-list">
							{results.length === 0 ? (
								<div className="empty-state">
									<p>No candidates selected. Try a semantic search query.</p>
								</div>
							) : (
								results.map((res, index) => (
									<div key={index} className="result-card">
										<div className="result-top">
											<h4>{res.meta.filename}</h4>
											<div
												className="score-pill"
												style={{
													backgroundColor: `${getScoreColor(
														res.meta.compliance_score
													)}15`,
													color: getScoreColor(res.meta.compliance_score),
												}}
											>
												{res.meta.compliance_score}% Compliant
											</div>
										</div>
										<div className="preview-box">
											<p>"{res.meta.preview}..."</p>
										</div>
										<div className="result-footer">
											<span>Exp Level: {res.meta.exp_level || "N/A"}</span>
											<button className="view-btn">Secure View</button>
										</div>
									</div>
								))
							)}
						</div>
					</div>
				</main>
			</div>
		</div>
	);
}

export default App;
