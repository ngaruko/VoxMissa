import { Calendar } from '@fullcalendar/core';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin!
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {
  StyleSheet,
  Text,
  View,
  Pressable,
  useWindowDimensions,
} from 'react-native';

export default function App() {
  const {height} = useWindowDimensions();
  const [number, setNumber] = useState(0);
  const [events, setEvents] = useState([]);
  const apiUrl = 'http://127.0.0.1:8000/api/calendarevents/'
  
  useEffect(() => {
    axios.get(apiUrl)
      .then(response => {
        setEvents(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  function handlePress() {
    setNumber(parseInt(Math.random() * 10000, 10) % 100);
  }
  
  return (
    <FullCalendar
      plugins={[ dayGridPlugin ]}
      initialView="dayGridMonth"
      events={
        [
        {
            "type": "election",
            "title": "Presidential",
            "description": "Unicameral",
            "start": "2024-01-21T00:00:00Z",
            "end": "2024-01-25T00:00:00Z",
        },
        {
            "type": "election",
            "title": "Presidential",
            "description": "Unicameral",
            "date": "2024-02-01"
        }
       
    ]}
      // eventSources={[
      //   {
      //     url: apiUrl,
      //     method:'GET',
      //     failure: function (){
      //       alert('Error fetching resources')
      //     }
      //   }
      // ]}
    />
  )

}

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
//   br: {
//     height: 12,
//   },
//   btn: {
//     backgroundColor: '#222',
//     padding: 10,
//   },
//   btnText: {
//     color: '#fff',
//   },
// });