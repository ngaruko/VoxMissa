from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Party, Ideology
from .forms import PartyForm, ReviewForm
from .utils import searchParties, paginateParties


def parties(request):
    parties, search_query = searchParties(request)
    custom_range, parties = paginateParties(request, parties, 6)

    context = {'parties': parties,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'parties/parties.html', context)


def party(request, pk):
    partyObj = Party.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.party = partyObj
        review.voter = request.user.profile
        review.save()

        partyObj.getVoteCount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('party', pk=partyObj.id)

    return render(request, 'parties/single-party.html', {'party': partyObj, 'form': form})


@login_required(login_url="login")
def createParty(request):
    profile = request.user.profile
    form = PartyForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form = PartyForm(request.POST, request.FILES)
        if form.is_valid():
            party = form.save(commit=False)
            party.owner = profile
            party.save()

            for tag in newtags:
                tag, created = Ideology.objects.get_or_create(name=tag)
                party.tags.add(tag)
            return redirect('account')

    context = {'form': form}
    return render(request, "parties/party_form.html", context)


@login_required(login_url="login")
def updateParty(request, pk):
    profile = request.user.profile
    party = profile.party_set.get(id=pk)
    form = PartyForm(instance=party)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = PartyForm(request.POST, request.FILES, instance=party)
        if form.is_valid():
            party = form.save()
            for tag in newtags:
                tag, created = Ideology.objects.get_or_create(name=tag)
                party.tags.add(tag)

            return redirect('account')

    context = {'form': form, 'party': party}
    return render(request, "parties/party_form.html", context)


@login_required(login_url="login")
def deleteParty(request, pk):
    profile = request.user.profile
    party = profile.party_set.get(id=pk)
    if request.method == 'POST':
        party.delete()
        return redirect('parties')
    context = {'object': party}
    return render(request, 'delete_template.html', context)

