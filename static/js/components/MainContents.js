require('../../styles/maincontents.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'


class MainContents extends Component {
  static propTypes = {
    currentViewIndex: PropTypes.number.isRequired,
  }

  render() {
    var placeholder = 'PLACEHOLDER CONTENT'

    switch(this.props.currentViewIndex) {
      case 0:
        placeholder = 'This is the contacts view'
        break;

      case 1:
        placeholder = 'This is the messages view'
        break;

      default:
        break;
    }


    return (
      <div className="main-contents">
        { placeholder }
      </div>
    )
  }
}

export default MainContents