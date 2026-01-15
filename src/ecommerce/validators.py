from typing import Optional
from django.core.exceptions import ValidationError

BLOCKER_WORDS = ['barato', 'malo']

def validate_for_blocker_words(value: Optional[str]) -> Optional[str]:
    init_string = f"{value}".lower()
    unique_words = set(init_string.split())
    blocked_words = set(BLOCKER_WORDS)
    invalid_words = (unique_words & blocked_words) # Compare Words that are both in unique_words and blocked_words
    has_error = len(invalid_words) > 0
    if has_error:
        errors: list[str] = []
        for word in invalid_words:
            msg = "{} es una palabra bloqueada.".format(word)
            errors.append(msg)
        raise ValidationError(errors) # type: ignore
    return value