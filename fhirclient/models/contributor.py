#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11157 (http://hl7.org/fhir/StructureDefinition/Contributor) on 2017-02-14.
#  2017, SMART Health IT.


from . import element

class Contributor(element.Element):
    """ Contributor information.
    
    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """
    
    resource_type = "Contributor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details of the contributor.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name of the contributor.
        Type `str`. """
        
        self.type = None
        """ author | editor | reviewer | endorser.
        Type `str`. """
        
        super(Contributor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contributor, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import contactdetail
