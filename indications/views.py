from django.shortcuts import render
from datetime import datetime
from .forms import IndicationsForm

def checkDate():
    year = datetime.today().year
    months = datetime.today().month
    todayDate = datetime.today()
    startDate = datetime(year, months, 18)
    finishDate = datetime(year, months, 20)
    if (startDate <= todayDate) or (finishDate <= todayDate):
        return True

    return False


def indications(request):
    form = IndicationsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'templatesGpteTlt/indications.html', locals())

