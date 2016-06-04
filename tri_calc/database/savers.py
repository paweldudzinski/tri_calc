import transaction
from ..db import DBSession
from ..models.athlete import Athlete


class BaseSaver:

    def __init__(self, model, session):
        self.model = model
        self.session = session


class AthleteSaver(BaseSaver):

    def upsert_athlete(self, strava_id, name, email, country):

        existing_athlete = self.session.query(
            Athlete).filter(Athlete.id == strava_id).first()
        if not existing_athlete:
            o = self.model(
                id=strava_id,
                name=name,
                email=email,
                country=country
            )
            self._save_athlete(o)
        else:
            existing_athlete.name = name
            existing_athlete.email = email
            existing_athlete.country = country
            transaction.commit()

    def _save_athlete(self, o):
        with transaction.manager:
            self.session.add(o)


class Savers:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def request_property(self, request):
        return self

    @classmethod
    def create(cls):
        return cls(
            athlete=AthleteSaver(Athlete, DBSession)
        )
