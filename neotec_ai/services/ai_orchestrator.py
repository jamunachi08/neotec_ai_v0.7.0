def _followups(mode):
    mapping = {
        "AI Chat": ["Ask for drill-down", "Generate follow-up summary", "Open related report"],
        "BI / Reports": ["Build KPI pack", "Create dashboard blueprint", "Suggest filters"],
        "Document AI": ["Show risks", "Draft communication", "Create next-step task"],
        "Automate Work": ["Create follow-up task", "Draft internal note", "Prepare approval summary"],
        "Voice": ["Confirm action", "Open route", "Try another command"],
    }
    return mapping.get(mode, ["Ask another question"])

def build_result(prompt, mode="AI Chat", context=None):
    context = context or {}
    summary = f"Mode: {mode}. Prompt received: {prompt}"
    if context.get("exists"):
        summary += f" | Context loaded for {context.get('doctype')} {context.get('name')}."
    elif context.get("doctype"):
        summary += f" | Context record not found for {context.get('doctype')} {context.get('name')}."
    return {
        "summary": summary,
        "next_steps": _followups(mode),
        "suggested_prompts": [
            "Summarize key risks",
            "Show next actions",
            "Generate management update",
        ],
    }

def build_doc_summary(doctype, docname, context):
    fields = list((context or {}).get("fields", {}).keys())[:8]
    return {
        "title": f"{doctype} {docname}",
        "summary": f"Document AI summary prepared for {doctype} {docname}.",
        "highlights": [
            "Current record context loaded",
            "Ready for risk, gap, and next-action prompts",
            "Use follow-up actions for communication or task drafting",
        ],
        "field_preview": fields,
    }
