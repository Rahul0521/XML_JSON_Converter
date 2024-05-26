# from django.shortcuts import render,redirect
# from .forms import XMLFileForm
# import xmltodict
# import json

# def upload_file(request):
#     if request.method == 'POST':
#         form = XMLFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Get the uploaded file
#             uploaded_file = request.FILES['file']

#             # Read the file content directly from memory
#             file_content = uploaded_file.read().decode('utf-8')

#             # Convert XML to JSON
#             data_dict = xmltodict.parse(file_content)
#             json_data = json.dumps(data_dict, indent=4)

#             return render(request, 'converter/result.html', {'json_data': json_data})
#         else:
#             print("Invaid Form!")
#     else:
#         print("GET request")
#         form = XMLFileForm()
#     return render(request, 'converter/upload.html', {'form': form})
# from django.http import HttpResponse
# import json


# def download_json(request):
#     if request.method == 'POST':
#         json_data = request.POST.get('json_data')
#         response = HttpResponse(json_data, content_type='application/json')
#         response['Content-Disposition'] = 'attachment; filename="converted_data.json"'
#         return response
# def error_page(request):
#     return render(request, 'converter/error.html')

# from django.shortcuts import render, redirect
# from .forms import XMLFileForm
# import xmltodict
# import json
# from django.http import HttpResponse

# def upload_file(request):
#     if request.method == 'POST':
#         form = XMLFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Get the uploaded file
#             uploaded_file = request.FILES['file']

#             # Read the file content directly from memory
#             file_content = uploaded_file.read().decode('utf-8')

#             try:
#                 # Convert XML to JSON
#                 data_dict = xmltodict.parse(file_content)
#                 json_data = json.dumps(data_dict, indent=4)

#                 # Create an HttpResponse to allow download
#                 response = HttpResponse(json_data, content_type='application/json')
#                 response['Content-Disposition'] = 'attachment; filename="converted_data.json"'
#                 return render(request, 'converter/result.html', {'json_data': json_data})
#             except Exception as e:
#                 print("Error converting XML to JSON:", e)
#                 # If conversion fails, redirect to error page
#                 return redirect('error_page')
#         else:
#             # If form is invalid, redirect to error page
#             return redirect('error_page')
#     else:
#         form = XMLFileForm()
#     return render(request, 'converter/upload.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import XMLFileForm
import xmltodict
import json
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST':
        form = XMLFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file
            uploaded_file = request.FILES['file']

            # Read the file content directly from memory
            file_content = uploaded_file.read().decode('utf-8')

            try:
                # Convert XML to JSON
                data_dict = xmltodict.parse(file_content)
                json_data = json.dumps(data_dict, indent=4)

                # Create an HttpResponse to allow download
                response = HttpResponse(json_data, content_type='application/json')
                response['Content-Disposition'] = 'attachment; filename="converted_data.json"'
                return render(request, 'converter/result.html', {'json_data': json_data})
            except Exception as e:
                print("Error converting XML to JSON:", e)
                # If conversion fails, redirect to error page
                return redirect('error_page')
        else:
            # If form is invalid, redirect to error page
            return redirect('error_page')
    else:
        form = XMLFileForm()
    return render(request, 'converter/result.html', {'form': form})

def download_json(request):
    if request.method == 'POST':
        json_data = request.POST.get('json_data')
        response = HttpResponse(json_data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="converted_data.json"'
        return response

def error_page(request):
    return render(request, 'converter/error.html')
