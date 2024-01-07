from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Policy, Tag, Subtopic
from .forms import PolicyForm, VoteForm
from .utils import searchPolicies, paginatePolicies
from django.views.generic.detail import DetailView


def policies(request):
    policies, search_query = searchPolicies(request)
    custom_range, policies = paginatePolicies(request, policies, 6)

    context = {'policies': policies,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'policies/policies.html', context)

def subtopics(request, policy_id):
    policyObj = Policy.objects.get(id=policy_id)
    subtopics = policyObj.subtopic_set.all()
    return render(request, 'policies/subtopics.html', {'subtopics': subtopics})

      
def policy(request, policy_id):
    policyObj = Policy.objects.get(id=policy_id)
    form = VoteForm()

    if request.method == 'POST':
        form = VoteForm(request.POST)
        review = form.save(commit=False)
        review.policy = policyObj
        review.owner = request.user.profile
        review.save()

        policyObj.getVoteCount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('policy', pk=policyObj.id)
    
    subtopics = policyObj.subtopic_set.all()

    context = {'policy': policyObj, 'subtopics': subtopics, 'form': form}

    return render(request, 'policies/single-policy.html', context)

def subtopic(request, policy_id, subtopic_id):
    policyObj = Policy.objects.get(id=policy_id)
    subtopic = Subtopic.objects.get(id=subtopic_id)
    # form = VoteForm()

    # if request.method == 'POST':
    #     form = VoteForm(request.POST)
    #     review = form.save(commit=False)
    #     review.policy = policyObj
    #     review.owner = request.user.profile
    #     review.save()

    #     policyObj.getVoteCount

    #     messages.success(request, 'Your review was successfully submitted!')
    #     return redirect('policy', pk=policyObj.id)
    
    # subtopics = subtopic.subtopic_set.all()

    context = {'policy': policyObj, 'subtopic': subtopic}

    return render(request, 'policies/subtopic.html', context)

@login_required(login_url="login")
def createPolicy(request):
    profile = request.user.profile
    form = PolicyForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form = PolicyForm(request.POST, request.FILES)
        if form.is_valid():
            policy = form.save(commit=False)
            policy.owner = profile
            policy.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                policy.tags.add(tag)
            return redirect('account')

    context = {'form': form}
    return render(request, "policies/policy_form.html", context)


@login_required(login_url="login")
def updatePolicy(request, pk):
    profile = request.user.profile
    policy = profile.policy_set.get(id=pk)
    form = PolicyForm(instance=policy)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = PolicyForm(request.POST, request.FILES, instance=policy)
        if form.is_valid():
            policy = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                policy.tags.add(tag)

            return redirect('account')

    context = {'form': form, 'policy': policy}
    return render(request, "policies/policy_form.html", context)


@login_required(login_url="login")
def deletePolicy(request, pk):
    profile = request.user.profile
    policy = profile.policy_set.get(id=pk)
    if request.method == 'POST':
        policy.delete()
        return redirect('policies')
    context = {'object': policy}
    return render(request, 'delete_template.html', context)