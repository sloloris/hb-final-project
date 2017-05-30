import { connect } from 'react-redux'
import { setCurrentView, getUserContacts, getMessages } from '../actions'
import MainContents from '../components/MainContents'

const mapStateToProps = (state, ownProps) => ({
    currentViewIndex: state.currentView,
    contacts: state.contacts,
    messages: state.messages
})

const mapDispatchToProps = {   
    getUserContacts: getUserContacts,
    getMessages: getMessages
}

const MainContentsContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(MainContents)

export default MainContentsContainer