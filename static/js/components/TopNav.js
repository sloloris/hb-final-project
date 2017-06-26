require('../../styles/topnav.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types';

class TopNav extends Component {
  static propTypes = {}

  render() {
    return (
      <div className="user-topnav">
        <div className="user-greeting">Welcome, NAME</div>
      </div>
    )   
  }
}

export default TopNav