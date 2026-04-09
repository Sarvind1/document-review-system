# Document Review System

A Streamlit-based web application for reviewing and comparing multiple PDF document batches. Supports side-by-side document comparison, audit trails, and integration with AWS S3 for document storage.

## Features

- **Batch Document Organization**: Review documents organized by batch and type (CI/PL)
- **Multi-Version Comparison**: View and compare different versions of the same document side-by-side
- **PDF Viewer**: Embedded PDF viewer with document display
- **Review Tracking**: Capture review decisions and notes with full audit trail
- **Cloud Storage Integration**: Seamless S3 integration with local fallback
- **Status Management**: Track portal and review status for each batch

## Tech Stack

- **Streamlit** - Interactive web framework
- **Python 3** - Core language
- **Pandas** - Data manipulation
- **boto3** - AWS S3 integration
- **Pillow** - Image processing

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate  # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS credentials:**
   - Create `.streamlit/secrets.toml` with AWS credentials (see `.streamlit/secrets.example.toml`)
   - Or set environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, etc.

4. **Prepare data:**
   - Place batch metadata in `data/Manual_Review.csv`
   - PDF documents in `static/documents/{CI,PL}/{BATCH}/`

5. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

1. Select a batch from the dropdown
2. Choose document type (CI or PL)
3. Compare multiple document versions side-by-side
4. Record your review decision and notes
5. System maintains automatic audit trail of all reviews

## Project Structure

```
.
├── src/
│   ├── app.py              # Main Streamlit application
│   ├── utils.py            # Utility functions (data loading, formatting)
│   ├── s3_utils.py         # AWS S3 integration
│   └── styles.py           # CSS styling
├── scripts/
│   ├── create_demo_pdfs.py # Generate sample PDFs
│   └── upload_to_s3.py     # S3 upload utility
├── data/                   # Batch metadata CSVs
├── static/documents/       # PDF documents organized by type/batch
└── requirements.txt        # Python dependencies
```