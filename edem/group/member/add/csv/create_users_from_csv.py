# -*- coding: utf-8 *-*
from gs.group.member.invite.csv.create_users_from_csv import \
    CreateUsersInviteForm
from gs.group.member.invite.csv.site import CreateUsersAddSiteForm
from utils import fn_to_nickname
import logging
log = logging.getLogger('EDemCreateUsersForm')


class EDemCreateUsersForm(CreateUsersInviteForm):

    def __init__(self, context, request):
        super(EDemCreateUsersForm, self).__init__(context, request)

    def create_user(self, fields):
        userInfo = CreateUsersInviteForm.create_user(self, fields)
        if userInfo.nickname == userInfo.id:
            m = 'Adding nickname to %s (%s)' % (userInfo.name, userInfo.id)
            log.info(m)
            nickname = fn_to_nickname(self.context, userInfo.name)
            userInfo.user.add_nickname(nickname)
        return userInfo


class EDemUsersAddForm(EDemCreateUsersForm):
    invite = False

    def __init__(self, context, request):
        super(EDemUsersAddForm, self).__init__(context, request)


class EDemUsersAddSiteForm(CreateUsersAddSiteForm):
    invite = False

    def __init__(self, context, request):
        super(EDemUsersAddSiteForm, self).__init__(context, request)

    def create_user(self, fields):
        userInfo = CreateUsersInviteForm.create_user(self, fields)
        if userInfo.nickname == userInfo.id:
            m = 'Adding nickname to %s (%s)' % (userInfo.name, userInfo.id)
            log.info(m)
            nickname = fn_to_nickname(self.context, userInfo.name)
            userInfo.user.add_nickname(nickname)
        return userInfo
