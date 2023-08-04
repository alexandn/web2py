# -*- coding: utf-8 -*-

db.define_table('emergencymessage',
                Field('em_code','integer'),
                Field('em_validity','datetime'),
                Field('em_action','integer'))
