
# 🚀 Kasparro – Multi-Agent Content Generation System  
### Author: **Amogh G**

This repository contains a complete **multi-agent automation system** built for the **Kasparro Applied AI Engineer Challenge**.

The system dynamically processes any product JSON input and automatically generates:

- **FAQ Page (faq.json)**
- **Product Detail Page (product_page.json)**
- **Comparison Page (comparison_page.json)**

It uses a **DAG-style agent workflow**, reusable logic blocks, JSON templates, and the **Google Gemini API** for AI-powered content generation.

---

# 📌 Features

### ✔ Multi-Agent Architecture  
The system intelligently divides work among four autonomous agents:
- **Input Parser Agent**
- **Question Generation Agent**
- **Template Engine Agent**
- **Orchestrator Agent**

### ✔ Dynamic Product Input  
Place any product JSON inside:


data/product.json

The system will auto-generate all three output pages using this new input.

### ✔ Template-Driven Architecture  
Uses JSON templates stored in `/templates` to ensure:
- Scalability
- Easy updates
- High consistency

### ✔ Google Gemini AI Question Generator  
Automatically generates **20+ customer questions**, clearly categorized into:
- Informational  
- Usage  
- Safety  
- Purchase  
- Comparison  

### ✔ Clean JSON Output  
Outputs are saved to:


output/
faq.json
product_page.json
comparison_page.json

These files are machine-readable and production-friendly.

---

# 📂 Project Structure


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
│ ├── input_parser_agent.py
│ ├── question_generation_agent.py
│ ├── template_engine_agent.py
│ └── orchestrator_agent.py
│
├── logic_blocks/
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
│ └── (generated files)
│
└── docs/
└── projectdocumentation.md

---

# ⚙️ Installation

### **1️⃣ Clone the repository**
git clone [https://github.com/AMOGH1308/kasparro-ai-agentic-content-generation-system-Amogh-Guruprakash](https://github.com/AMOGH1308/kasparro-ai-agentic-content-generation-system-Amogh-Guruprakash)
cd kasparro-ai-agentic-content-generation-system-Amogh-Guruprakash

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your Gemini API key
Create a .env file in the root:
GEMINI_API_KEY=your_api_key_here

▶️ Running the System
Run:
python main.py

If you're on Windows and facing encoding issues:
python -Xutf8 main.py

You will find your generated JSON files inside:
output/

📘 Documentation
Full system documentation (flowcharts, diagrams, detailed file explanations) is available here:
docs/projectdocumentation.md

📊 Example Output (Preview)
{
  "faq": {
    "title": "FAQ: GlowBoost Vitamin C Serum",
    "questions": {
      "Informational": ["What is this product used for?"],
      "Usage": ["How should this serum be applied?"],
      "Safety": ["Are there any side effects?"],
      "Purchase": ["What is the price?"],
      "Comparison": ["How does this differ from other serums?"]
    }
  },
  "product_page": {
    "name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "skin_type": "Oily, Combination",
    "ingredients": "Vitamin C, Hyaluronic Acid",
    "benefits": "Brightening, Reduces dark spots",
    "usage": "Apply 2-3 drops in the morning",
    "side_effects": "Mild tingling",
    "price": "₹699"
  },
  "comparison_page": {
    "product_a": "GlowBoost Vitamin C Serum",
    "product_b": "RadiantGlow Serum B",
    "ingredient_comparison": "Vitamin C + Hyaluronic Acid vs Vitamin E + Green Tea",
    "benefits_comparison": "Brightening vs Hydration",
    "price_comparison": "₹699 vs ₹899"
  }
}

⭐ Why This Project Stands Out
This system demonstrates:
Strong multi-agent engineering
Clean template-based content generation
AI-driven Q&A generation
Modular and scalable architecture
Professional documentation & diagrams
Real-world workflow automation
Dynamic product input handling
It aligns exactly with Kasparro's expectations for an Applied AI Engineer.

🏁 Conclusion
This repository delivers a fully automated, AI-powered agentic content generation engine that is:
Scalable
Modular
Automated
Well-documented
Ready for production
It fulfills all challenge requirements and demonstrates strong software engineering + AI integration skills.

🙌 Author
Amogh Guruprakash
Applied AI Engineer Candidate – Kasparro

---

