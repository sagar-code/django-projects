from django.shortcuts import render

# custom import
from django.shortcuts import get_object_or_404, redirect
from .models import UserInfo
from .forms import UserInfoModelForm


# Create your views here.
def list_all_user(request):
    data = UserInfo.objects.all()
    context = {
        'data': data
    }
    return render(request, "crudOperations/list.html", context=context)


def detail_of_user(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    context = {
        'user_object': user_object
    }
    return render(request, "crudOperations/detail.html", context=context)


def create_user_info(request):
    if request.method == 'POST':
        # process the form
        form_instance = UserInfoModelForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('/crud/list/')
        else:
            print("Form is invalid")
    else:
        form_instance = UserInfoModelForm()
    context = {
        'form_instance': form_instance
    }
    return render(request, 'crudOperations/create.html', context=context)


def update_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    if request.method == 'POST':
        # process the form
        form_instance = UserInfoModelForm(request.POST, instance=user_object)
        if form_instance.is_valid():
            form_instance.save()
            return redirect(f'/crud/detail/{user_id}')
        else:
            print("Form is invalid")
    else:
        form_instance = UserInfoModelForm(instance=user_object)
    context = {
        'form_instance': form_instance
    }
    return render(request, 'crudOperations/update.html', context=context)


def delete_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    # deleting the user object
    user_object.delete()

    return redirect(f'/crud/list/')
