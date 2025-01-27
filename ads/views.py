from django.shortcuts import render, get_object_or_404, redirect
from .models import Ad , Comment , Tag
from .forms import AdForm , CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import Http404 , JsonResponse





def ad_list(request):
    query = request.GET.get('q', '')  # دریافت پارامتر جستجو
    selected_tag = request.GET.get('tag', '')  # دریافت تگ انتخاب‌شده از URL
    ads = Ad.objects.all()  # گرفتن تمام آگهی‌ها
    tags = Tag.objects.all()  # گرفتن تمام تگ‌ها برای نمایش در فیلتر

    # فیلتر کردن آگهی‌ها بر اساس جستجو
    if query:
        ads = ads.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(tags__name__icontains=query)  # فیلتر بر اساس جستجو در تگ‌ها
        )

    # فیلتر کردن آگهی‌ها بر اساس تگ انتخاب‌شده
    if selected_tag:
        ads = ads.filter(tags__id=selected_tag)

    return render(request, 'ads/ad_list.html', {'ads': ads, 'query': query, 'tags': tags, 'selected_tag': selected_tag})




@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if ad.owner != request.user:
            raise Http404("You are not authorized to edit this ad.")
        if form.is_valid():
            form.save()
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm(instance=ad)

    return render(request, 'ads/edit_ad.html', {'form': form, 'ad': ad})



@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if ad.owner != request.user:
        raise Http404("You are not authorized to delete this ad.")
    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')  # پس از حذف آگهی، به لیست آگهی‌ها باز می‌گردیم

    return render(request, 'ads/delete_ad.html', {'ad': ad})




@login_required
def toggle_favorite(request, ad_id):
    if request.method == 'POST':
        ad = get_object_or_404(Ad, id=ad_id)
        
        # تغییر وضعیت علاقه‌مندی
        ad.favorite = not ad.favorite
        ad.save()

        return JsonResponse({'favorite': ad.favorite})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)




def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    tags = ad.tags.all()
    comments = ad.comments.all()
    return render(request, 'ads/ad_detail.html', {'ad': ad, 'comments': comments , 'tags' : tags})


@login_required
def add_comment(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, ad=ad, content=content)
    return redirect('ad_detail', ad_id=ad.id)



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('ad_list')  # یا هر صفحه‌ای که می‌خواهید پس از ورود به آن هدایت شوید
    else:
        form = AuthenticationForm()
    return render(request, 'ads/login.html', {'form': form})


def signup_view(request):
    return render(request, 'ads/signup.html')



@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)  # آگهی رو به صورت موقت ذخیره می‌کنیم
            ad.owner = request.user  # کاربر لاگین‌شده رو به عنوان مالک آگهی تنظیم می‌کنیم
            ad.save()  # ذخیره کردن آگهی تا ID آن ساخته شود
            
            # اضافه کردن تگ‌ها به آگهی
            tags = form.cleaned_data['tags']
            ad.tags.add(*tags)  # تگ‌ها رو به آگهی اضافه می‌کنیم
            ad.save()  # ذخیره آگهی با تگ‌ها
            
            return redirect('ad_list')  # هدایت به صفحه لیست آگهی‌ها
        else:
            return render(request, 'ads/create_ad.html', {'form': form})
    else:
        form = AdForm()  # فرم خالی در صورت درخواست GET
    return render(request, 'ads/create_ad.html', {'form': form})







def favorites(request):
    user_favorites = Ad.objects.filter(favorite=True) 
    return render(request, 'ads/favorites.html', {'ads': user_favorites})



@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return redirect('ad_detail', ad_id=comment.ad.id)  # اگر کاربر کامنت را خود ایجاد نکرده است، به صفحه جزئیات آگهی هدایت می‌شود

    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('ad_detail', ad_id=comment.ad.id)

    return render(request, 'ads/edit_comment.html', {'comment': comment})



@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return redirect('ad_detail', ad_id=comment.ad.id)  # اگر کاربر کامنت را خود ایجاد نکرده است، به صفحه جزئیات آگهی هدایت می‌شود

    ad_id = comment.ad.id
    comment.delete()
    return redirect('ad_detail', ad_id=ad_id)


