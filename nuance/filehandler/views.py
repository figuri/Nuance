from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import UploadedFile
from django.core.files.storage import default_storage

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        uploaded_file = UploadedFile(file=myfile, file_name=myfile.name)
        uploaded_file.save()
        return render(request, 'filehandler/upload.html', {
            'uploaded_file': uploaded_file
        })
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

def delete_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, pk=file_id)
    file_path = uploaded_file.file.path
    if default_storage.exists(file_path):
        default_storage.delete(file_path)
    uploaded_file.delete()
    return HttpResponse('File deleted successfully')

def update_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, pk=file_id)
    if request.method == 'POST':
        new_file_name = request.POST.get('file_name')
        if new_file_name:
            uploaded_file.file_name = new_file_name
            uploaded_file.save()
            return HttpResponse('File updated successfully')
    return HttpResponse('Invalid request', status=400)
