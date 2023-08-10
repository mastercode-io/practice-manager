from AnvilFusion.components.FormBase import FormBase, POPUP_WIDTH_COL2
from AnvilFusion.components.FormInputs import *


class CaseWorkflowItemForm(FormBase):
    def __init__(self, **kwargs):
        print('CaseWorkflowItemForm')
        
        practice_area = LookupInput(name='practice_area', label='Practice Area', model='PracticeArea')
        type = RadioButtonInput(name='type', label='Type', options=['Task', 'Event'], value='Task')
        activity = LookupInput(name='activity', label='Activity', model='Activity')
        related_task = LookupInput(name='related_task', label='Related Task', model='CaseWorkflowItem', text_field='item_name')
        due_date_base = RadioButtonInput(name='due_date_base', label='Due Date Based On', options=['Start Date', 'End Date'])
        before_after = RadioButtonInput(name='before_after', label='When', options=['Before', 'After'], save=False)
        duration = NumberInput(name='duration', label='Duration')
        assigned_to = LookupInput(name='assigned_to', label='Assigned To', model='Staff', select='multi',
                                  text_field='full_name')
        priority = RadioButtonInput(name='priority', label='Priority', options=['Normal', 'High'], value='Normal')
        notes = MultiLineInput(name='notes', label='Notes', rows=5)
        documents = FileUploadInput(name='documents', label='Documents', save=False)
        
        sections = [
            {
                'name': 'task_details',
                'cols': [
                    [practice_area, type, activity, assigned_to, notes, documents],
                    [due_date_base, related_task, before_after, duration, priority],
                ]
            }
        ]
        
        super().__init__(model='CaseWorkflowItem', sections=sections, width=POPUP_WIDTH_COL2, **kwargs)
