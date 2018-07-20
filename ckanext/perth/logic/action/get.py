import ckan.logic as logic
from ckan.plugins import toolkit

_check_access = logic.check_access


@toolkit.side_effect_free
def user_list(context, data_dict):
    '''We are overwriting the default user_list api action in
    order to make the users list available only
    for system administrators
    '''
    _check_access('sysadmin', context, data_dict)
    return logic.action.get.user_list(context, data_dict)
