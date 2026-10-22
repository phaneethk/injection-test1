import re
SUSPICIOUS_OUTPUT_PATTERNS = [
    r"(www\.|http[s]?://)[^\s]+",
    r"(discount|promo|voucher).{0,10}code",
    r"claim your.{0,20}(bonus|reward|prize|winnings|credit)",
    r"disable.{0,20}(ssl|certificate|signature|verification)",
    r"append (the following|this|a) confirmation",
    r"enter your (card|bank|password) (details|number|credentials)",
]

def filter_output(answer):
    for pattern in SUSPICIOUS_OUTPUT_PATTERNS:
        if re.search(pattern, answer, re.IGNORECASE):
            return "[RESPONSE BLOCKED: Output contains potentially unsafe or off-topic content.]", True
    return answer, False