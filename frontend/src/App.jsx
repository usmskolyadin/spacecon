import './App.css'
import {useDispatch, useSelector} from 'react-redux'
import { Link } from 'react-router-dom'

function App() {
  const dispatch = useDispatch()
  const cash = useSelector(state => state.cash.cash)
  const costumers = useSelector(state => state.costumer.costumers)

  const getCash = (cash) => {
    dispatch({type: "GET_CASH", payload: cash})
  }


  const addCash = (cash) => {
    dispatch({type: "ADD_CASH", payload: cash})
  }
  
  const addClient = (name) => {
    const costumer = {
      id: Date.now(),
      name,
    }

    dispatch({type: "ADD_COSTUMER", payload: costumer})
  }

  const removeClient = (costumer) => {
    dispatch({type: "REMOVE_COSTUMER", payload: costumer})
  }

  return (
    <div style={{backgroundColor: "blue"}}>
      <Link to="/auth/login">login</Link>
    </div>
  )
}

export default App
