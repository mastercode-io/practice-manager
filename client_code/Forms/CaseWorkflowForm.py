from AnvilFusion.components.FormBase import FormBase
from AnvilFusion.components.FormInputs import *


class CaseWorkflowForm(FormBase):
    def __init__(self, **kwargs):
        print('CaseWorkflowItemForm')
        
        self.name = TextInput(name='name', label='Name')
        self.practice_area = LookupInput(name='practice_area', label='Practice Area', model='PracticeArea', 
                                         on_change=self.update_workflow_name)
        self.items = LookupInput(name='items', label='Items', model='CaseWorkflowItem', select='multi', 
                                 text_field='item_name', add_item_text='Add Item', 
                                 add_item_model='CaseWorkflowItem', add_item_form='CaseWorkflowItemForm')
        
        fields = [self.name, self.practice_area, self.items]
        
        super().__init__(model='CaseWorkflowItem', fields=fields, **kwargs)
        
        
    def update_workflow_name(self, **event_args):
        print('update_worflow_name')
        self.name.value = self.practice_area.value
