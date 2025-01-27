document.addEventListener('DOMContentLoaded', function() {
    // انتخاب تمام دکمه‌های علاقه‌مندی
    const favoriteButtons = document.querySelectorAll('.toggle-favorite');

    favoriteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const adId = this.getAttribute('data-ad-id');
            const url = `/favorite/${adId}/`; // مسیری که دکمه باید به آن درخواست ارسال کند

            // ارسال درخواست POST به سرور
            fetch(url, {
                method: 'POST',  // روش ارسال
                headers: {
                    'Content-Type': 'application/json',  // نوع داده ارسالی
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,  // ارسال توکن CSRF
                },
                body: JSON.stringify({ 'favorite': true })  // داده‌های ارسالی
            })
            .then(response => response.json())
            .then(data => {
                if (data.favorite !== undefined) {
                    // تغییر محتوای دکمه بر اساس وضعیت جدید علاقه‌مندی
                    if (data.favorite) {
                        this.innerHTML = '<i class="fas fa-star"></i> Unfavorite';
                    } else {
                        this.innerHTML = '<i class="far fa-star"></i> Favorite';
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
