# QA Automation Portfolio

A complete testing strategy demonstration covering API testing, UI automation, and performance testing.

## 📊 Project Overview

This project showcases:
- **API Testing**: Data-driven testing with Pytest + Requests
- **UI Automation**: Page Object Model (POM) with Selenium
- **Performance Testing**: Load & spike testing with K6

## 🏗️ Project Structure

```
qa-automation-portfolio/
├── api-tests/           # API automation tests
├── ui-tests/            # UI automation tests
├── performance-tests/   # K6 performance tests
├── requirements.txt     # Python dependencies
└── README.md
```

## Quick Start

```bash
# Clone and setup
git clone 
cd qa-automation-portfolio

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)

# Install dependencies
pip install -r requirements.txt

# Run API tests
pytest api-tests/ -v

# Run UI tests
pytest ui-tests/ -v
```


## 🎓 Key Concepts

- Pytest fixtures & conftest
- RESTful API testing
- Page Object Model (POM)
- WebDriverWait & explicit waits
- K6 scenarios & thresholds
- GitHub Actions CI/CD

---
