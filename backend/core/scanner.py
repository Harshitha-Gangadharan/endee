import re

class ComplianceScanner:
    def __init__(self):
        self.pii_patterns = {
            "EMAIL": r'\S+@\S+',
            "PHONE": r'\b\d{10}\b|\+\d{1,3}\d{10}',
            "AGE_DOB": r'\b(dob|birth|age|born)\b'
        }

    def scan_and_redact(self, text: str):
        violations = []
        clean_text = text
        
        for label, pattern in self.pii_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                violations.append({"type": label, "severity": "High"})
                clean_text = re.sub(pattern, f"[{label}_REDACTED]", clean_text, flags=re.IGNORECASE)

        # Compliance Score (100 is perfect)
        score = max(0, 100 - (len(violations) * 20))
        return clean_text, violations, score