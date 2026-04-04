import frappe

@frappe.whitelist()
def bootstrap():
    return {
        "modes": [
            {"name": "AI Chat", "icon": "octicon-comment-discussion", "description": "Ask business questions and get guided answers."},
            {"name": "BI / Reports", "icon": "octicon-graph", "description": "Generate report and dashboard blueprints from prompts."},
            {"name": "Document AI", "icon": "octicon-file-text", "description": "Explain the current document, risks, and next steps."},
            {"name": "Automate Work", "icon": "octicon-zap", "description": "Use recipes for follow-ups, notes, tasks, and approvals."},
            {"name": "Voice", "icon": "octicon-unmute", "description": "Open modules, reports, and actions using voice intents."},
        ],
        "quick_cards": [
            {"title": "Sales Summary Today", "prompt": "Show today sales summary with KPIs and suggested actions."},
            {"title": "Receivables Risk", "prompt": "Summarize overdue receivables and collection priorities."},
            {"title": "Inventory Status", "prompt": "Show low stock items and warehouse exceptions."},
            {"title": "Project Delay Risk", "prompt": "Identify projects likely to slip and explain why."},
            {"title": "Explain This Record", "prompt": "Summarize this record, risks, missing data, and next actions."},
        ],
        "sample_voice": [
            "Open Sales Invoice",
            "Show overdue purchase orders",
            "Open payroll variance report",
            "Summarize this document",
        ]
    }
