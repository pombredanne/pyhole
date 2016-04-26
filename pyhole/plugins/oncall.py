#   Copyright 2016 Josh Kearney
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Pyhole On-Call Plugin"""

from pyhole.core import plugin
from pyhole.core import utils


class OnCall(plugin.Plugin):
    """Provide help with on-call duties."""

    @plugin.hook_add_command("note")
    def note(self, message, params=None, **kwargs):
        """Manage notes during an outage (ex: .note <message>)."""
        if params:
            pass
        else:
            message.dispatch(self.note.__doc__)
            return

    @plugin.hook_add_command("status")
    def status(self, message, params=None, **kwargs):
        """Manage status of a service (ex: .status <service> [<status>])."""
        if params:
            pass
        else:
            message.dispatch(self.status.__doc__)
            return
