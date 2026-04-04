frappe.ui.form.on('*', {
    refresh(frm) {
        if (frm.is_new()) return;
        if (frm.__neotec_ai_button_added) return;
        frm.__neotec_ai_button_added = true;
        frm.add_custom_button('✨ Ask AI', () => {
            frappe.call({
                method: 'neotec_ai.api.doc_ai.summarize',
                args: { doctype: frm.doctype, docname: frm.docname },
                callback(r) {
                    const msg = r.message || {};
                    const html = `<div>
                        <h4>${frappe.utils.escape_html(msg.title || 'Document AI')}</h4>
                        <p>${frappe.utils.escape_html(msg.summary || '')}</p>
                        <p><b>Highlights</b></p>
                        <ul>${(msg.highlights || []).map(x => `<li>${frappe.utils.escape_html(x)}</li>`).join('')}</ul>
                    </div>`;
                    frappe.msgprint({title: __('Neotec AI'), message: html, wide: true});
                }
            });
        }, __('Neotec AI'));
    }
});
