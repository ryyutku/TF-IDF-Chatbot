# 🤖 FAQ Chatbot with TF-IDF and Cosine Similarity
A lightweight, rule-based FAQ chatbot that uses TF-IDF vectorization and cosine similarity to provide instant answers to frequently asked questions without the need for large language models.

## 🎯 Purpose

This chatbot is designed for businesses and organizations that need a simple, cost-effective way to automate their FAQ responses. Instead of relying on complex and resource-intensive LLMs, this solution uses proven NLP techniques to match user questions with pre-defined answers from a knowledge base.

## ✨ Features

- **⚡ Fast & Lightweight**: No GPU required, instant responses
- **💰 Cost-Effective**: No API costs or expensive infrastructure
- **🔒 Privacy-Focused**: All processing happens locally
- **📝 Easy Maintenance**: Update FAQs via simple CSV file
- **🎚️ Configurable Threshold**: Adjust sensitivity for matching
- **🔄 Ready-to-Use**: Just add your FAQs and deploy

## 🚀 Quick Start

### Prerequisites
Python 3.7 or higher
pip install scikit-learn pandas

### Prepare your FAQ data:
Create a faqs.csv file in the project root with the following format:
question,answer
"What services do you provide?","We provide web development, mobile app development, and cloud consulting services."
"How can I contact support?","You can email support@company.com or call 1-800-555-0199."
"What are your business hours?","We are open Monday to Friday, 9 AM to 5 PM EST."

### Important CSV Requirements:
The CSV file must have two columns: question and answer
Column names are case-sensitive: use exactly question and answer
Each row should contain one FAQ pair
Questions and answers should be enclosed in double quotes if they contain commas

### Install dependencies & Run chatbot:
```bash
pip install pandas scikit-learn numpy
python chatbot.py
