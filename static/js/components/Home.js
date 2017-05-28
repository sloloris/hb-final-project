require('../../styles.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types';
import classNames from 'classnames';
import LeftNavContainer from '../containers/LeftNavContainer'

class Home extends Component {

  render() {
    return (
      <div className='app-container'>
        <LeftNavContainer
          navPages={['Contacts', 'Messages']} />
      </div>)
  }
}

export default Home