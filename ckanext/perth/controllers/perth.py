# encoding: utf-8

import logging

import ckan.logic as logic
import ckan.lib.base as base

from ckan.common import _, c

log = logging.getLogger(__name__)

abort = base.abort

check_access = logic.check_access
NotAuthorized = logic.NotAuthorized

from ckan.controllers.user import UserController

class PerthController(UserController):


    def index(self):
        '''We are overwriting the default index action in
        order to make the users list available only
        for system administrators
        '''

        context = {'return_query': True, 'user': c.user,
                   'auth_user_obj': c.userobj}

        data_dict = {'q': c.q,
                     'order_by': c.order_by}

        try:
            check_access('sysadmin', context, data_dict)
        except NotAuthorized:
            abort(403, _('Not authorized to see this page'))

        return super(PerthController, self).index()
