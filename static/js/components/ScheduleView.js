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
        // contacts: props.contacts
      };

      this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange = (event) => {
    const target = event.target;
    const value = target.value
    // target.type === 'checkbox' ? target.checked : target.value;
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
      <div className='schedule-form-container'>
        <form onSubmit={ this.handleSubmit }>
          <label>
            To: 

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
              name='chooseContact'
              value={this.state.chooseContact}
              onChange={(event, val) => this.setState({...this.state,'chooseContact': val})}
              onSelect={(val) => {this.setState({...this.state, 'chooseContact': val})}}
            />

{/*            <input
              name='chooseContact'
              type='text'
              placeholder='enter email'
              value={this.state.chooseContact} 
              onChange={this.handleInputChange} />*/}

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
