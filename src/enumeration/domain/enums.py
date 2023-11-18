from backbone.service_layer.general_types import BaseEnumeration


class TemplateCategory(BaseEnumeration):
    PERSONNEL_INFO = 1201
    LEAVE_REQUEST = 1202

    @classmethod
    def parent(cls):
        return 1200
