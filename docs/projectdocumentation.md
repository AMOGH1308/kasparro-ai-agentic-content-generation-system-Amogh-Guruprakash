# Kasparro – Multi-Agent Content Generation System  
### Project Documentation  
Author: **Amogh G**

---

# 1. Problem Statement

The Kasparro Applied AI Engineer Challenge requires building a **modular, multi-agent content generation system** capable of:

- Parsing product data  
- Generating categorized user questions using AI  
- Filling predefined templates  
- Producing three structured JSON content pages  
- Running through a **DAG-style (Directed Acyclic Graph) multi-agent workflow**  
- Supporting **dynamic input** rather than fixed hard-coded data  

This system demonstrates professional-level AI engineering:  
- Multi-agent orchestration  
- Content automation  
- Template-driven generation  
- Modular, clean architecture  
- AI-LangChain style pipeline  
- Strong documentation  

---

# 2. Solution Overview

This project implements:

### ✔ Four Autonomous Agents
1. **Input Parser Agent**  
2. **Question Generation Agent (Gemini-powered)**  
3. **Template Engine Agent**  
4. **Orchestrator Agent**  

### ✔ Six Logic Blocks
- Parsing logic  
- Question categorization logic  
- Comparison logic  
- Template loader  
- Template generator  
- Data normalization  

### ✔ Three Template Files
- faq_template.json  
- product_template.json  
- comparison_template.json  

### ✔ Three Output Files
- faq.json  
- product_page.json  
- comparison_page.json  

### ✔ Dynamic Data Support
The system reads from:  


Changing this file automatically updates all generated content.

---

# 3. Architecture Diagram (Mermaid)

```mermaid
flowchart TD

    A[Input<br>Product Data JSON]:::input

    B[Orchestrator Agent<br>DAG Workflow]:::orchestrator

    S1[Parsing Logic]:::support
    S2[Content Logic Blocks<br>Questions + Comparison]:::support
    S3[Template Engine<br>Loader + Renderer]:::support

    C1[Input Parser Agent]:::agent
    C2[Question Generation Agent]:::agent
    C3[Template Engine Agent]:::agent

    O1[faq.json]:::output
    O2[product_page.json]:::output
    O3[comparison_page.json]:::output

    %% Flow
    A --> B
    B --> C1
    C1 --> C2
    C2 --> C3

    S1 --- C1
    S2 --- C2
    S3 --- C3

    C3 --> O1
    C3 --> O2
    C3 --> O3

    %% STYLES
    classDef input fill:#f5a623,stroke:#333,color:#000;
    classDef orchestrator fill:#7ed321,stroke:#333,color:#000;
    classDef support fill:#4a90e2,stroke:#333,color:#fff;
    classDef agent fill:#9013fe,stroke:#333,color:#fff;
    classDef output fill:#50e3c2,stroke:#333,color:#000;


sequenceDiagram
    autonumber

    participant User
    participant Main
    participant Orchestrator
    participant ParserAgent
    participant QuestionAgent
    participant TemplateAgent
    participant Output

    User ->> Main: Run main.py
    Main ->> Orchestrator: Load product.json

    Orchestrator ->> ParserAgent: Parse product data
    ParserAgent -->> Orchestrator: Clean structured data

    Orchestrator ->> QuestionAgent: Generate + categorize questions
    QuestionAgent -->> Orchestrator: FAQ categories (JSON)

    Orchestrator ->> TemplateAgent: Apply templates
    TemplateAgent -->> Orchestrator: Rendered JSON pages

    Orchestrator ->> Output: Save faq.json
    Orchestrator ->> Output: Save product_page.json
    Orchestrator ->> Output: Save comparison_page.json

    Output -->> User: All pages generated successfully


# 📂 Folder: agents/ (Core Agents of the Pipeline)

---

## **agents/input_parser_agent.py**
### **Purpose**
Parses and normalizes raw product data into a clean internal dictionary.

### **Why this is needed**
- Ensures consistent field structure  
- Avoids missing/incorrect keys  
- Supplies clean, structured data for downstream agents  

---

## **agents/question_generation_agent.py**
### **Purpose**
Uses the Google Gemini model to generate **20 natural customer questions**, then categorizes them into:

- Informational  
- Usage  
- Safety  
- Purchase  
- Comparison  

### **Why this is important**
This directly fulfills the assignment requirement of generating **categorized FAQs** using an AI model.

---

## **agents/template_engine_agent.py**
### **Purpose**
Applies JSON templates by replacing placeholders with actual product data.

### **Responsibilities**
- Loads template JSON  
- Replaces placeholders such as `{name}`, `{price}`  
- Inserts dictionary objects like `{questions}` correctly  
- Produces clean, structured JSON content pages  

---

## **agents/orchestrator_agent.py**
### **Purpose**
Controls the entire **multi-agent DAG pipeline**.

### **Workflow**
1. Call **Input Parser Agent**  
2. Call **Question Generation Agent**  
3. Create a fictional **Product B**  
4. Generate a structured **comparison**  
5. Call **Template Engine Agent**  
6. Write all JSON outputs to the `/output` folder  

### **Why it matters**
This file is the **central brain** of the system and ensures all agents run in the correct order.

---

# 📂 Folder: logic_blocks/ (Reusable Logic Modules)

---

## **logic_blocks/parsing.py**
### **Purpose**
Defines extraction and normalization rules for:

- Product Name  
- Concentration  
- Skin Type  
- Ingredients  
- Benefits  
- Usage  
- Side effects  
- Price  

This ensures consistent downstream behavior.

---

## **logic_blocks/question_logic.py**
### **Purpose**
Categorizes generated questions using keyword/intent detection:

| Keyword(s)        | Category       |
|------------------|----------------|
| what, ingredient | Informational  |
| use, apply       | Usage          |
| safe, side effect | Safety         |
| price, buy       | Purchase       |
| otherwise        | Comparison     |

---

## **logic_blocks/template_logic.py**
### **Purpose**
Implements the **template substitution engine**:

- Replaces `{placeholder}` text  
- Inserts dictionary objects (`{questions}`)  
- Ensures JSON remains valid  

---

## **logic_blocks/template_loader.py**
### **Purpose**
Loads JSON templates from the `/templates` folder.

This cleanly separates:
- Template loading  
- Template filling  

---

## **logic_blocks/comparison_logic.py**
### **Purpose**
Generates structured comparison between:

- **Product A** (input product)  
- **Product B** (fictional competitor)  

### **Compares**
- Ingredients  
- Benefits  
- Price  

Used by the **Template Engine Agent** to fill comparison templates.

---

# 📂 Folder: templates/

---

## **templates/faq_template.json**
### **Purpose**
Defines FAQ page structure:

```json
{
  "title": "FAQ: {product}",
  "questions": "{questions}"
}


## 📂 Folder: templates/

---

### **templates/product_template.json**
#### **Purpose**
Defines the product detail page layout:

```json
{
  "name": "{name}",
  "concentration": "{concentration}",
  "skin_type": "{skin_type}",
  "ingredients": "{ingredients}",
  "benefits": "{benefits}",
  "usage": "{usage}",
  "side_effects": "{side_effects}",
  "price": "{price}"
}

## templates/comparison_template.json

### Purpose
Defines structured product comparison layout between Product A and Product B.
This template is filled by the Template Engine Agent using:
- Parsed product data
- Generated comparison logic output

## 📂 Folder: output/

### Generated Files
This folder contains all final generated machine-readable content pages:
- faq.json
- product_page.json
- comparison_page.json

Each file is created automatically by the Orchestrator Agent during execution.

## 🔄 6. Full Workflow Execution

1. User runs main.py
2. Product JSON is loaded from /data
3. Parser Agent cleans and normalizes input data
4. QGen Agent generates categorized user questions using Gemini
5. Comparison Logic compares Product A to a fictional Product B
6. Template Engine Agent fills JSON templates with structured data
7. Orchestrator Agent writes all JSON output files to /output

The entire pipeline is fully automated and modular.

## ⚙️ 7. Extensibility & Scalability

This architecture is designed for real production scalability.

Supports extension into:
- New agents (e.g., review generator, SEO content agent)
- More templates (landing pages, ads, descriptions, blogs)
- Additional output formats (HTML, PDF, Markdown)
- REST API version using FastAPI or Flask
- Batch processing of multiple products
- Database integration (MongoDB, PostgreSQL)
- Brand-specific and domain-specific content generation

Built as a production-friendly, modular pipeline.

## ⭐ 8. Why This Solution Should Be Selected

This project demonstrates:
- ✔ Strong multi-agent system design
- ✔ Clean content pipeline engineering
- ✔ Template-driven structured output generation
- ✔ Modular, readable, scalable architecture
- ✔ Reusable logic blocks and template system
- ✔ Dynamic product data handling
- ✔ Professional diagrams and documentation

This aligns perfectly with the expectations for an **Applied AI Engineer at Kasparro**.

## 🏁 9. Conclusion

This system is a complete end-to-end agentic content generation engine:
- Automated
- Scalable
- Modular
- AI-powered
- Professionally engineered
