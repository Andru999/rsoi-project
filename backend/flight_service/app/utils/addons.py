from pydantic import ValidationError


def remove_extra_symbols(text: str, symbols: str) -> str:
    translate_table = str.maketrans(symbols, "^" * len(symbols))
    return text.translate(translate_table).replace("^", "")


def get_pydantic_validation_error_text(err: ValidationError) -> str:
    errors = err.errors()
    return remove_extra_symbols(
        text="; ".join(f"{e['loc']}: {e['msg']}" for e in errors),
        symbols="()[],",
    )
