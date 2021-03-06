#!/usr/bin/env python3

"""
Copyright (C) 2021-2022 Samir OUCHENE, samirmath01@gmail.com
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.
"""

import random
import inkex


class CRandSel(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

        self.arg_parser.add_argument(
            "-p",
            "--property",
            action="store",
            type=str,
            dest="property",
            default="width",
            help="Property to modify",
        )

        self.arg_parser.add_argument(
            "-n",
            "--value",
            action="store",
            type=float,
            dest="value",
            default="10",
            help="property value",
        )
        self.arg_parser.add_argument(
            "-k",
            "--howMany",
            action="store",
            type=int,
            dest="howMany",
            default=1,
            help="How many object to select randomly",
        )

    def effect(self):

        objects = self.svg.selection
        _property = self.options.property
        _value = float(self.options.value)
        _howMany = int(self.options.howMany)

        total_sel_num = len(objects)
        rand_sel = random.sample(range(total_sel_num), _howMany)

        rand_objs = [objects[i] for i in rand_sel]

        for obj in rand_objs:
            # self.msg(f"{list(obj.bounding_box())}")
            x_x = list(obj.bounding_box().x)
            y_y = list(obj.bounding_box().y)
            x, y = float(x_x[0]), float(y_y[0])

            curr_width = obj.bounding_box().width
            curr_height = obj.bounding_box().height

            if _property.lower() == "width":
                orig_val = curr_width
                scalex = _value / orig_val
                scaley = 1

                targetx = (1 - scalex) * x
                targety = y

                obj.transform.add_scale(scalex, scaley)
                obj.transform.add_translate(targetx / scalex, 0)

            elif _property.lower() == "height":
                orig_val = curr_height
                scalex = 1
                scaley = _value / orig_val
                targetx = x
                targety = (1 - scaley) * y

                obj.transform.add_scale(scalex, scaley)
                obj.transform.add_translate(0, targety / scaley)

            else:
                self.errormsg(f"property '{_property}' Not implemented yet.")

        self.svg.update()


randSel = CRandSel()
randSel.run()
