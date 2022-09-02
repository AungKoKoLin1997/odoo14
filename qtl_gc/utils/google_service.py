from odoo.addons.google_account.models.google_service import TIMEOUT
from odoo.addons.google_calendar.utils.google_calendar import GoogleCalendarService, requires_auth_token
from odoo.addons.google_calendar.utils.google_event import GoogleEvent
import logging

@requires_auth_token
def get_events(self, sync_token=None, token=None, timeout=TIMEOUT):
    # add custom logic here
    #
    #
    #
    logging.info("Call get event function_________________")
    url = "/calendar/v3/calendars/primary/events"
    headers = {'Content-type': 'application/json'}
    params = {'access_token': token}
    if sync_token:
        params['syncToken'] = sync_token
    try:
        status, data, time = self.google_service._do_request(url, params, headers, method='GET', timeout=timeout)
    except requests.HTTPError as e:
        if e.response.status_code == 410 and 'fullSyncRequired' in str(e.response.content):
            raise InvalidSyncToken("Invalid sync token. Full sync required")
        raise e

    events = data.get('items', [])
    next_page_token = data.get('nextPageToken')
    while next_page_token:
        params = {'access_token': token, 'pageToken': next_page_token}
        status, data, time = self.google_service._do_request(url, params, headers, method='GET', timeout=timeout)
        next_page_token = data.get('nextPageToken')
        events += data.get('items', [])

    next_sync_token = data.get('nextSyncToken')
    default_reminders = data.get('defaultReminders')

    return GoogleEvent(events), next_sync_token, default_reminders

GoogleCalendarService.get_events = get_events