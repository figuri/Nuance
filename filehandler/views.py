from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from .models import UploadedFile
from django.core.files.storage import default_storage
import pandas as pd
from django.shortcuts import render, redirect
from .models import UploadedFile
import boto3
from django.conf import settings

def upload_file(request):
    if request.method == 'POST' and request.FILES.getlist('myfiles'):
        # Define the S3 client inside the function
        s3_client = boto3.client(
            's3', 
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, 
            region_name=settings.AWS_REGION
        )

        files = request.FILES.getlist('myfiles')
        first_header_saved = False

        for file in files:
            df = pd.read_csv(file)
            if not first_header_saved:
                first_header_saved = True
            else:
                df = df.iloc[1:]

            csv_data = df.to_csv(index=False)

            # Save the uploaded file to the database
            uploaded_file = UploadedFile(file=file, file_name=file.name)
            uploaded_file.save()

            # Upload to S3
            s3_client.put_object(
                Bucket=settings.AWS_S3_BUCKET_NAME,
                Key=f"uploads/{file.name}",
                Body=csv_data
            )

        return redirect('list_files')

    return render(request, 'filehandler/upload.html')

def download_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, pk=file_id)
    file_path = uploaded_file.file.path
    if default_storage.exists(file_path):
        with default_storage.open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={uploaded_file.file_name}'
            return response
    raise Http404('File not found')

def list_files(request):
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'filehandler/list.html', {
        'uploaded_files': uploaded_files
    })

def view_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, pk=file_id)
    return render(request, 'filehandler/view_file.html', {
        'file': uploaded_file
    })

#function handles deletion and then redirects to list_files
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    
    if request.method == 'POST':
        file.delete()
        return redirect('list_files')  # Redirect to the list of files
    
    return render(request, 'filehandler/confirm_delete.html', {'file': file})
    