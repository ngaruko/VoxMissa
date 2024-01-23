import React from 'react'
import { formatDate } from '@fullcalendar/core'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
//const { INITIAL_EVENTS, createEventId } = require('./event-utils')
const Calendar =()=> <View>FullCalendar</View>
import {
  StyleSheet,
  Text,
  View,
  Pressable,
  useWindowDimensions,
} from 'react-native';

const INITIAL_EVENTS = 
 [
      { id: 88,title: 'event 1', date: '2024-01-23' },
      { id: 99, title: 'event 2', date: '2024-02-02' }
    ] ;
console.log('initial..', INITIAL_EVENTS)

export default class EventCalendar extends React.Component {
  
  
  state = {
    weekendsVisible: true,
    currentEvents: []
  }

  render() {
    return (
      <View className='demo-app'>
        {this.renderSidebar()}
        <View className='demo-app-main'>
          <FullCalendar
            plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
            headerToolbar={{
              left: 'prev,next today',
              center: 'title',
              right: 'dayGridMonth,timeGridWeek,timeGridDay'
            }}
            initialView='dayGridMonth'
            editable={true}
            selectable={true}
            selectMirror={true}
            dayMaxEvents={true}
            weekends={this.state.weekendsVisible}
            // events={[
            //   { title: 'event 1', date: '2024-01-19' },
            //   { title: 'event 2', date: '2024-01-24' }
            // ]}
            //{getEvents}
            // eventSources={[{
            //   url: 'http://127.0.0.1:8000/api/calendarevents',
            //   method:'GET',
            //   Failure:function(){alert('Failed to fetch')}

            // }]}
            // initialEvents={[
            //   { id: 88,title: 'event 1', date: '2024-01-23' },
            //   { id: 99, title: 'event 2', date: '2024-02-02' }
            // ]}
            initialEvents={INITIAL_EVENTS} 
            // alternatively, use the `events` setting to fetch from a feed
            select={this.handleDateSelect}
            eventContent={renderEventContent} // custom render function
            eventClick={this.handleEventClick}
            eventsSet={this.handleEvents} // called after events are initialized/added/changed/removed
            /* you can update a remote database when these fire:
            eventAdd={function(){}}
            eventChange={function(){}}
            eventRemove={function(){}}
            */
          />
        </View>
      </View>
    )
  }

  renderSidebar() {
    return (
      <View className='demo-app-sidebar'>
        <View className='demo-app-sidebar-section'>
          <Text>Instructions</Text>
          <View>
            <Text>Select dates and you will be prompted to create a new event</Text>
            <Text>Drag, drop, and resize events</Text>
            <Text>Click an event to delete it</Text>
          </View>
        </View>
        <View className='demo-app-sidebar-section'>
          <label>
            <input
              type='checkbox'
              checked={this.state.weekendsVisible}
              onChange={this.handleWeekendsToggle}
            ></input>
            toggle weekends
          </label>
        </View>
        <View className='demo-app-sidebar-section'>
          <Text>All Events ({this.state.currentEvents.length})</Text>
          <View>
            {this.state.currentEvents.map(renderSidebarEvent)}
          </View>
        </View>
      </View>
    )
  }

  handleWeekendsToggle = () => {
    this.setState({
      weekendsVisible: !this.state.weekendsVisible
    })
  }

  handleDateSelect = (selectInfo) => {
    let title = prompt('Please enter a new title for your event')
    let calendarApi = selectInfo.view.calendar

    calendarApi.unselect() // clear date selection

    if (title) {
      calendarApi.addEvent({
        id: createEventId(),
        title,
        start: selectInfo.startStr,
        end: selectInfo.endStr,
        allDay: selectInfo.allDay
      })
    }
  }

  handleEventClick = (clickInfo) => {
    if (confirm(`Are you sure you want to delete the event '${clickInfo.event.title}'`)) {
      clickInfo.event.remove()
    }
  }

  handleEvents = (events) => {
    this.setState({
      currentEvents: events
    })
  }

}

function renderEventContent(eventInfo) {
  return (
    <>
      <Text>{eventInfo.timeText}</Text>
      <Text>{eventInfo.event.title}</Text>
    </>
  )
}

function renderSidebarEvent(event) {
  return (
    <View key={event.id}>
      <Text>{formatDate(event.start, {year: 'numeric', month: 'short', day: 'numeric'})}</Text>
      <Text>{event.title}</Text>
    </View>
  )
}

// function getEvents () {
//   let data =[]
//   axios.get('http://127.0.0.1:8000/api/calendarevents')
//     .then(response => {
//       console.log('data:::', response.data)
//       data.push(response.data)
//     })
//     .catch(error => {
//       console.log(error);
//     });
//     console.log('data', data)
// return data
// }

