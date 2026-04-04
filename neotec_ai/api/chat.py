import frappe
from neotec_ai.services.ai_orchestrator import build_result
from neotec_ai.services.context_loader import load_doc_context

@frappe.whitelist()
def ask(prompt, mode="AI Chat", doctype=None, docname=None):
    context = load_doc_context(doctype, docname) if doctype and docname else {}
    result = build_result(prompt=prompt, mode=mode, context=context)
    if frappe.db.exists("DocType", "Neotec AI Conversation"):
        doc = frappe.get_doc({
            "doctype": "Neotec AI Conversation",
            "prompt_text": prompt,
            "mode": mode,
            "context_doctype": doctype,
            "context_name": docname,
            "response_text": result.get("summary", "")
        })
        doc.flags.ignore_permissions = True
        doc.insert(ignore_permissions=True)
    return result
