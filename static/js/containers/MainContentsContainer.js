import { connect } from 'react-redux'
import { setCurrentView } from '../actions'
import MainContents from '../components/MainContents'

const mapStateToProps = (state, ownProps) => ({
    currentViewIndex: state.currentView,
})

const mapDispatchToProps = {   
}

const MainContentsContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(MainContents)

export default MainContentsContainer