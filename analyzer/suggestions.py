def generate_suggestions(slide_data, text_suggestions, layout_suggestions):
    """
    Combine text and layout suggestions.
    """
    all_suggestions = []

    if text_suggestions:
        all_suggestions.append("Text Suggestions:")
        all_suggestions.extend(text_suggestions)

    if layout_suggestions:
        all_suggestions.append("Layout Suggestions:")
        all_suggestions.extend(layout_suggestions)

    return all_suggestions