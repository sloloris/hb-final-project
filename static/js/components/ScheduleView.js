require('../../styles/scheduleview.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import moment from 'moment'
import { Autocomplete } from 'react-autocomplete'


class ScheduleView extends Component {
  static propTypes = { 

  }

  constructor(props) {
      super(props);
      this.state = {
        chooseContact: '',
        startDate: moment().format('YYYY-MM-DD'),
        contactPeriod: 90
      };

      this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange = (event) => {
    const target = event.target;
    const value = target.value
    // target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      // ...this.state,
      [name]: value
    });
  }

  handleSubmit = (event) => {
  alert('Message scheduled!');
  event.preventDefault();
  $.ajax({
      url: '/schedule',
      type: 'POST',
      data: { contact_id: 578,//this.state.chooseContact,
            start_date: this.state.startDate,
            period: this.state.contactPeriod
            },
      success: (response) => {
        console.log('Data posted to server');
      }
    })
  }

  render() {
    // var chooseContact = this.state.chooseContact
    return (
      <div className='schedule-form-container'>
        <form onSubmit={ this.handleSubmit }>
          <label>
            To: 
            <input
              name='chooseContact'
              type='text'
              placeholder='enter email'
              value={this.state.chooseContact} 
              onChange={this.handleInputChange} />

          </label>
          <br />

          <br />
          <br />
          <label>
            Start date: 
            <input
              name='startDate'
              type='date'
              value={this.state.startDate}
              onChange={this.handleInputChange} />
          </label>
          <br />
          <br />
          <label>
            Contact period (days): 
            <input
              name='contactPeriod'
              type='number'
              value={this.state.contactPeriod}
              onChange={this.handleInputChange} />
          </label>
          <br />
          <br />
          <input type='submit' className='btn schedule-btn' value='Schedule' />
        </form>
      </div>
    );
  }
}

export default ScheduleView
