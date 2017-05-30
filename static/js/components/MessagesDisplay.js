require('../../styles/messagesview.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'


class MessagesDisplay extends Component {
  static propTypes = { 
    messages: PropTypes.array.isRequired,
  }

  _generateMessageDisplayItems = () => {
    var messages = this.props.messages
    return this.props.messages.map((message, index) => {
      return (
        <li className='msg-list-item' key={index}>
          <div className='msg-field msg-id'>{ message.msg_id }</div>
          <div className='msg-field created-by'>{ message.created_by==1 ? 'default':'user' }</div>
          <div className='msg-field msg-text'>{ message.msg_text }</div>
        </li>
      ) 
    })
  }

  render() {
    return (
      <div className='msgs-display'>
        <div className='msg-table'>
          <div  className='msg-list msg-list-header msg-list-item'>
            <div className='msg-header-item msg-field msg-id'>ID</div>
            <div className='msg-header-item msg-field created-by'>Created By</div>
            <div className='msg-header-item msg-field msg-text'>Message Preview</div>    
          </div>           
            <ul className='msg-list'>
              {this._generateMessageDisplayItems()}
            </ul>
        </div>
      </div>
    )
  }
}

export default MessagesDisplay
