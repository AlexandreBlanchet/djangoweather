from django.shortcuts import render

def home(request):
  import json
  import requests

  if request.method == "POST":
    zipcode = request.POST['zipcode']
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=25&API_KEY=7CE66E0C-EECD-42E4-8948-87877395F6BF")

    try :
      api = json.loads(api_request.content)
    except Exception as e:
      api = "Error..."
    if api[0]['Category']['Name'] == "Good" :
      category_description = '(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk.'
      category_color = 'good'
    elif api[0]['Category']['Name'] == "Moderate":
      category_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
      category_color = 'moderate'

    return render(request, 'home.html', {'api' : api, 'category_description': category_description, 'category_color' : category_color})
  else :
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=78520&distance=25&API_KEY=7CE66E0C-EECD-42E4-8948-87877395F6BF")

    try :
      api = json.loads(api_request.content)
    except Exception as e:
      api = "Error..."
    if api[0]['Category']['Name'] == "Good" :
      category_description = '(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk.'
      category_color = 'good'
    elif api[0]['Category']['Name'] == "Moderate":
      category_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
      category_color = 'moderate'

    return render(request, 'home.html', {'api' : api, 'category_description': category_description, 'category_color' : category_color})

def about(request):
  return render(request, 'about.html', {})
