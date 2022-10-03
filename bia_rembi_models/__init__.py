from pydantic import BaseModel


class MetadataGroup(BaseModel):
    _atom = False


class FreeText(str):
    _help_description = "Free text"
    _atom = True