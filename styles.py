import gradio as gr

# Example Questions for Digital Twin
EXAMPLE_QUESTIONS = [
    "Can you walk me through your career journey?",
    "What technologies and tools do you specialize in?",
    "What are your most impactful recent projects?",
    "Ideal meal plan for a day out?",
    "Best desserts according to you in town?"
]

# Custom Baby Pink & Soft Charcoal Palette
custom_theme = gr.themes.Soft(
    primary_hue=gr.themes.Color(
        c50="#FFF8F9",
        c100="#FFEBF0",
        c200="#FCD2DC",
        c300="#F7AABF",
        c400="#F282A1",
        c500="#E85D82",  # Primary Pink Accent
        c600="#C94266",
        c700="#A32E4C",
        c800="#7D1E36",
        c900="#541122",
        c950="#360813",
        name="baby_pink",
    ),
    neutral_hue=gr.themes.Color(
        c50="#FAFAFA",
        c100="#F5F3F4",
        c200="#E8E5E6",
        c300="#D4D0D2",
        c400="#A39D9E",
        c500="#736D6F",
        c600="#504B4D",  # Charcoal
        c700="#3B3738",
        c800="#2C292A",
        c900="#201E1F",
        c950="#121111",
        name="soft_charcoal",
    ),
).set(
    body_background_fill="#FFF2F5",
    body_background_fill_dark="#FFF2F5",
    body_text_color="#3B3738",
    body_text_color_subdued="#736D6F",
    block_background_fill="#FFFFFF",
    block_border_color="#FCD2DC",
    block_border_width="1px",
    block_radius="18px",
    button_primary_background_fill="#E85D82",
    button_primary_background_fill_hover="#C94266",
    button_primary_text_color="#FFFFFF",
    input_background_fill="#FFFFFF",
    input_border_color="#F7AABF",
    shadow_drop="0 4px 12px rgba(232, 93, 130, 0.08)",
)

CUSTOM_CSS = """
/* Background setup */
body, .gradio-container {
    background-color: #FFF2F5 !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* Chatbot frame formatting */
.chatbot {
    border: 1px solid #FCD2DC !important;
    border-radius: 18px !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 4px 16px rgba(232, 93, 130, 0.06) !important;
}

/* Messages */
.message.user {
    background-color: #FFEBF0 !important;
    color: #3B3738 !important;
    border-radius: 16px 16px 4px 16px !important;
    border: 1px solid #FCD2DC !important;
}

.message.bot {
    background-color: #FFFFFF !important;
    color: #3B3738 !important;
    border-radius: 16px 16px 16px 4px !important;
    border: 1px solid #F7AABF !important;
}

/* Inputs & Buttons */
textarea {
    border-radius: 12px !important;
    border: 1px solid #F7AABF !important;
    color: #3B3738 !important;
}

textarea:focus {
    border-color: #E85D82 !important;
    box-shadow: 0 0 0 2px rgba(232, 93, 130, 0.2) !important;
}

/* Example Prompt Buttons */
.examples-container button, .gr-samples button, div[data-testid="Examples"] button {
    background-color: #FFFFFF !important;
    border: 1px solid #F7AABF !important;
    color: #3B3738 !important;
    border-radius: 12px !important;
    font-size: 0.9em !important;
    transition: all 0.2s ease-in-out !important;
}

.examples-container button:hover, .gr-samples button:hover, div[data-testid="Examples"] button:hover {
    background-color: #FFEBF0 !important;
    border-color: #E85D82 !important;
    color: #C94266 !important;
    transform: translateY(-1px);
}

footer {
    color: #736D6F !important;
}

@media (prefers-color-scheme: dark) {
    body, .gradio-container, .chatbot, .message {
        background-color: #FFF2F5 !important;
        color: #3B3738 !important;
    }
}
"""