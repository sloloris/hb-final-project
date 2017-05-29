require('../../styles/leftnav.css') // add stylings

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import classNames from 'classnames' // passes dictionary where key is a class and value is true or false, adds classes with true values to elements

// define LeftNav component
class LeftNav extends Component {

  // define LeftNav property types
  static propTypes = {
    currentViewIndex: PropTypes.number.isRequired,
    navPages: PropTypes.array.isRequired,
    onClick: PropTypes.func.isRequired,
    // onClickLogout: PropTypes.func.isRequired
  }

  // property understood by React; defines default props in case onClick is not otherwise found
  static defaultProps = {
    onClick: console.log('clicked!')
  }

  // define classes for nav pages and assign to list items
  _getNavPages = () => {
    return this.props.navPages.map((navPage, index) => {
      var navPageClasses = classNames ({
        'selected': this.props.currentViewIndex == index 
      })

      return (
        <li className={navPageClasses} key={index} onClick={this.props.onClick.bind(this, index)}>
          <div className='page-name'>{navPage}</div>
        </li>
        )
    })
  }
  
  // passes nav pages w/classes determined by _getNavPages to display of leftNav
  render() {
    return (
      <div>
        <ul className="nav-pages-list">
          {this._getNavPages()}
        </ul>
        <div className="logout-btn" onClick={this.props.onClickLogout}>Log Out</div>
      </div>
    )
  }
}
// what is exported for import into other files
export default LeftNav