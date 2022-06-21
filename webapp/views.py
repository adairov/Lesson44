from django.shortcuts import render

# Create your views here.
def index_view(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        secret_numbers = [3, 5, 4, 1]
        users_numbers = []
        bulls = 0
        cows = 0

        if int(request.POST.get("first_number")) >= 0 and int(request.POST.get("first_number")) <= 9:
            users_numbers.append(int(request.POST.get("first_number")))
        else:
            return render(request, "error.html")
        if int(request.POST.get("second_number")) >= 0 and int(request.POST.get("second_number")) <= 9 and int(request.POST.get("second_number")) not in users_numbers:
            users_numbers.append(int(request.POST.get("second_number")))
        else:
            return render(request, "error.html")
        if int(request.POST.get("third_number")) >= 0 and int(request.POST.get("third_number")) <= 9 and int(request.POST.get("third_number")) not in users_numbers:
            users_numbers.append(int(request.POST.get("third_number")))
        else:
            return render(request, "error.html")
        if int(request.POST.get("forth_number")) >= 0 and int(request.POST.get("forth_number")) <= 9 and int(request.POST.get("forth_number")) not in users_numbers:
            users_numbers.append(int(request.POST.get("forth_number")))
        else:
            return render(request, "error.html")

        for i in range(len(secret_numbers)):
            for j in range(len(users_numbers)):
                if int(secret_numbers[i]) == int(users_numbers[j]):
                    cows += 1
        for i in range(len(secret_numbers)):
            if int(secret_numbers[i]) == int(users_numbers[i]):
                bulls += 1

        cows = cows - bulls
        context = {"users_numbers": users_numbers, "cows": cows, "bulls": bulls}
        return render(request, "results.html", context)





def results_view(request):
    return render(request, "results.html")