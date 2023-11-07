# def generate_description(name, gender, grades, responses):
#     description = f"{name} {responses.get(grades[0])}. {responses.get(grades[1])}. {gender} {responses.get(grades[2])}."
#     return description



# name = "Jaś"
# gender = "Chłopiec"

# grades = [2, 0, 1]

# responses = {0: "kiepsko", 1: "średnio", 2: "super"}


# print(generate_description(name, gender, grades, responses))



def generate_sentence(i, name, gender, response_text):
    if i == 1:
        sentence = f"{name} {response_text} "
    elif i == 3:
        sentence = f"{gender.capitalize()} {response_text} "
    else:
        sentence = f"{response_text.capitalize()} "

    return sentence