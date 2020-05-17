msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" # .format(name="Renish", website='renishcharaniya.tech')

def format_msg(my_name="Renish", my_website="renishcharaniya.tech"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg