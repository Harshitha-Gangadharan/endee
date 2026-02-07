import { useState } from "react";
import SearchBox from "./components/SearchBox";
import "./App.css";

function App() {
	const [results, setResults] = useState([]);

	return (
		<div style={{ maxWidth: "800px", margin: "0 auto", padding: "40px" }}>
			<h1>🛡️ Resume-Shield Dashboard</h1>
			<p>Compliance-First AI Recruitment</p>

			<SearchBox setResults={setResults} />

			<div style={{ marginTop: "20px" }}>
				{results.map((res, index) => (
					<div
						key={index}
						style={{
							border: "1px solid #ddd",
							padding: "15px",
							marginBottom: "10px",
							borderRadius: "8px",
						}}
					>
						<h3>{res.meta.filename}</h3>
						<p>
							<strong>Compliance Score:</strong> {res.meta.compliance_score}
						</p>
						<p>
							<em>{res.meta.preview}...</em>
						</p>
					</div>
				))}
			</div>
		</div>
	);
}

export default App;
