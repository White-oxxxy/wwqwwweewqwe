import re


def to_dict(value: list) -> dict:
    def serialize_text(text):
        return {"id": text.id, "value": text.value, "uploader_id": text.uploader_id}

    return {int(index): serialize_text(text) for index, text in enumerate(value)}


def valid_tags(text: str) -> bool:
    return bool(re.fullmatch(r"(#\w+\s*)(,\s*#\w+)*", text))


def convert_tags_to_list(tags: str) -> list[str]:
    return [tag.strip() for tag in tags.split(",") if tag.strip()]


def convert_admin_ids_to_list(admin_ids: str) -> list[int]:
    return list(map(int, admin_ids.split(",")))


def join_tags(tags: list) -> str:
    return ", ".join(map(str, tags))
