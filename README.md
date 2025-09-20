<div align="center">

# 🤖 AI-Powered Customer Support Email Generator

**Transform customer complaints into professional, empathetic email responses using Google Gemini AI**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gemini AI](https://img.shields.io/badge/Powered%20by-Google%20Gemini-orange.svg)](https://ai.google.dev/)

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-api-documentation) • [🌟 Features](#-features) • [🛠️ Installation](#-installation--setup)

</div>

---

## 🌟 Features

<table>
<tr>
<td width="33%">
<h3>🧠 AI-Powered</h3>
<ul>
<li>Google Gemini 1.5 Flash integration</li>
<li>Context-aware response generation</li>
<li>Customizable creativity parameters</li>
</ul>
</td>
<td width="33%">
<h3>💼 Professional</h3>
<ul>
<li>Empathetic & solution-oriented</li>
<li>Consistent professional tone</li>
<li>Industry-standard responses</li>
</ul>
</td>
<td width="33%">
<h3>🎨 Modern UI</h3>
<ul>
<li>Responsive TailwindCSS design</li>
<li>Real-time generation feedback</li>
<li>Copy & download functionality</li>
</ul>
</td>
</tr>
</table>

### ✨ Core Capabilities

- **🔄 Real-time Generation**: Instant AI-powered email responses with progress indicators
- **📱 Responsive Design**: Seamless experience across desktop, tablet, and mobile devices
- **🛡️ Error Handling**: Comprehensive validation and user-friendly error messages
- **📊 API Monitoring**: Health check endpoints for system monitoring
- **⚙️ Configurable**: Adjustable AI parameters (temperature, tokens, sampling)
- **🔗 RESTful API**: Clean REST endpoints for integration with other systems

## 📋 Requirements

| Component | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.8+ | Runtime environment |
| **Google Gemini API** | Latest | AI response generation |
| **Internet Connection** | - | API communication |

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jayeshmahale932/AI-Email-Generator.git
cd AI-Email-Generator
```

### 2. Environment Setup

<details>
<summary><b>🐍 Python Virtual Environment</b></summary>

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
</details>

### 3. API Configuration

<details>
<summary><b>🔑 Gemini API Key Setup</b></summary>

1. **Get your API key** from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. **Configure** in one of these ways:

**Option A: Configuration File** (Recommended)
```yaml
# config.yaml
gemini:
  model: "gemini-1.5-flash"
  api_key: "your-actual-api-key-here"
  temperature: 0.7
  max_output_tokens: 1000
```

**Option B: Environment Variable**
```bash
# .env file
GEMINI_API_KEY=your-actual-api-key-here
```
</details>



## 🚀 Quick Start

### 1. Launch the Application

```bash
python app.py
```

You'll see:
```
🚀 Starting AI-Powered Customer Support Email Generator...
🌐 Server running at http://127.0.0.1:5000
```

### 2. Access the Web Interface

Open your browser and navigate to **`http://localhost:5000`**

### 3. Basic Usage

1. **📝 Input**: Enter a customer complaint in the text area
2. **🎯 Generate**: Click "Generate Professional Email"
3. **📋 Export**: Copy to clipboard or download as text file

### 4. API Integration

<details>
<summary><b>📡 REST API Examples</b></summary>

**Generate Single Response:**
```bash
curl -X POST http://localhost:5000/generate_email \
  -H "Content-Type: application/json" \
  -d '{
    "complaint": "I ordered a product 2 weeks ago and it still hasnt arrived!"
  }'
```

**Response:**
```json
{
  "success": true,
  "email": "Dear Valued Customer,\n\nWe sincerely apologize for the delay...",
  "timestamp": "2025-09-21T00:00:00Z"
}
```
</details>


## 📱 Web Interface Features

<table>
<tr>
<td width="50%">
<h4>🎨 User Experience</h4>
<ul>
<li><strong>Responsive Design</strong>: Desktop, tablet & mobile optimized</li>
<li><strong>Real-time Feedback</strong>: Loading animations & progress indicators</li>
<li><strong>Professional Styling</strong>: Modern TailwindCSS interface</li>
</ul>
</td>
<td width="50%">
<h4>⚡ Functionality</h4>
<ul>
<li><strong>One-Click Copy</strong>: Copy generated emails to clipboard</li>
<li><strong>Download Export</strong>: Save responses as text files</li>
<li><strong>Smart Validation</strong>: Prevents empty/invalid submissions</li>
</ul>
</td>
</tr>
</table>

## ⚙️ Configuration

<details>
<summary><b>🔧 Advanced Configuration</b></summary>

### Gemini AI Parameters

```yaml
# config.yaml
gemini:
  model: "gemini-1.5-flash"          # Model selection
  api_key: "your_api_key_here"       # API authentication
  temperature: 0.7                   # Creativity (0.0-1.0)
  max_output_tokens: 1000            # Response length limit
  top_p: 0.9                        # Nucleus sampling
  top_k: 40                         # Top-k sampling
```

| Parameter | Range | Description |
|-----------|-------|-------------|
| `temperature` | 0.0-1.0 | Controls response creativity |
| `max_output_tokens` | 100-2048 | Maximum response length |
| `top_p` | 0.0-1.0 | Nucleus sampling threshold |
| `top_k` | 1-100 | Top-k sampling parameter |

### Server Configuration

```yaml
api:
  host: "127.0.0.1"                 # Bind address
  port: 5000                        # Port number
  debug: true                       # Development mode

logging:
  level: "INFO"                     # Log verbosity
  file: "logs/email_generator.log"  # Log file path
```

</details>

## 🏗️ Project Structure

```
📦 ai-email-generator/
├── 📄 app.py                    # 🚀 Flask application & API endpoints
├── 📄 config.yaml              # ⚙️ Configuration settings
├── 📄 requirements.txt          # 📦 Python dependencies
├── 📄 .env                     # 🔐 Environment variables
├── 📁 templates/
│   └── 📄 index.html           # 🎨 Web interface (TailwindCSS)
├── 📁 static/                  # 🖼️ Static assets (optional)
├── 📁 logs/                    # 📊 Application logs
├── 📁 venv/                    # 🐍 Virtual environment
└── 📄 README.md               # 📖 Documentation
```

## 🛠️ Development Guide

<details>
<summary><b>🔨 Development Setup</b></summary>

### Local Development

```bash
# Enable development mode
export FLASK_ENV=development
export FLASK_DEBUG=True

# Run with auto-reload
python app.py
```

### Adding Features

| Component | File | Purpose |
|-----------|------|---------|
| **API Routes** | `app.py` | Backend endpoints |
| **UI Components** | `templates/index.html` | Frontend interface |
| **Configuration** | `config.yaml` | Settings & parameters |
| **Styling** | `templates/index.html` | TailwindCSS classes |

</details>

## 🆘 Troubleshooting

<details>
<summary><b>🔍 Common Issues & Solutions</b></summary>

### ❌ API Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| "AI model not available" | Invalid API key | ✅ Verify Gemini API key in `config.yaml` |
| Request timeout | Network/API issues | ✅ Check internet connection & API status |
| Rate limiting | Too many requests | ✅ Implement request throttling |

### ❌ Installation Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| "Module not found" | Missing dependencies | ✅ Run `pip install -r requirements.txt` |
| "Port already in use" | Port conflict | ✅ Change port in `config.yaml` or kill process |
| Permission errors | Directory access | ✅ Check folder permissions |

### 🩺 Health Checks

```bash
# Test API health
curl http://localhost:5000/health

# Check logs
tail -f logs/email_generator.log

# Verify dependencies
pip list | grep -E "(flask|google-generativeai|pyyaml)"
```

</details>

## � Example Usage

<details>
<summary><b>📝 Real-World Examples</b></summary>

### Example 1: Delivery Delay

**Input Complaint:**
```
I ordered a laptop from your website 3 weeks ago and it still hasn't arrived. 
I've tried calling customer service multiple times but no one answers. 
This is completely unacceptable and I want a full refund immediately!
```

**Generated Response:**
```
Dear Valued Customer,

Thank you for contacting us regarding your recent laptop order. I sincerely 
apologize for the delay in delivery and the difficulty you've encountered 
reaching our customer service team.

I understand how frustrating this situation must be, especially after waiting 
3 weeks for your order. This does not meet our usual standards of service, 
and I want to make this right for you immediately.

I will personally track your order and provide you with a detailed update 
within 24 hours. Additionally, I'm escalating your case to our priority 
support team to ensure faster resolution.

As an apology for this inconvenience, I would like to offer you:
- Expedited shipping at no additional cost
- A 15% discount on your current order
- Priority customer service access for any future needs

Please reply with your order number so I can begin tracking this immediately.

We value your business and appreciate your patience as we resolve this matter.

Best regards,
Customer Support Team
```

### Example 2: Product Defect

**Input:** `"The phone I bought last week has a cracked screen out of the box!"`

**Generated:** Professional response acknowledging the defect, offering immediate replacement, and providing clear next steps.

### Example 3: Billing Issue

**Input:** `"I was charged twice for the same subscription!"`

**Generated:** Empathetic response explaining the investigation process, timeline for resolution, and immediate credit offer.

</details>

## 🔒 Security & Best Practices

<div align="center">

| ⚠️ **Security Checklist** |
|---------------------------|
| ✅ API keys in environment variables |
| ✅ Input validation & sanitization |
| ✅ Rate limiting for production |
| ✅ HTTPS for public deployment |
| ✅ Regular dependency updates |

</div>

### 🛡️ Security Guidelines

- **🔐 API Key Security**: Never commit API keys to version control
- **🌐 Network Security**: Use HTTPS in production environments
- **📝 Input Validation**: All user inputs are validated and sanitized
- **⚡ Rate Limiting**: Implement rate limiting for public deployments
- **📦 Dependencies**: Keep dependencies updated for security patches

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

<details>
<summary><b>🔄 Development Workflow</b></summary>

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

</details>

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### 📋 Third-Party Licenses
- Google Gemini AI: Subject to [Google's Terms of Service](https://ai.google.dev/terms)
- Flask: BSD-3-Clause License
- TailwindCSS: MIT License

---

<div align="center">

### 🌟 Built With

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Google AI](https://img.shields.io/badge/Google%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

**Made with ❤️ for better customer support**

[⭐ Star this project](https://github.com/yourusername/ai-email-generator) • [🐛 Report Bug](https://github.com/yourusername/ai-email-generator/issues) • [💡 Request Feature](https://github.com/yourusername/ai-email-generator/issues)

</div>

## 📚 API Documentation

<details>
<summary><b>🔗 REST API Reference</b></summary>

### Core Endpoints

#### `POST /generate_email`
Generate a professional email response to a customer complaint.

**Request:**
```json
{
  "complaint": "Your service is absolutely terrible!"
}
```

**Response:**
```json
{
  "success": true,
  "email": "Dear Valued Customer,\n\nWe sincerely apologize for your...",
  "timestamp": "2025-09-21T00:00:00Z"
}
```

#### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "model_available": true,
  "timestamp": "2025-09-21T00:00:00Z"
}
```

#### `GET /`
Serves the interactive web interface.

</details>

## 🎯 Response Quality Guidelines

Our AI model generates responses following these principles:

| Principle | Description | Example |
|-----------|-------------|---------|
| **🤝 Empathetic** | Acknowledges customer feelings | "We understand your frustration..." |
| **💼 Professional** | Maintains formal, courteous tone | Avoids casual language |
| **🎯 Solution-Oriented** | Offers concrete next steps | Clear action items & timelines |
| **🔒 Privacy-Conscious** | No hallucinated personal details | Generic, safe responses |
| **📏 Appropriate Length** | Concise but thorough | 50-200 words typically |