from django.shortcuts import render
from django.db.models import Q
from tgapi.models import CarAd, RealtyAd, JobAd


def search_view(request):
    query = request.GET.get('q')
    results = []

    if query and len(query) >= 3:
        car_ads = CarAd.objects.filter(title__icontains=query)
        realty_ads = RealtyAd.objects.filter(title__icontains=query)
        job_ads = JobAd.objects.filter(title__icontains=query)

        # Combine the querysets into a single list of results
        results = list(car_ads) + list(realty_ads) + list(job_ads)

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search/search_result.html', context)