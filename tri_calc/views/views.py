from pyramid.view import view_config
from ..dependencies import strava_auth, strava_api


@view_config(route_name='home', renderer='tri_calc:templates/index.mako')
def home(request):
    return {
        'auth_url': strava_auth.get_auth_url()
    }


@view_config(route_name='auth', renderer='tri_calc:templates/index.mako')
def auth(request):
    code = request.params.get('code')
    access_token = strava_auth.get_access_token(code)
    strava_api.register_token(access_token)
    athlete = strava_api.get_athlete()
    request.savers.athlete.upsert_athlete(
        athlete.id,
        "{0} {1}".format(athlete.firstname, athlete.lastname),
        athlete.email,
        athlete.country
    )
    return {
        'auth_url': strava_auth.get_auth_url()
    }
