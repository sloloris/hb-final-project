// require('../../styles/contactsview.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'


class ContactsView extends Component {
  static propTypes = { 
    contacts: PropTypes.array.isRequired,
  }

  _generateContactListItems = () => {
    var contacts = this.props.contacts
    return this.props.contacts.map((contact, index) => {
      return (
        <li className='contact-list-item' key={index}>
          <div className='contact-fname'>{ contact.first_name }</div>
          <div className='contact-lname'>{ contact.last_name }</div>
          <div className='contact-email'>{ contact.email }</div>
        </li>
      ) 
    })
  }

  render() {
    return (
      <div className='contacts-view'>
        <ul className='contacts-list'>
          {this._generateContactListItems()}
        </ul>
      </div>
    )
  }
}

export default ContactsView
