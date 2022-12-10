

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


from tendril.utils.db import DeclBase
from tendril.utils.db import BaseMixin
from tendril.utils.db import TimestampMixin
from tendril.authn.db.mixins import UserMixin

from tendril.utils import log
logger = log.get_logger(__name__, log.DEFAULT)


class Artefact(DeclBase, BaseMixin, TimestampMixin, UserMixin):
    _type_name = "artefact"
    type = Column(String(50), nullable=False)
    logs = relationship("ArtefactLogEntry", back_populates="artefact")

    __mapper_args__ = {
        "polymorphic_identity": _type_name,
        "polymorphic_on": type
    }


class ArtefactLogEntry(DeclBase, BaseMixin, TimestampMixin, UserMixin):
    action = Column(String(50), nullable=False)
    reference = Column(MutableDict.as_mutable(JSONB))
    artefact_id = Column(Integer(),
                         ForeignKey('Artefact.id'), nullable=False)
    artefact = relationship("Artefact", back_populates="logs")
