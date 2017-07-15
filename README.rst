Overview
========

Perform one or more actions if someone performed a login, e.g. to the
admin interface. This is based on django-axes.
Currently implemented action is to send a notification mail to the site admins.


Dependencies
============

* `django_axes` (https://pypi.python.org/pypi/django-axes/)


Installation
============

- Install:

    pip install django-axes-login-action

- Add `axes_login_action` to `INSTALLED_APPS`


Usage
=====

On any login recognized by `django-axes`, `django-axes-login-actions` executes
the configured actions.
By default, a notification mail is sent to the configured site admins (
see Django's `ADMINS` setting). This is handled in `axes_login_actions.actions.email.notify`.

You can add or replace the default action with custom actions if you like.
To do so, set the setting `AXES_LOGIN_ACTIONS` to a list of paths to any callable
function or class.
Each configured action is called with a positional argument `instance` which is
a `axes.models.AccessAttempt` instance and the same kwargs as sent by the Django
`django.db.models.signals.post_save` signal.


Changes
=======

* 2017-07-15 - 1.2.0:
    * Support Python3

* 2017-03-26 - 1.1.0:
    * Add current datetime to the notification email
    * Add a proper Django app config
    * Ensure the signal handler is connected only once

* 2015-08-16 - 1.0.1:
    * Use importlib from Python instead from Django
      (to remove Django deprecation warning)

* 2014-05-25 - 1.0.0:
    * Initial release


License
=======

Copyright (c) 2014-2017, Enrico Tröger
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name django-wakawaka nor the names of its contributors
      may be used to endorse or promote products derived from this software without
      specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
