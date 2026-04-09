# Document Review System

A Streamlit-based web application for reviewing, comparing, and managing batch PDF documents with side-by-side comparison, audit trails, and AWS S3 integration.

## Features

- **Batch Document Management**: Organize and review documents by batch ID
- **Side-by-Side Comparison**: Compare different versions of the same document
- **Portal Status Tracking**: Track document status across review stages (Pending, Accepted, Rejected, In Review)
- **Audit Trail**: Automatic logging of all review decisions and notes
- **S3 Integration**: Seamless upload/download of documents from AWS S3 with fallback to local storage
- **CSV Data Support**: Load and manage review metadata from CSV files
- **Review Notes**: Add custom notes and decision reasons during document review

## Tech Stack

- **Framework**: Streamlit
- **Language**: Python 3.x
- **Data Processing**: pandas
- **Cloud Storage**: AWS S3
- **Deployment**: Streamlit Cloud / Local / Docker

## Requirements

- Python 3.8+
- pandas
- streamlit
- boto3 (for AWS S3)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/document-review-system.git
   cd document-review-system
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AWS credentials** (optional, for S3 support)
   ```bash
   cp .streamlit/secrets.example.toml .streamlit/secrets.toml
   # Edit secrets.toml with your AWS credentials
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

The app will open at `http://localhost:8501`

## Usage

1. **Select a Batch**: Choose a batch ID from the dropdown to load related documents
2. **Choose Document Type**: Select between document types (CI, PL, etc.)
3. **Compare Versions**: Select two versions to view side-by-side
4. **Add Review Notes**: Enter your review decision and notes
5. **Submit Review**: Save your review decision to the audit trail
6. **Export Results**: Download the review audit trail as CSV

## Project Structure

```
document-review-system/
├── src/
│   ├── app.py           # Main Streamlit application
│   ├── utils.py         # Utility functions for data processing
│   ├── s3_utils.py      # AWS S3 integration
│   └── styles.py        # Custom CSS styling
├── static/
│   └── documents/       # Local document storage
├── data/
│   ├── Manual_Review.csv        # Review metadata
│   └── Manual_Review_2.csv      # Additional review data
├── .streamlit/
│   └── secrets.example.toml     # Template for Streamlit secrets
├── requirements.txt             # Python dependencies
├── app.py                       # Application entry point
└── README.md
```

## Environment Variables

For S3 integration, configure the following in `.streamlit/secrets.toml`:
- `aws_access_key_id`: AWS access key
- `aws_secret_access_key`: AWS secret key
- `bucket_name`: S3 bucket name
- `aws_region`: AWS region (default: us-east-1)

## License

MIT