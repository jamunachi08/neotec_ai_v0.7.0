from neotec_ai import __version__ as app_version

app_name = "neotec_ai"
app_title = "Neotec AI"
app_publisher = "Neotec"
app_description = "Cross-module AI automation platform for ERPNext"
app_email = "support@neotec.ai"
app_license = "MIT"

app_include_js = ["neotec_ai.bundle.js"]
app_include_css = ["neotec_ai.bundle.css"]

doctype_js = {
    "*": "public/js/neotec_ai_doc_assist.js"
}

add_to_apps_screen = [
    {
        "name": "neotec_ai",
        "logo": "/assets/neotec_ai/images/neotec-ai.svg",
        "title": "Neotec AI",
        "route": "/app/neotec-ai-hub",
        "has_permission": "neotec_ai.api.permissions.has_app_permission",
    }
]

after_install = "neotec_ai.install.after_install"
after_migrate = "neotec_ai.install.after_migrate"

scheduler_events = {
    "hourly": [
        "neotec_ai.services.crm_social_service.run_due_jobs"
    ]
}
