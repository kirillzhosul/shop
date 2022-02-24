#!env/bin/python
"""
    Merchandise shop auth service.
    Provides interfaces for auth.
"""

from flask import redirect, url_for, render_template, Response
from flask_login import current_user


def render_or_profile_if_not_guest(template_name: str) -> Response:
    """
    Will render given template if user is not authorized (not guest).
    Otherwise, will redirect to profile page, as user is already authenticated.
    :param template_name: Template name to render.
    :return: Redirect or page response.
    """
    if current_user.is_authenticated:
        return redirect(url_for("profile.index"))
    return Response(render_template(template_name, user=current_user))
