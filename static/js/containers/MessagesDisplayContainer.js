import { connect } from 'react-redux'
import { addMessage } from '../actions'
import MessagesDisplay from '../components/MessagesDisplay'

const mapStateToProps = (state, ownProps) => ({
    messages: ownProps.messages
})

const mapDispatchToProps = {  
    addMessage: addMessage
}

const MessageDisplayContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(MessagesDisplay)

export default MessagesDisplayContainer