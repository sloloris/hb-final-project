require('../../styles/contactsview.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'
// import { userId } from '../actions'
import ContactPeriodForm from './ContactPeriodForm'


class ContactsView extends Component {
  static propTypes = { 
    contacts: PropTypes.array.isRequired,
  }

  constructor(props) {
    super(props);
    this.state = {
      searchContacts: '',
      // contacts: props.contacts
    };

    this.handleInputChange = this.handleInputChange.bind(this);
  }

  // componentWillReceiveProps(nextProps) {
  //   if (nextProps.contacts != this.props.contacts) {
  //     this.setState({
  //       ...this.state,
  //       contacts: nextProps.contacts
  //     })
  //   }
  // }

  handleInputChange = (event) => {
    const target = event.target;
    const value = target.value
    const name = target.name;

    this.setState({
      ...this.state,
      [name]: value
    });
  }

  _generateContactListItems = () => {
    var contacts = this.props.contacts
    contacts.sort(function(a,b) {return (a.first_name > b.first_name) ? 1 : ((b.first_name > a.first_name) ? -1 : 0);} ); 
    return contacts.map((contact, index) => {
      return (
        <li className='contact-list-item' key={index}>
          <div className='field contact-fname'>{ contact.first_name }</div>
          <div className='field contact-lname'>{ contact.last_name }</div>
          <div className='field contact-email'>{ contact.email }</div>
        </li>
      ) 
    })
  }
  
  _onClickSortContactListByLastName = () => {
    var contacts = this.props.contacts
    contacts.sort(function(a,b) {return (a.last_name > b.last_name) ? 1 : ((b.last_name > a.last_name) ? -1 : 0);} ); 
    this.setState({...this.state, contacts:contacts })
    // return contacts.map((contact, index) => {
    //   return (
    //     <li className='contact-list-item' key={index}>
    //       <div className='field contact-fname'>{ contact.first_name }</div>
    //       <div className='field contact-lname'>{ contact.last_name }</div>
    //       <div className='field contact-email'>{ contact.email }</div>
    //     </li>
    //  )
    // })
  }

  render() {
    return (
      <div className='contacts-view'>
        <div className='search-bar contacts-content'>
          Find a friend: <input
            name='searchContacts'
            type='text'
            value={this.state.searchContacts}
            onChange={this.handleInputChange} />
        </div>
        <div className='contacts-table contacts-content'>
          <div  className='contacts-list contacts-list-header'>
            <div className='header-item contact-list-item field'>First Name</div>
            <div className='header-item contact-list-item field' onClick={ this._onClickSortContactListByLastName } >Last Name</div>
            <div className='header-item contact-list-item field'>Email</div>  
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
