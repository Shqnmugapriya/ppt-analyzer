def analyze_layout(slide):
    """
    Analyze slide layout: bullet points and word count.
    """
    layout_suggestions = []
    total_words = 0
    bullet_count = 0

    for text in slide['texts']:
        total_words += len(text.split())
        bullets = [line for line in text.split('\n') if line.startswith('-') or line.startswith('•')]
        bullet_count += len(bullets)

    if total_words > 100:
        layout_suggestions.append("Slide has too many words: Consider simplifying.")
    if bullet_count > 7:
        layout_suggestions.append("Slide has too many bullet points: Reduce to 5-7.")

    return layout_suggestions