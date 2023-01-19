from django.contrib.auth.models import User
from rest_framework import status
import pytest
import json
import uuid

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/collection/',collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollection:

    def test_if_user_is_anonymous_return_401(self,api_client,create_collection):
        context={
                    "title": "My Favorite Romantics Movies",
                    "description": "A collection of my avorite romantic movies",
                    "movies": [
                        {
                            "title":"The Notebook",
                            "description": "A romantic drama film directed by Nick Cassavetes",
                            "genres": "romance,drama,comedy",
                            "uuid":"586455dc-8c6e-494e-b408-d6c922249137"
                        }
                    
                    ]
                }
        
        response=create_collection(context)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_invalid_return_400(self,api_client,create_collection):

        api_client.force_authenticate(user=User())
        context={
                    "title": " ",
                    "description": " ",
                    "movies": [
                        {
                            "title":"  ",
                            "description": " ",
                            "genres": " ",
                            "uuid":" "
                        }
                    
                    ]
                }

        response=create_collection(context)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None #making sure the error message is not none
    
    """""
    def test_if_data_is_valid_or_400(self,api_client,create_collection):
        api_client.force_authenticate(user=User())
        context={"title": "My Favorite Action Movies",
                "description": "A collection of my favorite action movies",
                "movies":[
                            {"title":"The Matrix",
                            "description": "A science fiction action film directed by the Wachowskis",
                            "genres": "science fiction,action",
                            "uuid":"1234-5678-abcd-efgh"
                            }
                    ]
                            
                }

        response=create_collection(context)
        print(response.data)
        assert response.status_code ==status.HTTP_201_CREATED
    """