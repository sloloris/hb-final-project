
import React, { Component } from 'react'
import PropTypes from 'prop-types'

class ContactPeriodForm extends Component {
  static propTypes = {
    contact_id: PropTypes.number.isRequired
  }
  constructor(props) { // need?
    super(props);
    this.state = {value: 90};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({contact_id: contact_id,
      value: event.target.value});
  }

  handleSubmit(event) {
    alert('Contact period updated to' + this.state.value);
    event.preventDefault();
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
            <option selected value="90">90</option>
            <option value="60">180</option>
          </select>
        </label>
        <input type="submit" value="submit" />
      </form>
    );
  }
}

export default ContactPeriodForm