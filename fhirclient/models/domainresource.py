#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11157 (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2017-02-14.
#  2017, SMART Health IT.


from . import resource

class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.
    
    A resource that includes narrative, extensions, and contained resources.
    """
    
    resource_type = "DomainResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contained = None
        """ Contained, inline Resources.
        List of `Resource` items (represented as `dict` in JSON). """
        
        self.extension = None
        """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.modifierExtension = None
        """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(DomainResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DomainResource, self).elementProperties()
        js.extend([
            ("contained", "contained", resource.Resource, True, None, False),
            ("extension", "extension", extension.Extension, True, None, False),
            ("modifierExtension", "modifierExtension", extension.Extension, True, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
        ])
        return js


from . import extension
from . import narrative
