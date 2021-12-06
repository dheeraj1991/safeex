from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import JsonResponse, Http404
from lunar_phase.custom_decorator import logged_in_or_basicauth


# Create your views here.
@login_required
def dashboard(request):
    """
        Dashboard view renders the HTML, CSS and Javscript required to show the current day moon phase,
        It internally makes a call to the moon data api to fetch the required data to present on the UI
    """
    if request.method == 'GET':
        return render(request, 'lunar-phase.html')
    else:
        raise Http404


@logged_in_or_basicauth
def moon_data(request):
    """
        The view returns a JSON response with details of the current day moon phase, the date is
        taken from the browser hence the data will be always user timezone set on the browser
        The api calcualtes considering that On 1/6/2000 at 12:24:01, the moon was New.
    """
    Y = int(request.GET.get('year'))
    M = int(request.GET.get('month'))
    D = int(request.GET.get('day'))
    if M in [1, 2]:
        Y -= 1
        M += 12
    A = int(Y / 100)
    B = int(A / 4)
    C = 2 - A + B
    E = int(365.25 * (Y + 4716))
    F = int(30.601 * (M + 1))
    JD = C + D + E + F - 1524.5
    day_since_known_new_moon = JD - 2451549.5
    no_of_new_moons = day_since_known_new_moon // 29.53
    current_cycle_of_the_moon = (day_since_known_new_moon / 29.53) % 1
    number_of_days_into_moon_cycle = current_cycle_of_the_moon * 29.53
    if number_of_days_into_moon_cycle == 0 or number_of_days_into_moon_cycle == 29.53:
        moon_stage = "New"
    elif 0 < number_of_days_into_moon_cycle < 7:
        moon_stage = "Waxing Crescent"
    elif number_of_days_into_moon_cycle == 7:
        moon_stage = "First Quarter"
    elif 7 < number_of_days_into_moon_cycle < 15:
        moon_stage = "Waxing Gibbous"
    elif number_of_days_into_moon_cycle == 15:
        moon_stage = "Full"
    elif 15 < number_of_days_into_moon_cycle < 22:
        moon_stage = "Waning Gibbous"
    elif number_of_days_into_moon_cycle == 7:
        moon_stage = "Last Quarter"
    elif 22 < number_of_days_into_moon_cycle < 29.53:
        moon_stage = "Waning Crescent"

    percentage_of_moon_cycle = round((number_of_days_into_moon_cycle / 29.53) * 100, 2)

    return JsonResponse({
        'day_since_known_new_moon': day_since_known_new_moon, 'current_cycle_of_the_moon': current_cycle_of_the_moon,
        'percentage_of_moon_cycle': percentage_of_moon_cycle, 'no_of_new_moons': no_of_new_moons,
        'moon_stage': moon_stage, 'moon_image': "{}.png".format(moon_stage.lower().replace(" ", "-"))
    })
