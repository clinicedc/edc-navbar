# edc_navbar

Simple Navbar class for edc

Include `edc_navbar` in `INSTALLED_APPS`.

Navbars are declared in your apps `navbars.py` and will be autodiscovered by `edc_navbar` and stored in the  site global `site_navbars`.

An example `navbars.py`:

    from edc_navbar import NavbarItem, site_navbars, Navbar
    
    url_namespace = 'edc_pharmacy_dashboard'
    
    # instantiate a Navbar
    pharmacy_dashboard = Navbar(name='pharmacy_dashboard')
    
    # add items to the navbar
    pharmacy_dashboard.append_item(
        NavbarItem(
            name='prescribe',
            title='Prescribe',
            label='prescribe',
            url_name=f'{url_namespace}:prescribe_listboard_url'))
    
    pharmacy_dashboard.append_item(
        NavbarItem(
            name='dispense',
            title='Dispense',
            label='dispense',
            icon='medicines.png',
            url_name=f'{url_namespace}:dispense_listboard_url'))
    
    # register the navbar to the site
    site_navbars.register(pharmacy_dashboard)
 
 Add `NavbarViewMixin` to your view and indicate the navbar by name. The navbar will be rendered to string
 and added to the context.
 
    ...
    from edc_navbar import NavbarViewMixin

    class HomeView(EdcBaseViewMixin, NavbarViewMixin, AppConfigViewMixin, TemplateView):

        navbar_name = 'pharmacy_dashboard'
        navbar_selected_item = 'prescribe'

