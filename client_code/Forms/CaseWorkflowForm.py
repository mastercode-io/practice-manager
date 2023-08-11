from AnvilFusion.components.FormBase import FormBase
from AnvilFusion.components.FormInputs import *


class CaseWorkflowForm(FormBase):
    def __init__(self, **kwargs):
        print('CaseWorkflowItemForm')
        
        name = TextInput(name='name', label='Name')
        practice_area = LookupInput(name='practice_area', label='Practice Area', model='PracticeArea')
        items = LookupInput(name='items', label='Items', model='CaseWorkflowItem', select='multi', text_field='item_name')
        
        fields = [name, practice_area, items]
        
        super().__init__(model='CaseWorkflowItem', fields=fields, **kwargs)
