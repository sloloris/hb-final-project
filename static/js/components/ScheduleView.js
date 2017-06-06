require('../../styles/scheduleview.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import moment from 'moment'
import Autocomplete from 'react-autocomplete'


class ScheduleView extends Component {
  static propTypes = { 
    contacts: PropTypes.array.isRequired
  }

  constructor(props) {
      super(props);
      this.state = {
        chooseContact: '',
        startDate: moment().format('YYYY-MM-DD'),
        contactPeriod: 90,
      };

      this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange = (event) => {
    const target = event.target;
    const value = target.value
    const name = target.name;

    this.setState({
      ...this.state,
      [name]: value
    });
  }

  _onChangeChooseContact = (event, value) => {
    // const target = event.target;
    // const value = target.value
    // const name = 'chooseContact'

    this.setState({
      ...this.state,
      'chooseContact': value
    })

    console.log('chooseContact is now ' + value)
  }

  _generateChooseContactAutocompleteItems = () => {
    var contacts = this.props.contacts
    console.log(contacts)
    return contacts.map((contact, index) => {
      return (
      { label: contact.first_name + ' ' + contact.last_name + ' <' + contact.email + '>' }
      )
    })
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
    return (
      <div className='schedule-form-view'>
        <div className='schedule-form-container'>
          <div className='form-container'>
            <form onSubmit={ this.handleSubmit } className='form'>
              <label>
              To (contact): &nbsp;
                <Autocomplete
                  getItemValue={(item) => item.label}
                  items=
                    { this._generateChooseContactAutocompleteItems() }

                  
                  renderItem={(item, isHighlighted) =>
                    <div style={{ background: isHighlighted ? 'lightgray' : 'white' }} key={item.label}>
                      {item.label}
                    </div>
                  }
                  shouldItemRender={(item, val) => {
                    return item.label.lastIndexOf(val, 0) === 0
                  }}
                  className='autocomplete-input'
                  name='chooseContact'
                  value={this.state.chooseContact}
                  onChange={(event, val) => this.setState({...this.state,'chooseContact': val})}
                  onSelect={(val) => {this.setState({...this.state, 'chooseContact': val})}}
                />
              </label>
              <br />
              <br />
              <br />
              <br />
              Start date: &nbsp;
              <label>
                
                <input
                  className='start-date-input'
                  name='startDate'
                  type='date'
                  value={this.state.startDate}
                  onChange={this.handleInputChange} />
              </label>
              <br />
              <br />
              <br />
              <br />
              <label>
                Contact period (days): &nbsp;
                <input
                  className='contact-period-input'
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
          <div className='schedule-instructions'>
            To select a contact, start typing their name.
            <br /><br /><br />
            Select a date from which to start your email messaging schedule.
            <br /><br /><br />
            The contact period is how many <p className='highlighted-text'>days</p> by which emails will regularly be sent to your selected contact. Messages will be randomly selected from your message template collection accessible in the Messages tab. 
          </div>
        </div>
      </div>
    );
  }
}

export default ScheduleView
