

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy_json import mutable_json_type
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr


from tendril.utils.db import DeclBase
from tendril.utils.db import BaseMixin
from tendril.utils.db import TimestampMixin
from tendril.authn.db.mixins import UserMixin

from tendril.utils import log
logger = log.get_logger(__name__, log.DEFAULT)


class ArtefactModel(DeclBase, BaseMixin, TimestampMixin, UserMixin):
    _type_name = "artefact"
    type = Column(String(50), nullable=False, default=_type_name)

    @declared_attr
    def logs(cls):
        return relationship("ArtefactLogEntryModel", back_populates="artefact")

    __mapper_args__ = {
        "polymorphic_identity": _type_name,
        "polymorphic_on": type
    }


class ArtefactLogEntryModel(DeclBase, BaseMixin, TimestampMixin, UserMixin):
    action = Column(String(50), nullable=False)
    reference = Column(mutable_json_type(dbtype=JSONB))
    artefact_id = Column(Integer(),
                         ForeignKey('Artefact.id'), nullable=False)
    artefact = relationship("ArtefactModel", back_populates="logs")
