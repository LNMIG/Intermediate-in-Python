DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    all_python_devs1 = [worker["name"] for worker in DATA if worker["language"] == "python"] #usamos list comprehension
    
    all_python_devs2 = list(filter(lambda worker: worker["language"] == "python", DATA)) #usamos high order function FILTER
    all_python_devs2 = list(map(lambda worker: worker["name"], all_python_devs2)) #usamos high order function MAP


    all_platzi_workers1 = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"] #usamos list comprehension

    all_platzi_workers2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA)) #usamos high order function FILTER
    all_platzi_workers2 = list(map(lambda worker: worker["name"], all_platzi_workers2)) #usamos high order function MAP
    
    all_adults1 = list(filter(lambda worker: worker["age"] > 18, DATA)) #usamos high order function FILTER
    all_adults1 = list(map(lambda worker: worker["name"], all_adults1)) #usamos high order function MAP

    all_adults2 = [worker["name"] for worker in DATA if worker["age"] > 18] #usamos list comprehension

    old_people1 = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) # sumamos a un diccionario un nuevo key: value usando high order fucntion MAP

    old_people2 = [worker | {"old": worker["age"] > 70} for worker in DATA] # sumamos a un diccionario un nuevo key: value usando list comprehension


    for i in old_people2:
        print(i)

if __name__ == '__main__':
    run()