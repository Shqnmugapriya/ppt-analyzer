# AI-Powered PPT Analyzer 📊🤖

An intelligent web application that analyzes PowerPoint presentations and PDF documents using **OCR and Generative AI** to provide meaningful feedback on content clarity, organization, sentence quality, and missing information.

## 📌 Overview

Presentations are an important way to communicate ideas, but creating clear, well-structured, and informative slides can be challenging.

The **AI-Powered PPT Analyzer** helps users evaluate their presentation content by extracting text from uploaded files and analyzing it with Google's Gemini AI model. It generates actionable suggestions to improve readability, content organization, and overall presentation quality.

The application supports OCR-based text extraction, making it possible to analyze text contained in scanned documents and image-based slides.

## 🎯 Objectives

- Extract text from uploaded PowerPoint presentations and PDF documents.
- Use Optical Character Recognition (OCR) to process text embedded in images and scanned pages.
- Analyze extracted content using Generative AI.
- Identify unclear sentences, missing information, and poorly organized content.
- Suggest improvements to make presentations clearer, more informative, and easier to understand.

## ✨ Key Features

- **📂 File Upload:** Upload supported PowerPoint and PDF files for analysis.
- **🔍 OCR-Based Text Extraction:** Extract text from scanned pages and image-based content.
- **🧠 AI-Powered Analysis:** Use the Gemini 2.5 Flash model to evaluate presentation content.
- **✍️ Clarity Suggestions:** Identify unclear sentences and recommend better wording.
- **🗂️ Content Organization:** Receive suggestions for improving the flow and structure of information.
- **📝 Missing Information Detection:** Highlight areas where additional explanations or details may be useful.
- **💡 Actionable Feedback:** Generate suggestions for expanding, simplifying, or refining sentences.
- **🌐 Web-Based Interface:** Interact with the analyzer through a user-friendly React application.

## 🛠️ Technology Stack

| Component         | Technology              |
| ----------------- | ----------------------- |
| Frontend          | React.js                |
| Backend           | Java                    |
| Backend Framework | Spring Boot             |
| Text Extraction   | OCR                     |
| AI Integration    | Google Gemini 2.5 Flash |
| API Communication | REST APIs               |
| Build Tool        | Maven                   |
| Version Control   | Git and GitHub          |

## 🏗️ System Architecture

The application follows a frontend-backend architecture.

1. **Upload:** The user uploads a PowerPoint presentation or PDF document.
2. **Text Extraction:** The backend processes the document and uses OCR to extract readable text where required.
3. **Content Preparation:** The extracted text is prepared for AI analysis.
4. **AI Processing:** The backend sends the extracted content and an analysis prompt to the Gemini API.
5. **Feedback Generation:** The AI generates feedback on clarity, structure, missing details, and sentence quality.
6. **Result Display:** The frontend displays the generated suggestions to the user.

## 🔄 Application Workflow

```text
          User
            |
            v
   Upload PPT / PDF
            |
            v
    React.js Frontend
            |
            v
   Spring Boot Backend
            |
            v
   Document Text Extraction
            |
            v
       OCR Processing
            |
            v
   Extracted Text + Prompt
            |
            v
    Gemini 2.5 Flash API
            |
            v
     AI-Generated Feedback
            |
            v
   Display Results in React
```

## 📁 Project Structure

The exact directory structure may vary depending on your implementation.

```text
AI-PPT-Analyzer/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── .env.example
│
├── backend/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   └── resources/
│   │   └── test/
│   ├── pom.xml
│   └── .env.example
│
├── .gitignore
└── README.md
```

*Note: Update the structure to match your actual project folders and files.*

## ⚙️ Prerequisites

Before running the application, ensure you have installed:

- Node.js and npm
- Java Development Kit (JDK)
- Maven, or use the project's Maven Wrapper if available
- A Google Gemini API key
- The OCR engine or library configured by the project

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-PPT-Analyzer
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Configure the Backend

Navigate to the backend directory:

```bash
cd backend
```

Configure the Gemini API key using the environment variable or configuration method supported by your implementation.

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

Make sure the backend reads this value from its configuration. Never commit real API keys or other secrets to GitHub.

Run the Spring Boot application:

```bash
mvn spring-boot:run
```

### 3. Configure the Frontend

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed in the terminal to access the application.

> **Note:** The commands and environment variable names above are examples. Adjust them to match your actual project configuration.

## 🧪 Example Analysis

**Input:** A presentation about Artificial Intelligence in Healthcare.

**Possible AI-generated feedback:**

- **Clarity:** Simplify technical sentences that may be difficult for a general audience.
- **Organization:** Arrange the problem statement before introducing the proposed solution.
- **Missing Information:** Add relevant examples or supporting evidence to strengthen key claims.
- **Sentence Improvement:** Rewrite lengthy sentences into shorter, clearer statements.
- **Content Development:** Expand sections that introduce concepts without sufficient explanation.

*The output depends on the uploaded document and the AI model's response.*

## 🔐 Security Considerations

- Keep API keys on the backend and out of frontend source code.
- Store secrets in environment variables or an appropriate secret-management system.
- Validate uploaded files and enforce reasonable file-size limits.
- Handle unsupported formats, extraction failures, and API errors gracefully.
- Avoid logging sensitive document contents unnecessarily.

## 🔮 Future Enhancements

- Slide-by-slide analysis with slide-specific suggestions.
- Presentation quality scoring based on defined evaluation criteria.
- Grammar and readability analysis.
- Recommendations for improving slide titles and summaries.
- Exportable analysis reports in PDF format.
- Support for additional document formats.
- More detailed feedback on logical flow and content consistency.

## 🎓 Learning Outcomes

This project provides practical experience in:

- Full-stack web application development.
- Building REST APIs with Java and Spring Boot.
- Integrating a Generative AI API into a backend application.
- Applying OCR to document-processing workflows.
- Connecting a React frontend with a Spring Boot backend.
- Handling file uploads, API responses, and error scenarios.
- Designing AI-assisted content analysis workflows.

## 🖥️ Application Screenshots

### 1. Dashboard

<img width="1906" height="908" alt="AI PPT Analyzer Dashboard" src="C:\Users\DELL\Downloads\ss.jpg" />

### 2. Presentation Upload

<img width="1906" height="908" alt="AI PPT Analyzer Upload Page" src="C:\Users\DELL\Downloads\ss2.jpg"
 />

### 3. AI Analysis Results

<img width="1906" height="908" alt="AI PPT Analyzer Analysis Results" src="C:\Users\DELL\Downloads\ss3.jpg"
 />

## 👩‍💻 Author

**Shanmugapriya S**

B.Tech – Artificial Intelligence and Data Science
