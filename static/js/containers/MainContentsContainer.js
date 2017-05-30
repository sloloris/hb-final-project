import { connect } from 'react-redux'
import { setCurrentView, getUserContacts, userId } from '../actions'
import MainContents from '../components/MainContents'

const mapStateToProps = (state, ownProps) => ({
    currentViewIndex: state.currentView,
    contacts: state.contacts
})

const mapDispatchToProps = {   
    getUserContacts: getUserContacts
}

const MainContentsContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(MainContents)

export default MainContentsContainer