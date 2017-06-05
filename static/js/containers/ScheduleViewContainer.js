import { connect } from 'react-redux'
import ScheduleView from '../components/ScheduleView'

const mapStateToProps = (state, ownProps) => ({
    contacts: ownProps.contacts
})

const mapDispatchToProps = {  
}

const MessagesDisplayContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(ScheduleView)

export default ScheduleViewContainer