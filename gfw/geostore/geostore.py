# Global Forest Watch API
# Copyright (C) 2013 World Resource Institute
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import json

from appengine_config import runtime_config
from google.appengine.ext import ndb

class Geostore(ndb.Model):
    geojson = ndb.JsonProperty()

    kind = 'Geostore'

    """ Instance Methods """

    def to_dict(self):
        result = super(Geostore,self).to_dict()
        result['id'] = self.key.urlsafe()
        return result
