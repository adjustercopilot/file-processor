import os
import sys
import pytest
from fastapi.testclient import TestClient
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from json_data_extraction import app


client = TestClient(app)

def create_test_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 750, "This is a test PDF document.")
    c.save()


def test_process_pdf_file(tmp_path):
    pdf_file_path = tmp_path / "test_claim_report.pdf"
    
    create_test_pdf(str(pdf_file_path)) 

    with open(pdf_file_path, "rb") as f:
        response = client.post(
            "/api/template/generate",
            files={"uploaded_files": (pdf_file_path.name, f, "application/pdf")}
        )

    assert response.status_code == 200
    assert "inspections" in response.json()


def test_process_no_files_uploaded():
    response = client.post("/api/template/generate", files={})

    assert response.status_code == 422

    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "uploaded_files"],
                "msg": "Field required",
                "type": "missing",
                "input": None
            }
        ]
    }

