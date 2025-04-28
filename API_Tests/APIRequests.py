import pytest
import requests
import json

auth_token = ""
base_url = "https://gorest.co.in/public"


# Get Request
@pytest.mark.run(order=1)
def get_request_test():
    headers = f"Authorization :{auth_token}"

    # response = requests.get(f"{base_url}/v2/users", headers)
    # json_data = response.json()
    # json_str = json.dumps(json_data, indent=4)
    # print(json_str)

@pytest.mark.run(order=2)
def post_request_test():
    data = {
        "id": 1,
        "name": "Aman Gupta",
        "email": "aasha_sr_dhawan@turcotte.test",
        "gender": "Male",
        "status": "Active"
    }

    response = requests.post(f"{base_url}/v2/posts", data=data)
    print(response)



get_request_test()
