require('../../styles/contactsview.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'
// import { userId } from '../actions'
import ContactPeriodForm from './ContactPeriodForm'


class ContactsView extends Component {
  static propTypes = { 
    contacts: PropTypes.array.isRequired,
  }

  _generateContactListItems = () => {
    var contacts = this.props.contacts
    return this.props.contacts.map((contact, index) => {
      return (
        <li className='contact-list-item' key={index}>
          <div className='field contact-fname'>{ contact.first_name }</div>
          <div className='field contact-lname'>{ contact.last_name }</div>
          <div className='field contact-email'>{ contact.email }</div>
          <div className='field contact-period'><ContactPeriodForm contact_id={ contact.contact_id }/></div>
        </li>
      ) 
    })
  }

  render() {
    return (
      <div className='contacts-view'>
        <div className='contacts-table'>
          <div  className='contacts-list contacts-list-header'>
            <div className='header-item contact-list-item field'>First Name</div>
            <div className='header-item contact-list-item field'>Last Name</div>
            <div className='header-item contact-list-item field'>Email</div>  
            <div className='header-item contact-list-item field'>Period</div>   
          </div>           
          <ul className='contacts-list'>
            {this._generateContactListItems()}
          </ul>
        </div>
      </div>
    )
  }
}

export default ContactsView
