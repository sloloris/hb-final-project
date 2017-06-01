require('../../styles/main.css')

import React, { Component } from 'react'
import PropTypes from 'prop-types';
import classNames from 'classnames';
import LeftNavContainer from '../containers/LeftNavContainer'
// import TopNavContainer from '../containers/TopNavContainer'
import MainContentsContainer from '../containers/MainContentsContainer'

class Home extends Component {

  render() {
    return (
      <div className='account-home'>
        <div className='left-nav'>
          <LeftNavContainer
            navPages={['Contacts', 'Messages', 'Schedule']} />
        </div>
        <div className='right-contents'>
          {/*<TopNavContainer />*/}
          <MainContentsContainer />
        </div>
      </div>
    )
  }
}

export default Home