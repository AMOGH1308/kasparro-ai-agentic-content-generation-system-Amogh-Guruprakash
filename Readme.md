# Kasparro – Multi-Agent Content Generation System  
### Author: **Amogh G**

This repository contains a complete **multi-agent automation system** designed for the **Kasparro Applied AI Engineer Challenge**.  
The system processes dynamic product data and generates three structured JSON pages:

- **FAQ Page**  
- **Product Description Page**  
- **Comparison Page**

It uses a **DAG-style orchestration** with multiple agents, reusable content logic blocks, and JSON templates.  
AI-driven question generation is powered by **Google Gemini**.

---

## 🚀 Features

### ✔ Multi-Agent Architecture  
Each agent solves a specific task:
- Input Parser Agent  
- Question Generation Agent  
- Template Engine Agent  
- Orchestrator Agent  

### ✔ Dynamic Product Input  
Place any product info in:  


→ System automatically generates all content pages.

### ✔ Template-Based Content System  
Fillable JSON templates allow flexible, maintainable content generation:
- `faq_template.json`
- `product_template.json`
- `comparison_template.json`

### ✔ AI-Powered Question Generation  
20+ user questions are generated automatically using the Google Gemini API and categorized into:
- Informational  
- Usage  
- Safety  
- Purchase  
- Comparison  

### ✔ Clean, Machine-Readable JSON Output  
All pages are saved inside `/output`:
output/
├── faq.json
├── product_page.json
└── comparison_page.json


---

## 🏗 Folder Structure

project/
│── main.py
│── genai_client.py
│── .env
│── .gitignore
│
├── data/
│ └── product.json
│
├── agents/
│ ├── init.py
│ ├── input_parser_agent.py
│ ├── question_generator_agent.py
│ ├── template_engine_agent.py
│ └── orchestrator_agent.py
│
├── logic_blocks/
│ ├── init.py
│ ├── parsing.py
│ ├── question_logic.py
│ ├── template_logic.py
│ ├── template_loader.py
│ └── comparison_logic.py
│
├── templates/
│ ├── faq_template.json
│ ├── product_template.json
│ └── comparison_template.json
│
├── output/
│ └── (generated JSON files)
│
└── docs/
└── projectdocumentation.md


---

## ⚙️ Installation

### 1️⃣ Install dependencies  
pip install -r requirements.txt

### 2️⃣ Create `.env` file  
GEMINI_API_KEY=YOUR_API_KEY_HERE


### 3️⃣ (Windows fix)  
If output shows encoding issues (â‚¹ instead of ₹):  
Run Python with UTF-8 mode:

python -Xutf8 main.py



---

## ▶️ Running the System

To run the entire multi-agent pipeline:


This will:
- Parse product data  
- Generate categorized questions  
- Fill templates  
- Save JSON pages into `/output`  

---

## 🧠 Technologies Used

- Python  
- Google Gemini API  
- Modular Agent Architecture  
- JSON templating  
- Reusable content logic blocks  
- DAG-style orchestration  

---

## 📘 Documentation

Full project documentation including **architecture diagrams**, **sequence diagrams**, and **file-level explanations** is available in:

docs/projectdocumentation.md

(Or `docs/complete_documentation.md` if you used the combined version.)

---

## 🏁 Conclusion

This project demonstrates:

- Strong system design  
- Modular, scalable architecture  
- Real AI engineering practices  
- Multi-agent orchestration  
- Template-based content automation  
- Clean JSON generation  



