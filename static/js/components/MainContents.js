require('../../styles/maincontents.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types'


class MainContents extends Component {
  static propTypes = {
    currentViewIndex: PropTypes.number.isRequired,
  }

  render() {
    return (
      <div className="main-contents">
      HERE ARE SOME CONTENTS
      </div>
    )
  }
}

export default MainContents