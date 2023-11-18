from inspect import getmembers, isclass

from enumeration.domain import enums
from enumeration.domain.entities.enumeration import Enumeration


def migrate_enumerations(session_maker=None):
    with session_maker() as session:
        for p, c in getmembers(enums, isclass):
            if hasattr(c, "parent") and hasattr(c, "members"):
                members = c.members()
                parent_id = c.parent()
                session.add(enumeration_factory(parent_id, p, None))
                for member in members:
                    session.add(enumeration_factory(member.value, member.name, parent_id))
                    try:
                        session.commit()
                    except Exception as e:
                        session.rollback()


def enumeration_factory(enum_id, title, parent_id) -> Enumeration:
    enumeration = Enumeration()
    enumeration.id = enum_id
    enumeration.title = title
    enumeration.parent_id = parent_id
    return enumeration
