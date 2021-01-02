# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy
from .operators import exploder as exploder_ot
from .panels import exploder as exploder_pt

bl_info = {
    "name" : "Exploder",
    "author" : "DESIGN3D",
    "description" : "Automatic exploded view and animation generator",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Animation"
}

classes = [
    exploder_ot,
    exploder_pt,
]

def register():
    for cls in classes:
        cls.register()

def unregister():
    for cls in classes:
        cls.unregister()

if __name__ == "__main__":
    register()