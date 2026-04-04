import frappe
from neotec_ai.services.voice_router import resolve_voice_intent

@frappe.whitelist()
def process(text):
    return resolve_voice_intent(text)
