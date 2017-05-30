require('../../styles/maincontents.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import ContactsView from './ContactsView'
import MessagesDisplay from './MessagesDisplay'


class MainContents extends Component {
  static propTypes = {
    currentViewIndex: PropTypes.number.isRequired,
    contacts: PropTypes.array.isRequired,
    getUserContacts: PropTypes.func.isRequired,
    messages: PropTypes.array.isRequired,
    getMessages: PropTypes.func.isRequired
  }

  componentDidMount() {
    this.props.getUserContacts(),
    this.props.getMessages()
  }

  render() {
    var contents = 'CONTENTS'

    switch(this.props.currentViewIndex) {
      case 0:
        contents = <ContactsView contacts={this.props.contacts} /> // (instance of component ContactsView)
        break;

      case 1:
        contents = <MessagesDisplay messages={this.props.messages} />
        break;

      default:
        break;
    }


    return (
      <div className="main-contents">
        { contents }
      </div>
    )
  }
}

export default MainContents