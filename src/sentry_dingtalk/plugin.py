# coding: utf-8

import json

import requests
from sentry.plugins.bases.notify import NotificationPlugin

import sentry_dingtalk
from .forms import DingTalkOptionsForm

DingTalk_API = "https://oapi.dingtalk.com/robot/send?access_token={token}"


class DingTalkPlugin(NotificationPlugin):
    """
    Sentry plugin to send error counts to DingTalk.
    """
    author = 'ansheng'
    author_url = 'https://github.com/anshengme/sentry-dingtalk'
    version = sentry_dingtalk.VERSION
    description = 'Send error counts to DingTalk.'
    slug = 'DingTalk'
    title = 'DingTalk'
    conf_key = slug
    conf_title = title
    resource_links = [
        ('Source', 'https://github.com/anshengme/sentry-dingtalk'),
        ('Bug Tracker', 'https://github.com/anshengme/sentry-dingtalk/issues'),
        ('README', 'https://github.com/anshengme/sentry-dingtalk/blob/master/README.md'),
    ]
    project_conf_form = DingTalkOptionsForm

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('access_token', project))

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        access_token = self.get_option('access_token', group.project)

        send_url = DingTalk_API.format(token=access_token)

        metadata = event.get_event_metadata()

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "{0}".format(metadata["type"]),
                "text": "#### {title}  \n > {message} [href]({url})".format(
                    title=metadata["type"],
                    message=event.message,
                    url="{0}events/{1}/".format(group.get_absolute_url(), event.id)
                )
            }
        }

        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )
