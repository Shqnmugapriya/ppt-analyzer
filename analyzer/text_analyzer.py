import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def analyze_text(text):
    """
    Analyze grammar, spelling, and sentence length of the text.
    """
    issues = tool.check(text)
    suggestions = []

    for issue in issues:
        # Changed ruleId to rule_id
        suggestions.append(f"{issue.rule_id}: {issue.message} (position {issue.offset})")

    # Suggest splitting long sentences
    if len(text.split()) > 40:
        suggestions.append("Too long: Consider splitting into shorter sentences.")

    return suggestions