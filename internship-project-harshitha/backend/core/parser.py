import re
import io
from pypdf import PdfReader

class ComplianceParser:
    def __init__(self):
        # These are for classification, but our goal is to find what to HIDE
        self.sensitive_sections = ["Personal Info", "Contact Details", "References"]

    def extract_clean_stream(self, pdf_stream: io.BytesIO):
        """
        Extracts raw text while preserving layout as much as possible 
        so the Compliance Scanner can find patterns like phone numbers.
        """
        reader = PdfReader(pdf_stream)
        text = ""
        for page in reader.pages:
            # We use extract_text() with spacing to keep phone/email formats intact
            page_text = page.extract_text(extraction_mode="plain")
            if page_text:
                text += page_text + "\n"
        return text

    def get_compliance_metadata(self, text: str):
        """
        Detects 'Compliance Anchors' like location and years of experience 
        which are allowed to be stored, unlike PII.
        """
        # Detection for Bengaluru, Pune, etc.
        cities = ["Bengaluru", "Bangalore", "Pune", "Mumbai", "Hyderabad", "Delhi", "Chennai"]
        detected_city = next((c for c in cities if c.lower() in text.lower()), "Not Specified")
        
        # Detection for Experience
        exp_match = re.search(r"(\d+)\+?\s*(years?|yrs?)", text, re.IGNORECASE)
        years = exp_match.group(0) if exp_match else "0"
        
        return {
            "detected_location": detected_city,
            "experience_level": years,
            "data_source": "Redacted PDF"
        }