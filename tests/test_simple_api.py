import requests


user_id = None

def test_create_user(base_url):
    
    user = dict(name="John1",
                job="new job")
    
    res = requests.post(base_url + "/api/users",
                        data=user)
    
    assert res.status_code == 201

    user_id = res.json().get("id")
    

def test_update_user(base_url):
    
    user_to_update = dict(name="John007",
                job="Big Salary")
    
    res = requests.put(f"{base_url}/api/users/{user_id}",
                       data=user_to_update)
    
    assert res.status_code == 200
    assert res.json().get('name') == user_to_update["name"]


def test_delete_user(base_url):
    
        
    res = requests.delete(f"{base_url}/api/users/{user_id}")
    
    assert res.status_code == 204

    
    
    
