from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from eventcalendar.models import Event

from parties.models import Party
from .serializers import CalendarEventSerializer, PolicySerializer, ProjectSerializer, PartySerializer, EventSerializer
from projects.models import Project, Review, Tag
from policies.models import Topic


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

        {'GET': '/api/policies'},
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,
    )

    review.value = data['value']
    review.save()
    project.getVoteCount

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)

    return Response('Tag was deleted!')

@api_view(['GET'])
def getPolicies(request):
    policies = Topic.objects.all()
    serializer = PolicySerializer(policies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPolicy(request, pk):
    policy = Topic.objects.get(id=pk)
    serializer = PolicySerializer(policy, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getParties(request):
    country_query = request.GET.get("country")
    parties = Party.objects.filter(country=country_query) if country_query else Party.objects.all()
    serializer = PartySerializer(parties, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getParty(request, pk):
    party = Party.objects.get(id=pk)
    serializer = PartySerializer(party, many=False)
    return Response(serializer.data)

#events
@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

#calendar-events
@api_view(['GET'])
def getCalendarEvents(request):
    events = Event.objects.all()
    calendarevents = []
        # start: '2020-09-16T16:00:00'
    for event in events:
            calendarevents.append(
                {   
                    "id": event.id,
                    "country": event.country,
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%d"),
                    "end": event.end_time.strftime("%Y-%m-%d"),
                    "description": event.description,
                }
            )
    serializer = EventSerializer(calendarevents, many=True)
    return Response(calendarevents)

@api_view(['GET'])
def getEvent(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)