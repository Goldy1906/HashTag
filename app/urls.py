from django.urls import path, include
from . import views 

app_name="app"
urlpatterns=[
     path('', views.index, name='index'),
     path('<str:name>/',views.download, name='download'),
     
 ]

  # time.sleep(5)
        # zip_file = open('E:\\project Shaky\\shaky\\dataset.zip', 'r')
        # response = HttpResponse(zip_file, content_type='application/forced-download')
        # response['Content-Disposition'] = 'attachment; filename=dataset.zip'
        # return render(request,'index.html',{'data1': response})
        # file_path='E:\\project Shaky\\shaky\\dataset.zip'
        # if os.path.exists(file_path):
        #     with open(file_path,'rb')as fh:
        #         response=HttpResponse(fh.read(),content_type="application/force-download")
        #         response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
       