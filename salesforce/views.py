from django.shortcuts import render

def trailhead_profile(request):
    # Base URL for the badges
    base_url = 'https://developer.salesforce.com/resource/images/trailhead/badges/modules/'

    # List of badges with names and filenames
    badges = [
        {'name': 'Apex Basics and Database', 'filename': 'trailhead_module_apex_basics_and_database.png'},
        {'name': 'Apex Integration', 'filename': 'trailhead_module_apex_integration.png'},
        {'name': 'Apex Testing', 'filename': 'trailhead_module_apex_testing.png'},
        {'name': 'Apex Triggers', 'filename': 'trailhead_module_apex_triggers.png'},
        {'name': 'Asynchronous Apex', 'filename': 'trailhead_module_asynchronous_apex.png'},
        {'name': 'Data Modeling', 'filename': 'trailhead_module_data_modeling.png'},
        {'name': 'Developer Console', 'filename': 'trailhead_module_developer_console.png'},
        {'name': 'Dotnet Apex Basics', 'filename': 'trailhead_module_dotnet_apex_basics.png'},
        {'name': 'Dotnet Database Basics', 'filename': 'trailhead_module_dotnet_database_basics.png'},
        {'name': 'Formulas and Validations', 'filename': 'trailhead_module_formulas_and_validations.png'},
        {'name': 'Lightning Component Core Concepts', 'filename': 'trailhead_module_lightning_component_core_concepts.png'},
        {'name': 'Lightning Data Management', 'filename': 'trailhead_module_lightning_data_management.png'},
        {'name': 'Lightning Experience Development', 'filename': 'trailhead_module_lightning_experience_development.png'},
        {'name': 'Lightning Process Automation', 'filename': 'trailhead_module_lightning_process_automation.png'},
        {'name': 'Platform Development Basics', 'filename': 'trailhead_module_platform_development_basics.png'},
        {'name': 'Platform Events Basics', 'filename': 'trailhead_module_platform_events_basics.png'},
        {'name': 'Search Solution Basics', 'filename': 'trailhead_module_search_solution_basics.png'},
        {'name': 'Trailhead Playground Management', 'filename': 'trailhead_module_trailhead_playground_management.png'},
        {'name': 'Visualforce Basics', 'filename': 'trailhead_module_visualforce_basics.png'},
    ]

    # Generate full badge URLs by appending filenames to the base URL
    for badge in badges:
        badge['img_url'] = base_url + badge['filename']

    # Pass the badges to the template
    return render(request, 'salesforce/trailhead_profile.html', {'badges': badges})

