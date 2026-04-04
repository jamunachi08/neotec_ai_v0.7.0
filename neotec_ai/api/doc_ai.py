import frappe
from neotec_ai.services.context_loader import load_doc_context
from neotec_ai.services.ai_orchestrator import build_doc_summary

@frappe.whitelist()
def summarize(doctype, docname):
    context = load_doc_context(doctype, docname)
    return build_doc_summary(doctype, docname, context)
