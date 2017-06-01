require('../../styles/maincontents.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import ContactsView from './ContactsView'
import MessagesDisplayContainer from '../containers/MessagesDisplayContainer'
import ScheduleView from './ScheduleView'


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
        contents = <MessagesDisplayContainer messages={this.props.messages} />
        break;

      case 2:
        contents = <ScheduleView />

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