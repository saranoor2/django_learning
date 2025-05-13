python3 -m venv env
source env/bin/activate

django-admin startproject advertisement .

python manage.py runserver

python manage.py startapp api 

### Types of views:

## class based view

class AdAPI(APIView):
    def get(self, request):
    def post(self,request):
    def put(self, request, pk):
    def delete(self, request, pk):
    def get_random(self, request):

### post request body for ad:
{"title":"Selling Afghan carpets","type": "Household"}