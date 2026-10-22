import re

SUSPICIOUS_PATTERNS = [
    r"for (any\s+)?(ai|automated|content).{0,40}(system|assistant|processor)",
    r"note (to|for) (ai|automated|any)",
    r"please (note|append|include|confirm)",
    r"append.{0,30}(confirmation|verification|code)",
    r"confirm.{0,30}(receipt|inclusion|indexing)",

]

def sanitise_content(page_content):

     # Removes sentences from page_content that match suspicious injection-style patterns.
    sentences = re.split(r'(?<=\.)\s+', page_content)
    clean_sentences = []
    for sentence in sentences:
        is_suspicious = False
        for pattern in SUSPICIOUS_PATTERNS:
            if re.search(pattern, sentence, re.IGNORECASE):
                is_suspicious = True
                break
        if not is_suspicious:
            clean_sentences.append(sentence)

    return ". ".join(clean_sentences)