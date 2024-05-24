# MindTickle-Semantic-Search-System
MindTickle Semantic Search System

## Overview

This project implements a web application that performs semantic search on case study documents for a fictitious company, MindTickle. The application is built using FastAPI and focuses on prioritizing relevant search results based on meaning and context, rather than exact keyword matches.

## Features

- **Upload API**: Allows uploading new case study documents in PDF format.
- **Search API**: Takes a search query and returns a list of relevant case study document names.
- **Semantic Search**: Utilizes document embeddings to provide context-aware search results.

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- PyPDF2 (for PDF processing)
- Sentence-Transformers (for generating document embeddings)
- Pinecone (or any other vector database)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/dee161/MindTickle-Semantic-Search-System
    cd mindtickle-semantic-search
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up Pinecone (or your chosen vector database) and add your API key and environment to a `.env` file:
    ```sh
    PINECONE_API_KEY=your_api_key
    PINECONE_ENV=your_environment
    ```

### Running the Application

1. Start the FastAPI server using Uvicorn:
    ```sh
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Upload Document

- **Endpoint**: `/upload`
- **Method**: `POST`
- **Description**: Uploads a new case study document to the system.
- **Request**:
    - `file`: Form-data containing the PDF file to upload.
- **Response**:
    ```json
    {
        "message": "File uploaded successfully",
        "file_name": "example.pdf"
    }
    ```

### Search Documents

- **Endpoint**: `/docs`
- **Method**: `GET`
- **Description**: Returns a list of relevant case study document names based on the search query.
- **Request**:
    - `q`: The search query as a URL parameter.
- **Response**:
    ```json
    {
        "results": [
            "Case Study 1",
            "Case Study 2",
            ...
        ]
    }
    ```

## Folder Structure

