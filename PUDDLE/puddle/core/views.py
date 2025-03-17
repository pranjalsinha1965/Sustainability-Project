from django.shortcuts import render, redirect
from .forms import SDAPunjabForm, SDAHaryanaForm, GovtBuildingForm, DivisionDetailForm, RailwayDetailForm, UploadFileForm
from .models import SDAPunjab, SDAHaryana, GovtBuilding, DivisionDetail, RailwayDetail
from .forms import SignupForm
import pandas as pd
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse
import pandas as pd 

# from .serializers import ImportSerializer 

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

# Index view
def index(request):
    return render(request, 'core/index.html')

# Contact view
def contact(request):
    return render(request, 'core/contact.html')

# Add SDA Punjab view
def add_sda_punjab(request):
    if request.method == "POST":
        form = SDAPunjabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sda_punjab_list')  # Redirect to the list page
    else:
        form = SDAPunjabForm()
    return render(request, 'core/add_sda_punjab.html', {'form': form})

# Add SDA Haryana view
def add_sda_haryana(request):
    if request.method == "POST":
        form = SDAHaryanaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sda_haryana_list')  # Redirect to the list page
    else:
        form = SDAHaryanaForm()
    return render(request, 'core/add_sda_haryana.html', {'form': form})

# Add Govt Building view
def add_govt_building(request):
    if request.method == "POST":
        form = GovtBuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('govt_building_list')  # Redirect to the list page
    else:
        form = GovtBuildingForm()
    return render(request, 'core/add_govt_building.html', {'form': form})

# Add Division Detail view
def add_division_detail(request):
    if request.method == "POST":
        form = DivisionDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('division_detail_list')  # Redirect to the list page
    else:
        form = DivisionDetailForm()
    return render(request, 'core/add_division_detail.html', {'form': form})

# Add Railway Detail view
def add_railway_detail(request):
    if request.method == "POST":
        form = RailwayDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('railway_detail_list')  # Redirect to the list page
    else:
        form = RailwayDetailForm()
    return render(request, 'core/add_railway_detail.html', {'form': form})

# SDA Punjab List view
def sda_punjab_list(request):
    sda_punjab_data = SDAPunjab.objects.all()  # Fetch all data from the SDAPunjab model
    return render(request, 'core/sda_punjab_list.html', {'sda_punjab_data': sda_punjab_data})

# SDA Haryana List view
def sda_haryana_list(request):
    sda_haryana_data = SDAHaryana.objects.all()  # Fetch all data from the SDAHaryana model
    return render(request, 'core/sda_haryana_list.html', {'sda_haryana_data': sda_haryana_data})

# Govt Building List view
def govt_building_list(request):
    govt_building_data = GovtBuilding.objects.all()  # Fetch all data from the GovtBuilding model
    return render(request, 'core/govt_building_list.html', {'govt_building_data': govt_building_data})

# Division Detail List view
def division_detail_list(request):
    division_detail_data = DivisionDetail.objects.all()  # Fetch all data from the DivisionDetail model
    return render(request, 'core/division_detail_list.html', {'division_detail_data': division_detail_data})

# Railway Detail List view
def railway_detail_list(request):
    railway_detail_data = RailwayDetail.objects.all()  # Fetch all data from the RailwayDetail model
    return render(request, 'core/railway_detail_list.html', {'railway_detail_data': railway_detail_data})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Read the uploaded Excel file using pandas (openpyxl engine for .xlsx files)
                df = pd.read_excel(file, engine='openpyxl')

                # Define the required columns for each sheet/model
                required_columns_sdapunjab = ['Name', 'Designation', 'Email', 'Responsibilities']
                required_columns_sdaharyana = ['State', 'Name of officer', 'Designation', 'Headquarter', 'Email-ID', 'EPBX No.']
                required_columns_govtbuilding = ['Department', 'Address', 'Email', 'Contact', 'Website']
                required_columns_divisiondetails = ['Division Name', 'DRM Name', 'Zone Name', 'Zone Code', 'No of Division', 'No of Stations', 'Headquarters', 'Address']
                required_columns_railwaydetails = ['Zone', 'Division name', 'name', 'city']

                # Process SDA Punjab data
                if all(col in df.columns for col in required_columns_sdapunjab):
                    for index, row in df.iterrows():
                        SDAPunjab.objects.create(
                            name=row['Name'],
                            designation=row['Designation'],
                            email=row['Email'],
                            responsibilities=row['Responsibilities'],
                        )

                # Process SDA Haryana data
                if all(col in df.columns for col in required_columns_sdaharyana):
                    for index, row in df.iterrows():
                        SDAHaryana.objects.create(
                            state=row['State'],
                            officer_name=row['Name of officer'],
                            designation=row['Designation'],
                            headquarter=row['Headquarter'],
                            email=row['Email-ID'],
                            epbx_no=row['EPBX No.'],
                        )

                # Process Govt Buildings data
                if all(col in df.columns for col in required_columns_govtbuilding):
                    for index, row in df.iterrows():
                        GovtBuilding.objects.create(
                            department=row['Department'],
                            address=row['Address'],
                            email=row['Email'],
                            contact=row['Contact'],
                            website=row['Website'],
                        )

                # Process Division Details data (Assuming data is in Sheet5)
                division_df = pd.read_excel(file, engine='openpyxl', sheet_name='Sheet5')  # Read the specific sheet for Division Details
                if all(col in division_df.columns for col in required_columns_divisiondetails):
                    for index, row in division_df.iterrows():
                        DivisionDetail.objects.create(
                            division_name=row['Division Name'],
                            drm_name=row['DRM Name'],
                            zone_name=row['Zone Name'],
                            zone_code=row['Zone Code'],
                            no_of_division=row['No of Division'],
                            no_of_stations=row['No of Stations'],
                            headquarters=row['Headquarters'],
                            address=row['Address'],
                        )

                # Process Railway Details data (Assuming data is in Sheet4)
                railway_df = pd.read_excel(file, engine='openpyxl', sheet_name='Sheet4')  # Read the specific sheet for Railway Details
                if all(col in railway_df.columns for col in required_columns_railwaydetails):
                    for index, row in railway_df.iterrows():
                        RailwayDetail.objects.create(
                            zone=row['Zone'],
                            division_name=row['Division name'],
                            name=row['name'],
                            city=row['city'],
                        )

                messages.success(request, "File processed and data saved successfully.")
                return redirect('upload_file')  # Redirect after success
            except Exception as e:
                messages.error(request, f"Error processing file: {str(e)}")
                return redirect('upload_file')
    else:
        form = UploadFileForm()

    return render(request, '/uploads', {'form': form})
