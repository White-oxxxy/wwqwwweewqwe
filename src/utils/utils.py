# ---- конвертация няяя (костыль фу) ----


def to_dict(value: list) -> dict:
    def serialize_text(text):
        return {"id": text.id, "value": text.value, "uploader_id": text.uploader_id}

    return {int(index): serialize_text(text) for index, text in enumerate(value)}
