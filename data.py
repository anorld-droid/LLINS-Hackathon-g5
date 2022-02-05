import json

service_dict_data = []
issue_dict_data = []


def service_data():
    with open("service.json", "r") as file:
        my_data = json.load(file)

        service_dict_data.append(my_data)

    print(service_dict_data)
    


def issue_data():
    with open("issue.json", "r") as file:
        my_data = json.load(file)

        issue_dict_data.append(my_data)

    print(issue_dict_data)


issue_data()

service_data()