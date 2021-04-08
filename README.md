# Project  *My_web*



## 목적.

> 1. 기본적인 Django를 이용한 CRUD 구현과 함께
>
> 2. Rest API 를 추가로 정리





## Rest 란 ?

- 정의

  - '**Representational State Transfer**' : 요약하자면 **정보**와 **상태표현**을 같이 전달하는 것을 의미

- 구체적인 개념

  - HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)를 명시하고,

    HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD 구현

  - CRUD 랑 Matching

    - Create == POST
    - Read == GET
    - Update == PUT
    - Delete == DELETE



## REST API 란?

- API ( Application Programming Interface )

  - 데이터와 기능의 집합을 제공해, 서로 정보를 교환가능 하도록 하는 것

  ` 쉽게 말하면 API를 이용해 REST 통신!` 



---



## Django에서 REST API 

- 다른 Spring과는 다르게 `rest_framework`에서 제공하는 APIView 라는 Class 가 있어 

  상속받아서 작성할 수 있다. 장고의 큰 장점인 것 같다.

- View를 설정해주기 전에 `serializers.py` 파일을 생성해준다. 

  - `serializers.py` 는 REST 로 통신하는데 <u>data 를 `dict ( json )` 형태로 바꿔 전송</u>한다.  

`views.py`

```python
# 해당 app 에 view에 설정해준다.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView): # rest_framework에 APIView를 상속
    """
    POST /user
    """
    def post(self, request): # 해당 요청과 동일하게 함수이름을 짓는다. 
        ...
        return 

    """
    Get /user
    Get /user/{user_id}
    """
    def get(self, request):
        ...
        return
    ...
```





`serializers.py`

```python
from rest_framework import serializers   
from .models import User

class UserSerializer(serializers.ModelSerializer): # rest_framework에서 serializers 를 상속받아 구현
    class Meta:
        model = User
        fields = '__all__'
        
```



