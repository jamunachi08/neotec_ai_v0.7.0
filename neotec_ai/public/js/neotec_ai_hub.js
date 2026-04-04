frappe.provide('neotec_ai');

neotec_ai.renderHub = function(wrapper) {
    const $wrapper = $(wrapper);
    $wrapper.html('<div class="neotec-ai-loading">Loading Neotec AI...</div>');
    frappe.call({
        method: 'neotec_ai.api.workspace.bootstrap',
        callback(r) {
            const data = r.message || {};
            const modes = (data.modes || []).map(m => `
                <div class="neotec-card">
                    <div class="neotec-card-title">${frappe.utils.escape_html(m.name)}</div>
                    <div class="neotec-card-text">${frappe.utils.escape_html(m.description)}</div>
                </div>`).join('');
            const quick = (data.quick_cards || []).map(c => `
                <button class="btn btn-default btn-sm neotec-quick" data-prompt="${frappe.utils.escape_html(c.prompt)}">${frappe.utils.escape_html(c.title)}</button>`).join('');
            const voice = (data.sample_voice || []).map(v => `<li>${frappe.utils.escape_html(v)}</li>`).join('');
            $wrapper.html(`
                <div class="neotec-shell">
                    <div class="neotec-hero">
                        <h2>Neotec AI Hub</h2>
                        <p>Cross-module AI workspace for prompts, reports, document summaries, automations, and voice actions.</p>
                    </div>
                    <div class="neotec-grid">${modes}</div>
                    <div class="neotec-panel">
                        <h4>Quick Start</h4>
                        <div class="neotec-quick-wrap">${quick}</div>
                        <textarea class="form-control neotec-prompt" rows="5" placeholder="Ask Neotec AI about sales, finance, HR, projects, stock, support, or this current business process."></textarea>
                        <div class="mt-2">
                            <button class="btn btn-primary neotec-run">Run Prompt</button>
                        </div>
                    </div>
                    <div class="neotec-panel">
                        <h4>Sample Voice Commands</h4>
                        <ul>${voice}</ul>
                    </div>
                    <div class="neotec-result"></div>
                </div>
            `);
            $wrapper.find('.neotec-quick').on('click', function() {
                $wrapper.find('.neotec-prompt').val($(this).data('prompt'));
            });
            $wrapper.find('.neotec-run').on('click', function() {
                const prompt = $wrapper.find('.neotec-prompt').val();
                frappe.call({
                    method: 'neotec_ai.api.chat.ask',
                    args: { prompt: prompt, mode: 'AI Chat' },
                    callback(res) {
                        const out = res.message || {};
                        $wrapper.find('.neotec-result').html(`
                            <div class="neotec-panel">
                                <h4>Result</h4>
                                <p>${frappe.utils.escape_html(out.summary || '')}</p>
                                <p><b>Next steps</b></p>
                                <ul>${(out.next_steps || []).map(x => `<li>${frappe.utils.escape_html(x)}</li>`).join('')}</ul>
                            </div>
                        `);
                    }
                });
            });
        }
    });
};
