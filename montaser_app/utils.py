import frappe

def get_user_home_page(user):
    """
    Custom function to redirect users to custom homepage after login.
    This function will be called for all users after they log in.
    
    Args:
        user: The user object or user name
        
    Returns:
        str: The route to redirect to (custom_homepage)
    """
    # Redirect all users to the custom homepage
    return "custom_homepage" 
