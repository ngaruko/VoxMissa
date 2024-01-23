import React from 'react'

import { formatDate } from '@fullcalendar/core'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import listPlugin from '@fullcalendar/list';
//import EventCalendar from './events/EventCalendar'
import {
  StyleSheet,
  StatusBar,
  Platform,
  Text,
  View,
  Pressable,
  useWindowDimensions,
  SafeAreaView,
} from 'react-native';
import { Calendar } from 'react-native-big-calendar'

const events = [
  {
    title: 'Meeting',
    start: new Date(2024, 1, 22, 10, 0),
    end: new Date(2024, 1, 23, 10, 30),
  },
  {
    title: 'Coffee break',
    start: new Date(2024, 1, 24, 15, 45),
    end: new Date(2024, 1, 24, 16, 30),
  },
]

export default class App extends React.Component {

  state = {
    weekendsVisible: true,
    currentEvents: []
  }

  render() {
    return Platform.OS=='web'?(
      <SafeAreaView style={styles.container}>
        <Calendar 
        events={events} 
        height={600} 
        mode='month' 
        locale='fr'
        showAdjacentMonths='true'
        renderHeader={() => <Text>Calendar</Text>}
        //renderHeaderForMonthView={() => <Text>Calendar</Text>}
        dayHeaderHighlightColor={'#000'}
        weekDayHeaderHighlightColor={'#aaa'}
        headerComponent={
          <Text style={{ color: '#aaa', fontSize: 25 }}>CalendarBody's headerComponent</Text>
        }
        showTime='true'
        // onPressCell={onPressCell} 
        // onPressEvent={onPressEvent}
        // onChangeDate={onChangeDate}
        />
        <StatusBar style="auto" />
      </SafeAreaView>      
    ):
    (
      <FullCalendar
        plugins={[ dayGridPlugin ]}
        initialView="dayGridMonth"
        events={[
          { title: 'event 1', date: '2024-01-22' },
          { title: 'event 2', date: '2024-01-25' }
        ]}
      />
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
  
  },
  text: {
    fontSize: 25,
    fontWeight: '500',
  },
});

