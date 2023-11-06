
def generate_description(child, response, description):
    description += f"{child.first_name} {response.response_text} "
    return description