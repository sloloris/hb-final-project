require('../../styles/messagesdisplay.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import classnames from 'classnames'
import { userId } from '../actions'


class MessagesDisplay extends Component {
  static propTypes = { 
    messages: PropTypes.array.isRequired,
    addMessage: PropTypes.func.isRequired
  }

  constructor(props) {
    super(props)
    this.state = {
      displayAdd: false,
      msgText: ''
    }
  }

  _generateMessageDisplayItems = () => {
    var messages = this.props.messages
    return this.props.messages.map((message, index) => {
      return (
        <li className='msg-list-item' key={index}>
          <div className='msg-field created-by'>{ message.created_by==1 ? 'default':'user' }</div>
          <div className='msg-field msg-text'>{ message.msg_text }</div>
        </li>
      ) 
    })
  }

  _onClickAdd = (event) => {
    this.setState({
      ...this.state,
      displayAdd: true
    })
  }

  _onClickCancel = (event) => {
    this.setState({
      ...this.state,
      displayAdd: false
    })
  }

  _onClickSave = (event) => {
        $.ajax({
        url: '/user/' + userId + '/messages',
        type: 'POST',
        data: {userId: userId,
              msgText: this.state.msgText},
        success: (response) => {
          this.props.addMessage({            
            // msg_id: 3,
            created_by: response['created_by'],
            msg_text: response['msg_text']
          })
        }
    })
    this.setState({
      ...this.state,
      displayAdd: false
    })
  }

  _onChangeMsgInput = (event) => {
    this.setState({
      ...this.state,
      msgText: event.target.value
    })
  }

  render() {
    var addMsgContainerClasses = classnames('msg-list-item', 'add-msg-container', { 'no-display': !this.state.displayAdd })
    return (
      <div className='msgs-display'>
        <div className='msg-table'>
          <div  className='msg-list msg-list-header msg-list-item'>
            <div className='msg-header-item msg-field created-by'>Created By</div>
            <div className='msg-header-item msg-field msg-text'>Message Preview
              <div className='btn add-msg-btn' onClick={ this._onClickAdd }>Add Template</div> 
            </div>
               
          </div>    
          <div className={ addMsgContainerClasses }>
            <textarea 
              className='msg-textarea' 
              value={ this.state.msgText } 
              onChange={ this._onChangeMsgInput } />
            <div className='btn-container'>
              <div className='btn btn-cancel' onClick={ this._onClickCancel }>Cancel</div>
              <div className='btn btn-save' onClick={ this._onClickSave }>Save</div>
            </div>

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
