import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-timesheet",
    description="Meta package for oca-timesheet Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-crm_phonecall_timesheet',
        'odoo12-addon-crm_timesheet',
        'odoo12-addon-hr_employee_product',
        'odoo12-addon-hr_timesheet_activity_begin_end',
        'odoo12-addon-hr_timesheet_analysis',
        'odoo12-addon-hr_timesheet_employee_cost_contract',
        'odoo12-addon-hr_timesheet_employee_cost_currency',
        'odoo12-addon-hr_timesheet_employee_required',
        'odoo12-addon-hr_timesheet_nonpayable',
        'odoo12-addon-hr_timesheet_report',
        'odoo12-addon-hr_timesheet_role',
        'odoo12-addon-hr_timesheet_sheet',
        'odoo12-addon-hr_timesheet_sheet_activity',
        'odoo12-addon-hr_timesheet_sheet_attendance',
        'odoo12-addon-hr_timesheet_sheet_autodraft',
        'odoo12-addon-hr_timesheet_sheet_autodraft_project',
        'odoo12-addon-hr_timesheet_sheet_no_create',
        'odoo12-addon-hr_timesheet_sheet_period',
        'odoo12-addon-hr_timesheet_sheet_policy_department_manager',
        'odoo12-addon-hr_timesheet_sheet_policy_direct_manager',
        'odoo12-addon-hr_timesheet_sheet_policy_project_manager',
        'odoo12-addon-hr_timesheet_sheet_role',
        'odoo12-addon-hr_timesheet_task_domain',
        'odoo12-addon-hr_timesheet_task_required',
        'odoo12-addon-hr_timesheet_task_stage',
        'odoo12-addon-hr_timesheet_time_type',
        'odoo12-addon-hr_utilization_analysis',
        'odoo12-addon-hr_utilization_report',
        'odoo12-addon-project_task_stage_allow_timesheet',
        'odoo12-addon-project_timesheet_holidays_integrity',
        'odoo12-addon-sale_timesheet_existing_project',
        'odoo12-addon-sale_timesheet_hook',
        'odoo12-addon-sale_timesheet_limit_date',
        'odoo12-addon-sale_timesheet_line_exclude',
        'odoo12-addon-sale_timesheet_order_line_sync',
        'odoo12-addon-sale_timesheet_rounded',
        'odoo12-addon-sale_timesheet_task_exclude',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
