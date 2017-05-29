import { connect } from 'react-redux'
import LeftNav from '../components/LeftNav'
import { setCurrentView } from '../actions'

// takes properties of LeftNavContainer defined in Dashboard and maps to the state
const mapStateToProps = (state, ownProps) => ({
    navPages: ownProps.navPages,
    currentViewIndex: state.currentView // currentView defined for the state via the currentView reducer
})

// dispatch = broadcast for listening
// makes sure prop changes are dispatched
const mapDispatchToProps = (dispatch) => ({
    // logoutUser defined in index.js
    // onClickLogout: logoutUser().bind(this, dispatch), 
    // setCurrentView defined in index.js creates action event & dispatch broadcasts it (index is bound to clicked item)
    onClick: (index) => {dispatch(setCurrentView(index))}
})

// connects LeftNav via LeftNavContainer to state via store
const LeftNavContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(LeftNav)

export default LeftNavContainer