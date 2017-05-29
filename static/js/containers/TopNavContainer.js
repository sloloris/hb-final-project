import { connect } from 'react-redux'
import TopNav from '../components/TopNav'

// first function passed into connect function always receives state as first argument - react then subscribes component to all those state variables
const mapStateToProps = (state, ownProps) => ({ 
})

const mapDispatchToProps = (dispatch) => ({
})

const TopNavContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(TopNav)

export default TopNavContainer
