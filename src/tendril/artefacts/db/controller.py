

from tendril.utils.db import with_db
from .model import Artefact

from tendril.utils import log
logger = log.get_logger(__name__, log.DEFAULT)


@with_db
def get_artefact(id, session=None):
    q = session.query(Artefact).filter_by(id=id)
    return q.one()


@with_db
def create_artefact(type, session=None):
    if not type:
        raise ValueError("type cannot be None")
    artefact = Artefact(type=type)
    session.add(artefact)
    return artefact


@with_db
def register_artefact(artefact: Artefact, session=None):
    session.add(artefact)
    return artefact
