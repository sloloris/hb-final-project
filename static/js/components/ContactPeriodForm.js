
import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { postContactPeriod } from '../actions'

class ContactPeriodForm extends Component {
  static propTypes = {
    contact_id: PropTypes.number.isRequired
  }
  constructor(props) { // need?
    super(props);
    this.state = {value: 90}; // figure out how to make this the form input

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({contact_id: this.props.contact_id,
      value: event.target.value});
  }

  handleSubmit(event) {
    alert('Contact' + this.props.contact_id + 'period updated to' + this.state.value);
    event.preventDefault();
    $.ajax({
        url: '/set_period',
        type: 'POST',
        data: {contact_id: this.props.contact_id,
              value: this.state.value},
        success: () => {
          alert('Data posted to server');
        }
    })
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          <select value={this.state.value} onChange={this.handleChange}>
            <option value="15">7</option>
            <option value="15">15</option>
            <option value="30">30</option>
            <option value="60">60</option>
            <option defaultValue="90">90</option>
            <option value="180">180</option>
          </select>
        </label>
        <input type="hidden" name="contact_id" value={this.props.contact_id} />
        <input type="submit" value="submit" />
      </form>
    );
  }
}

export default ContactPeriodForm