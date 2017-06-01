require('../../styles/scheduleview.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'


class ScheduleView extends Component {
  static propTypes = { 

  }

constructor(props) {
    super(props);
    this.state = {
      chooseContact: null,
      userEmail: 'isabelle.k.miller@gmail.com',
      // startDate: ,
      contactPeriod: 90
    };

    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(event) {
  alert('Message scheduled!');
  event.preventDefault();
  // $.ajax({
  //     url: '/set_period',
  //     type: 'POST',
  //     data: {contact_id: this.props.contact_id,
  //           value: this.state.value},
  //     success: (response) => {
  //       alert('Data posted to server');
  //     }
  //   })
  }

  render() {
    return (
      <div className='schedule-form-container'>
        <form onSubmit={ this.handleSubmit }>
          <label>
            To: 
            <input
              name='chooseContact'
              type='text'
              value='Start typing a name...' //{this.state.chooseContact}
              onChange={this.handleInputChange} />
          </label>
          <br />
          <label>
            From: 
            <input
              name='userEmail'
              type='text'
              value='isabelle.k.miller@gmail.com' //{this.state.numberOfGuests}
              onChange={this.handleInputChange} />
          </label>
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
            Contact period: 
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
