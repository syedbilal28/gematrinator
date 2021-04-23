from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def search(request):
    entry=request.POST.get("entry")
    ordinal={}
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(1,27):
        ordinal[letters[i-1]]=i
    
    ordinal[" "]=0
    reverse_ordinal={}
    reverse_letters=letters.reverse()
    for i in range(26,0,-1):
        reverse_ordinal[letters[i-1]]=i
    #     print(i)
    # print(reverse_ordinal)
    reverse_ordinal[" "]=0
    text=entry.lower()
    text_letters=list(text)
    ordinal_count=0
    reverse_ordinal_count=0
    full_reduction_count=0
    for i in text_letters:
        ordinal_count+=ordinal[i]
        reverse_ordinal_count+=reverse_ordinal[i]
        temp=ordinal[i]
        if temp >=20:
            temp+=2
        elif temp >=10:
            temp+=1
            
        full_reduction_count+=(temp%10)
        reverse_full_reduction_count+=(reverse_temp%10)
    return JsonResponse({"ordinal_count":ordinal_count,"rever_ordinal":reverse_ordinal_count,"full_reduction":full_reduction_count})
