from AnvilFusion.components.FormBase import FormBase, POPUP_WIDTH_COL2
from AnvilFusion.components.FormInputs import *


class CaseWorkflowForm(FormBase):
    def __init__(self, **kwargs):
        print('CaseWorkflowForm')
        
        # build the form fields based on the model in models.py
        # practice_area = Relationship('PracticeArea')
        # type = Attribute(field_type=types.FieldTypes.ENUM_SINGLE)
        # activity = Relationship('Activity')
        # related_task = Relationship('CaseWorkflowTask')
        # due_date_base = Attribute(field_type=types.FieldTypes.ENUM_SINGLE)
        # duration = Attribute(field_type=types.FieldTypes.NUMBER)
        # assigned_to = Relationship('Staff', with_many=True)
        # priority = Attribute(field_type=types.FieldTypes.ENUM_SINGLE)
        practice_area = LookupInput(label='Practice Area', name='practice_area', required=True)
        
        

        super().__init__(model='CaseWorkflow', fields=fields, width=POPUP_WIDTH_COL2, **kwargs)
