import { connect } from 'react-redux'
import ScheduleView from '../components/ScheduleView'

const mapStateToProps = (state, ownProps) => ({
    contacts: state.contacts
})

const mapDispatchToProps = {  
}

const ScheduleViewContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(ScheduleView)

export default ScheduleViewContainer